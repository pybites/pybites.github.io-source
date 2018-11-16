Title: How to Test Your Django App with Selenium and pytest
Date: 2018-11-16 12:30
Category: Testing
Tags: django, pytest, selenium, platform, fixtures
Slug: selenium-pytest-and-django
Authors: Bob
Summary: In this article I will show you how to test a Django app with pytest and Selenium. We will test our [CodeChalleng.es platform](https://codechalleng.es) comparing the logged out homepage with the logged in dashboard. We are going to see how to connect to a real database, login to a webpage with Selenium, navigate the DOM seeing if elements shown on the page match up with what's in the DB. We even see some dateutil to come up with the expected values for our new coding streak calendar headers. Overall you should learn enough Selenium and pytest to start testing your Django app end-to-end. Sounds exciting? Let's dive straight in!
cover: images/featured/pb-article.png

In this article I will show you how to test a Django app with pytest and Selenium. We will test our [CodeChalleng.es platform](https://codechalleng.es) comparing the logged out homepage with the logged in dashboard. We are going to see how to connect to a real database, login to a webpage with Selenium, navigate the DOM seeing if elements shown on the page match up with what's in the DB. We even see some dateutil to come up with the expected values for our new coding streak calendar headers. Overall you should learn enough Selenium and pytest to start testing your Django app end-to-end. Sounds exciting? Let's dive straight in!

## Dependencies and environment variables

First we want to make sure we have proper support for `pytest` in Django, hence after [setting up my virtual environment](https://pybit.es/the-beauty-of-virtualenv.html), I installed [`pytest`](https://docs.pytest.org/en/latest/), [`pytest-django`](https://pytest-django.readthedocs.io/en/latest/) and [`selenium`](https://selenium-python.readthedocs.io/):

	$ more requirements_dev.txt
	pytest
	pytest-django
	selenium

I am using Selenium to test with the real UI and database, so I set up some environment variables in my `venv/bin/activate`:

	export DB_HOST=0.0.0.0
	export DB_PORT=5432
	export DB_NAME=
	export DB_USER=
	export DB_PASSWORD=
	export HOMEPAGE="localhost:8000"  # swappable wit uat environment
	export FREE_USER=Github user
	export FREE_USER_PASSWORD=
	export PREMIUM_USER=another Github user
	export PREMIUM_USER_PASSWORD=

I also `unset` these in the `deactivate` function of `venv/bin/activate` so they don't linger around when I leave the virtual env, a trick I learned when writing [Building a Simple Web App With Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/):

	...
	...
	deactivate () {
		...
		...
		unset DB_HOST
		unset DB_PORT
		unset DB_NAME
		unset DB_USER
		unset DB_PASSWORD
		unset HOMEPAGE
		unset FREE_USER
		unset FREE_USER_PASSWORD
		unset PREMIUM_USER
		unset PREMIUM_USER_PASSWORD
	}

To illustrate this:

	[bobbelderbos@imac codechalleng.es (master)]$ env|grep HOMEPAGE
	[bobbelderbos@imac codechalleng.es (master)]$ source venv/bin/activate
	(venv) [bobbelderbos@imac codechalleng.es (master)]$ env|grep HOMEPAGE
	HOMEPAGE=localhost:8000
	(venv) [bobbelderbos@imac codechalleng.es (master)]$ deactivate
	[bobbelderbos@imac codechalleng.es (master)]$ env|grep HOMEPAGE
	[bobbelderbos@imac codechalleng.es (master)]$


## pytest setup

Next let's create a `pytest.ini` file to set the `DJANGO_SETTINGS_MODULE` environment variable to point to Django's configuration file, by default `settings.py` inside the main app:

	$ cat pytest.ini
	[pytest]
	DJANGO_SETTINGS_MODULE = mysite.core.settings
	# -- recommended but optional:
	python_files = tests.py test_*.py *_tests.py

## Testing using a DB / conftest.py

Then we need to connect to the app's database. It took me a bit of trial and error how to use a real database because `pytest-django` takes a _conservative approach_:

> pytest-django takes a conservative approach to enabling database access. By default your tests will fail if they try to access the database. Only if you explicitly request database access will this be allowed. This encourages you to keep database-needing tests to a minimum which is a best practice since next-to-no business logic should be requiring the database. Moreover it makes it very clear what code uses the database and catches any mistakes. [docs](https://pytest-django.readthedocs.io/en/latest/database.html)

The use of a real DB here is experimental. I could probably work around it by inferring the number of objects from the pages rather than the DB. I am leaving this in here though, because I think it's good to know how to have `pytest-django` connect to a real DB. The other nice thing is that you can simply toggle the use of the DB on a test-by-test basis using the `@pytest.mark.django_db` _fixture_ as we will see later.

First create a `conftest.py` file in your main app folder, loading in the database connection environment variables:

	$ cat mysite/core/conftest.py
	import os
	from django.conf import settings
	import pytest

	DEFAULT_ENGINE = 'django.db.backends.postgresql_psycopg2'

	@pytest.fixture(scope='session')
	def django_db_setup():
		settings.DATABASES['default'] = {
			'ENGINE': os.environ.get("DB_ENGINE", DEFAULT_ENGINE),
			'HOST': os.environ["DB_HOST"],
			'NAME': os.environ["DB_NAME"],
			'PORT': os.environ["DB_PORT"],
			'USER': os.environ["DB_USER"],
			'PASSWORD': os.environ["DB_PASSWORD"],
		}

This is a predefined _fixture_ `pytest-django` provides which will be triggered by `@pytest.mark.django_db`. As we want to set this up once for the whole test session, I set `scope='session'` in fixture's argument.

## Test our homepage

Now let's use both `pytest` and `selenium` to test the homepage of [our platform](https://codechalleng.es) logged in vs logged out. I added the following code to a `tests.py` file in my main app folder. `pytest.ini` makes that the `pytest` command line interface will find it.

### Setup work

As per PEP8 first we have some standard library modules, then external ones, then own modules:

	from datetime import date
	import os
	import re

	from dateutil.relativedelta import relativedelta
	import pytest
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys

	from mysite.core.models import Challenge
	from bites.models import Bite

I load in my remaining env variables:

	HOME = os.environ["HOMEPAGE"]
	TODAY = date.today()

	FREE_USER = os.environ['FREE_USER']
	FREE_USER_PASSWORD = os.environ['FREE_USER_PASSWORD']
	PREMIUM_USER = os.environ['PREMIUM_USER']
	PREMIUM_USER_PASSWORD = os.environ['PREMIUM_USER_PASSWORD']

And I define a helper function to convert a `datetime` to an uppercase 3-char month string (SEP/OCT/NOV), we see why in a bit ...

	def _make_3char_monthname(dt):
		return dt.strftime('%b').upper()

### Selenium driver and pytest's tearDown

First I need to instantiate a Selenium webdriver. As required I have the _geckodriver_ (I am using Chrome) sitting in my `~/bin` folder which is in my `$PATH`, see the [Selenium with Python documentation](https://selenium-python.readthedocs.io/installation.html#drivers).

I wrote a second _fixture_ to return a Selenium driver object which will span all test so I set `scope="module"` (when I will have multiple modules I will probably set this to `session`, like the `django_db_setup` fixture).

One really cool and elegant thing I learned is to simply replace `return` with `yield` in a fixture, to have some `tearDown` code which suited me perfectly here to close out the Chrome browser Selenium opens while testing:

> pytest supports execution of fixture specific finalization code when the fixture goes out of scope. By using a yield statement instead of return, all the code after the yield statement serves as the teardown code [docs](https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code)

	@pytest.fixture(scope="module")
	def driver():
		driver = webdriver.Chrome()
		yield driver
		driver.quit()

### Test the logged out homepage

Next a _hello world_ Selenium test: `driver.get(HOME)` reaches out to the platform's homepage and it just checks if the title is as expected. Here is the logged out homepage:

![homepage logged out]({filename}/images/homepage-loggedout.png)

	def test_loggedout_homepage(driver):
		driver.get(HOME)
		expected = "PyBites Code Challenges | Hone Your Python Skills"
		assert driver.title == expected

Note I am using `localhost` for `HOME` here so prior to this I started my Django app server in a second terminal tab: `python manage.py runserver`;

### Test the logged in dashboard

Let's do something more interesting. Here is the [CodeChalleng.es](https://codechalleng.es) dashboard of my test user:

![homepage logged in]({filename}/images/homepage-loggedin.png)

Let's see if we can test the following:

1. The H2 headers are as expected.
2. The new _coding streak_ calendar at the right bottom shows the last 3 months.
3. In that widget only one day has the css class _today_ (orange border).
4. Match the number of _Bite of Py_ links with the number of published Bites in the DB.
5. Match the number of _Blog Challenges_ links (2nd tab alongside "Bites of Py") with the number of published Challenges in the DB.

### DB fixture and login

`pytest-django`'s predefined `@pytest.mark.django_db` fixture will magically reference my `django_db_setup` in `conftest.py`. I go to `HOME` again and login using the _Sign In With Github_ button image we saw in the logged out view above. Of course we use our loaded in environment variables for the login and password:

	@pytest.mark.django_db
	def test_loggedin_dashboard(driver):
		driver.get(HOME)
		login_btn = '//a[img/@src="/static/img/ghlogin.png"]'
		driver.find_element_by_xpath(login_btn).click()
		driver.find_element_by_name('login').send_keys(FREE_USER)
		driver.find_element_by_name('password').send_keys(FREE_USER_PASSWORD
														+ Keys.RETURN)

### Finding elements

I use Selenium's `find_elements_by_tag_name` to find all h2 elements, then I check if the expected headers are in there:

		h2s = [h2.text for h2 in driver.find_elements_by_tag_name('h2')]
		expected = [f'Happy Coding, {FREE_USER}!', 'Announcements',
					'PyBites Ninjas (score ≥ 50)', 'Become a better Pythonista!',
					'Keep Calm and Code in Python!    SHARE ON TWITTER']
		for header in expected:
			assert header in h2s, f'{header} not in h2 headers'

### Assert calendar headers and a CSS class

You want to learn about `dateutil`'s `relativedelta`. I use it here because `datetime`'s `timedelta` does not have a delta of months. Here I calculate the last 3 months, at the time of this writing NOV-, OCT-, and SEP 2018. I then check if these are in the H2 headers:  

		# calendar / coding streak feature
		this_month = _make_3char_monthname(TODAY)
		last_month = _make_3char_monthname(TODAY-relativedelta(months=+1))
		two_months_ago = _make_3char_monthname(TODAY-relativedelta(months=+2))
		for month in (this_month, last_month, two_months_ago):
			month_year = f'{month} {TODAY.year}'
			assert month_year in h2s, f'{month_year} not in h2 headers'

Only one day should be marked with the _today_ css class, we can use Selenium's `find_elements_by_class_name`:

		# only current date is marked active
		assert len(driver.find_elements_by_class_name('today')) == 1

### Inspect links

Selenium has a powerful `find_elements_by_xpath` method that lets me grab all links from the page like so:

		# all bites and challenges show up
		all_links = driver.find_elements_by_xpath("//a[@href]")

Then I check how many Bites we have in the database and match the link using a regex in list comprehension:

		expected_num_bites = Bite.objects.filter(published=True).count()
		actual_num_bites = len([link for link in all_links
								if re.match(r'^Bite \d+\..*',  # no class
											link.text)])
		assert actual_num_bites == expected_num_bites

Ditto for Challenges but I don't need the regex because it conveniently has a class name of _challengeTitle_ so I can use Selenium's `find_elements_by_class_name`:

		expected_num_challenges = Challenge.objects.filter(published=True).count()
		challenge_titles = driver.find_elements_by_class_name('challengeTitle')
		actual_num_challenges = len(challenge_titles)
		assert actual_num_challenges == expected_num_challenges

That's an additional advantage of writing tests: you will find refactoring candidates. The example here - add a class name to Bite links - is trivial, but it highlights a point.

And the results:

![pytest selenium result]({filename}/images/pytest-selenium-result.png)

It took some time to write all this, and maybe we want to split this into multiple tests.

One useful tip in this context: set a _breakpoint_ in the test you are writing. You can use `breakpoint()` if on >= 3.7 else `import pdb; pdb.set_trace()`. In the debugger start playing around with Selenium's methods till you get it exactly right. At that point you can just copy+paste it into your test. This will save you a lot of time and makes the learning experience more fun :)

The exciting thing is that at this point I can just run this every time we make changes to check for any regression bugs. Imagine having a suite of hundreds of these tests, it's a real safeguard and time saver!

---

Of course this is only one page and even so it only hits the surface. Other tests we could write for this page:

1. Resolve a Bite, does your score go up? Cheat a Bite, is only 1 point added to score?
2. Go from 8 to 10 points, do I earn my first badge?
3. Go from 48 to 50 points, is my user starting to show up on the leader board (right top)?
4. Are _bitecoins_ changing from grey to colored when I complete a Bite?
5. Are coding actions over multiple days get the corresponding green cells in the _coding streak_ / calendar widget?
6. The NEW background image label for _new_ (< 1 week old) Bites and Challenges.
7. The Bite Token Counter for the Cherry-Pick Tier this user is on.
8. Etc. etc.

It is good to start thinking about all these scenarios because as your app grows the permutations of all possible outcomes grow exponentially, so automate testing is paramount. And with that I hope this gave you a feel how you can test your Django app with `pytest` and `selenium`.

---

Keep Calm and Code|Test in Python!

-- Bob
