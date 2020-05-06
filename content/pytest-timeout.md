Title: How to Debug a Hanging Test Using pytest
Date: 2020-03-18 21:15
Category: Testing
Tags: testing, debugging, pytest, pytest-timeout, APIs, tricks, learning, requests, pip, time
Slug: pytest-timeout
Authors: Bob
Summary: Today a wanted to share a neat trick that might save you some headache: debugging a hanging test.
cover: images/featured/pb-article.png

Today a wanted to share a neat trick that might save you some headache: debugging a hanging test.

## Setup

Let's write some really simple (contrived) code to test:

	from time import sleep

	def call_api():
		return dict(
			status=200,
			response=[1, 2, 3])


	def sum_numbers(numbers):
		return sum(numbers)


And some test code to test it:

	from script import sum_numbers, call_api


	def test_sum_numbers():
		assert sum_numbers([1, 2, 3]) == 6
		assert sum_numbers([4, 5]) == 9


	def test_call_api():
		resp = call_api()
		assert resp['status'] == 200
		assert resp['response'] == [1, 2, 3]

Run `pytest` and: `2 passed in 0.03s` - all good.

Now let's emulate a hanging test by adding a sleep of 60 seconds in `call_api`

Oops:

	(venv) [bobbelderbos@imac test-debug]$ pytest
	===================================================================== test session starts ======================================================================
	platform darwin -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
	rootdir: /Users/bobbelderbos/code/test-debug
	plugins: timeout-1.3.4
	collected 2 items

	test_script.py . (hangs here)

Eventually you'll get there (`2 passed in 60.06s (0:01:00)`), but this might be far worse.

Even with 1 or 2 minutes delay, you need to fix it. Tests need to be fast, because you will constantly run them to refactor and adding new features.

## Debugging timeouts

I discovered a neat plugin for this: [pytest-timeout](https://pypi.org/project/pytest-timeout/). With your virtualenv enabled:

	pip install pytest-timeout

Let's use it:

	(venv) [bobbelderbos@imac test-debug]$ pytest --timeout=3
	test_script.py .F                                                                                                                                        [100%]

	=========================================================================== FAILURES ===========================================================================
	________________________________________________________________________ test_call_api _________________________________________________________________________

	def test_call_api():
	>       resp = call_api()

	test_script.py:10:
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

	def call_api():
	>       sleep(60)
	E       Failed: Timeout >3.0s

	script.py:5: Failed
	=================================================================== short test summary info ====================================================================
	FAILED test_script.py::test_call_api - Failed: Timeout >3.0s
	================================================================= 1 failed, 1 passed in 3.07s

How cool is that, no?

## A more complex use case

What if the bug is in some external module though?

Here I pulled a fork of `requests` and:

- added a `import time; time.sleep(60)` to the `get` function of the `api` module,

- added `import requests; requests.get('https://pybit.es')` to my `call_api` function,

- cd'd into the _requests_ subfolder and did a `pip install -e .` to install THIS modified version (as opposed the one on the net).

		(venv) [bobbelderbos@imac test-debug]$ pip freeze|grep request
		-e git+git@github.com:bbelderbos/requests.git@4bda7b66e7ece5be51b459edd046a70915b4792c#egg=requests

And ... boom!

	(venv) [bobbelderbos@imac test-debug]$ pytest --timeout=3
	===================================================================== test session starts ======================================================================
	platform darwin -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
	rootdir: /Users/bobbelderbos/code/test-debug
	plugins: timeout-1.3.4
	timeout: 3.0s
	timeout method: signal
	timeout func_only: False
	collected 2 items

	test_script.py .F                                                                                                                                        [100%]

	=========================================================================== FAILURES ===========================================================================
	________________________________________________________________________ test_call_api _________________________________________________________________________

		def test_call_api():
	>       resp = call_api()

	test_script.py:10:
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
	script.py:5: in call_api
		requests.get('https://pybit.es')
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

	url = 'https://pybit.es', params = None, kwargs = {}

		def get(url, params=None, **kwargs):
			r"""Sends a GET request.

			:param url: URL for the new :class:`Request` object.
			:param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
			:param \*\*kwargs: Optional arguments that ``request`` takes.
			:return: :class:`Response <Response>` object
			:rtype: requests.Response
			"""
	>       time.sleep(60)
	E       Failed: Timeout >3.0s

## Getting more debug info

What if the failing code is more layers down?

Sometimes the issue is really nested and `pytest-timeout` might not be that smart. 

In that case you can swap the default `signal` of the `--timeout_method` flag for `thread` and it will dump a complete stacktrace!

This can be very useful for debugging:

	(venv) [bobbelderbos@imac test-debug]$ pytest --timeout=3 --timeout_method=thread
	===================================================================== test session starts ======================================================================
	platform darwin -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
	rootdir: /Users/bobbelderbos/code/test-debug
	plugins: timeout-1.3.4
	timeout: 3.0s
	timeout method: thread <== using "thread now"
	timeout func_only: False
	collected 2 items

	test_script.py .
	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Timeout ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Stack of MainThread (4523748800) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	...
	many calls
	...

	File "/Users/bobbelderbos/code/test-debug/venv/lib/python3.8/site-packages/_pytest/python.py", line 184, in pytest_pyfunc_call
		result = testfunction(**testargs)
	File "/Users/bobbelderbos/code/test-debug/test_script.py", line 10, in test_call_api
		resp = call_api()
	File "/Users/bobbelderbos/code/test-debug/script.py", line 5, in call_api
		requests.get('https://pybit.es')
	File "/Users/bobbelderbos/Downloads/requests.org/requests/api.py", line 71, in get <== external module
		time.sleep(60)

	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Timeout ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	(venv) [bobbelderbos@imac test-debug]$

Really cool stuff.

I hope this is useful. Comment below next time this saves you some debugging time ...

---

Keep Calm and Code in Python!

-- Bob
