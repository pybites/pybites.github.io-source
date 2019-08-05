Title: PyCon Australia 2019
Date: 2019-08-05 10:29
Category: PyCon
Tags: conference, pycon, learning, community, networking
Slug: pycon-australia-2019
Authors: Julian
Summary: PyCon Australia 2019 was bigger and better than I could have imagined. Here are my takeaways.

PyCon Australia 2019 was, surprisingly, my first Australian Python Convention. It was also the first Python Convention I've attended purely as a spectator. I didn't contribute officially and was just there to learn and meet people.

What an experience!

# The Talks

Let's get to the meat of it. I was impressed by the quality, topic range and professionalism of the talks. Almost all talks I attended, delivered a solid experience. There were very few I got bored in or was underwhelmed with.

Here are my top picks:

<br>
### The unspeakable horror of discovering you didn't write tests - Melanie Crutchfield

Tests are tough. They're even tougher to get into. Melanie delivered a quality, educational and entertaining talk on why it's important to use them. Her story on how she came to use and appreciate tests made the talk relatable which kept me hooked. As a result, I'm actually super excited to get cracking with `pytest`, `selenium` and `pytest-cov`!

**Takeaway:** `pytest-cov` is an awesome tool to check what test coverage your code has. Very cool! Also, Melanie is pretty damn awesome and an incredibly entertaining presenter!

