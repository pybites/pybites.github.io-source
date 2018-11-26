Title: How to Test Your Django App with Selenium and pytest
Date: 2018-11-22 22:10
Category: Testing
Tags: django, pytest, selenium, platform, fixtures, dateutil
Slug: selenium-pytest-and-django
Authors: Bob
Summary: In this article I will show you how to test a Django app with pytest and Selenium. We will test our [CodeChalleng.es platform](https://codechalleng.es) comparing the logged out homepage vs the logged in dashboard. We will navigate the DOM matching elements and more. Overall you should learn enough Selenium and pytest to start testing a web page including a login. Sounds exciting? Let's dive straight in!
cover: images/featured/pb-article.png

In this article I will show you how to test a Django app with pytest and Selenium. We will test our [CodeChalleng.es platform](https://codechalleng.es) comparing the logged out homepage vs the logged in dashboard. We will navigate the DOM matching elements and more. Overall you should learn enough Selenium and pytest to start testing a web page including a login. Sounds exciting? Let's dive straight in!

> This article focuses on getting Selenium + pytest working with Django, but as the pytest + Selenium part is applicable to any web app, I ditched the Django / DB part from the final script which I will link to at the end of this article.

## Project setup

First we want to make sure we have proper support for `pytest` in Django, hence after [setting up my virtual environment](https://pybit.es/the-beauty-of-virtualenv.html), I installed [`pytest`](https://docs.pytest.org/en/latest/), [`pytest-django`](https://pytest-django.readthedocs.io/en/latest/), [`selenium`](https://selenium-python.readthedocs.io/) and [`python-dateutil`](https://dateutil.readthedocs.io/en/stable/):

	$ more requirements.txt
	python-dateutil
	pytest
	pytest-django
	selenium

I am going to use a test user account and need to access the DB (which we see in a bit) so I set the following environment variables in my `venv/bin/activate`:

	export DB_HOST=0.0.0.0
	export DB_PORT=5432
	export DB_NAME=
	export DB_USER=
	export DB_PASSWORD=
	export USER_NAME=Github user
	export USER_PASSWORD=

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
		unset USER_NAME
		unset USER_PASSWORD
	}

## pytest setup

Next let's create a `pytest.ini` file to set the `DJANGO_SETTINGS_MODULE` environment variable to point to Django's configuration file, by default `settings.py` inside the main app:

	$ cat pytest.ini
	[pytest]
	DJANGO_SETTINGS_MODULE = mysite.core.settings
	# -- recommended but optional:
	python_files = tests.py test_*.py *_tests.py

## Testing using a DB / conftest.py

Overall I don't need the DB for Selenium testing but for some tests it would be nice to match up the page elements with what's in the DB, for example the amount of Bite exercises shown on the page vs records in the DB.

Another use case I found while writing more Selenium code for our platform was the activation link when users add their email. No real email gets sent from my localhost and/or when testing so I needed to query the user's object to retrieve the newly generated link.  

It took me a bit of trial and error to figure out how to use a real database because `pytest-django` [takes a conservative approach](https://pytest-django.readthedocs.io/en/latest/database.html).

I ended up using a `conftest.py` file (in the main app folder) as specified in the documentation:

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
			'NAME': os.environ["DB_NAME"],  # my dedicated test database (!)
			'PORT': os.environ["DB_PORT"],
			'USER': os.environ["DB_USER"],
			'PASSWORD': os.environ["DB_PASSWORD"],
		}

This is a predefined _fixture_ `pytest-django` provides which will be triggered if you _decorate_ your test function with `@pytest.mark.django_db`. As we want to set this up once for the whole test session, I set `scope='session'` in the fixture's argument.

## Test our homepage

Now let's use both `pytest` and `selenium` to test the homepage of [our platform](https://codechalleng.es) logged in vs. logged out. I added the following code to a `tests.py` file in my main app folder. `pytest.ini` makes that the `pytest` command line interface will find it.

### Setup work

As per PEP8 first we have some standard library modules, then external ones, then own modules:

	from datetime import date
	import os
	import re

	from dateutil.relativedelta import relativedelta
	import pytest
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys

	# here I use the DB/ORM Models to match page elements
	from mysite.core.models import Challenge
	from bites.models import Bite

	HOMEPAGE = 'http://localhost:8000'
	TODAY = date.today()

I load in my user from the corresponding env variables:

	USER_NAME = os.environ['USER_NAME']
	USER_PASSWORD = os.environ['USER_PASSWORD']

And I define a helper function to convert a `datetime` to an uppercase 3-char month string (SEP/OCT/NOV), we see why in a bit ...

	def _make_3char_monthname(dt):
		return dt.strftime('%b').upper()

### Selenium driver and pytest's tearDown

First I need to instantiate a Selenium webdriver. As required I have the _geckodriver_ (I am using Chrome) sitting in my `~/bin` folder which is in my `$PATH`, see the [Selenium with Python documentation](https://selenium-python.readthedocs.io/installation.html#drivers).

I wrote a second _fixture_ to return a Selenium driver object which will span all tests in my module, so I set `scope="module"` (for now ... if I'd need to re-run this setup for each function, then I would leave `scope` off, defaulting to _per function scope_).

One really elegant thing I learned is to simply replace `return` with `yield` in a fixture, to have some `tearDown` code which suited me perfectly here to close out the Chrome browser that Selenium opens while testing:

> pytest supports execution of fixture specific finalization code when the fixture goes out of scope. By using a yield statement instead of return, all the code after the yield statement serves as the teardown code [docs](https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code)

	@pytest.fixture(scope="module")
	def driver():
		driver = webdriver.Chrome()
		yield driver
		driver.quit()

Generators are awesome!

### Test the logged out homepage

Next a _hello world_ Selenium test: `driver.get(HOMEPAGE)` reaches out to the platform's homepage and it just checks if the title is as expected. Here is the logged out homepage:

![homepage logged out]({filename}/images/homepage-loggedout.png)

	def test_loggedout_homepage(driver):
		driver.get(HOMEPAGE)
		expected = "PyBites Code Challenges | Hone Your Python Skills"
		assert driver.title == expected

And that is how easy it is to write a Selenium test in pytest!

**Note** I am using `localhost` for `HOMEPAGE` here so prior to this I started my Django app server in a second terminal tab: `python manage.py runserver`!

### Test the logged in dashboard

Let's do something more interesting. Here is the [CodeChalleng.es](https://codechalleng.es) dashboard of my test user:

![homepage logged in]({filename}/images/homepage-loggedin.png)

Let's see if we can test the following:

1. The `h2` headers are as expected.
2. The new _coding streak_ calendar at the right bottom shows the last 3 months.
3. In that widget only one day has the css class _today_ (orange border).
4. Match the number of _Bite of Py_ links with the number of published Bites in the DB.
5. Match the number of _Blog Challenges_ links (2nd tab alongside "Bites of Py") with the number of published Challenges in the DB.

### DB fixture and login

As I am going to access my DB for steps 4. and 5. I need to decorate my new test function with `pytest-django`'s predefined `@pytest.mark.django_db` fixture. This will then (magically) reference my `django_db_setup` in `conftest.py` (this took me some trial and error).

	@pytest.mark.django_db
	def test_loggedin_dashboard(driver):
		...

First I go to `HOMEPAGE` again and login using the _Sign In With Github_ button. First I located the image and clicked it:

		driver.get(HOMEPAGE)
		login_btn = '//a[img/@src="/static/img/ghlogin.png"]'
		driver.find_element_by_xpath(login_btn).click()

But we fixed that on the platform setting a class attribute on the login button: `class="ghLoginBtn"` (not an `id` because sometimes there are two buttons and `id` attributes should be unique).

So now I can just do:

		driver.find_element_by_class_name('ghLoginBtn').click()

This takes me to the Github login page and I can login using Selenium's `send_keys` method. Note the extra return key:

		driver.find_element_by_name('login').send_keys(USER_NAME)
		driver.find_element_by_name('password').send_keys(USER_PASSWORD + Keys.RETURN)

### Finding elements

I use Selenium's `find_elements_by_tag_name` to find all `h2` elements (note the **s** in _elements_ which gets  you a list of all), then I check if the expected headers are in there:

		h2s = [h2.text for h2 in driver.find_elements_by_tag_name('h2')]
		expected = [f'Happy Coding, {USER_NAME}!', 'PyBites Platform Updates [all]',
					'PyBites Ninjas (score ≥ 50)', 'Become a better Pythonista!',
					'Keep Calm and Code in Python!    SHARE ON TWITTER']
		for header in expected:
			assert header in h2s, f'{header} not in h2 headers'

### Assert calendar headers and a CSS class

You want to learn about `dateutil`'s `relativedelta`. I use it here because `datetime`'s `timedelta` does not have a delta of months. Here I calculate the last 3 months, at the time of this writing NOV-, OCT-, and SEP 2018. I then check if these are in the `h2` headers:  

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

		# next test if all bite and challenge links are present
		all_links = driver.find_elements_by_xpath("//a[@href]")

Then I check how many Bites we have in the database and match the link using a regex in a _list comprehension_:

		expected_num_bites = Bite.objects.filter(published=True).count()
		actual_num_bites = len([link for link in all_links
								if re.match(r'^Bite \d+\..*',  # no class in html anchors :(
											link.text)])
		assert actual_num_bites == expected_num_bites

Ditto for Challenges but I don't need the regex because they conveniently have a class name of _challengeTitle_ so I can again use Selenium's `find_elements_by_class_name`:

		expected_num_challenges = Challenge.objects.filter(published=True).count()
		challenge_titles = driver.find_elements_by_class_name('challengeTitle')
		assert len(challenge_titles) == expected_num_challenges

That's an additional advantage of writing tests: you will find refactoring candidates. Like the Github button earlier we could add a class name to the Bite links to make it easier to target them.

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

It is good to start thinking about all these scenarios because as your app grows the permutations of all possible outcomes grow exponentially, so automated testing is paramount.

And with that I hope this gave you a feel how you can test your Django app with `pytest` and `selenium`.

### The final (stripped down) code

And the result:

![pytest selenium result]({filename}/images/pytest-selenium-result.png)

Check out a simplified version [here](https://github.com/pybites/blog_code/tree/master/selenium). I took out the Django requirement omitting the last two (DB) checks. No more Django `runserver` made me change the `HOMEPAGE` constant to use the live site instead of _localhost_.

### Your turn!

Up for a challenge? We have a dedicated Django + Selenium Code Challenge available on our platform: [PCC32 - Test a Simple Django App With Selenium](https://codechalleng.es/challenges/32/). 

### Final tip when writing Selenium code

Set a _breakpoint_ in the test you are writing. You can use `breakpoint()` if on >= 3.7, else `import pdb; pdb.set_trace()`. 

In the debugger it's easier to Selenium's methods on the website in _frozen_ state. Then you can just copy+paste from debugger to script and vice versa. This will save you a lot of time and makes it more fun :)

It takes time to write extended Selenium tests but the exciting part is that you build up your regression suite that will catch future bugs for you, saving you time and assuring you write more reliable code!

### Using Selenium on CodeChalleng.es

**Update 26th of Nov 2018**: I took this concept a bit further and started a serious regression test suite for [our platform](http://codechalleng.es/). Here you can see multiple users (tiers) logged in, going through various workflows, pretty exciting stuff!

<iframe src="https://www.youtube.com/embed/Jpwn2yOppPo" frameborder="0" allowfullscreen class="video"></iframe>

---

Keep Calm and Code|Test in Python!

-- Bob
