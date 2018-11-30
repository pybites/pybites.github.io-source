Title: 3 Cool Things You Can do With the dateutil Module
Date: 2018-11-30 12:00
Category: Modules
Tags: dateutil, parse, relativedelta, rrule, fuzzy parser, datetime, timedelta, 100DaysOfCode
Slug: python-dateutil
Authors: Bob
Summary: In this short article I will show you how to use `dateutil`'s `parse`, `relativedelta` and `rrule` to make it easier to work with datetimes in Python.
cover: images/featured/pb-article.png

In this short article I will show you how to use `dateutil`'s `parse`, `relativedelta` and `rrule` to make it easier to work with datetimes in Python.

Firt some necessary imports:

	>>> from datetime import date
	>>> from dateutil.parser import parse
	>>> from dateutil.relativedelta import relativedelta
	>>> from dateutil.rrule import rrule, WEEKLY, WE

## 1. Parse a datetime from a string

This is actually what made me look into `dateutil` to start with. [Camaz](https://github.com/camaz) shared this technique in the forum for [Bite 7. Parsing dates from logs](https://codechalleng.es/bites/7/) 

Imagine you have this log line:

	>>> log_line = 'INFO 2014-07-03T23:27:51 supybot Shutdown complete.'

Up until recently I used `datetime`'s `strptime` like so:

	>>> date_str = '%Y-%m-%dT%H:%M:%S'
	>>> datetime.strptime(log_line.split()[1], date_str)
	datetime.datetime(2014, 7, 3, 23, 27, 51)

More string manipulation and you have to know the [format string syntax](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior). `dateutil`'s `parse` takes this complexity away:

	>>> timestamp = parse(log_line, fuzzy=True)
	>>> print(timestamp)
	2014-07-03 23:27:51
	>>> print(type(timestamp))
	<class 'datetime.datetime'>

## 2. Get a timedelta in months

A limitation of `datetime`'s `timedelta` is that it does not show the number of months:

	>>> today = date.today()
	>>> pybites_born = date(year=2016, month=12, day=19)
	>>> (today-pybites_born).days
	711

So far so good. However this does not work:

	>>> (today-pybites_born).years
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	AttributeError: 'datetime.timedelta' object has no attribute 'years'

Nor this:

	>>> (today-pybites_born).months
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	AttributeError: 'datetime.timedelta' object has no attribute 'months'

`relativedelta` to the rescue:

	>>> diff = relativedelta(today, pybites_born)
	>>> diff.years
	1
	>>> diff.months
	11

When you need months, use `relativedelta`. And yes, we can almost celebrate two years of PyBites! 

Another use case of this we saw in my previous article, [How to Test Your Django App with Selenium and pytest](https://pybit.es/selenium-pytest-and-django.html), where I used it to get the last 3 months for our new [Platform Coding Streak feature](https://codechalleng.es):

	>>> def _make_3char_monthname(dt):
	...     return dt.strftime('%b').upper()
	...
	>>> this_month = _make_3char_monthname(today)
	>>> last_month = _make_3char_monthname(today-relativedelta(months=+1))
	>>> two_months_ago = _make_3char_monthname(today-relativedelta(months=+2))
	>>> for month in (this_month, last_month, two_months_ago):
	...     print(f'{month} {today.year}')
	...
	NOV 2018
	OCT 2018
	SEP 2018

Let's get next Wednesday for the next example:

	>>> next_wednesday = today+relativedelta(weekday=WE(+1))
	>>> next_wednesday
	datetime.date(2018, 12, 5)

## 3. Make a range of dates

Say I want to schedule my next batch of Italian lessons, each Wednesday for the coming 10 weeks. Easy:

	>>> rrule(WEEKLY, count=10, dtstart=next_wednesday)
	<dateutil.rrule.rrule object at 0x1033ef898>

As this will return an iterator and it does not show up vertically, let's materialize it in a `list` and pass it to `pprint`:

	>>> from pprint import pprint as pp
	>>> pp(list(rrule(WEEKLY, count=10, dtstart=next_wednesday)))
	[datetime.datetime(2018, 12, 5, 0, 0),
	datetime.datetime(2018, 12, 12, 0, 0),
	datetime.datetime(2018, 12, 19, 0, 0),
	datetime.datetime(2018, 12, 26, 0, 0),
	datetime.datetime(2019, 1, 2, 0, 0),
	datetime.datetime(2019, 1, 9, 0, 0),
	datetime.datetime(2019, 1, 16, 0, 0),
	datetime.datetime(2019, 1, 23, 0, 0),
	datetime.datetime(2019, 1, 30, 0, 0),
	datetime.datetime(2019, 2, 6, 0, 0)]

Double-check with Unix `cal`

	$ cal 12 2018
	December 2018
	Su Mo Tu We Th Fr Sa
					   1
	 2  3  4  5  6  7  8
	 9 10 11 12 13 14 15
	16 17 18 19 20 21 22
	23 24 25 26 27 28 29
	30 31

	$ cal 1 2019
		January 2019
	Su Mo Tu We Th Fr Sa
		   1  2  3  4  5
	 6  7  8  9 10 11 12
	13 14 15 16 17 18 19
	20 21 22 23 24 25 26
	27 28 29 30 31

	$ cal 2 2019
	February 2019
	Su Mo Tu We Th Fr Sa
					1  2
	 3  4  5  6  7  8  9
	...

We added [an exercise](https://codechalleng.es/bites/147/) to our platform to create a [#100DaysOfCode](https://pybit.es/pages/courses.html) planning, skipping weekend days. `rrule` made this relatively easy.

---

And that's it, my favorite use cases of `dateutil` so far. There is some timezone functionality in `dateutil` as well, but I have mostly used `pytz` for that. 

Learn more? Check out this nice [dateutil examples page](https://dateutil.readthedocs.io/en/stable/examples.html) and feel free to share your favorite snippets in the comments below.

Don't forget this is an external library (`pip install python-dateutil`), for most basic operations `datetime` would suffice. Another nice stdlib module worth checking out is [`calendar`](https://docs.python.org/3.7/library/calendar.html).

---

Keep Calm and Code in Python!

-- Bob
