Title: 10 Tips to Get More out of Your Regexes
Date: 2017-03-15 7:45
Category: Tips
Tags: regex, tips, parsing, regular expressions, findall
Slug: mastering-regex
Authors: Bob
Summary: Regular expressions can be arcane, yet when used with care they can also be very powerful. In this post a couple of tips to get more out of your regexes when using Python's re module.
cover: images/featured/pb-article.png

Regular expressions can be arcane, yet when used with care they can also be very powerful. In this post a couple of tips to get more out of your regexes when using Python's re module.

> Some people, when confronted with a problem, think, "I know, I'll use regular expressions." Now they have two problems. - Jamie Zawinski

## 1. Do we need a regex?

First and foremost don't overuse them, specially when you can use simple string operations.

I like this comparison [by Jeff Atwood](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/), explaining the quote above:

> Regular expressions are like a particularly spicy hot sauce – to be used in moderation and with restraint only when appropriate.

	>>> import re
	>>> text = 'regexes are powerful but use with care, some more text, lets play!'

	# overkill!
	>>> re.sub(r'some', 'a bit', text)
	'regexes are powerful but use with care, a bit more text, lets play!'
	>>> re.match(r'^regex', text)
	<_sre.SRE_Match object; span=(0, 5), match='regex'>

	# just use
	>>> text.replace('some', 'a bit')
	'regexes are powerful but use with care, a bit more text, lets play!'
	>>> text.startswith('regex')
	True

## 2. re.match() vs re.search()

* match() checks at the start of a string and returns None if nothing is found.
* search() moves up the string, looking for the first occurrence of the given pattern, and returns None only if the pattern occurs nowhere in the string.

		>>> text = 'Use match vs search appropriately'
		>>> re.match('search', text)
		# don't do:
		>>> re.match('.*search', text)
		# better:
		>>> re.search('search', text)
		<_sre.SRE_Match object; span=(13, 19), match='search'>

## 3. Non-capturing parenthesis 

Use (?: ) to not capture matching contents, for example lets get all links and hashtags out of the tweet below. I need the outer parenthesis for capturing and the inner parenthesis to say '# or http', latter should not capture anything:

	>>> tweet = 'New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html … #python #APIs'
	>>> re.findall(r'((?:#|http)\S+)', tweet)
	['http://pybit.es/requests-cache.html', '#python', '#APIs']

When I don't use (?: ) it goes wrong:

	>>> re.findall(r'((#|http)\S+)', tweet)
	[('http://pybit.es/requests-cache.html', 'http'), ('#python', '#'), ('#APIs', '#')]

## 4. Always use raw string (r'<your_regex>')

