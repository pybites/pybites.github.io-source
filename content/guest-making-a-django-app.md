Title: Making my First Django App
Date: 2020-04-23 21:15
Category: TBD
Tags: Django
Slug: my-first-django-app
Authors: Ryan Cheley
summary: Building my first Django Site and learning so much more than Django
cover: images/featured/pb-guest.png


# My First Django Project

<!-- Indexes are always a good start! -->
## Index
* [The Django App I wanted to create](#my_app)
* [What does it do? ](#do)
* [What’s next?](#next)
* [Final Thoughts](#thoughts)


I've been writing code for about 15 years (on and off) and Python for about 4 or 5 years. With Python it's mostly small scripts and such. I’ve never considered myself a ‘real programmer’ (Python or otherwise). 

About a year ago, I decided to change that (for Python at the very least) when I set out to do [100 Days Of Web in Python](https://training.talkpython.fm/courses/details/100-days-of-web-in-python) from [Talk Python To Me](https://talkpython.fm/home).  Part of that course were two sections taught by [Bob](https://pybit.es/author/bob.html) regarding [Django](https://www.djangoproject.com). I had tried learn [Flask](https://flask.palletsprojects.com/en/1.1.x/) before and found it ... overwhelming to say the least. 

Sure, you could get a ‘hello world’ app in 5 lines of code, but then what? If you wanted to do just about anything it required ‘something’ else. 

I had tried Django before, but wasn't able to get over the 'hump' of deploying. Watching the Django section in the course made it just click for me. Finally, a tool to help me make AND deploy something! But what? 

<a name="my_app"></a>
## The Django App I wanted to create

A small project I had done previously was to write a short [script](https://github.com/ryancheley/itfdb) for my Raspberry Pi to tell me when LA Dodger (Baseball) games were on (it also has beloved Dodger Announcer [Vin Scully](https://en.wikipedia.org/wiki/Vin_Scully) say his catch phrase, “It’s time for Dodger baseball!!!”). 

I love the Dodgers. But I also love baseball. I love baseball so much I have on my bucket list a trip to visit all 30 MLB stadia. Given my love of baseball, and my new found fondness of Django, I thought I could write something to keep track of visited stadia. I mean, how hard could it *really* be?

<a name="do"></a>
## What does it do? 

My Django Site uses the [MLB API](https://statsapi.mlb.com) to search for games and allows a user to indicate a game seen in person. This allows them to track which stadia you've been to. My site is composed of 4 apps:

* Users
* Content
* API
* Stadium Tracker

The API is written using [Django Rest Framework (DRF)](https://www.django-rest-framework.org) and is super simple to implement. It’s also [really easy to changes to your models if you need to](https://www.ryancheley.com/index.php/2019/11/06/updating-the-models-for-my-django-rest-framework-api/). 

The Users app was inspired by [Will S Vincent](https://wsvincent.com) ( a member of the [Django Software Foundation](https://www.djangoproject.com/foundation/), author, and [podcaster](https://djangochat.com)). He (and others) recommend creating a custom user model to more easily extend the User model later on. Almost all of what’s in my Users App is directly taken from his recommendations. 

The Content App was created to allow me to update the [home page](https://stadium-tracker-api.herokuapp.com), and [about page](https://stadium-tracker-api.herokuapp.com/Pages/About) (and any other content based page) using the database instead of updating html in a template. 

The last App, and the reason for the site itself, is the Stadium Tracker! I created a search tool that allows a user to find a game on a specific day between two teams. Once found, the user can add that game to ‘Games Seen’. This will then update the list of games seen for that user AND mark the location of the game as a stadium visited. The best part is that because the game is from the MLB API I can do some interesting things:

1. I can get the actual stadium from visited which allows the user to indicate historic (i.e. retired) stadia
2. I can get details of the game (final score, hits, runs, errors, stories from MLB, etc) and display them on a details page. 

That's great and all, but what does it look like? 

### The Search Tool

![Search](images/making-a-django-app/add-a-game.png)


### Stadia Listing


#### National League West

![Search](images/making-a-django-app/visited-stadia-nl-west.png)


#### American League West

![Search](images/making-a-django-app/visited-stadia-al-west.png)


<a name="next"></a>
## What’s next? 

I had created a roadmap at one point and was able to get through some (but not all) of those items. Items left to do:

* Get Test coverage to at least 80% across the app (currently sits at 70%)
* Allow users to be based on social networks (right now I’m looking at Twitter, and Instagram) probably with the [Django Allauth Package](https://django-allauth.readthedocs.io/en/latest/installation.html)
* Add ability to for minor league team search and stadium tracking (this is already part of the MLB API, I just never implemented it)
* Allow user to search for range of dates for teams 
* Update the theme ... it’s the default MUI CSS which is nice, but I’d rather it was something a little bit different
* Convert Swagger implementation from `django-rest-swagger` to `drf-yasg`

<a name="thought"></a>
## Final Thoughts

Writing this app did several things for me. 

First, it removed some of the tutorial paralysis that I felt. Until I wrote this I didn’t think I was a web programmer (and I still don’t really), and therefore had no business writing a web app.

Second, it taught me how to use git more effectively. This directly lead to me [contributing to Django itself](https://www.ryancheley.com/index.php/2019/12/07/my-first-commit-to-an-open-source-project-django/) (in a very small way via updates to documentation). It also allowed me to feel comfortable enough to write my first post on [this very blog](https://pybit.es/using-python-to-check-for-file-changes-in-excel.html).

Finally, it introduced me to the wonderful ecosystem around Django. There is so much to learn, but the great thing is that EVERYONE is learning something. There isn’t anyone that knows it all which makes it easier to ask questions! And helps me in feeling more confident to answer questions when asked.

The site is deployed on [Heroku](https://www.heroku.com) and can be seen [here](https://stadium-tracker-api.herokuapp.com). The code for the site can be seen [here](https://github.com/ryancheley/StadiumTrackerAPI). 

-- [Ryan](pages/guests.html#ryancheley)