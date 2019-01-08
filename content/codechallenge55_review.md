Title: Code Challenge 55 - #100DaysOfCode Curriculum Generator - Review
Date: 2018-10-23 11:10
Category: Challenges
Tags: code challenge, challenges, 100DaysOfCode, json, books, learning, data science
Slug: codechallenge55_review
Authors: PyBites
Summary: In this article we review last week's [#100DaysOfCode Curriculum Generator](http://pybit.es/codechallenge55.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [#100DaysOfCode Curriculum Generator](http://pybit.es/codechallenge55.html) code challenge. 

## Final reminder: Hacktoberfest

8 days left to have your PRs to our challenges repo count towards [Hacktoberfest No. 5](https://hacktoberfest.digitalocean.com).

## Community Pull Requests

Another 10+ PRs this week, cool!

Check out the [awesome PRs by our community for PCC55](https://github.com/pybites/challenges/tree/community/55) (or from fork: `git checkout community && git merge upstream/community`):

### Featured 

[vipinreyo](https://github.com/pybites/challenges/tree/community/55/vipinreyo) wrote a script that requests and parses [our platform](https://codechalleng.es) and collects meta data from our challenges and bites. From that list it will randomly create a task list for 100 days and return it as a JSON string.

[danshorstein](https://github.com/pybites/challenges/tree/community/55/danshorstein) built _100 Days of Awesome Python_. Using the [Awesome Python repo](https://raw.githubusercontent.com/vinta/awesome-python/master/README.md) it creates a curriculum of 100 days of python awesomeness. Each day you get a new library to explore. It started as a random selection, but he then wrote a second version to sort the libraries on the lowest number of stars so the libraries selected are lesser known.

[bbelderbos](https://github.com/pybites/challenges/tree/community/55/bbelderbos) made a _#100DaysOfCode Reading Planner_, a script that takes one or more book IDs from [our reading list app](http://pbreadinglist.herokuapp.com/) which allowed him to put his curriculum to test starting his long desired [#100DaysOfData](https://codechalleng.es/100days/bbelderbos/1596).

### PCC55 Lessons

> I had fun with list comprehensions and JSON

<!-- -->
> Requests and Beautifulsoup are awesome.

<!-- -->
> The json part was easy, the complex part was how to evenly split 4 or 5 books over 100 days: some days you finish a book, but still have pages left (from "avg pages per day") you need to spend on the new book, going with generators / itertools.islice made this easier to accomplish, which was a great learning exercise.

## Read Code for Fun and Profit

You can look at all submitted code [here](https://github.com/pybites/challenges/pulls?q=is%3Apr+is%3Aclosed) and/or [on our Community branch](https://github.com/pybites/challenges/tree/community).

Other learnings we spotted in Pull Requests for other challenges this week: 

> (PCC02) I had more practice with generators and itertools, learning how to use them effectively.

<!-- -->
> (PCC04) `yield`  and Tweepy

<!-- -->
> (PCC14) More knowledge about decorators

<!-- -->
> (PCC42) I improved my regular expression skills, learning about _capturing groups_.

---

Thanks to everyone for your participation in our blog code challenges! [Keep the PRs coming](https://codechalleng.es/challenges/) and **include a README.md with one or more screenshots if you want to be featured in this weekly review post**.

## Become a Python Ninja

Master Python through Code Challenges:

* Subscribe to our blog (sidebar) to get new PyBites Code Challenges (PCCs) in your inbox.

* Take any of our 50+ challenges [on our platform](https://codechalleng.es/challenges/). 

* Prefer coding bite-sized Python exercises in the comfort of your browser? Try our growing collection of _[Bites of Py](https://codechalleng.es/bites/)_.

* Want to do the [#100DaysOfCode](https://twitter.com/hashtag/100DaysOfCode?src=hash&lang=en) but not sure what to work on? Take [our course](https://talkpython.fm/100days?utm_source=pybites) and/or start logging your 100 Days progress using our _Progress Grid Feature_ [on our platform](https://codechalleng.es/100days/).

---

Keep Calm and Code in Python!

-- Bob and Julian
