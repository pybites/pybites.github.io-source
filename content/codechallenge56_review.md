Title: Code Challenge 56 - Calculate the Duration of a Directory of Audio Files - Review
Date: 2018-10-30 11:45
Category: Challenges
Tags: code challenge, challenges, audio, music, FFmpeg, subprocess, glob, os.path, pathlib, datetime, eyeD3, csv, Pandas, pathlib, itertools, re, SQL, property, decorator
Slug: codechallenge56_review
Authors: PyBites
Summary: In this article we review last week's [Calculate the Duration of a Directory of Audio Files](http://pybit.es/codechallenge56.html) code challenge. 
cover: images/featured/pb-challenge.png

In this article we review last week's [Calculate the Duration of a Directory of Audio Files](http://pybit.es/codechallenge56.html) code challenge. 

## Hacktoberfest almost over

The last two days of [Hacktoberfest No. 5](https://hacktoberfest.digitalocean.com)! Wrap up your PRs!

## Community Pull Requests

Another 14 PRs this week, cool!

~~~
$ git pull origin community
...
From github.com:pybites/challenges
 * branch            community  -> FETCH_HEAD
   6ac949d..8eec5f9  community  -> origin/community
Updating 6ac949d..8eec5f9
Fast-forward
...
 25 files changed, 1854 insertions(+)
~~~

Check out the [awesome PRs by our community for PCC56](https://github.com/pybites/challenges/tree/community/56) (or from fork: `git checkout community && git merge upstream/community`):

### PCC56 Lessons

> I learned how to use python os module to get all files(mp3, m4a, mp4) of a given directory. Also, I learned how to use Mutagen module to get files info such as durations in seconds and bitrate. In the future, I would like to use pathlib module as an alternative to os

<!-- -->
> Got to utilize pathlib, and isinstance for type checking.

<!-- -->
> Equated with subprocess, datetime, csv libraries. 

<!-- -->
> Refreshed my memory on pandas and glob, these are not something I get to use everyday.

<!-- -->
> Learned new mp3 metadata library (eyeD3), learned dataclasses, and got better at using os.

<!-- -->
> Practiced with subprocess (call and parse external ffmpeg binary), calculate with datetimes, glob.glob to list files in a directory. Another nice refresher: "how to have this script in my PATH": I put it in ~/bin (already in my $PATH) + chmod 755 + added a bang (#!/usr/bin/env python)

## Read Code for Fun and Profit

You can look at all submitted code [here](https://github.com/pybites/challenges/pulls?q=is%3Apr+is%3Aclosed) and/or [on our Community branch](https://github.com/pybites/challenges/tree/community).

Other learnings we spotted in Pull Requests for other challenges this week: 

> (PCC01) Learned about rstrip and the use of dictionary get to set a default value.

<!-- -->
> (PCC02) Learned about list extend and itertools.permutations.

<!-- -->
> (PCC20) Learned how to use inheritance, class properties with the property decorator, some error handling, and using magic methods for printing and comparing.

<!-- -->
> (PCC42) Learned a few extra `re` tricks

<!-- -->
> (PCC51) Learned SQL

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
