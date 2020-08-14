Title: Freezegun - Real Joy for Fake Dates in Python
Date: 2020-08-14 19:10
Category: Modules
Tags: packages, testing, mocking, freezegun, datetime, timedelta
Slug: guest-freezegun
Authors: AJ Kerrigan
Summary: Freezegun is a library for mocking Python datetimes. It does one thing, does it well, and lets you get on with your life.
Cover: images/featured/pb-guest.png

### Introduction

If you've ever tested code involving dates and times in Python you've probably had to mock the [datetime](https://docs.python.org/3/library/datetime.html) module. And if you've mocked the datetime module, at some point it probably mocked you back when your tests failed.

![Icelandic horse mocks you](images/guest-freezegun/dan-cook-MCauAnBJeig-unsplash.jpg)
> Photo by [Dan Cook](https://unsplash.com/@dan_scape?utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_content=creditCopyText)

Let's look at some problems that pop up with fake datetimes, and how [freezegun](https://github.com/spulec/freezegun) can help address them.

### A simple test

First, here's a snippet of date-sensitive code:

_tomorrow.py_
```python
import datetime

def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)
```

When we test that function, we probably want the result to be the same every day. One way to handle that is by using a fake date in the test:

```python
import datetime
from unittest.mock import patch, Mock

import tomorrow

fake_date = Mock(wraps=datetime.date)
fake_date.today.return_value = datetime.date(2020, 7, 2)

@patch('datetime.date', fake_date)
def test_tomorrow():
    assert tomorrow.tomorrow() == datetime.date(2020, 7, 3)
```

That works, great! Now let's break it.

### A catalog of failures

Let's say that during a refactor, we change this:

```python
import datetime

def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)
```

to this:

```python
from datetime import date, timedelta

def tomorrow():
    return date.today() + timedelta(days=1)
```

or perhaps this:

```python
from datetime import date as dt, timedelta as td

def tomorrow():
    return dt.today() + td(days=1)
```

Both changes cause the test to fail, even though there is no functional change. Why?

With `from datetime import date, timedelta`, the code under test gets a reference to the unpatched `datetime.date` at import time. By the time the test runs, its `@patch` has no practical effect.

Following the advice in ["Where to patch"](https://docs.python.org/3/library/unittest.mock.html#where-to-patch), we could get the test working again by patching our own code rather than the builtin datetime module:

```python
@patch('tomorrow.date', fake_date)
def test_tomorrow():
    assert tomorrow.tomorrow() == datetime.date(2020, 7, 3)
```

That wouldn't cover the second change though - we'd need to also patch `tomorrow.dt` for that. Just a couple examples make this test start to feel brittle and tightly coupled to the implementation.

We can do better though.

### A more resilient test

We're looking for a test that can verify the behavior of our code even if subtle implementation details change. Aside from import variations, we've got different ways to fetch the current date (`date.today()`, `datetime.now()`, `datetime.utcnow()`, et cetera). By starting with the simplest test possible and working toward flexibility, it's possible to end up with something like this:

```python
fake_dttm = Mock(wraps=datetime)
fake_dttm.date.today.return_value = datetime.date(2020, 7, 2)
fake_dttm.datetime.now.return_value = datetime.datetime(2020, 7, 2)
fake_dttm.datetime.utcnow.return_value = datetime.datetime(2020, 7, 2)

@patch('tomorrow.date', fake_dttm.date, create=True)
@patch('tomorrow.datetime', fake_dttm, create=True)
@patch('tomorrow.dt', fake_dttm, create=True)
def test_tomorrow():
    assert tomorrow.tomorrow() == datetime.date(2020, 7, 3)
```

Which feels like an uncanny valley between thoroughness and pragmatism.

For a PyBites [code challenge ](https://codechalleng.es/), the tests carry an extra consideration. You write tests for an "official solution", but the tests also run against user-submitted code. So it shouldn't matter if one person uses `import datetime as dt` while another opts for `from datetime import date as dt, timedelta as td`.

There are a few different ways to tackle this. I list some references at the end of this post, but for now we'll look at the [freezegun](https://github.com/spulec/freezegun) library.

### Adding freezegun to our tests

[Freezegun](https://github.com/spulec/freezegun) provides a `freeze_time()` decorator that we can use to set a fixed date for our test functions. Picking up from the last section, that helps evolve this:

```python
fake_date = Mock(wraps=datetime.date)
fake_date.today.return_value = datetime.date(2020, 7, 2)

@patch('tomorrow.date', fake_date)
def test_tomorrow():
    assert tomorrow.tomorrow() == datetime.date(2020, 7, 3)
```

into this:

```python
from freezegun import freeze_time

@freeze_time('2020-07-02')
def test_tomorrow():
    assert tomorrow.tomorrow(include_time=True) == datetime.datetime(2020, 7, 3)
```

There are a few neat things going on there. For one, we can use a friendly date string (courtesy of the excellent [dateutil](https://dateutil.readthedocs.io) library) rather than a handcrafted `date` or `datetime` object. That gets even more useful when we're dealing with full timestamps rather than dates.

It's also useful (but less immediately clear) that `freeze_time` patches a number of common datetime methods under the hood:

* `datetime.datetime.now()`
* `datetime.datetime.utcnow()`
* `datetime.date.today()`
* `time.time()`
* `time.localtime()`
* `time.gmtime()`
* `time.strftime()`

Because of _how_ freezegun patches those methods, we can guarantee seeing the frozen date as long as the code under test uses those builtin methods. So our tests will smoothly handle import variations like:

* `import datetime`
* `from datetime import date`
* `from datetime import date as dt`

### Deep and thorough fakes

Freezegun keeps your tests simple by faking Python datetimes thoroughly. Not only does it patch methods from `datetime` and `time`, it looks at existing imports so it can be sure they're patched too. For anyone interested in the details, [this section](https://github.com/spulec/freezegun/blob/6cfbc48/freezegun/api.py#L589-L668) of the freezegun API code is a fine read!

If you're rolling your own fakes, you're not likely to be as thorough as freezegun. You probably don't need to be! But for at least some cases, a library like freezegun can offer more thorough tests that are also simpler and more readable.

### Taking it further

For high volume, performance-sensitive tests with fake dates, [libfaketime](https://pypi.org/project/libfaketime/) may be worth a look. Additionally, there are [pytest](https://pytest.org) plugins available for both [freezegun](https://pypi.org/project/pytest-freezegun/) and [libfaketime](https://gitlab.com/yaal/pytest-libfaketime).

### References

This post was a pretty narrowly-focused look at some common issues that pop up when testing with fake dates. I'm not an expert on any of this stuff, but I've been inspired by folks who know it better. So if you found this post interesting, some of these resources may also be worth a look:

* [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/) (Real Python)
* [Why your mock doesn't work](https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html) (Ned Batchelder)
* [Stop using datetime.now!](https://hakibenita.com/python-dependency-injection) (Haki Benita)
* [unittest.mock - "Where to patch"](https://docs.python.org/3/library/unittest.mock.html#id6) (Python Documentation)
* Anything with Brian Okken's name attached to it. There's a whole Okkensphere out there, including:
    * [Test and Code](https://testandcode.com/) (Podcast)
    * [Python Testing with Pytest](https://pythontesting.net/books/pytest/) (Book)
    * [Python Testing](https://pythontesting.net/start-here/) (Web site)

And since we're talking about dates and times here, I can't help including [Falsehoods programmers believe about time](FalsehoodsAboutTime.com).

### Acknowledgements

Thanks to the [PyBites](https://pybit.es/) community for inspiring this post. Notably:

* Nitin George Cherian, for kickstarting a discussion about fake dates
* Terry Spotts, for authoring and refactoring a relevant code challenge
* Bob Belderbos, for pointing out that this topic deserved a post

And of course, thanks to [Steve Pulec](https://github.com/spulec/) for creating freezegun. (While I'm at it, thanks for [moto](https://github.com/spulec/moto) too!)

Keep calm and code in Python!

-- [AJ](pages/guests.html#ajkerrigan)
