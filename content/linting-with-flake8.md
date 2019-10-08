Title: Linting with Flake8
Date: 2019-10-08 20:43
Category: Concepts
Tags: python, beginner, learning, examples, code, linking, flake8
Slug: linting-with-flake8
Authors: Julian
Summary: What the heck is linting? Let's dive into the concept and talk about how flake8 can help us make our code better.
cover: images/featured/pb-article.png

For so long the word "Linting" meant nothing to me. It sounded like some supercoder leet speak that was way out of my league. Then I discovered `flake8` and realised I was a fool.

This article is a simple one. It covers what linting is; what Flake8 is and has an embarrassing example of it in use.

Before we get started, I need to get something off my chest. I don't know why but I really hate the word "linting". It's a hatred akin to people and the word "moist".

Linting. Linting. Linting. *shudder*. Let's move on!


##What is Linting?

Just so I never have to type it again, let's quickly cover off what linting is.

It's actually pretty simple. Linting is the process of running a program that analyses code for programmatic errors such as bugs, actual errors, styling issues etc.

Put it in the same basket as the process running in your favourite text editor that keeps an eye out for typos and grammatical errors.

This brings us to Flake8.


##What is Flake8?

It's one of these linting programs and is pretty damn simple to use. It also happens to analyse your code for PEP8 standard violations!

I love it for a few reasons:

- I'm constantly learning something new. It picks away at my code, pointing out my failings, much like annoying friends.
- It keeps my code looking schmick. It's easy to miss spacing and other tiny things while coding so running Flake8 against my code catches little annoyances before it's pushed to prod.
- It's a much nicer word than "linting".


##Flake8 in Action

To demonstrate my beloved Flake8 I thought I'd grab an old, and I mean old, script that's likely riddled with issues. Judge me not friends!

