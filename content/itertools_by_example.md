Title: 5 cool things you can do with itertools
Date: 2017-01-12 23:55
Category: Modules
Tags: iterators, itertools, tricks, generators, game, notebooks, permutations
Slug: itertools-examples
Authors: Bob
Summary: Itertools is a very useful module. In this short post I show some 5 examples how you can use it. Some of this stuff might be useful in next week's challenge ...
cover: images/featured/pb-article.png

## What is itertools?

Itertools is a stdlib module that provides functions that create [iterators](http://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols) "inspired by constructs from APL, Haskell, and SML". See [the docs page](https://docs.python.org/3/library/itertools.html), [pymotw](https://pymotw.com/2/itertools/), as well as [this great EuroPython preso](https://github.com/vterron/EuroPython-2016/blob/master/kung-fu-itertools.ipynb).

## 5 cool things you can do with itertools

I created [this notebook](https://github.com/pybites/blog_code/blob/master/notebooks/itertools.ipynb) so you can follow along. Below a summary:

### 1. Use product to get all combinations between two iterators

Common game techniques: build a card deck or roll two dices:

	import itertools
	import random 

	# from Fluent Python
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'S D C H'.split() # spades diamonds clubs hearts
	# but instead of double list comprehension, using product
	cards = ['{}{}'.format(*p) for p in itertools.product(suits, ranks)]

Another use case: roll 2 dices ([SO is your friend](http://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions-in-python)): 

	dice = range(2, 7)
	random.choice([p for p in itertools.product(dice, repeat=2)])

	# output: 
	(5, 2)
	(2, 5)
	(2, 5)
	(6, 5)

### 2. Show a progress spinner for a console app

From [before-mentioned EuroPython preso](https://github.com/vterron/EuroPython-2016/blob/master/kung-fu-itertools.ipynb):

	import itertools
	import sys
	import time

	def spinner(seconds):
		"""Show an animated spinner while we sleep."""
		symbols = itertools.cycle('-\|/')
		tend = time.time() + seconds
		while time.time() < tend:
			# '\r' is carriage return: return cursor to the start of the line.
			sys.stdout.write('\rPlease wait... ' + next(symbols)) # no newline
			sys.stdout.flush()
			time.sleep(0.1)
		print() # newline

	if __name__ == "__main__":
		spinner(3)

### 3. Use dropwhile to get counts of >= n in a Counter dict

Given a books Counter object, get me books with >= 2 occurences. 

I needed this for my [tools of titans kata](http://bobbelderbos.com/2016/12/code-kata/) to see which books got recommended more than once by Tim Ferriss' podcast guests. 

	def get_multiple_mentions(books, keep=2):
		for key, count in itertools.dropwhile(lambda key_count: key_count[1] >= keep, books.most_common()):
			del books[key]
		return books

	# filters all books with count (occurence = 1) out:
	Counter({'4-hour-workweek-escape-live-anywhere': 2,
			'alchemist-paulo-coelho': 2,
			'atlas-shrugged-ayn-rand': 3,
			'black-swan-improbable-robustness-fragility': 2,
			'checklist-manifesto-how-things-right': 2,
			...

### 4. Combinations and permutations

For the difference read [this great explanation](https://betterexplained.com/articles/easy-permutations-and-combinations/). 

Given a list of friends how many pairs can be formed?

	friends = 'bob tim julian fred'.split()
	# as these are "Combinatoric generators" I consume them here for example purposes using list()
	list(itertools.combinations(friends, 2))

	# output:
	[('bob', 'tim'),
	('bob', 'julian'),
	('bob', 'fred'),
	('tim', 'julian'),
	('tim', 'fred'),
	('julian', 'fred')]

How many 4 letter strings can you from 7 letters? (hint: upcoming challenge)

	import string
	letters = random.sample(string.ascii_uppercase, 7)
	len(list(itertools.permutations(letters, 4)))
	# = 840 (7 * 6 * 5 * 4)

### 5. Groupby to count amount of keys for specific value in dict

Count the number of keys for a value, for example count the number of users (keys) that have email as pref (value) in a user_prefs dict.

This example is based on the one I found at [pymotw](https://pymotw.com/2/itertools/).

	# set up dict
	users = 'tim bob julian sue fred frank maria'.split()
	prefs = 'email phone IM email F2F email phone'.split()
	user_prefs = dict(zip(users, prefs))
	user_prefs

	user_prefs_sorted = sorted(user_prefs.items(), key=itemgetter(1))
	for pref, users in itertools.groupby(user_prefs_sorted, key=itemgetter(1)):
		print(pref, list(map(itemgetter(0), users)))

	# output: 
	F2F ['fred']
	IM ['julian']
	email ['frank', 'tim', 'sue']
	phone ['bob', 'maria']

## Practice

Enough theory. This stuff only sinks in when you actively start using it.

You can now get plenty of exercise via [our itertools learning path](https://codechalleng.es/bites/paths/itertools).
