Title: 10 Cool Pytest Tips You Might Not Know About
Date: 2021-02-26 15:55
Category: Testing
Illustration: pytest-planes.jpeg
Tags: pytest, testing, tips, exceptions, logging, poetry, fixtures, floats, debugging, command line, pytest-pythonpath, capsys, caplog
Slug: pytest-tips
Authors: Bob
Summary: Here are 10 things we learned writing `pytest` code that might come in handy.
cover: images/featured/pb-article.png

Here are 10 things we learned writing `pytest` code that might come in handy:

## 1. Testing package structure

People new to `pytest` are often thrown off by this:

	:::console
	$ tree
	.
	├── src
	│   ├── __init__.py
	│   └── script.py
	└── tests
		└── test_script.py

	2 directories, 3 files

	$ more src/script.py
	def hello():
		return 'hello'

	$ more tests/test_script.py
	from src.script import hello


	def test_hello():
		assert hello() == "hello"

	$ pytest
	...
	ImportError while importing test module '/Users/bobbelderbos/Downloads/demo/tests/test_script.py'.
	Hint: make sure your test modules/packages have valid Python names.
	Traceback:
	/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/importlib/__init__.py:127: in import_module
		return _bootstrap._gcd_import(name[level:], package, level)
	tests/test_script.py:1: in <module>
		from src.script import hello
	E   ModuleNotFoundError: No module named 'src'
	============================================================================================= short test summary info ==============================================================================================
	ERROR tests/test_script.py
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	================================================================================================= 1 error in 0.42s =================================================================================================
	$ touch tests/__init__.py
	$ pytest
	...

	tests/test_script.py .                                                                                                                                                                                       [100%]
	================================================================================================ 1 passed in 0.19s =================================================================================================

So the `tests` directory needs an `__init__.py` file as well.

