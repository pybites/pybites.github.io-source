Title: Code Challenge 53 - Query the Spotify API - Review
Date: 2018-10-09 12:40
Category: Challenges
Tags: Spotify, music, API, Bokeh, Flask, readlines, itertools, Google, difflib, visualization, data analysis, regex, Counter, web scraping, Selenium, email
Slug: codechallenge53_review
Authors: PyBites
Summary: In this article we review last week's [Query the Spotify API](http://pybit.es/codechallenge53.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Query the Spotify API](http://pybit.es/codechallenge53.html) code challenge. 
## Reminder: new structure review post / Hacktoberfest is back!

From now on we will merge our solution into our Community branch and include anything noteworthy here, because:

* we are learning just like you, we are all equals :)

* we _need_ the PRs too ;) ... as part of [Hacktoberfest No. 5](https://hacktoberfest.digitalocean.com) that just kicked of (5 PRs and you get a cool t-shirt)

_Don't be shy, share your work!_

## Community Pull Requests

20+ PRs this week, wow!

	$ git pull origin community
	...
	104 files changed, 242507 insertions(+)

Check out the [awesome PRs by our community for PCC53](https://github.com/pybites/challenges/tree/community/53) (or from fork: `git checkout community && git merge upstream/community`):

Some learnings for PCC53:

> Spotify Web apis are not so straight forward. It takes a bit of time to understand the type of Authorization approach to call the APIs. I've started with Spotipy module and did a test run. Once all good, I've walked through the Spotipy code in github and coded my own Wrapper classes.

<!-- -->
> The Spotify API was more complex than I realised. Had to wrap my head around their authentication which was tough.  Parsing the returned super nested dict was also a bit of a challenge. Once I figured that out though it was a matter of presenting it. I wrapped it all in Flask so that was fun!

<!-- -->
> Always nice to keep practicing Flask and Web APIs. Funny to see that out of Git's 200 additions, 152 lines are html/css and the Python took no more than 30 lines, awesome when you can just plug these robust libraries in!

## Read Code for Fun and Profit

You can look at all submitted code [here](https://github.com/pybites/challenges/pulls?q=is%3Apr+is%3Aclosed) and/or [on our Community branch](https://github.com/pybites/challenges/tree/community).

Other learnings we spotted in Pull Requests for other challenges this week: 

> (PCC01) I learned a shortcut using .read().splitlines() instead of .readlines() and requiring me to .split() afterwords.

<!-- -->
> (PCC02) Learned about itertools.permutations.

<!-- -->
> (PCC03) I got introduced to difflib.SequenceMatcher and itertools.product. Which are both very nice and I learned about a method of the Counter object called most_common which I didn't know about yet.

<!-- -->
> (PCC19) Interacted with any Google API for the first time. Learned about doing an HTTP POST. Learning about clean code. Explored .gitignore

<!-- -->
> (PCC22) Learned a lot on web scraping, selenium and email notifications.

<!-- -->
> (PCC28) New package 'bokeh'!. So easy to plot the data!. Python ecosystem for visualization is awesome. It's a good challenge to get hands own on Flask and Bokeh.

<!-- -->
> (PCC42) Find consecutive equal words, how to handle greedy regex

<!-- -->
> (PCC44) This was a good challenge to go back to the basics of Data analysis (cleaning, parsing and manipulate).

We are happy to include more detailed learning, just send us a _quotable blurb_ for this post when preparing your PR [on our platform](https://codechalleng.es/challenges/).

Thanks to everyone for your participation in our blog code challenges! 

Keep the PRs coming, again this month it counts for __[Hacktoberfest](https://hacktoberfest.digitalocean.com)__!

## Need more Python Practice?

Subscribe to our blog (sidebar) to get periodic PyBites updates.

And/or take any of our 50+ challenges [on our platform](https://codechalleng.es/challenges/). 

Prefer coding self contained exercises in the comfort of your browser? Try our growing collection of [Bites of Py](https://codechalleng.es/bites/).

Want to do the [#100DaysOfCode](https://twitter.com/hashtag/100DaysOfCode?src=hash&lang=en) but not sure what to work on? Take [our course](https://talkpython.fm/100days?utm_source=pybites) and/or start logging your progress [on our platform](https://codechalleng.es/100days/).

---

Keep Calm and Code in Python!

-- Bob and Julian