In an older (I'm really stressing old here) article I wrote a simple script to send emails. No functions or anything, just line by line code. Ignoring what the code actually does take a look at this snippet below. [Full code here](https://github.com/pybites/blog_code/blob/master/generic_emailer/generic_emailer.py).

~~~~
λ cat generic_emailer.py
#!python3
#emailer.py is a simple script for sending emails using smtplib
#The idea is to assign a web-scraped file to the DATA_FILE constant.
#The data in the file is then read in and sent as the body of the email.

<snip> 

DATA_FILE = 'scraped_data_file'
from_addr = 'your_email@gmail.com'
to_addr = 'your_email@gmail.com'  #Or any generic email you want all recipients to see
bcc = EMAILS 

<snip>
~~~~

Now that we have my script, let's run flake8 against it.

1. pip install the sucker:

~~~~
(venv) λ pip install flake8
~~~~

2. Simply run `flake8` and point it at your script. Given `generic_emailer.py` is in my current directory I'd run the following:

~~~~
(venv) λ flake8 generic_emailer.py
~~~~

3. In traditional CLI fashion, if you don't receive any output at all, you have no issues. In my case, yeah, nope. The output I receive when running Flake8 against my script is as follows:

~~~~
(venv) λ flake8 generic_emailer.py
generic_emailer.py:2:1: E265 block comment should start with '# '
generic_emailer.py:3:1: E265 block comment should start with '# '
generic_emailer.py:4:1: E265 block comment should start with '# '
generic_emailer.py:14:35: E262 inline comment should start with '# '
generic_emailer.py:14:80: E501 line too long (86 > 79 characters)
generic_emailer.py:27:50: E261 at least two spaces before inline comment
generic_emailer.py:27:51: E262 inline comment should start with '# '
generic_emailer.py:29:19: E261 at least two spaces before inline comment
generic_emailer.py:29:20: E262 inline comment should start with '# '
generic_emailer.py:31:23: E261 at least two spaces before inline comment
generic_emailer.py:31:24: E262 inline comment should start with '# '
generic_emailer.py:33:1: E265 block comment should start with '# '
generic_emailer.py:38:1: E265 block comment should start with '# '
generic_emailer.py:41:1: E265 block comment should start with '# '
generic_emailer.py:44:1: E265 block comment should start with '# '
~~~~


##Analysing the Output

Before we look into the actual issues, here's a quick breakdown of what the above means.

- The first section is the name of the file we're... flaking... Yes, I'm making the word "flaking" a thing!
- The next two numbers represent the line number and the character position in that line. ie: line 2, position 1.
- Finally, we have the actual issue. The "E" number is the error/violation number. The rest is the detail of the problem.

Now what does it all mean?

Well, the majority of my violations here have to do with the spacing in front of my comments. 

- The E265 violations are simply telling me to add a space after my `#` to satisfy standards.
- E510 is saying I have too many characters in my line with the limit being 79.

You can read the rest!


##Fixing the Violations

Let's quickly fix two of the violations: 

- `generic_emailer.py:14:35: E262 inline comment should start with '# '`
- `generic_emailer.py:14:80: E501 line too long (86 > 79 characters)`

The code in question on line 14 is this:

~~~~
to_addr = 'your_email@gmail.com'  #Or any generic email you want all recipients to see
~~~~

I can actually fix both issues by simply removing the comment. Doing this and running Flake8 again gets me the following output:

~~~~
(venv) λ flake8 generic_emailer.py
generic_emailer.py:2:1: E265 block comment should start with '# '
generic_emailer.py:3:1: E265 block comment should start with '# '
generic_emailer.py:4:1: E265 block comment should start with '# '
generic_emailer.py:27:50: E261 at least two spaces before inline comment
generic_emailer.py:27:51: E262 inline comment should start with '# '
generic_emailer.py:29:19: E261 at least two spaces before inline comment
generic_emailer.py:29:20: E262 inline comment should start with '# '
generic_emailer.py:31:23: E261 at least two spaces before inline comment
generic_emailer.py:31:24: E262 inline comment should start with '# '
generic_emailer.py:33:1: E265 block comment should start with '# '
generic_emailer.py:38:1: E265 block comment should start with '# '
generic_emailer.py:41:1: E265 block comment should start with '# '
generic_emailer.py:44:1: E265 block comment should start with '# '
~~~~

Note the two violations are gone.


##Ignoring Violations

What if I don't care about the spacing of my comment `#`s?

Sometimes you'll want Flake8 to ignore specific issues. One of the most common use cases is to ignore line length.

You can do this by running `flake8 --ignore=E<number>`. Just specify which violations you want to ignore and Flake8 will overlook them.

To save yourself time you can also create a Flake8 config file and hardcode the violation codes into that. This method will save you specifying the code every time you run Flake8.

In my case I'm going to ignore those pesky `E265` violations because I can.

I need to create a `.flake8` file in my parent directory and add the following (with vim of course!):

~~~~
(venv) λ touch flake8
(venv) λ cat .flake8
[flake8]
ignore = E265
~~~~

When I re-run Flake8 I now see the following:

~~~~
(venv) λ flake8 generic_emailer.py
generic_emailer.py:27:50: E261 at least two spaces before inline comment
generic_emailer.py:27:51: E262 inline comment should start with '# '
generic_emailer.py:29:19: E261 at least two spaces before inline comment
generic_emailer.py:29:20: E262 inline comment should start with '# '
generic_emailer.py:31:23: E261 at least two spaces before inline comment
generic_emailer.py:31:24: E262 inline comment should start with '# '
~~~~

The rest of the errors are an easy clean up so I'll leave it here.


##Flake8 on PyBites CodeChallenges

As luck would have it, we've just implemented a new feature on the [PyBites CodeChallenges](https://codechalleng.es) platform that allows you to run flake8 against your browser based code!

Now you can have flake8 lint your code to perfection while you solve our Bites.

Check it out in all its glory:

![flake8-codechallenges.png]({filename}/images/flake8-codechallenges.png){.border}


##Conclusion

Whether you like the word Linting or not, there's no denying the value it can provide - Flake8 case in point.

While it can definitely grow a little tiresome at times if you have a well crafted config file you can customise it to your liking and pain threshold.

It really is a brilliant tool to add to your library so give it a try!

Keep Calm and Code in Python!

-- Julian