Setting your project up with [Poetry](https://python-poetry.org/docs/basic-usage/) makes this a lot easier / automatic.

If you don't turn your code directory into a package (so not including an `__init__.py` file), you might want to use [`pytest-pythonpath`](https://pypi.org/project/pytest-pythonpath/):

> ... a py.test plugin for adding to the PYTHONPATH from the pytests.ini file before tests run.

Thanks [Martin](https://twitter.com/martin_heroux) for telling us about this plugin.

## 2. Organize your fixtures

You can use a `conftest.py` file to create [your fixtures](https://pybit.es/pytest-fixtures.html) (setup and tear down code) for reuse across your test modules.

See more info [in the documentation](https://docs.pytest.org/en/stable/fixture.html?highlight=conftest#conftest-py-sharing-fixtures-across-multiple-files) and a practical example [in one of our projects](https://github.com/PyBites-Open-Source/pysource/tree/main/tests). This will definitely make your test modules leaner.

## 3. Filter out particular tests

You can use `pytest`'s `-k` switch to filter tests by expression:

```
  -k EXPRESSION         only run tests which match the given substring
                        expression. An expression is a python evaluatable
                        expression where all names are substring-matched
                        against test names and their parent classes. Example:
                        -k 'test_method or test_other' matches all test
                        functions and classes whose name contains
                        'test_method' or 'test_other', while -k 'not
                        test_method' matches those that don't contain
                        'test_method' in their names. ...
```

Or you can mark tests using `@pytest.mark`, for example:

```
@pytest.mark.slow
def test_func_slow():
    pass
```

For this to work though you need to register the mark in your `pytest.ini` file, as per [docs](https://docs.pytest.org/en/stable/mark.html):

```
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
```

Now you can run "slow" tests with: `pytest -m slow`.

Another cool use case is `@pytest.mark.skipif` to skip a test based on a condition:

	# comments.py (code with a syntax error)
	def time_printer():
		this line should be commented

	# test_comments.py
	import pytest

	def _can_import():
		try:
			import comments  # noqa F401
			return True
		except IndentationError:
			return False

	def test_import_fails_because_not_all_garbage_commented():
		if not _can_import():
			raise pytest.fail(…

	@pytest.mark.skipif(not _can_import(), reason="Only run if import works")
	def test_output_time_printer_with_time_arg_returns_string(capfd):
		# tests past successful import ...

	# nicer output + skip other test
	$ pytest [output truncated]
	E           Failed: comments.py raised an IndentationError, did you comment it properly?
	=== 1 failed, 1 skipped in 0.05 seconds ===

## 4. Testing floats

Ever hit this when testing `float`s? 

```
E       assert 0.30000000000000004 == 0.3
E        +  where 0.30000000000000004 = sum_numbers(0.1, 0.2)
```

Yikes!

No worries though, `pytest`'s `approx` has your back, this passes: 

```
assert sum_numbers(0.1, 0.2) == approx(0.3)
```

## 5. Working with temporary files

Creating and cleaning up temporary files can be a lot of work, but `pytest` makes this quite effortlessly.

In this example taken from [Bite 161](https://codechalleng.es/bites/161/) we create 5 files in a temporary directory and assert that `count_dirs_and_files` returns a tuple of counts (0 directories and 5 files):

```
def test_only_files(tmp_path):
    for i in range(1, 6):
        path = tmp_path / f'{i}.txt'
        with open(path, 'w') as f:
            f.write('hello')
    assert count_dirs_and_files(tmp_path) == (0, 5)
```

The files were created in a temporary directory and I did not have to clean anything up manually.

## 6. Testing exceptions

Here is an example from [Intro Bite #10](https://codechalleng.es/bites/110/) that uses `pytest.raises(...)` to test an exception:

	@pytest.mark.parametrize("numerator, denominator", [
		(2, 's'),
		('s', 2),
		('v', 'w'),
	])
	def test_divide_numbers_raises_value_error(numerator, denominator):
		with pytest.raises(ValueError):
			divide_numbers(numerator, denominator)

## 7. Enhance your parametrized tests

For this tip I changed `divide_numbers` to have `test_divide_numbers_raises_value_error` fail:

```
FAILED test_division.py::test_divide_numbers_raises_value_error[2-s] - TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

This is ok, but we can make the `[2-s]` part a bit more readable.

We can wrap the `parametrize` list arguments inside `pytest.param` giving it _test IDs_ (see [here](https://docs.pytest.org/en/stable/example/parametrize.html#different-options-for-test-ids)):

```
@pytest.mark.parametrize("numerator, denominator", [
    pytest.param(2, 's', id="denominator_wrong_type"),
    pytest.param('s', 2, id="numerator_wrong_type"),
    pytest.param('v', 'w', id="both_numerator_denominator_wrong_type"),
])
def test_divide_numbers_raises_value_error(numerator, denominator):
    with pytest.raises(ValueError):
        divide_numbers(numerator, denominator)
```

Now this string will show up in the failing test:

```
FAILED test_division.py::test_divide_numbers_raises_value_error[denominator_wrong_type] - TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

And we can target these strings with `pytest -k` as well, for example `pytest -k both_numerator` runs only the third test of `test_divide_numbers_raises_value_error`, `pytest -k numerator` would run two tests.

## 8. Drop into the debugger upon failure

This is one the most useful tips in my opinion: when something breaks you want to be able to debug right then and there.

So in the previous failing example if we run the tests with `pytest --pdb` it drops into the debugger:

	:::console
	> /Users/bobbelderbos/code/bitesofpy/110/division.py(9)divide_numbers()
	-> return int(numerator)/denominator
	(Pdb)

For more variations check out [the docs](https://docs.pytest.org/en/stable/usage.html#dropping-to-pdb-python-debugger-on-failures).

And in order to debug a hanging test, check out [our related article](https://pybit.es/pytest-timeout.html).

## 9. Test logging

You can test logging with `pytest`'s [`caplog` fixture](https://docs.pytest.org/en/stable/logging.html):

	# script.py
	import logging

	def func():
		logging.debug("a debug message to ignore")
		logging.info("an info message")
		try:
			1 / 0
		except ZeroDivisionError:
			logging.exception("cannot divide by 0")

	# test_script.py
	import logging

	from script import func

	def test_func(caplog):
		caplog.set_level(logging.INFO)
		func()
		record1, record2 = caplog.records
		assert record1.levelname == "INFO"  # no debug
		assert record1.message == "an info message"
		assert record2.message == "cannot divide by 0"
		assert record2.exc_info[0] is ZeroDivisionError

Here we made a function called `func` that logs 3 messages: `DEBUG`, `INFO` and `ERROR` (by the way, [`logging.exception`](https://docs.python.org/3/library/logging.html#logging.exception) is really useful, it adds exception info the logging message!)

In the test we use the `caplog` fixture to grab those logging messages and test them.

## 10. Test standard output

How to test a function that prints to standard output (as opposed to returning something)?

You can use the [`capsys` / `capfd` fixtures](https://docs.pytest.org/en/stable/capture.html) for this.

Here is an example from [Intro Bite #01](https://codechalleng.es/bites/101/).

Code (spoiler alert!):

```
MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
    print(f'{name} {is_allowed} to drive')
```

Tests:

```
from driving import allowed_driving


def test_not_allowed_to_drive(capfd):
    allowed_driving('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to drive'

...
```

---

I hope you learned something new and that you can use any of this when you are writing `pytest` code.

If you want to share other cool `pytest` tips, please comment below ...

Keep Calm and Write more Tests!

-- Bob
