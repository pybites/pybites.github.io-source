Title: Why Python is so popular in Devops?
Date: 2018-06-25 18:25
Category: DevOps
Tags: guest, devops, deployment, scripting, netaddr, data visualization, sysadmin, automation
Slug: python-and-devops
Authors: Rhys Powell
Summary: Along with the growth of Python for developers in the machine learning and data science space, Python is also a growing language for devops / in the ops tooling side. In this article Rhys will explain why that is ...
cover: images/featured/pb-guest.png

Along with the growth of Python for developers in the machine learning and data science space, Python is also a growing language for devops / in the ops tooling side. In this article Rhys will explain why that is ...

## A bit of background

To understand why Python has been chosen you need to look at the environments and backgrounds of the people that have traditionally done ops works.

For many years \*nix systems and their operators have had the mindset of automating their works flows, _a good sysadmin is a lazy sysadmin_. This has been supported through the ability to code in the shell, _bash_ being the default on many systems for many years.

The ability to string together your shell commands into script files then run them time and time again was a very powerful thing. The difficulty was that trying to match what you get from modern languages is sometimes difficult and messy, so alternatives were sought. This is where Python stepped in ...

## Why Python?

1. Its ubiquity and the fact it has been used for many years by OS providers gave admins the same warm fuzzy feeling as bash: they knew that they could write their scripts locally and that it should work anywhere, saving the need for individual scripts for all the different systems.

2. Python is easy to read and learn. It’s also easy to copy, paste and run. Sometimes things just need to get done and Python allows you to jump into some complex things without the need to fully understand everything that’s happening. I’m not saying that’s a good thing, but if your site is down and the boss is screaming, sometimes the ability to just google, copy, paste and run, knowing you stand a good chance of achieving what you want, is just enough.

3. No need for object oriented programming. No structured coding required either. You can go straight into grabbing what you want and doing the work. Much like shell scripting (PyBites addition - related Pycon 2018 talk: [Solve Your Problem With Sloppy Python](https://www.youtube.com/watch?v=QsTVDx20y1M)).

4. Batteries are mostly included but if not, there is likely a module out there. If you need to poke at a network, no problem, try [netaddr](http://netaddr.readthedocs.io/en/latest/). Need to grab data from a website? Use [BeautifulSoup](https://pybit.es/tag/beautifulsoup.html). Make a simple dashboard/data visualization with [Matplotlib](https://pybit.es/tag/matplotlib.html) or [Bokeh](https://pybit.es/tag/bokeh.html). Python can do it all!

## Big tools, same language

Beyond the day-to-day of ops work there are some big tools based on Python. Infrastructure management has [Ansible](https://www.ansible.com) and [Saltstack](https://saltstack.com), both written in Python. [AWS](https://aws.amazon.com)'s default command line tool is built in Python. [Supervisor](http://supervisord.org) can be used to control services on systems. Or take pytest's [testinfra](https://github.com/philpep/testinfra) which is specifically used for testing infrastructure deployments. Finally, we have [openstack](https://www.openstack.org), the open source cloud platform. Many of the components and management of these tools use Python underneath!

The use of Python in many other areas, and the fact that devops is focused on breaking down silos and working across previously fixed boundaries, has also helped in increasing its use. If your data scientists and your ops guys are using it, the ability to talk and use code across disciplines is very useful.

## Compared with other languages

While Python is certainly a leading choice, there is still the case for Ruby, where tools like [Chef](https://www.chef.io) and [puppet](https://puppet.com) are used. What both languages (as well as JS) can suffer from though is the need to install additional packages. I feel Python is a lot better as you can get most things done with the standard library. However external modules will often allow you to do things in an easier way, [requests](https://requests.readthedocs.io/en/master/) being the perfect example.

This difficulty has moved some developers into using [Golang](https://golang.org), which has many of the benefits of Python, but in addition can produce a _deployable_ component fast and capable of running on anything. This is certainly another language to look out for.

---
Keep Calm and Code in Python!

[Rhys](pages/guests.html#rhyspowell)