The [excellent Regex HOWTO](https://docs.python.org/3.6/howto/regex.html) gives a nice example: in order to match \section you end up writing \\\\\\\\section in your regex :( 

> The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with 'r', so r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline. Regular expressions will often be written in Python code using this raw string notation.

Regexes can be complex enough, use r'' and take escaping out of the equation.

## 5. Regexes are greedy!

Take this modified html from our blog: 

	html = """<div><p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p></div>"""

Imagine we want to match the first paragraph:

	>>> m = re.search('<p>.*</p>', html)

Oops, it matched too much:

	>>> m.group()
	'<p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p>'

You can prevent this default greediness by using the ? after the repeating metacharacter (*, +, etc) which makes it match as little text as possible:

	>>> m = re.search('<p>.*?</p>', html)
	>>> m.group()
	'<p>Today a quick article on a nice caching module when working with APIs.</p>'
	 
## 6. Backreferences are powerful

I like this example from the HOWTO: find double words in a text:

	>>> p = re.compile(r'(\b\w+)\s+\1')
	>>> p.search('Paris in the the spring').group()
	'the the'

See also 8/re.sub where we use them for string replacements.

## 7. findall (finditer) is awesome

We used it [here](https://github.com/pybites/blog_code/blob/1f4dc534d43ec2c8582a890a15fb54486b58af39/katas/course_time/js_course_time_scraper.py) for example to get al mm:ss timestamps of a course TOC, very cool:

	def search_file(file):
    	file_content = open(file).read()  # should have used with
	    time_regex = re.compile(r'\(\d+:\d+\)')  # seems we needed literal parenthesis as part of the match
		return time_regex.findall(file_content) 

Output: 

	$ python js_course_time_scraper.py

	# intermediate result from findall:
	['(3:47)', '(4:41)', '(1:21)', '(5:32)', '(2:23)', '(1:01)', ...
	
	# further parsing + sum
	The course takes 6.841944444444445 hours to complete.

## 8. String replacements

re.sub is your friend, I use it quite often, for example [for our last challenge](https://github.com/pybites/challenges/blob/master/10/movies.py) to extract a movie title:

	MOVIE_TITLE = re.compile(r'\d+\.\s+(.*)\s\(.*').sub
	
	def get_movie():
		with open('movies.txt') as f:
			rand_line = random.choice(f.readlines())
			return MOVIE_TITLE(r'\1', rand_line.rstrip())

Use subn to also get the number of replacements done. Here for example it stripped 6 html tags:

	>>> html
	'<div><p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p></div>'
	>>> def strip_html(text):
	...     return re.subn(r'<[^<]+?>', '', text)  # non-greediness again
	...
	>>> strip_html(html)
	('Today a quick article on a nice caching module when working with APIs.Read more ...', 6)

re.sub even can take a function, nice example from [the documentation](https://docs.python.org/2/library/re.html):

	>>> def repl(m):
	...     inner_word = list(m.group(2))
	...     random.shuffle(inner_word)
	...     return m.group(1) + "".join(inner_word) + m.group(3)
	>>> text = "Professor Abdolmalek, please report your absences promptly."
	>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
	'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'

## 9. Compilation flags / modifiers

See [this table](https://docs.python.org/3.6/howto/regex.html#compilation-flags): apart from re.I (IGNORECASE), I don't use them often, but they can be very handy when your match spans various lines or working with other character sets.

The VERBOSE (X) flag can make a regex much more readable as nicely shown [in Jeff Atwood's article](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/) or taking this example from the [mentioned HOWTO](https://docs.python.org/3.6/howto/regex.html):

	pat = re.compile(r"""
	\s*                 # Skip leading whitespace
	(?P<header>[^:]+)   # Header name
	\s* :               # Whitespace, and a colon
	(?P<value>.*?)      # The header's value -- *? used to
						# lose the following trailing whitespace
	\s*$                # Trailing whitespace to end-of-line
	""", re.VERBOSE)

## 10. Python's unique naming style

Another readability feature is Python's specific regex syntax for named groups. This allows you to grab matches by key instead of number. I have not used this much, but writing one now I really like this so planning to adopt this syntax: 

	>>> bio = '''
	... name: Bob Belderbos
	... country: Spain
	... language: Python'''

	>>> m = re.search(r'name: (?P<name>.*)\ncountry: (?P<country>.*)\nlanguage: (?P<lang>.*)', bio)
	>>> m.group('name')
	'Bob Belderbos'
	>>> m.groupdict()
	{'name': 'Bob Belderbos', 'country': 'Spain', 'lang': 'Python'}

---

## Further reading

* [Regular Expression HOWTO doc](https://docs.python.org/3.6/howto/regex.html) 

* [Docs: 6.2. re — Regular expression operations](https://docs.python.org/3.6/library/re.html)

* [Wesley Chun's book Core Python Applications Programming](http://amzn.to/2mHe00T) - Chapter 1. Regular Expressions

* [Codinghorror article: Regular Expressions: Now You Have Two Problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)

* To go really deep: [Mastering Regular Expressions](http://amzn.to/2n5AFYh) is THE book on regular expressions, an awesome reference. Note though that language specific chapters include Perl/Java/.NET/PHP, not Python. 

* Lookahead assertions: I have not needed those yet, but they have their use cases. They finally 'clicked' reading [the example of the HOWTO](https://docs.python.org/3.6/howto/regex.html#lookahead-assertions).

---

I hope you picked up something useful from this article. Use the comments below to share any cool regexes you use on a regular basis. 

Cheers

## Update Reddit

Thanks for [the upvotes](https://redd.it/5ziccw), some useful feedback:

* To test your regexes you can use [regex101](https://regex101.com/#python) or [this site](https://extendsclass.com/regex-tester.html#python) for explaining how a pattern is being matched. See the Reddit thread for some other ones.

* Above HMTL examples are to show regex, but in real life you should use a parser (plenty of [options](https://www.google.com/search?q=html+parser+python&oq=html+parser+&aqs=chrome.0.0l2j69i57j0l3.2035j0j7&sourceid=chrome&ie=UTF-8)), see also SO ["You can't parse HTML with regex"](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454).

* [regex 2017.02.08](https://pypi.python.org/pypi/regex/) is an alternative regex module, a superset of re.

## Update June 2017

There was a gentle intro to regex at PyCon 2017 by Al Sweigart: *Yes, It's Time to Learn Regular Expressions*:

<div class="container">
	<iframe src="https://www.youtube.com/embed/abrcJ9MpF60" frameborder="0" allowfullscreen class="video"></iframe>
</div>

---

Keep Calm and Code in Python!

-- Bob
