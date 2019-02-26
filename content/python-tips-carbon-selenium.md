Title: Generating Beautiful Code Snippets with Carbon and Selenium
Date: 2019-02-26 12:00
Category: Tools
Tags: Selenium, BeautifulSoup, requests, collections, random, urllib, carbon, tips, pprint, automation
Slug: python-tips-carbon-selenium
Authors: Bob
Summary: Did you notice our [Python tips](https://twitter.com/search?q=pybites%20carbon&src=typd) lately? They looks more sexy, don't they? That's thanks to [Carbon](https://carbon.now.sh/) which lets you _create beautiful images of your source code_. As much as I love its interface, what if we can automate this process generating the image for us? That's what we did and posting new tips to Twitter is now a breeze. In this article I will show you how I did it using a bit of `BeautifulSoup` and `selenium`. Enjoy
cover: images/featured/pb-article.png

Did you notice our [Python tips](https://twitter.com/search?q=pybites%20carbon&src=typd) lately? They looks more sexy, don't they? That's thanks to [Carbon](https://carbon.now.sh/) which lets you _create beautiful images of your source code_. As much as I love its interface, what if we can automate this process generating the image for us? That's what we did and posting new tips to Twitter is now a breeze. In this article I will show you how I did it using a bit of `BeautifulSoup` and `selenium`. Enjoy

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

At the time of this writing we have 92 tips on our platform. You can check them out [here](https://codechalleng.es/tips).

![pybites tips page]({filename}/images/selenium-carbon/pybites-tips.png)

Let's inspect the html what we need to parse with BeautifulSoup:

![html of each tip]({filename}/images/selenium-carbon/tip-html.png)

Each tip is wrapped in a `tr` where the tip text is in a `blockquote` and the code in `pre` tags.

We also want to know if a tip has already been shared out by inspecting the Twitter link. In this example it has _pybites/status_ which means we did share it out.

![check if there is a twitter link href]({filename}/images/selenium-carbon/twitter-href.png)

---

By the way, I didn't realize it at the time of coding this, but we did make an [API GET endpoint](https://codechalleng.es/api/tips/) some time ago. I will do a follow-up post how to convert this into a Tips API ...

## Bootstrapping the script

Before scraping this page, let's define the overall structure of the script:

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

- We are going to use some nice stdlib modules like `collections` and `random`.

- Secondly we import the external modules we just installed.

- We define some constants. I will explain `TWEET_BTN_CLASS` when we get to the carbon section ...

- `TWEET` is the template of the tweet we want to build.

- I define a `namedtuple` (aka a `class` without methods or behavior) to hold one tip.

- We are going to do the work in two functions: `retrieve_tips` and `get_carbon_image` (I probably should add some [type hints](https://docs.python.org/3/library/typing.html) on the next iteration ...)

- Under `if __name__ == '__main__'` (aka "I, the script, am called, not imported") I define two modes of operation:

	- called with exactly one argument (`len(sys.argv) == 2`, `sys.argv[0]` is the script name), it retrieves the tip by numeric ID (see the left column on the tips page).

	- called with any other argument length, it takes a random tip from the retrieved `dict` using `random.choice`.

- It retrieves the tip from the `tips dict` and creates the tweet using the `TWEET` template and prints it to stdout. For now I am happy to manually post it. See a demo towards the end of this article.

## Parsing the tips

At this point the code at best will throw an `AttributeError` because it does not have a tips `dict` to pull a tip from. So let's write `retrieve_tips`:

	def retrieve_tips():
		"""Grab and parse all tips from https://codechalleng.es/tips
		returning a dict of keys: tip IDs and values: Tip namedtuples
		"""

Firt we need to retrieve the page with `requests`:

		html = requests.get(TIPS_PAGE)

We instantiate a `BeautifulSoup` object passing it in the response text and parser:

		soup = BeautifulSoup(html.text, 'html.parser')

As we saw all tips are in a table, each one in a table row or `tr`, so let's get all those:

		trs = soup.findAll("tr")

Next let's use return data structure. At first I used a `list` but later wanted to index by tip ID, so a `dict` turned out to be more appropriate:

		tips = {}

Next let's loop through the rows and make a Tip `namedtuple` object:

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

Wait, what is going on here?

- First I get al table cells or `td` elements in the table row.

- I parse the tip ID from the first cell, stripping off the dot and storing it in a variable called `id_`.

- The tip html is in the second table cell.

- I see if there any links in the tips html. As you scroll down on the [tips page](https://codechalleng.es/tips) there is always a share link (Twitter icon), and there is an optional second resource link (Info icon).

- I put the tip code in a variable called `code`.

- Then I check if the tip was already shared on Twitter by checking if `PYBITES_HAS_TWEETED` ('pybites/status') is in the share link. If so we want to exclude it.

- Next we put the tip txt in a variable called `tip`.

- We add the optional resource link in a variable called `src`. As it's optional we first check the length of the `links` list.
- Finally we make the `Tip namedtuple` and assign it as value to the `id_` key in the `tips dict`.

Lastly let's return the tips `dict`:

    return tips

Let's see if this works using `pprint`:

![adding a pprint]({filename}/images/selenium-carbon/add-pprint.png)

Running this:

![getting a tips dict]({filename}/images/selenium-carbon/tips-dict.png)

Great. Let's make a carbon image next.

## Meet carbon: beautiful images of your source code

This is carbon:

![carbon home]({filename}/images/selenium-carbon/carbon-home.png)

It allows you add code, choose a language and other settings, then generate and tweet it out. Really awesome.

Of course we want to automate some of this. While playing with this tool I found that clicking the Tweet button it would generate a shareable picture hosted on Twitter :)

For example clicking the Tweet button I get this popup:

![clicking tweet button]({filename}/images/selenium-carbon/clicking-tweet-button.png)

And that Twitter link shows the generated code snippet image:

![resulting carbon image]({filename}/images/selenium-carbon/resulting-carbon-image.png)

This is why I made the TWEET\_BTN\_CLASS constant. We will use Selenium next to target this button to generate the image for us.

## Use Selenium to create tip code image

Let's write the second function `get_carbon_image`:

	def get_carbon_image(tip):
		"""Visit carbon.now.sh with the code, click the Tweet button
		and grab and return the Twitter picture url
		"""

First we need to encode (replace special characters) the code. `quote_plus` _also replace spaces by plus signs, as required for quoting HTML form values when building up a query string to go into a URL_ ([docs](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote_plus)).

		code = urllib.parse.quote_plus(tip.code)

We define the full url:

		url = CARBON.format(code=code)

Start the Chromedriver. Unlike [last time](https://pybit.es/selenium-headless-on-heroku.html) I am not going to use _headless_ mode here, I am OK with Selenium opening a browser to see what happens, `driver.get` actually does that.

		driver = webdriver.Chrome()
		driver.get(url)

Here we locate mentioned `TWEET_BTN_CLASS` ('jsx-2739697134') button and click on it:

		driver.find_element_by_class_name(TWEET_BTN_CLASS).click()

Trial and error taught me that this might have a slight delay so let's `sleep` a bit:

		sleep(5)  # this might take a bit

## Retrieve the image from popup

And here is the tricky part. The Tweet button opened a popup but the driver is still on the main browser page window. You can use the `driver`'s `switch_to.window` though to switch to it:

		window_handles = driver.window_handles
		driver.switch_to.window(window_handles[1])

Now I am on the popup window and I can target the status ID field and grab the image URL from it:

		status = driver.find_element_by_id('status')
		img = status.text.split(' ')[-1]

Finally I quite the `driver` (this closes the browser) and return the image string:

		driver.quit()
		return img

## See it in action

Here you can see this automation script in action, first generating an image from a random tip, then from a specific tip ID:

<div class="container">
▸␣␣␣<iframe src="https://www.youtube.com/embed/V3-7RvipiSU" frameborder="0" allowfullscreen class="video"></iframe>
</div>

And voilà: two new tips posted to our Twitter ([here](https://twitter.com/pybites/status/1100343735299252225) and [here](https://twitter.com/pybites/status/1100342422473719809)).

After manually tweeting it out as [@pybites](https://twitter.com/pybites), we set the obtained tweet URL on the tip (in the DB) so it's not selected upon next run.

### Room for improvement

Here are some things we can do to take it to the next level:

1. Auto-post the tweet to Twitter (we [already have the code](https://pybit.es/selenium-headless-on-heroku.html) for this).
2. Make a Tips API (pending article):
	- allow GET to retrieve a tip and POST to receive new ones,
	- do a `PUT` request on the tip with the tweet link after running this script and/or auto-posting to Twitter (1.)

Feel free to PR any of this [here](https://github.com/pybites/blog_code/pulls).

---

I hope you enjoyed this and it inspired you to build your own automation script. To learn how to run Selenium in headless mode on Heroku, check out [our article from last week](https://pybit.es/selenium-headless-on-heroku.html).

Feel free to share more Python tips [on our platform](https://codechalleng.es/inbox/new/pytip/).

What would you like us to write about more? You can leave a request [here](https://codechalleng.es/inbox/new/feature/).

And/or brainstorm with our amazing community, joining [our Slack](https://join.slack.com/t/pybites/shared_invite/enQtNDAxODc0MjEyODM2LTNiZjljNTI2NGJiNWI0MTRkNjY4YzQ1ZWU4MmQzNWQyN2Q4ZTQzMTk0NzkyZTRmMThlNmQzYTk5Y2Y5ZDM4NDU).

---

Keep Calm and Code in Python!

-- Bob
