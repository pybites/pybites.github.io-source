Title: Effective Developers Leverage Their Toolset
Date: 2020-04-06 10:00
Category: Productivity
Tags: tools, ag, vim, unix, kindle, shell, perl, bookcision
Slug: developer-tools
Authors: Bob
Illustration: tools.jpg
Summary: Last week I did a couple of shared screen sessions debugging and teaching. I paused and reflected on the tools I used and how I sharpened my sword over the years. 
cover: images/featured/pb-article.png

(Photo by Fleur on Unsplash)

> Compound interest is the 8th wonder of the world. He who understands it, earns it; he who doesn’t, pays it. - Albert Einstein

Last week I did a couple of shared screen sessions debugging and teaching.

I paused and reflected on the tools I used and how I sharpened my sword over the years. 

This is not an article on how to deploy software with Docker, how to use git, or how to set up your env, although it has some shell and Vim goodness.

It's more about how small tweaks made me more productive as a programmer and learner.

## Command line

My favorite tool of all time!

A silly example: what day is my birthday?

I could search the web.

I could write a Python program.

Or just use Unix:

	$ cal 4 2020
		April 2020
	Su Mo Tu We Th Fr Sa
			1  2  3  4
	5  6  7  8  9 10 11
	12 13 14 15 16 17 18
	19 20 21 22 23 24 25
	26 27 28 29 30

Nice, this year the 18th will be on a Saturday :)

I often go to my terminal and use simple shell commands before even writing a script (e.g. to iterate over files is as easy as: `for i in *; do ls $i; done` - the `ls` can be any operation).

Combining this with some regex (`perl -pe 's///g'`) can be pretty powerful.

Another example are shell _aliases_, some of my common ones:

	$ alias pvenv
	alias pvenv='/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -m venv venv && source venv/bin/activate'
	$ alias ae
	alias ae='source venv/bin/activate'
	$ alias brc
	alias brc='vim ~/.bashrc'
	$ alias lt
	alias lt='ls -lrth'

I even use it to go to my Kindle highlights:

	$ alias kindle
	alias kindle='open https://read.amazon.com/notebook'

I can just type _kindle_ and get to my book notes instantly.

(Talking about notes, I was actually going to write some code to download my notes, but there is already a tool for this: [Bookcision](https://readwise.io/bookcision), so sometimes the best code is the code you never write!)

---
OK one more.

I have been a nerd about [terminal search for a while](https://bobbelderbos.com/2013/01/search-copy-stackoverflow-data-in-vim-with-conque/), but an easier way is to just use a clever Python tool called [howdoi](https://github.com/gleitz/howdoi) (demonstrated for its elegant code in [The Hitchhiker's Guide to Python](https://www.amazon.com/Hitchhikers-Guide-Python-Practices-Development/dp/1491933178)):

	$ alias howdoi
	alias howdoi='cd $HOME/code/howdoi && source venv/bin/activate && howdoi'

Check this out:

	$ howdoi argparse
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("a")
	args = parser.parse_args()

	if args.a == 'magic.name':
		print 'You nailed it!'

## Text editing

I never felt more awkward having to use Vim in a terminal when I started at Sun Microsystems.

However when I got past the steep learning curve, I became quite fast, using repeated replacement (dot (.) or `:s/string/replace/g`), leverage settings (`.vimrc`) and later on even Python syntax checking ([preventing saving for various errors in VIM](https://gist.github.com/kyokley/0d7bb03eede831bea3fa) -> this is really cool!)

[Here](https://pybit.es/vim-tricks.html) are some more Vim tricks if interested.

## Navigating code bases

At first I was typing `find . -name '*string*' | xargs grep ...` the whole time.

Pretty inefficient.

Till somebody suggested `ag` (aka [The Silver Searcher](https://github.com/ggreer/the_silver_searcher)) and my dev life became so much better.

---
There are many more examples, the key lessons though are:

- Try to constantly improve your toolset, if you realize _there must be a better way to do this_, there probably is and you owe it to yourself to find out about it.

- **Invest the time to become really good at the tools you use**. Your future self will thank you. The time saved (and joy in your daily work) will compound!

---

Again these are sometimes just small tweaks, but they shave off minutes a day, hours a week, days a year. 

Of course for the more serious work I would write shell or Python scripts (preferably latter).

It feels awesome knowing the time and effort you invested learning the tools of the craft is seriously paying off.

---

Keep Calm and Code in Python!

-- Bob

<div class="ctaBox">
<p>With so many avenues to pursue in Python it can be tough to know what to do. If you're looking for some <strong>direction</strong> or want to take your Python code and career to the next level, <a href="https://pybit.es/pages/apply.html" target="_blank">schedule a call with us now</a>. We can help you!</p>
</div>
