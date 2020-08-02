Title: Learning Python Decorators by Example
Date: 2017-10-20 12:00
Category: Concepts
Tags: decorators, design patterns, logging, caching, memoization, Flask, Django, properties, classmethod, staticmethod, lru_cache, mock.patch, contextmanager
Slug: decorators-by-example
Authors: Bob
Summary: Decorators are a sometimes overlooked feature and they might be hard to grasp for beginning Pythonistas. I agree with Aaron Maxwell that mastering them "can massively magnify the positive impact of the code you write", so make sure you add them to your toolkit if not done so already. In this article I explain what they do, why you want to use them and give some practical examples.
cover: images/featured/pb-article.png

Decorators are a sometimes overlooked feature and they might be hard to grasp for beginning Pythonistas. I agree with Aaron Maxwell that mastering them "can massively magnify the positive impact of the code you write", so make sure you add them to your toolkit if not done so already. In this article I explain what they do, why you want to use them and give some practical examples.

![decorators are a bit like Russian dolls]({filename}/images/banners/pb_decorators.png)

## Definition

> A decorator is any callable Python object that is used to modify a function, method or class definition. A decorator is passed the original object being defined and returns a modified object, which is then bound to the name in the definition. - [PythonDecorators wiki](https://wiki.python.org/moin/PythonDecorators)

GoF's [Design Patterns](http://www.amazon.com/dp/0201633612/?tag=pyb0f-20) defines a decorator's intent as:

> Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

Two common use cases are caching and access checks in web frameworks which I will cover later.

## When to use?

If you want to add common behavior to multiple objects think about abstracting it away using decorators. It will make your code more DRY and encapsulated. It is a nice way to abstract away functionality not directly related to the function's main goal. Your team will thank you for having more reusable code.

Aaron Maxwell wrote a nice article in this context: [5 reasons you need to learn to write Python decorators](https://www.oreilly.com/ideas/5-reasons-you-need-to-learn-to-write-python-decorators).

## Syntax

Python lets you decorate a function (or class) by the `@` symbol followed by the decorator.

For example:

	@mydecorator
	def my_function(args):
		...

Note that this is the same as:

	def my_function(args):
		...
	my_function = mydecorator(my_function)

The '@' syntactic sugar is more concise and easier to read though.

Decorators can be stacked and will be run inside out:

	@second_decorator
	@first_decorator
	def my_function(args):
		...

This can be quite confusing so I found a good example [on SO](https://stackoverflow.com/a/739665):

	def makebold(fn):
		def wrapped():
			return "<b>" + fn() + "</b>"
		return wrapped

	def makeitalic(fn):
		def wrapped():
			return "<i>" + fn() + "</i>"
		return wrapped

	@makebold
	@makeitalic
	def hello():
		return "hello world"

	print hello()  ## returns "<b><i>hello world</i></b>"

(now you know why I put Russian dolls in the banner)

What about passing arguments?

[Expert Python](http://www.amazon.com/dp/1785886851/?tag=pyb0f-20) provides a nice commented snippet of the complete pattern:

	def mydecorator(function):
		def wrapped(*args, **kwargs):     
			# do some stuff before the original
			# function gets called
			result = function(*args, **kwargs)
			# do some stuff after function call and
			# return the result
			return result
		# return wrapper as a decorated function
		return wrapped

Make sure to add [`functools.wraps`](https://docs.python.org/3.7/library/functools.html#functools.wraps) decorator so the original name and docstring (metadata) are not lost, specially important when debugging:

	def mydecorator(function):
		@wraps(function)
		def wrapped(*args, **kwargs):
		...

---

Before you read any further, maybe it's a good time to roll a decorator of your own!

Check out our [Decorators and Context Managers Learning Path](https://codechalleng.es/bites/paths/decorators-context) and write some code. Decorators (or any Python concept for that matter) only really stick if you write the code yourself ...

---

## Some practical examples

I went back to our code base and found two examples where we used decorators:

### Caching

For our [100 Days of Code](https://pybit.es/special-100days-of-code.html) I wrote a class to cache The Movie Database (TMDb) API responses ([source](https://github.com/pybites/100DaysOfCode/tree/master/095)):

	@store_results
	def get_items(self, obj_method):
		...

`decorators.py`

	def store_results(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			func_name = str(args[1]).lower()
			kind = re.sub(r'.*bound.*?\.(\S+) of.*', r'\1', func_name)
			print(kind)
			resp = f(*args, **kwargs)
			_store(kind, resp)
			print(len(resp))
			return resp
		return wrapped

Another caching example can be found [here](http://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/).

For caching / memoization you also might want to learn about [@functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache).

> In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. - [Wikipedia](https://en.wikipedia.org/wiki/Memoization)

For Django checkout [cached_property](https://docs.djangoproject.com/en/1.11/ref/utils/#django.utils.functional.cached_property) demo'd [here](https://lincolnloop.com/blog/django-patterns-fat-models-and-cached_property/). What's cool about it is that you can dramatically reduce making database calls improving your site's performance.

### Access checking

In [Never Forget A Friend’s Birthday with Python, Flask and Twilio](https://www.twilio.com/blog/2017/09/never-forget-friends-birthday-python-flask-twilio.html) I used a decorator to check login ([source](https://github.com/pybites/bday-app/blob/master/app.py)):

	def login_required(test):
		'''From RealPython Flask course'''
		@wraps(test)
		def wrap(*args, **kwargs):
			if 'logged_in' in session:
				return test(*args, **kwargs)
			else:
				flash('You need to log in first')
				return redirect(url_for('login'))
		return wrap

A similar example can be found [here](http://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/).

Distinguishing between public and private endpoints just takes one line of extra code. It's a nice way of abstracting away the access implementation so it does not clutter and distract from writing the main Flask code:

	@app.route('/login', methods=['GET', 'POST'])
	def login():
		...

	@app.route('/')
	@login_required
	def index():
		...

## Decorators in the wild

* See Python's [Built-in Functions](https://docs.python.org/3/library/functions.html) for some decorators that come with the Python language:

	* `@property` we covered [here](https://pybit.es/property-decorator.html) and it's an awesome decorator.
	* `@staticmethod` and `@classmethod` you probably want to know about, they are well explained [in this Real Python article](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/).
	* Another important one to add to your toolbox is [contextlib.contextmanager](https://docs.python.org/3.7/library/contextlib.html#contextlib.contextmanager) which we used for [code challenge #09](https://pybit.es/codechallenge09_review.html).

* In the previous section, right above `login_required` was the all too common `@app.route` Flask decorator. [This article](https://ains.co/blog/things-which-arent-magic-flask-part-1.html) explains *how Flask makes it possible to write "@app.route()" at the top of the function*. Another interesting discussion about this decorator and Flask's source in general can be found in [The Hitchhiker's Guide to Python](http://www.amazon.com/dp/1491933178/?tag=pyb0f-20).

* The [Click](http://click.pocoo.org/5/) package (Flask author) shows another elegant use of decorators.

* Lastly take notice of [`mock.patch`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch) which I used [here](https://github.com/pybites/100DaysOfCode/blob/master/081/test_whotweeted.py). It wraps each test method faking (mocking) the `get_status` *Tweepy* API to not hit the API while testing.

## Advanced concepts

One less obvious aspect of decorators for me was the passing of optional arguments, so I wrote [an article about it](https://pybit.es/decorator-optional-argument.html).

See [this article](https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv) for more examples of decorators that take arguments and how to decorate classes.

## Don't stop here ... practice!

All you've read so far is only useful if you PUT IT INTO PRACTICE!

So head over to our [Decorators and Context Managers Learning Path](https://codechalleng.es/bites/paths/decorators-context) and start coding ...

---

Keep Calm and Code in Python!

-- Bob