**YouTube:** [https://www.youtube.com/watch?v=QD9YlNoTm2c](https://www.youtube.com/watch?v=QD9YlNoTm2c)

**Slides/Notes**: TBD

<br>
### It's dark and my lights aren't working (an asyncio success story) - Jim Mussared

While the talk didn't end up diving too much into asyncio it more than made up for it by being damn interesting. Jim tells the story of his experience trying to automate the lights in his home. It's a story of hardship, dedication to the cause and is down right inspiring. Seriously, watch this one and see just how technical he gets with the technology he's playing with. I'll also add that he had us laughing for the majority of the talk!

**Takeaway:** Sometimes tech just doesn't work. The stubbornness to never give up is what makes us techies and programmers such an amazing group. Even when the odds are against you, keep searching, keep digging and you'll find a way.

**YouTube:** [https://www.youtube.com/watch?v=grouP9QfdyA](https://www.youtube.com/watch?v=grouP9QfdyA)

**Slides/Notes**: [Slides](https://docs.google.com/presentation/d/1hleL_huvj0Pz2MYzwtxARM7jkqkO2ezi1LF_wJG6TnA/edit?usp=sharing). Transcript is in the speaker notes of the first slide.

<br>
### Shipping your first Python package and automating future publishing - Chris Wilcox

I really enjoyed this one as I've never had to package anything up to publish on PyPI before. I'm even still a little green when it comes to packaging in general so having Chris go through the whole `setup.py` and `setup.cfg` thing was great. He covers best practices, Tox and Nox as well.

**Takeaway:** While `setup.py` is still a thing, `setup.cfg` is much more flexible to use. I'll be seeing how I can utilise setup.cfg from now on. I also need to start diving into Tox (and Nox) to see what all the hubbub is about.

**YouTube:** [https://www.youtube.com/watch?v=nietrteetKQ](https://www.youtube.com/watch?v=nietrteetKQ)

**Slides/Notes:** [Slides](https://speakerdeck.com/crwilcox/pycon-au-2019-shipping-your-first-python-package-and-automating-future-publishing)

<br>
### Python Oddities Explained - Trey Hunner

This was easily one of my favourite talks. Trey has such a deep understanding of how Python works *and* has a wonderfully engaging presentation style. He covers a bunch of weird behaviours in Python that he's encountered over the years. It's a highly informative talk and I loved it.

**Takeaway:** There is a *lot* that can catch you out in Python. If you have any weird behaviour, have a good look through your code and make sure you have your scope referenced correctly. The `+=` operator can be insanely useful and painful!

**YouTube:** [https://www.youtube.com/watch?v=4MCT4WLf7Ac](https://www.youtube.com/watch?v=4MCT4WLf7Ac)

**Slides/Notes:** [Slides](https://treyhunner.com/python-oddities/#/)

<br>
### Goodbye print statements, hello debugger! - Nina Zakharenko

Debugging my code has long been a fear of mine. At most, I use `print()` statements to help me see what's going on where and what object is being assigned what value. It's a pain, but it's comfortable and it works. Nina shattered the barrier into debugging for me. Using `pdb` and `ipdb` she demonstrated how to use the tool to debug code and managed to do so in a way that didn't make the complete noob (me) feel like an idiot. I've never been so excited for my code to break!

**Takeaway:** `ipdb` is going to be the debugger I jump into. I should also stop being so afraid to dive into a new topic when it comes to coding. Also, Microsoft Clippy still lives! (In sticker form).

**YouTube:** [https://www.youtube.com/watch?v=HHrVBKZLolg](https://www.youtube.com/watch?v=HHrVBKZLolg)

**Slides/Notes:** [Slides and Blog](https://www.nnja.io/post/2019/pycon-australia-2019-goodbye-print-hello-debugger/)


<br>
# The People

I've said before that it's the people that make the conference special. PyCon AU was no different. I met so many incredible people over the 3 days. Some were even drawn to the [@PythonicStaff](https://twitter.com/PythonicStaff) I was carrying around in Anthony Shaw's absence.

Of special note, I have to mention two fantastic members of our PyBites Community - [Anthony](https://twitter.com/anthlis) and [Marc](https://twitter.com/Gwalmachi). Both of these chaps came out and allowed me to spend time with them throughout the conference.

Attending talks is always fun but doing it with friends (I'm assuming we're now friends) makes it a little more special. We learned a lot together and the guys were so inspired they even ran off to buy some MicroBit devices so they could play around with MicroPython.

Of course, PyBites Community aside, there were all sorts of cluey people around. Within 10 minutes of being at the conference I met a guy named Gavin who was doing audio analysis with an Adafruit device mounted to a home-made wooden box. (This is totally an understatement, what he was doing was way over my head!).

I was able to forge new relationships with Pythonistas from around Australia (including one who was taking the [#100DaysofCode in Python course](https://talkpython.fm/100days?s=pybites) !) and I got to spend much needed time with friends I'd made at PyCon US. Trey and Melanie, you guys rock!


<br>
# The Code

Some of the coding concepts, ideas and thoughts I've taken away from the conference:

- I need to push having tests on all of my code. I'll be using `pytest` and `pytest-cov` for most code but will dive into Selenium where required. It's time to stop being intimidated and just start doing it.

- On that same note, `pdb` or `ipdb` is going to start making an appearance. I want to debug properly.

- Never leave `pdb` `breakpoint()`s in Production Code! (Python 3.7)

- As I've wanted to get into drones, I should take a look at `pyparrot` to add some Python goodness to the experience.

- Give `doctest` a go as a testing framework. Could be useful in smaller situations where I don't *want* my code to be able to run unless it passes all tests.

- It's way out of my area of expertise right now but WASM looks like it could be fun to dive into.

- If I want to have a play with 3D Rendering in Python, I should take a look at `vpython` and [glowscript.org](https://glowscript.org).

- Have a stab at using cookiecutter.

- I really need to make a concerted effort to understand the "behind the scenes" of Python. Which functions call which dunder methods and how they work.

- MicroPython is awesome.

- Consider the impact to my users when I roll out updates. Something I already do but just a timely reminder from the ["What PHP Learned from Python"](https://www.youtube.com/watch?v=V9ZC2CwkE0I) talk.


<br>
# The Missed Talks

There were quite a few talks I missed due to conflicts in the schedule, my ability to get to them or just plain being knackered:

- ["Git hook\[ed\]" on images & up your documentation game - Veronica Hanus](https://www.youtube.com/watch?v=alej-1P411A)

- [Creating Lasting Change - Aurynn Shaw](https://www.youtube.com/watch?v=2fAorT_bc1I)

- [Tracing, Profiling & Debugging in Production (eBPF) - Trent Lloyd](https://www.youtube.com/watch?v=jXzEzmz-oag)

- [What makes Micro:bits different? - Jack Reichelt](https://www.youtube.com/watch?v=ZEg0cLKwzF4)

- [Threat Modeling the Death Star - Mario Areias](https://www.youtube.com/watch?v=kYD5OrzsvMI)

- [Building a Sustainable Python Package Index - Dustin Ingram](https://www.youtube.com/watch?v=gcbNT3tLgUg)

> [All PyCon AU 2019 talks can be seen on YouTube here](https://www.youtube.com/playlist?list=PLs4CJRBY5F1LKqauI3V4E_xflt6Gow611).

<br>
# Inclusivity

It'd be remiss of me not to mention just how inclusive PyCon AU is. It doesn't matter what race, gender or however you identify, you'll have a home there. 

Everyone was comfortable in their own skin. Everyone was respectful of opinions and appearance. Heck, the bathrooms even had powerful signage to ensure people were empowered to use whichever bathroom they felt comfortable using.

Seeing people of all shapes, sizes, colours, \*, all learning harmoniously without any prejudice was truly a highlight for me. I couldn't be more proud to be part of this community.


<br>
# Conclusion

As you can see, I missed quite a few quality talks but that's how it goes at PyCon. The chance to spend time with friends and to learn is one you should never pass up. There's so much to be gained from the PyCon conferences thanks largely to the amazing Python Community.

It's been 3 brilliant, insightful and inspirational days and I'm grateful for the time I was allowed there. I was even able to, finally, introduce one of my favourite colleagues to the community!

If you haven't been to a PyCon yet, make it happen. If you can get to one in Australia, even better. Just make sure you stop by and <a href="https://youtu.be/WdAun0NpF5A?t=87" target="_blank">say G'day</a>!

Keep Calm and Code in Python!

-- Julian
