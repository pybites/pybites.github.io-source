Title: Code Challenge 56 - Calculate the Duration of a Directory of Audio Files
Date: 2018-10-23 11:15
Category: Challenge
Tags: code challenge, challenges, audio, music, FFmpeg, subprocess, glob, os.path, pathlib, datetime
Slug: codechallenge56
Authors: PyBites
Summary: Hi Pythonistas, Welcome to Pybites Code Challenge 56! In this challenge we're asking you to work with directory, files and audio meta data!
cover: images/featured/pb-challenge.png

> There is an immense amount to be learned simply by tinkering with things. - Henry Ford

Hey Pythonistas,

It's time for another code challenge! This week we're asking you to work with directory, files and audio meta data!

## The Challenge

Write a script that receives a directory name and retrieves all mp3 (or mp4 or m4a) files. It then sums up the durations of each file and prints them in a nice table with a total duration.

This could look like the following:

		$ module_duration.py ~/Music/iTunes/iTunes\ Media/Music/Manu\ Chao/Manu\ Chao\ -\ Esperanza/
		Manu Chao - Bixo.m4a                    : 112
		Manu Chao - Denia.m4a                   : 279
		Manu Chao - El Dorrado 1997.m4a         : 89
		Manu Chao - Homens.m4a                  : 198
		Manu Chao - Infinita Tristeza.m4a       : 236
		Manu Chao - La Chinita.m4a              : 93
		Manu Chao - La Marea.m4a                : 136
		Manu Chao - La Primavera.m4a            : 112
		Manu Chao - La Vacaloca.m4a             : 143
		Manu Chao - Le Rendez Vous.m4a          : 116
		Manu Chao - Me Gustas Tu.m4a            : 240
		Manu Chao - Merry Blues.m4a             : 216
		Manu Chao - Mi Vida.m4a                 : 152
		Manu Chao - Mr Bobby.m4a                : 229
		Manu Chao - Papito.m4a                  : 171
		Manu Chao - Promiscuity.m4a             : 96
		Manu Chao - Trapped by Love.m4a         : 114
		--------------------------------------------------
		Total                                   : 0:45:32

### What will you learn?

Why do we think this is cool? There are a couple of subtasks here:

1. You learn how to do a common sysadmin task of listing files in a directory (check out the `os`, `glob` and `pathlib` modules).

2. You learn how to convert and calculate mm:ss (minutes/seconds) timings, which will hone your `datetime` skills.

3. As far as we know Python cannot extract audio meta data natively (yet), so you probably want to try a tool like [FFmpeg](https://www.ffmpeg.org) which is cool because then you need to know how to call an external command with Python and parse its output. You probably want to check out `subprocess` for this:

	> The `subprocess` module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. - [docs](https://docs.python.org/3/library/subprocess.html)

Good luck and have fun!

## PyBites Community

A few more things before we take off:

* Do you want to discuss this challenge and share your Pythonic journey with other passionate Pythonistas? Confirm your email on our platform then request access to our Slack via [settings](https://codechalleng.es/settings/).

* PyBites is here to challenge you because becoming a better Pythonista requires practice, a lot of it. For any feedback, issues or ideas use [GH Issues](https://github.com/pybites/challenges/issues), [tweet us](https://twitter.com/pybites) or ping us on our Slack.

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!
