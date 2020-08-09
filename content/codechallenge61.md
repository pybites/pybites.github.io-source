Title: Code Challenge 61 - Build a URL Shortener
Date: 2019-02-21 12:00
Category: Challenge
Tags: code challenge, challenges, Flask, mentoring, code review, PR, github
Slug: codechallenge61
Authors: PyBites
Summary: Hey Pythonistas, in this challenge you will build an URL shortener. Enjoy!
cover: images/featured/pb-challenge.png

> There is an immense amount to be learned simply by tinkering with things. - Henry Ford

Hey Pythonistas,

##Changing the PCC game a bit

Let's be honest: we slacked off a bit on our blog code challenges! Apart from the increased workload overall, our _synchronous_ approach of solving a challenge before launching a next one, is holding us back.

So we are going to change our approach a bit. We're going to keep launching PyBites Code Challenges (PCCs) on our blog, because most importantly this is what gets **YOU to write Python code**!

However we are dropping hard deadlines and review posts. Solving them is an ongoing thread and you can see merged solutions [on the community branch](https://github.com/pybites/challenges/tree/community) (each challenge # has a dedicated folder).

You can collaborate with each other [on our Slack](https://join.slack.com/t/pybites/shared_invite/enQtNDAxODc0MjEyODM2LTNiZjljNTI2NGJiNWI0MTRkNjY4YzQ1ZWU4MmQzNWQyN2Q4ZTQzMTk0NzkyZTRmMThlNmQzYTk5Y2Y5ZDM4NDU) (= dedicated #codechallenge channel). And of course keep PR'ing your code via [our platform](https://codechalleng.es/challenges/).

##Want to code review / become a mentor?

We are still getting a pretty manageable number of PRs to be able to merge them all in ourselves.

However we think it would be really cool to give each PR a bit more of a code check. Hence we also want to make this a *community effort*.

So if you want to help out merging PRs into our challenges branch, become a moderator. You can volunteer [on Slack](https://join.slack.com/t/pybites/shared_invite/enQtNDAxODc0MjEyODM2LTNiZjljNTI2NGJiNWI0MTRkNjY4YzQ1ZWU4MmQzNWQyN2Q4ZTQzMTk0NzkyZTRmMThlNmQzYTk5Y2Y5ZDM4NDU).

It's a great chance to read other people's code honing your code review skills, and (last but not least!) become a mentor building up great relationships with other Pythonistas.

---

##Back to business ... our new challenge:

In this challenge we're asking you to spice up your life with your very own URL Shortener!

We've all seen sites like [bit.ly](https://bitly.com/) that allow you to shorten a URL into something... well... shorter! It's time to you make your own.

There are roughly four parts to this challenge:

1. Make a small Django/Flask/Bottle app that receives in a URL.

2. Using the supplied URL, generate a unique URL with the base of [pybit.es](https://pybit.es/). It should be generated keeping uniqueness in mind. 

3. Return the shortened URL.

4. **Bonus**: track the visits in a second DB table for stats.

It sounds more complex but breaking it down into these steps should help you tackle the problem more effectively.

Good luck and have fun!

## Ideas and feedback

If you have ideas for a future challenge or find any issues, open a [GH Issue](https://github.com/pybites/challenges/issues) or reach out via [Twitter](https://twitter.com/pybites), [Slack](https://codechalleng.es/settings/) or [Email](mailto:support@pybit.es).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

## Become a Python Ninja

At PyBites you get to [*master Python* through Code Challenges](https://pybit.es/special-learning-python.html):

* Subscribe to our blog (sidebar) to periodically get new PyBites Code Challenges (PCCs) and updates in your inbox.

* Apart from this blog code challenge we have a growing collection which you can check out [on our platform](https://codechalleng.es/challenges/). 

* Prefer coding bite-sized Python exercises, using effective Test-Driven Learning, and in the comfort of your browser? Try our growing collection of _[Bites of Py](https://codechalleng.es/bites/)_ on our platform.

	<iframe width="560" height="315" src="https://www.youtube.com/embed/5AQg2UxvXbI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* Want to do the [#100DaysOfCode](https://twitter.com/hashtag/100DaysOfCode?src=hash&lang=en) but not sure what to work on? Take [our course](https://talkpython.fm/100days?utm_source=pybites) and/or start logging your 100 Days progress using our _Progress Grid Feature_ [on our platform](https://codechalleng.es/100days/) (you can also use the Grid to do 100 Bite exercises in 100 days, earning a die hard PyBites Ninja Certificate!)

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!
