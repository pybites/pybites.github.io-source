Title: 7 Tips to Improve Your Error Handling in Python
Date: 2020-05-06 14:08
Category: Concepts
Tags: exceptions, exception handling, anti-patterns, EAFP, best practices, pitfalls
Slug: pythonic-exceptions
Authors: Bob
Summary: Error handling in Python can be simplified by following these 7 tips.
cover: images/featured/pb-article.png

Error handling in Python can be simplified by following these 7 tips.

## 1. Explicit is better than implicit

This is basic exception clause breakdown in Python:

	try:
		...
	except ...:
		# handle exception
	except ...:
		# handle another exception
	(optionally)
	else:
		# code if no exception was hit
	finally:
		# cleanup code, always executes

So `try` + `except` is all it takes, but with freedom comes responsibility. A bare `try except:` might cause you headaches debugging. So name your exceptions specificly.

Note that order matters here. Address more specific exceptions before more general ones. If you put `Exception` before `ZeroDivisionError` for example, it will become a catch-all.

## 2. Flat is better than nested

Raising an exception (using `raise`) is a great way to avoid unnecessary indenting in your code.

Take one of our Bites. Right off the bat we raise an exception if the input doesn't make sense:

	def pretty_date(date):
		"""Receives a datetime object and converts/returns a readable string"""
		if not isinstance(date, datetime) or date > NOW:
			raise ValueError('expecting past date')

## 3. Write custom exceptions

This is literally all it takes:

	class NoInternetConnection(Exception):
		"""Exception raised when there is no internet"""

(We have always used `pass` here, but [Python in a Nutshell](http://www.amazon.com/dp/B06Y4DVSBM/?tag=pyb0f-20), actually suggests using a docstring instead.)

The advantage: it's like a _contract_ with the caller of your function (_this is how we gonna play the game_).

It can increase the readability of your code as your module has more specific (granular) expressions as compared to the standard library ones.

You could even build up exception class hierarchies and namespace them by using a dedicated module [like the `requests` library does](https://github.com/psf/requests/blob/master/requests/exceptions.py).

When to do this? [Here](https://stackoverflow.com/a/43772787) is a good answer:

> Generally, the only times you should be defining your own exceptions are when you have a specific case where raising a custom exception would be more appropriate than raising a existing Python exception.

## 4. Keep your try/except blocks narrow

Because handling too many exceptions is a red flag.

Reducing the amount of code in your `try` block limits this temptation, which reduces the amount of error handling code you'll need.

## 5. Actually use them

Instead of excessive condition checking (aka _look before you leap_), it's [_easier to ask for forgiveness than permission_ (EAFP)](https://docs.python.org/3.4/glossary.html).

As we showed in [our previous exception handling article](https://pybit.es/error_handling.html) instead of checking:

	if os.path.exists("file.txt"):
		...

It's more idiomatic (_pythonic_) to just _try_ things and catch the corresponding exception(s):

	try:
		# assume the file is there
		os.unlink("file.txt")
	except OSError:
		# if not, handle the exception

## 6. Verbose logging

Be verbose in your logging. As stated [here](https://stackoverflow.com/a/5191885) can use [`logger.exception`](https://docs.python.org/3/library/logging.html#logging.Logger.exception) to log the stack trace alongside the error message.

## 7. Rely on tools (remote environments)

We can have perfect exception handling, but sometimes something slips through the cracks. You can use a tool like [Sentry](https://sentry.io/welcome/) to send you an email when a user hits an unexpected error and doesn't tell you about it. Not only will you know right away, you will also get the full stacktrace which greatly helps fixing the issue.

---

I hope this helps. What have you learned dealing with exceptions in Python? Share you insights in the comments below.

Keep Calm and Code in Python!

-- Bob
