Title: Code Challenge 22 - Packt Free Ebook Web Scraper
Date: 2017-06-05 11:20
Category: Challenges
Tags: codechallenges, webscraping, BeautifulSoup, Selenium, Packt, Pybonacci, ebooks, community, automation, sponsoring
Slug: codechallenge22
Authors: PyBites
Summary: Hi Pythonistas, a new week, a new 'bite' of Python coding! This week we will do some web scraping of Packt's daily free ebook, sending out daily notifications. This week we even have a unique opportunity to sponsor the Python Community, read on ... and happy coding!
cover: images/featured/pb-challenge.png

> A smooth sea never made a skilled sailor. - Franklin D. Roosevelt

Hi Pythonistas, a new week, a new 'bite' of Python coding :)

This week we will do some web scraping. As you might know [Packt](https://www.packtpub.com/) gives away a free ebook [every (!) single day](https://www.packtpub.com/packt/offers/free-learning). In this challenge you will scrape that page and send out a notification to never miss an interesting title.

## Sponsor the Python Community

But it gets better: the guys from [Pybonacci](https://pybonacci.es/) (great Spanish Python science blog) partnered up with Packt:


<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/Pybonacci">@Pybonacci</a> Inviting you to participate in our free eBook initiative next week, including a donation to a tech charity of your choice.</p>&mdash; Packt (@PacktPub) <a href="https://twitter.com/PacktPub/status/870223070027550720">June 1, 2017</a></blockquote>

Packt will donate up till 1000 bucks ($ 1 per free ebook download) to a Python related non-profit (more info [here](https://pybonacci.es/2017/06/03/donaciones-gracias-a-packtpub/#en), you can vote for the non-profit [here](https://twitter.com/Pybonacci/status/870943704500056065)).

So taking this challenge you get to promote the awesome Python community, isn't that cool?

## The Challenge

The challenge is to make a script that scrapes [the free learning link](https://www.packtpub.com/packt/offers/free-learning) every day for meta data about the book (title, description, cover, promo time left).

Then have the script share this info together with this affiliation link: [https://www.packtpub.com/packt/offers/free-learning?utm_source=Pybonacci&utm_medium=referral&utm_campaign=FreeLearning2017CharityReferrals](https://www.packtpub.com/packt/offers/free-learning?utm_source=Pybonacci&utm_medium=referral&utm_campaign=FreeLearning2017CharityReferrals) to your favorite channel: email, Twitter, Facebook, reddit, slack, etc.

That's it for the basic requirements. You probably want to put this in OS cron or you can use Dan Bader's [schedule package](https://schedule.readthedocs.io/).

For the web scraping you could use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) or [Scrapy](https://scrapy.org/) for example. We did an article [on the former](https://pybit.es/simplewebscraper.html) and used it [in our 100days Challenge](https://github.com/pybites/100DaysOfCode/tree/master/055).

### Bonus

If you really want to challenge yourself, you could have the script login to your Packt account and click the 'Claim Your Free eBook', making it fully automated. It might not be easy because they use a [CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA), but hey we like a good challenge, right? It would definitely be a useful tool and a good skill to add.

Not sure where to start? Check out [this repo](https://github.com/igbt6/Packt-Publishing-Free-Learning) (Github is your friend!). They used [Requests / Session](https://requests.readthedocs.io/en/master/user/advanced/#session-objects) to do this.

You could also look at [Selenium](http://selenium-python.readthedocs.io/) (here is [some 100days code](https://github.com/pybites/100DaysOfCode/blob/master/066/packt.py)).

---

## Getting ready

See [our INSTALL doc](https://github.com/pybites/challenges/blob/master/INSTALL.md) how to fork [our challenges repo](https://github.com/pybites/challenges) to get cracking.

This doc also provides you with instructions how you can submit your code to our community branch via a Pull Request (PR). We will feature your PRs in our end-of-the-week challenge review ([previous editions](http://pybit.es/pages/challenges.html)).

## Feedback

If you have ideas for a future challenge or find any issues, please [contact us](http://pybit.es/pages/about.html) or open a [GH Issue](https://github.com/pybites/challenges/issues).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian
