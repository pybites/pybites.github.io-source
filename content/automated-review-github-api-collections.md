Title: Automating PyBites Review Post Using Github API and collections.defaultdict
Date: 2018-11-13 10:00
Category: Data
Tags: collections, defaultdict, re, regular expressions, requests, challenges, review post, parsing, string manipulation, github, API, requests
Slug: github-api-collections-defaultdict
Authors: Bob
Summary: In this post I share a quick script I produced last week to automate a portion of our review post. There are some nice idioms that you might find useful.
cover: images/featured/pb-article.png

In this post I share a quick script I produced last week to automate a portion of our review post. I used the Github API and the `collections.defaultdict`.

The goal of this script and post is to show you how to convert [open PRs](https://github.com/pybites/challenges/pulls) of [our challenges repo](https://github.com/pybites/challenges) into markdown for [our weekly review post](https://pybit.es/pages/challenges.html).

## Setting the stage

First I am importing the libraries to use and some constants:

	from collections import defaultdict
	import re

	import requests

	GH_API_PULLS_ENDPOINT = 'https://api.github.com/repos/pybites/challenges/pulls'
	PR_LINK = "https://github.com/pybites/challenges/pull/{id}"
	CHALLENGE_LINK = "http://codechalleng.es/challenges/{id}"
	EXTRACT_TEMPLATE = re.compile(r'.*learn\?\):\s+\[(.*?)\]Other.*')

We will use the `EXTRACT_TEMPLATE` regex in a bit. I had to escape the `?`, `)`, `[` and `]`, because they have special meaning in regex land. Here I want to match the literal ones which are part of the PR template.

## Parsing the review template

Each PR has a fixed template we use to have developers document their learning and provide us feedback. Here is my last submission for example:

	Difficulty level (1-10): [3]
	Estimated time spent (hours): [1]
	Completed (yes/no): [No]
	I stretched my coding skills (if yes what did you learn?): [Nice one to get back into Pandas, blabla ...]
	Other feedback (what can we improve?): []

I defined a helper to parse the learning part ("what did you  learn") from this template. As it might span multiple lines, I cannot just index a list, hence I used the `EXTRACT_TEMPLATE` regex to parse the full string.

The nice thing about `re.compile` is that you can define your regex once (here in a _constant_) and call regex methods like `sub` on it. The `\1` is the user's learning part I am interested in, which I captured using parenthesis in the regular expression.

Before anything else I make sure we're dealing with a single-line string by taking the `\r\n`s out (you can probably also use `re.M` = multi-line matching, but that does not always work for me):

	def get_learning(template):
		"""Helper to extract learning from PR template"""
		learning = ''.join(template.split('\r\n'))
		return EXTRACT_TEMPLATE.sub(r'\1', learning).strip()

By the way, I am not sure why I got a Windows-like `\r` but it does give me the opportunity to highlight two things here:

1. The first iteration of this script I did in a Jupyter notebook which is a great tool to play around with Python and document your progress!

2. Another great way to inspect a data structure when you are writing a script like this, is to pop a quick `import pdb;pdb.set_trace()` into your code (since Python 3.7 [we can actually use `breakpoint()`](https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c)).

## Github API and collections.defaultdict

To pull the open PRs from Github I don't need an API key. Secondly notice the nice way you can _chain_ operations in Python and the fact `requests` has a convenient `json` method. This is as expressive as it can get no?

	open_pulls = requests.get(GH_API_PULLS_ENDPOINT).json()

This is part of the `get_open_prs` function in which I loop through the pull requests and add each (PR number, learning) `tuple` into a `defaultdict` which I return. The nice thing about `defaultdict` is that it prevents having to write code to look for a key before inserting a value into the dictionary:

	def get_open_prs():
		"""Parse GH API pulls JSON into a dict of keys = code challenge ids
		and values = lists of (pr_number, learning) tuples"""
		open_pulls = requests.get(GH_API_PULLS_ENDPOINT).json()
		prs = defaultdict(list)

		for pull in open_pulls:
			pr_number = pull['number']

			pcc = pull['head']['ref'].upper()
			learning = get_learning(pull['body'])
			if learning:
				prs[pcc].append((pr_number, learning))

		return prs

I used a dictionary here to sort the code challenge ids (or "PCCs") as we'll see next.

## Print markdown compatible with our review post

Lastly I print the resulting `prs` dictionary sorting on key to show all PRs per challenge in ascending order (I needed the `<!-- -->` to visually separate blockquotes well):

	def print_review_markdown(prs):
		"""Return markdown for review post, e.g.
		https://pybit.es/codechallenge57_review.html ->
		Read Code for Fun and Profit"""
		for pcc, prs in sorted(prs.items()):
			challenge_link = CHALLENGE_LINK.format(id=pcc.strip('PCC'))
			print(f'\n#### [{pcc}]({challenge_link})')

			for i, (pr_number, learning) in enumerate(prs):
				if i > 0:
					print('\n<!-- -->')
				pr_link = PR_LINK.format(id=pr_number)
				print(f'\n> {learning} - [PR]({pr_link})')


And I have my `main` block to call the two functions:

	if __name__ == '__main__':
		prs = get_open_prs()
		print_review_markdown(prs)


## Running the script

You can check out the complete script in [our blog code repo](https://github.com/pybites/blog_code/blob/master/pybites_review/prs.py). Here is when I run it (output changes depending on the current open challenge PRs):

	$  python prs.py

	#### [PCC01](http://codechalleng.es/challenges/01)

	> Before this exercise I never came across dictionary comprehensions. A bit confusing at first! - [PR](https://github.com/pybites/challenges/pull/428)

	<!-- -->

	> testing - [PR](https://github.com/pybites/challenges/pull/427)

	#### [PCC03](http://codechalleng.es/challenges/03)

	> - Learned about SequenceMatcher. Great thing.- Started to think about how tests actually work, since I did get the results from the website but could not manage to pass the tests 8()- Heard about nltk (looks interesting). - [PR](https://github.com/pybites/challenges/pull/423)

	#### [PCC16](http://codechalleng.es/challenges/16)

	> I learn how to make request to remote database (in this project used RIPE DB) and how to parse JSON output from DB - [PR](https://github.com/pybites/challenges/pull/426)

---

We love automated scripts because the time saved each week easily compounds. It's also a nice way to hone your Python skills so I encourage you to always find opportunities to write these kind of utilities.

Feel free to share use cases in the comments below or on our Slack which you can join via [our platform](https://codechalleng.es).

---

Keep Calm and Code in Python!

-- Bob
