Title: Code Challenge 63 - Automatically Generate Blog Featured Images
Date: 2019-09-02 09:00
Category: Challenge
Tags: code challenge, challenges, web scraping, images, selenium, automation, material design, file handling, zipfile
Slug: codechallenge63
Authors: PyBites
Summary: Hey Pythonistas, in this new blog code challenge you are going to use `selenium` to automatically generate some cool featured images for PyBites. Have fun!
cover: images/featured/pb-challenge.png

> There is an immense amount to be learned simply by tinkering with things. - Henry Ford

Hey Pythonistas,

In this new blog code challenge you are going to use `selenium` to automatically generate some cool featured images for PyBites. Let's write some Python code, shall we?

## The Challenge

Some time ago Bob made a tool to automate blog image generation: [Featured Image Creator](http://projects.bobbelderbos.com/featured_image/).

In this challenge you will help PyBites create some nice featured images for their code challenges or articles (heck, we could even use them on Twitter!)

Steps:

1. Make a virtual env and pip install `selenium` (and optionally `bs4` or `feedparser`), however this is not a requirement, use your favorite tools ...

2. Scrape all [blog code challenge titles](https://pybit.es/pages/challenges.html) and/or [PyBites articles](https://pybit.es/pages/articles.html) (feel free to `feedparse` our [RSS feed](https://pybit.es/feeds/all.rss.xml)). We want images for all of them.

3. Using Selenium navigate to [Featured Image Creator](http://projects.bobbelderbos.com/featured_image/) and set the canvas (button ID `#submitDimensions`) to your preferred size (e.g. w=300/ h=100, or w=200 / h=200)

4. Loop over the challenge and/or article titles you scraped and for each title:

	- enter the title alongside _Title text in image (blog post)_ (`#title` ID field).

	- choose a _Margin-top_ and _Google Font_ from the two dropdown fields (`#topoffset` and `#font` field IDs respectively).

	- choose a theme: _BG theme: material_ or _BG theme: bamboo_ (`#collection` ID field).

	- choose a picture from the auto-complete (`#bg1_url` ID field), or just fill in the field picking random ones from the 2 lists below (one per theme):

			featured_image/images/material]# ls -C1|grep full|sort|sed 's@\(.*\)@images/material/\1@g'
			images/material/black-blue_full.jpg
			images/material/black_full.jpg
			images/material/black-red_full.jpg
			images/material/blue-black_full.jpg
			images/material/blue-brown_full.png
			images/material/blue_full.jpg
			images/material/blue-green_full.png
			images/material/blue-lightblue-white_full.jpg
			images/material/blue-white_full.jpg
			images/material/blue-yellow_full.png
			images/material/darkgreen-red-yellow_full.png
			images/material/green-blue_full.jpg
			images/material/green_full.png
			images/material/green-red_full.jpg
			images/material/orange-black_full.jpg
			images/material/orange-blue_full.jpg
			images/material/purple-blue_full.jpg
			images/material/purple-blue-red_full.jpg
			images/material/purple-red-orange_full.png
			images/material/purple-red-white_full.png
			images/material/purple-yellow-white_full.png
			images/material/red_full.jpg
			images/material/red-green_full.jpg
			images/material/white-blue_full.png
			images/material/yellow-darkgrey-red_full.jpg

			featured_image/images/bamboo]# ls -C1|grep full|sort -n|sed 's@\(.*\)@images/bamboo/\1@g'
			images/bamboo/1_green_full.jpg
			images/bamboo/2_black_full.jpg
			images/bamboo/3_black_full.jpg
			images/bamboo/4_black_full.jpg
			images/bamboo/5_black_full.jpg
			images/bamboo/6_white_black_full.jpg
			images/bamboo/7_black_full.jpg
			images/bamboo/8_black_full.jpg
			images/bamboo/9_black_full.jpg
			images/bamboo/10_green_full.jpg
			images/bamboo/11_black_full.jpg
			images/bamboo/12_black_olive_full.jpg
			images/bamboo/13_gray_full.jpg
			images/bamboo/14_black_full.jpg
			images/bamboo/15_green_full.jpg
			images/bamboo/16_black_full.jpg
			images/bamboo/17_green_white_olive_full.jpg
			images/bamboo/18_black_full.jpg
			images/bamboo/19_green_full.jpg
			images/bamboo/20_gray_full.jpg
			images/bamboo/21_silver_full.jpg
			images/bamboo/22_white_full.jpg
			images/bamboo/23_black_olive_full.jpg
			images/bamboo/24_white_full.jpg
			images/bamboo/25_black_white_full.jpg

- Feel free to set the other fields as well, but so far your should have a decent featured image, so move onto to saving the image ...

- Click the _Save_ button (`#btnSave` ID field).

- Move the obtained file to an output directory and zip them up (using Python's `zipfile`).

[PR your work on our platform](https://codechalleng.es/challenges/63/) including the generated zipfile (or host it yourself and link in the PR to keep our challenges repo lean).

Good luck and have fun coding Python! Ideas for future challenges? use [GH Issues](https://github.com/pybites/challenges/issues).

---

## Get serious, take your Python to the next level ...

At PyBites we're all about creating Python ninjas through challenges and real-world exercises. Read more about [our story](https://pybit.es/special-learning-python.html).

We are happy and proud to share that we now hear monthly stories from our users that they're landing new Python jobs. For many this is a dream come true, especially as they're often landing roles with significantly higher salaries!

Our _[200 Bites of Py exercises](https://codechalleng.es/bites/)_ are geared toward instilling the habit of coding frequently, if not daily which will dramatically improve your Python and problem solving skills. This is __THE__ number one skillset necessary to becoming a linchpin in the industry and will enable you to crush it wherever codes need to be written.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5AQg2UxvXbI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Take [our free trial](https://codechalleng.es) and let us know on Slack how it helps you improve your Python!

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!
