Title: Behind the Scenes of PyBites - a Blog for Passionate Pythonistas (Post #100 Special)
Date: 2017-04-18 08:24
Category: Special
Tags: special, milestone, softskills, learning, lessons, community, pelican, challenge, python, pybites, automation
Slug: special-building-pybites
Authors: PyBites
Summary: Python is hot according to [Dice](http://insights.dice.com/2016/02/01/whats-hot-and-not-in-tech-skills/). It’s an easy language to learn, has an elegant design and is widely used. In this article we proudly present our now 4 months journey into building PyBites. It’s a reflection of what we achieved and lessons learned. We hope to inspire fellow developers to start their own venture. It is very rewarding!
cover: images/featured/pb-special.png

Python is hot according to [Dice](http://insights.dice.com/2016/02/01/whats-hot-and-not-in-tech-skills/). It’s an easy language to learn, has an elegant design and is widely used. In this article we proudly present our now 4 months journey into building PyBites. It’s a reflection of what we achieved and lessons learned. We hope to inspire fellow developers to start their own venture. It is very rewarding!

## \_\_init\_\_.py

Julian and Bob met (virtually) 8 years ago both working for Sun Microsystems. As we wrote on our about page: 

> They quickly realised that their mutual enthusiasm for technology, programming and self development was unrivalled and have thus remained the best of friends.

We had already been sharing our passion for Python for some time. We had not done any major publicly documented project / effort together though. Hence we needed a platform …

### Just get started

Around last Christmas break we decided to take action. It is important to take that first step, it’s also the hardest part. Don’t expect your first iteration to be perfect. In fact perfectionism might be your biggest enemy.

Looking back we made a lot of decisions on the fly, you simply can’t plan for everything in advance. Like writing an article: you have an outline, yet the meat of the story presents itself while writing.

### Have a success buddy

Physical proximity is not required to start a successful project / partnership. Being held accountable is. As Darren Hardy succinctly wrote in [The Compound Effect](http://www.amazon.com/dp/159315724X/?tag=pyb0f-20): 

> Find a success buddy: there are few things as powerful as two people locked arm and arm marching forward the same goal. To up your chances of success, get a success buddy, someone who’ll keep you accountable as you cement your new habit while you return the favor.

### First steps: assert toolset and domain name

Based on prior good experience with Jekyll and Github Pages (git + performance), we decided to use a static site generator. To keep it Python we forced ourselves to use and learn [Pelican](https://github.com/getpelican/pelican). We used an [existing Pelican theme](https://github.com/alexandrevicenzi/Flex). Terminal (Vim), markdown, Git(hub), we felt right at home.

We also put some thought into picking a cool domain name *pybit.es*: short, startswith(‘py’), bite as in learning Python in bite-sized units and .es is from Spain (couldn’t figure out what to do with .au ...). After a quick hello world post [we were online](http://bobbelderbos.com/assets/pybites_home.png), now we had to deliver ...

## Grinding it out

At the start you are just writing, building up a content base. It is hard work and you have to persist. There is no shortcut. You will see a few visitors a day, no comments, no shares, it gets pretty lonely at times, self doubt might kick in. The majority give up at this point but, if you stick with it consistently eventually you will get noticed and traffic starts to flow in. 


We had 2 breakpoints in this regard:

1. We posted the initial idea to Hacker News (appropriately using ‘Show HN: ...’) and got [some positive feedback](https://news.ycombinator.com/item?id=13274876). 

2. After a while we recognized that a lot of developers were stuck in the between-Beginner-and-Intermediate stage, so we wrote a [Python resources post](https://redd.it/5sjt3l) which got a lot of upvotes on the [learnpython subreddit](https://www.reddit.com/r/learnpython/) and got featured on the [Python Bytes podcast](https://pythonbytes.fm/episodes/show/14/lots-of-python-style-and-python-3000-is-3000-days-old). 

From there the ball started rolling.

## Expose your learning, be unique

What makes an interesting blog? We decided from the start that we had to fully expose our learning to get the most out of it. Obviously this takes some courage, especially with the code challenges. Be it writing or coding, it is the best way to learn: 

1. You force yourself to practice at regular intervals, 

2. You care about submitting the best content/code you possibly can, 

3. If you get it wrong, you learn even more. 

There is no shame in that. As [Tim Ferriss said](https://en.wikiquote.org/wiki/Timothy_Ferriss): 

> A person's success in life can usually be measured by the number of uncomfortable conversations he or she is willing to have. 

Anybody performing on stage gets criticized at some point, it goes with the territory. It is hard to please everybody, nor should you want that.

We wanted our blog to be original which meant not limiting ourselves to just [articles](https://pybit.es/archives.html). We cannot exactly recall how the [code challenges](http://pybit.es/pages/challenges.html) came about, but we needed a vehicle to learn and it didn’t seem prevalent elsewhere. 

We inquired HN again and [people seemed interested](https://news.ycombinator.com/item?id=13352447). Our weekly code challenges ([140 forks at this writing](https://github.com/pybites/challenges)) turned out to be a great way to learn from each other, and it is adding an interesting dynamic to our site and brand.

### Market yourself

Brand? Yes. That is the advantage of starting a blog: to help create your brand. We recommend reading [Soft Skills](http://www.amazon.com/dp/1617292397/?tag=pyb0f-20) for practical advice how to market yourself. 

In our second month we hired a designer to make an attractive logo and this really gave PyBites its unique flavor. We became more active on social media. We reached out to fellow Pythonistas. We got invaluable feedback from our readers. We gained quite some traction from Reddit’s [learnpython](https://www.reddit.com/r/learnpython/) (and grew some thicker skin!). 

We started a [Facebook group](https://www.facebook.com/groups/pybites/). We even created two Cheat Sheets to condense part of our learning. It is important to spend some time on marketing your content. You can have top-notch content but if nobody can find you, it might as well just not exist. However ...

### Content is king 

The number one focus should be content. We write our articles with great care. We try to come up with interesting and varied code challenges. We want to develop our own style and voice. To keep the momentum we also commit to a certain weekly volume of work: one code challenge, two articles, and a news digest.

### Automate the boring stuff

To allow us to focus on the important, automation is key. Although we manually craft our newsletter we get the article links via a cron script. We parse [Planet Python](http://planetpython.org), emailing a daily digest to keep up2date. We [auto-tweet our daily script](http://pybit.es/100days-autotweet.html) for our [100DaysOfCode challenge](http://pybit.es/special-100days.html) we are doing these days. 

We use a tool to assist in creating [our weekly Twitter news digest](http://pybit.es/pages/news.html). We have automatic featured images on our posts (red = challenge, blue = article, green = news, purple = special occasion). Code challenge participation has [a process](https://github.com/pybites/challenges/blob/master/INSTALL.md). 

4 months in PyBites is pretty streamlined and that makes things more consistent and compounds to saved time we can use to focus on what matters: the content.

## Sharpen the saw

PyBites made us push the envelope resulting in significant Python learning in the last 4 months. From mastering important concepts of the language to building useful utilities using Pythonic code. If it was not for the blog we would not have had this kind of drive, inspiration nor tooling. 

![pybites is everywhere]({filename}/images/coffee.jpg)

## Building a community

From the start we decided to do a weekly newsletter, growing our following. The number of page views only tells you so much. What you really want is returning visitors and loyal followers that want to read your content every week and can provide you with useful feedback. We want to build a community of passionate Pythonistas that want to learn with us (both directions).

### And we’re just getting started

With this sort of momentum, we only can go forward. With such positive results we are pretty stoked to continue to learn Python inside-out sharing our progress and to keep growing our community. 

### We challenge you

If you like this article we ask you one favor: send this to a friend or co-worker. Identify something that passionates you and partner up with somebody to start creating a blog, open source project, or some other platform to share your learning. There is no better way to hone your skills than daily practice and holding each other accountable. 

We’re eager to hear from you so leave a comment below to share your story / feedback.

We hope this article has inspired you to *take action*. We hope it convinced you that starting a programming endeavor is not that difficult if you are willing to put in *consistent* hard work. 

Besides, helping other people get better is highly rewarding in itself and is an invaluable skill in your developer toolkit. Good luck!

---

Keep Calm and Code in Python!

-- Bob and Julian
