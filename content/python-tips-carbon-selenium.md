Title: Generating Beautiful Code Snippets with Carbon and Selenium
Date: 2019-02-26 12:00
Category: Tools
Tags: Selenium, BeautifulSoup, requests, collections, random, urllib, carbon, tips, pprint, automation
Slug: python-tips-carbon-selenium
Authors: Bob
Summary: Did you notice our [Python tips](https://twitter.com/search?q=pybites%20carbon&src=typd) lately? They looks more sexy, don't they? That's thanks to [Carbon](https://carbon.now.sh/) which lets you _create beautiful images of your source code_. As much as I love its interface though, what if we can automate this process generating the image for us? That's what we did and posting new tips to Twitter is now a breeze. In this article I will show you how using a bit of `BeautifulSoup` and `selenium`. Enjoy!
cover: images/featured/pb-article.png

Did you notice our [Python tips](https://twitter.com/search?q=pybites%20carbon&src=typd) lately? They looks more sexy, don't they? That's thanks to [Carbon](https://carbon.now.sh/) which lets you _create beautiful images of your source code_. As much as I love its interface though, what if we can automate this process generating the image for us?

That's what we did and posting new tips to Twitter is now a breeze. In this article I will show you how using a bit of `BeautifulSoup` and `selenium`. Enjoy!

## Getting Ready

If you want to follow along, the final code is [here](https://github.com/pybites/blog_code/blob/master/tips/tips.py).

First make [a virtual environment](https://pybit.es/the-beauty-of-virtualenv.html) and `pip install` [the requirements](https://github.com/pybites/blog_code/blob/master/tips/requirements.txt). Also make sure you have the [chromedriver](http://chromedriver.chromium.org/) in your `PATH`.

	[bobbelderbos@imac code]$ mkdir carbon && cd $_
	[bobbelderbos@imac carbon]$ alias pvenv
	alias pvenv='/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 -m venv venv && source venv/bin/activate'
	[bobbelderbos@imac carbon]$ pvenv
	(venv) [bobbelderbos@imac carbon]$ python -V
	Python 3.7.0
	(venv) [bobbelderbos@imac carbon]$ pip install -r requirements.txt
	...
	Successfully installed beautifulsoup4-4.7.1 bs4-0.0.1 certifi-2018.11.29 chardet-3.0.4 idna-2.8 requests-2.21.0 selenium-3.141.0 soupsieve-1.8 urllib3-1.24.1
	(venv) [bobbelderbos@imac carbon]$ ls ~/bin/chromedriver
	/Users/bobbelderbos/bin/chromedriver

## Introducing our Platform Tips

At the time of this writing we have [92 tips on our platform](https://codechalleng.es/tips):

![pybites tips page]({filename}/images/selenium-carbon/pybites-tips.png)

Let's inspect the tip html we need to parse with BeautifulSoup:

![html of each tip]({filename}/images/selenium-carbon/tip-html.png)

Each tip is wrapped in a `tr` where the tip text is in a `blockquote` and the code in `pre` tags.

We also want to know if a tip has already been shared out by inspecting the Twitter link. In this example it has _pybites/status_ which means we did.

![check if there is a twitter link href]({filename}/images/selenium-carbon/twitter-href.png)

---

By the way, I didn't realize it at the time of coding this, but we did make an [API GET endpoint](https://codechalleng.es/api/tips/) some time ago. If there is an API it's preferred to use that to retrieve data. However knowing `BeautifulSoup` might come in handy too :)

I will do a follow-up post how to convert this into a Tips API ...

## Bootstrapping the script

Before scraping the tips page, let's define the overall structure of the script:

	from collections import namedtuple
	from random import choice
	import sys
	from time import sleep
	import urllib.parse

	from bs4 import BeautifulSoup
	import requests
	from selenium import webdriver

	TIPS_PAGE = 'https://codechalleng.es/tips'
	PYBITES_HAS_TWEETED = 'pybites/status'
	CARBON = 'https://carbon.now.sh/?l=python&code={code}'
	TWEET_BTN_CLASS = 'jsx-2739697134'
	TWEET = '''{tip} {src}

	🐍 Check out more @pybites tips at https://codechalleng.es/tips 💡

	(image built with @carbon_app)

	{img}
	'''

	Tip = namedtuple('Tip', 'tip code src')


	def retrieve_tips():
		"""Grab and parse all tips from https://codechalleng.es/tips
		returning a dict of keys: tip IDs and values: Tip namedtuples
		"""
		pass


	def get_carbon_image(tip):
		"""Visit carbon.now.sh with the code, click the Tweet button
		and grab and return the Twitter picture url
		"""
		pass


	if __name__ == '__main__':
		tips = retrieve_tips()
		if len(sys.argv) == 2:
			tip_id = int(sys.argv[1])
		else:
			tip_id = choice(list(tips.keys()))

		tip = tips.get(tip_id)
		if tip is None:
			print(f'Could not retrieve tip ID {tip_id}')
			sys.exit(1)

		src = tip.src and f' - see {tip.src}' or ''
		img = get_carbon_image(tip)

		tweet = TWEET.format(tip=tip.tip, src=src, img=img)
		print(tweet)

OK step by step:

- We are going to use some nice stdlib modules like `collections` and `random`. Secondly we import the external modules we just installed.

- We define some constants. `TWEET` is the template of the tweet we want to build. I will explain why we need `TWEET_BTN_CLASS` when we get to the carbon section ...

- I define a `namedtuple` (basically a `class` without behavior) to hold a tip.

- We are going to do the work in two functions: `retrieve_tips` and `get_carbon_image` (I probably should add some [type hinting](https://docs.python.org/3/library/typing.html) on the next iteration ...)

- Under `if __name__ == '__main__'` (aka "I, the script, am called, not imported") I define two ways to call the script:

	- with exactly one argument (`len(sys.argv) == 2`, `sys.argv[0]` is the script name), retrieving the tip by numeric ID (see the first column of the [tips table](https://codechalleng.es/tips)).

	- with any other number of arguments, taking a random tip from the retrieved `dict` using `random.choice`.

- It retrieves the tip from the `tips dict` and creates the tweet using the `TWEET` template and prints it to stdout. For now I am happy to manually post it (see demo at the end).

## Parsing the tips

At this point the code at best will throw an `AttributeError`, because our tips `dict` is empty. So let's write `retrieve_tips` to populate it:

	def retrieve_tips():
		"""Grab and parse all tips from https://codechalleng.es/tips
		returning a dict of keys: tip IDs and values: Tip namedtuples
		"""

Firt we need to retrieve the page with `requests`:

		html = requests.get(TIPS_PAGE)

We then instantiate a `BeautifulSoup` object passing it in the response text and parser:

		soup = BeautifulSoup(html.text, 'html.parser')

As we saw all the tips are in a table, each one in a table row or `tr`, so let's get all of them:

		trs = soup.findAll("tr")

Next let's use a data structure to store the tips. At first I used a `list` but later I wanted to index by tip ID, so a `dict` turned out to be more appropriate:

		tips = {}

Next let's loop through the rows, creating Tip `namedtuple`s and adding them to our `tips dict`:

		for tr in trs:
			tds = tr.find_all("td")
			id_ = int(tds[0].text.strip().rstrip('.'))
			tip_html = tds[1]

			links = tip_html.findAll("a", class_="left")
			share_link = links[0].attrs.get('href')

			pre = tip_html.find("pre")
			code = pre and pre.text or ''

			# skip if tweeted or not code in tip
			if PYBITES_HAS_TWEETED in share_link or not code:
				continue

			tip = tip_html.find("blockquote").text
			src = len(links) > 1 and links[1].attrs.get('href') or ''

			tips[id_] = Tip(tip, code, src)

Step by step:

- First I get all table cells or `td` elements in the table row.

- I parse the tip ID from the first cell, stripping off the dot and storing it in a variable called `id_`.

- The tip html is in the second table cell.

- I check if there are any links in the tips html. As you scroll down on the [tips page](https://codechalleng.es/tips) there is always a share link and an optional second resource link.

- I put the tip code in a variable called `code`.

- Then I check if the tip was already shared on Twitter by checking if `PYBITES_HAS_TWEETED` (_pybites/status_) is in the share link, or if the tip does not contain any code (some are just quotes). In these instances we want to exclude the tip.

- Next we put the tip text in a variable called `tip`.

- We add the resource link in a variable called `src`. As it's optional we first check the length of the `links` list.

- Finally we make the `Tip namedtuple` and assign it as value to the `id_` key in the `tips dict`.

Lastly we return the tips `dict`:

    	return tips

Let's see if this works using `pprint`:

![adding a pprint]({filename}/images/selenium-carbon/add-pprint.png)

Running this it outputs:

![getting a tips dict]({filename}/images/selenium-carbon/tips-dict.png)

Great. Let's make a carbon image next.

## Beautiful images of your source code

Meet [carbon](https://carbon.now.sh/):

![carbon home]({filename}/images/selenium-carbon/carbon-home.png)

It allows you to add code, choose a language and configure other settings, then generate the image and/or tweet it out. It's really nice!

While playing with the interface I found that clicking the _Tweet_ button it would generate a shareable picture hosted on Twitter. For example clicking the _Tweet_ button I get this popup:

![clicking tweet button]({filename}/images/selenium-carbon/clicking-tweet-button.png)

And that Twitter link shows the generated code snippet image:

![resulting carbon image]({filename}/images/selenium-carbon/resulting-carbon-image.png)

We can automate this using Selenium to click the _Tweet_ button, capturing the generated image link. This is why I defined the `TWEET_BTN_CLASS` constant which is the class set on this button.

## Use Selenium to create tip code image

Let's write the second function `get_carbon_image`:

	def get_carbon_image(tip):
		"""Visit carbon.now.sh with the code, click the Tweet button
		and grab and return the Twitter picture url
		"""

First we need to encode (replace special characters) the tip code snippet. `quote_plus` (from `urllib.parse`) _also replaces spaces by plus signs, as required for quoting HTML form values when building up a query string to go into a URL_ (see [docs](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote_plus)).

		code = urllib.parse.quote_plus(tip.code)

With that done we define the full url:

		url = CARBON.format(code=code)

We then start the Chromedriver. Unlike [last time](https://pybit.es/selenium-headless-on-heroku.html) I am not going to use _headless_ mode here, because I'd actually like to see what Selenium is doing:

		driver = webdriver.Chrome()
		driver.get(url)

Here we locate mentioned `TWEET_BTN_CLASS` (_jsx-2739697134_) button and click on it:

		driver.find_element_by_class_name(TWEET_BTN_CLASS).click()

Trial and error taught me that this might take a bit so I use `sleep`:

		sleep(5)

## Retrieve the image from popup

And here is the tricky part. The _Tweet_ button opened a popup but the driver is still on the main browser page window (see seconds 15 and 41 of the demo below).

You can toggle windows though using `driver.switch_to.window`:

		window_handles = driver.window_handles
		driver.switch_to.window(window_handles[1])

Now I am on the Twitter popup window and I can target the _status_ ID field and grab the image URL from it:

		status = driver.find_element_by_id('status')
		img = status.text.split(' ')[-1]

Finally I quit the `driver` (this closes the browser) and return the image string:

		driver.quit()
		return img

## See it in action

Here you can see this automation script in action, generating an image from a random tip as well as when specifying a specific ID:

<div class="container">
<iframe src="https://www.youtube.com/embed/V3-7RvipiSU" frameborder="0" allowfullscreen class="video"></iframe>
</div>

And voilà: two new tips I could post to our Twitter ([here](https://twitter.com/pybites/status/1100343735299252225) and [here](https://twitter.com/pybites/status/1100342422473719809)).

Note that after manually tweeting it out as [@pybites](https://twitter.com/pybites), we set the obtained tweet URL on the tip (in the DB) so it's not selected upon next run (the `if PYBITES_HAS_TWEETED in share_link` check above).

### Room for improvement

Here are some things we can do to take it to the next level:

1. Auto-post the tweet to Twitter (we [already have the code](https://pybit.es/selenium-headless-on-heroku.html) for this).
2. Make a Tips API (pending article):
	- allow `GET` to retrieve a tip and `POST` to receive new ones,
	- do a `PUT` request on the tip with the tweet link after running this script and/or auto-posting to Twitter (1.)

Feel free to PR any of this [here](https://github.com/pybites/blog_code/pulls).

---

I hope you enjoyed this and it inspired you to build your own automation scripts. To learn how to run Selenium in headless mode on Heroku, check out [our article from last week](https://pybit.es/selenium-headless-on-heroku.html).

Feel free to share more Python tips [on our platform](https://codechalleng.es/inbox/new/pytip/).

Question: what would you like us to write about more? You can [drop us an email](mailto:pybitesblog@gmail.com) or brainstorm with us and our amazing community [on our Slack](https://join.slack.com/t/pybites/shared_invite/enQtNDAxODc0MjEyODM2LTNiZjljNTI2NGJiNWI0MTRkNjY4YzQ1ZWU4MmQzNWQyN2Q4ZTQzMTk0NzkyZTRmMThlNmQzYTk5Y2Y5ZDM4NDU). We do accept [guest posts](https://pybit.es/pages/guests.html)!

---

Keep Calm and Code in Python!

-- Bob
