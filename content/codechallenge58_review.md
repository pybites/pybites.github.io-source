Title: Code Challenge 58 - Analyze Podcast Transcripts with NLTK - Part I - Review
Date: 2019-01-07 19:00
Category: Challenges
Tags: code challenge, challenges, NLTK, podcast, text parsing, data mining, data science, talk python, itertools, sqlite3, dictionary comprehensions, list comprehensions, splitlines, iterators, SequenceMatcher, OrderedDict, praw, collections, defaultdict, namedtuple, Counter, JSON, XML, pomodoro, Flask, regex, datetime, timedelta, CLI applications, f-strings, feedparser, requests
Slug: codechallenge58_review
Authors: PyBites
Summary: In this article we review our [PCC58 - Analyze Podcast Transcripts with NLTK - Part I](http://pybit.es/codechallenge58.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review our [PCC58 - Analyze Podcast Transcripts with NLTK - Part I](http://pybit.es/codechallenge58.html) code challenge. 

## Community Pull Requests

It has been a while but we're all caught up: we merged in 40+ Pull Requests. Kudos to all of you that submitted code, really cool seeing all the different solutions for our code challenges! 

Below is a digest of last month's learning ...

~~~
$ git pull origin community
...
remote: Total 504 (delta 213), reused 176 (delta 170), pack-reused 247
...
   aff4834..54cebc2  community  -> origin/community
...
 72 files changed, 3959 insertions(+)
~~~

### PCC58 Lessons

> Used `itertools.chain` because some Talk Python transcripts were missing, so I had to skip those. I also used `sqlite3` for the first time. It's really easy to use, I think I'll use it more in the future to store data that I retrieve from APIs. I also got more experience using the GitHub API for retrieving repo content. - [PR](https://github.com/pybites/challenges/pull/431)

<!-- -->

> Nice challenge! I scraped Talk Python's RSS feed (requests/ feedparser) getting the transcripts from GH, saved all this in a `sqlite3` DB, also wrote a function to generate an HTML for consumption on my Kindle (after Save-to-PDF on Mac). Some details: `decode("utf-8")` to work around some transcripts being stored as `bytes` (required some debugging), `f'{episode_id:0>3}'` as alternative for `zfill`, cur.executemany is awesome as it works flawlessly with a generator of namedtuples, to get row dicts from sqlite use `conn.row_factory = sqlite3.Row`, I also used `writelines` for the first time! - [PR](https://github.com/pybites/challenges/pull/471)

### Reading Code for Fun and Profit

The best way to learn/improve programming is to read and write a lot of code. Apart from following along with our review posts, you can look at [all submitted PRs](https://github.com/pybites/challenges/pulls?q=is%3Apr+is%3Aclosed) and/or checking our [our Community branch](https://github.com/pybites/challenges/tree/community) where we merge in all solutions.  

Here are the Pythonic learnings we spotted in Pull Requests made during the last month: 

#### [PCC01](http://codechalleng.es/challenges/01)

> I have an opportunity with discover more sorted list with all given arguments, get some more details with some commands in git I didn't know yet. - [PR](https://github.com/pybites/challenges/pull/448)

<!-- -->

> To reverse an `OrderedDict` one must create another one by the use of `OrderedDict(sorted(..., reverse=True, ...))` - [PR](https://github.com/pybites/challenges/pull/439)

<!-- -->

> Mostly, I learned about _list comprehensions_ after looking at the official solution and refining my own. I kept my original code in comments, but it helped me better understand the official one by typing it in myself. - [PR](https://github.com/pybites/challenges/pull/464)

<!-- -->

> I learned how to read a file and create a list from it. I practiced my recent git skills and was introduced to unit tests. - [PR](https://github.com/pybites/challenges/pull/465)

<!-- -->

> Before this exercise I never came across _dictionary comprehensions_. A bit confusing at first! - [PR](https://github.com/pybites/challenges/pull/428)

<!-- -->

> Yes, I learned how to better format lines from input files by using `splitlines()` - [PR](https://github.com/pybites/challenges/pull/430)

#### [PCC02](http://codechalleng.es/challenges/02)

> I introduced myself to `itertools` package to create permutations. I also focused on breaking my code into smaller, easier to manage functions. Practiced basic game logic and list manipulation. - [PR](https://github.com/pybites/challenges/pull/466)

<!-- -->

> Refresher on manipulating lists and using `itertools` functionality - [PR](https://github.com/pybites/challenges/pull/452)

<!-- -->

> Yes, I learned how to build a set using _iterators_ - [PR](https://github.com/pybites/challenges/pull/445)

#### [PCC03](http://codechalleng.es/challenges/03)

> Yes, I learned how to parse from `xml` documents. I also found a fun side effect of sets: as unordered collections, the order in which they return data is inconsistent and seems to be dependent on where that data is in memory. If it's important to display the information consistently or in the same order every time a program is run, either refrain from using a set or change it back to a list to sort it. - [PR](https://github.com/pybites/challenges/pull/446)

<!-- -->

> Learned about `SequenceMatcher`. Great thing. Started to think about how tests actually work, since I did get the results from the website but could not manage to pass the tests. Heard about `nltk` (looks interesting). - [PR](https://github.com/pybites/challenges/pull/423)

#### [PCC11](http://codechalleng.es/challenges/11)

> I learned about the power of generators when you need to pass lists, dicts, or sets around - [PR](https://github.com/pybites/challenges/pull/468)

#### [PCC12](http://codechalleng.es/challenges/12)

> I gained experience in compartmentalizing code, I broke down big code chunks into smaller functions to make it easier to understand. I didn't use any new features of Python, but I got better with software development practices. - [PR](https://github.com/pybites/challenges/pull/457)

#### [PCC13](http://codechalleng.es/challenges/13)

> yes, how to tie together a few tools from the `collections` module to get a seemingly complicated task done relatively quickly. - [PR](https://github.com/pybites/challenges/pull/470)

<!-- -->

> I learnt a lot more about `collections`, in particular `defaultdict`. Using it with `namedtuple` was a great exercise. - [PR](https://github.com/pybites/challenges/pull/455)

<!-- -->

> I learned `collections` - `defaultdict`, `namedtuple`, `Counter`. I learned how to use `f-string`. I still do not know how I can sort specific element inside the value of the default dict e.g. in this case I can't sort the score of movies under the director. - [PR](https://github.com/pybites/challenges/pull/437)

<!-- -->

> I learned about `namedtuple` - [PR](https://github.com/pybites/challenges/pull/436)

#### [PCC16](http://codechalleng.es/challenges/16)

> I learn how to make request to remote database (in this project used RIPE DB) and how to parse `JSON` output from DB - [PR](https://github.com/pybites/challenges/pull/426)

#### [PCC27](http://codechalleng.es/challenges/27)

> I learned how to use `praw`, the library for accessing the reddit API through a python wrapper. This challenge was fun, I think I'll be using praw more in the future. - [PR](https://github.com/pybites/challenges/pull/461)

#### [PCC39](http://codechalleng.es/challenges/39)

> Create an Interval class that can be leveraged by a pomodoro app. I learned `pytest` methodology for testing a custom class - [PR](https://github.com/pybites/challenges/pull/460)

<!-- -->

> yes, I mucked around with `flask` testing - [PR](https://github.com/pybites/challenges/pull/459)

#### [PCC42](http://codechalleng.es/challenges/42)

> Solidified my understanding of regex. - [PR](https://github.com/pybites/challenges/pull/467)

<!-- -->

> Didn't know non-capture group can be used like that. - [PR](https://github.com/pybites/challenges/pull/429)

#### [PCC52](http://codechalleng.es/challenges/52)

> Kind of? `datetime` is pretty new to me, and this is the first time I actually used the time module. It was also the first time I used `os.system`, and the "\r" character. It was a good experience, but I wouldn't go as far as to say that I "stretched" my skills. I will most likely come back to the timer and improve the interface a bit. - [PR](https://github.com/pybites/challenges/pull/443)

<!-- -->

> I learned how to define the `timedelta`, how to use string to properly show `datetime.` - [PR](https://github.com/pybites/challenges/pull/432)

<!-- -->

> Yes, I learned that when I print `timedelta`, it shows the string in this format: "0:00:00". - [PR](https://github.com/pybites/challenges/pull/434)

<!-- -->

> `argparse`, `datetime`, making CLI applications - [PR](https://github.com/pybites/challenges/pull/440)

---

Thanks to everyone for your participation in our blog code challenges! [Keep the PRs coming](https://codechalleng.es/challenges/) and **include a README.md with one or more screenshots if you want to be featured in this review post**.

## Become a Python Ninja

Master Python through Code Challenges:

* Subscribe to our blog (sidebar) to get new PyBites Code Challenges (PCCs) in your inbox.

* Take any of our 50+ challenges [on our platform](https://codechalleng.es/challenges/). 

* Prefer coding bite-sized Python exercises in the comfort of your browser? Try our growing collection of _[Bites of Py](https://codechalleng.es/bites/)_.

* Want to do the [#100DaysOfCode](https://twitter.com/hashtag/100DaysOfCode?src=hash&lang=en) but not sure what to work on? Take [our course](https://talkpython.fm/100days?utm_source=pybites) and/or start logging your 100 Days progress using our _Progress Grid Feature_ [on our platform](https://codechalleng.es/100days/).

---

Keep Calm and Code in Python!

-- Bob and Julian
