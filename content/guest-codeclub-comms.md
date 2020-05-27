Title: Rockstar Python Developers Need Great communication Skills Too
Date: 2020-05-04 09:15
Category: Communication
Tags: communication, Code Club, mentoring, coaching, soft skills, kids, duck typing, meetups
Slug: guest-communication-skills
Authors: Anthony Lister
Illustration: kids.jpg
summary: Mentoring children is a whole new challenge, and one that served to help me think about my own communication and empathy skills at work too.
cover: images/featured/pb-guest.png

Mentoring children is a whole new challenge, and one that served to help me think about my own communication and empathy skills at work too.

## Introduction

I wonder how people get into software programming, whether it be for a job or hobby? 

It's one of the first things I often listen for at the start of [Michael Kennedy's Talk Python To Me podcast](https://talkpython.fm/).

Who was it that inspired you? 

What was it about their character that got you fired up and writing ```print("hello world")``` for the first time? 

How did someone make you feel when they recently guided you to a solution that you came up with by yourself?

## Coding is perhaps the easiest part of being a developer

Python programming is a way I keep my technical chops sharp while I do commercial, contractual and financial work in my management role nowadays. This article draws on my experience in volunteering my time mentoring children around the ages 9-13. I have done this through [STEM](https://en.wikipedia.org/wiki/Science,_technology,_engineering,_and_mathematics#Europe) initiatives in local New Zealand schools; by also being a judge at a high profile regional schools' science and technology fair, and more recently, at a local after-school digi-tech club through Code Club Aotearoa. Volunteering for a Code Club involves travelling to your local primary or intermediate school, or public venue, once a week to help run your club with other volunteers and a schoolteacher for one hour.

I'm grateful to have a supportive boss who lets me take an hour of my week to do this. It comes under creating a sustainable future in my personal development plan - i.e. getting schoolchildren interested in technology at an early age and showing them the various career paths available. My boss happens to be an ex-fighter pilot flying instructor, so he knows a thing or two about teaching people and getting them to do the right thing at the right time! I was surprised he agreed to let me do this and we've often exchanged the challenges of teaching, and developing communication skills, in our own catchups since. 

Mentoring children is a whole new challenge, and one that served to help me think about my own communication and empathy skills at work too. 


## One of my first Code Club Python sessions went something like this...

Let's set the scene. It's a few weeks into the school term, and those students that have completed their project work using Scratch 3 can start to learn Python.

A student is working on writing a program to ask the user their age, and then tell them their age in dog years! You can calculate a person’s age in dog years by multiplying their age by 7 apparently. 

So, after failing to set-up their installed VS Code because their school managed device won't allow installation of the Python extension, I encourage the use of [repl.it](https://repl.it/) instead. Next comes the hurdle of explaining why the multiplication sign is a '*' and not a 'x' like the teacher writes on the whiteboard in maths lessons. Some children have used a computer for solving maths problems more than others it seems.  

Eventually, the coding session goes something along these lines...

```python
>>> input("What is your age? ")
```

"That's a good start but have a think about creating a variable so you can re-use the same piece of code over and over again and printing out the result."

```python
>>> input("What is your age? ")
>>> age = 9
```
"Hmmm, not quite, let me explain....", and a conversation around variables, names and objects begins. This is where I've broken out and used [PythonTutor](http://www.pythontutor.com/) before, but it can also confuse and overwhelm a 9-year-old.  

We make some success. 

```python
>>> age = input("What is your age? ")
What is your age? 9
>>> print(age)
9 
```
So far, so good. "Now, multiply that by seven and present your answer". 
"That's easy", they say.

```python
>>> age = input("What is your age? ")
What is your age? 9
>>> print(age)
9 
>>> dog_years = age * 7
>>> print(dog_years)
9999999
```

"It doesn't quite work!", the student exclaims. The class teacher hears this, and I smile knowingly. The other students put their heads in their hands upon reaching the same point in the lesson plan too. They soon start talking and spark up a browser tab to play an online game that admittedly looks quite cool. 

And immediately a dialog starts in my head that goes something like this: 

"Python uses duck typing and has typed objects but untyped variable names. Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that the given object is not of a suitable type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are not well-defined (for example, adding a number to a string) rather than silently attempting to make sense of them."

But I can't say any of that to a nine year old! 

"Erm, it's because of... ", and I mentally pause because what I was about to say is "there's this thing called duck typing in Python. If it walks like a duck and it quacks like a duck, then it must be a duck!", and I just know that I'm going to be laughed out of the classroom and be admonished forever if I said that.

"It's because the result is a string, not a number", as I scan the child's face for the rolling of their eyes at me. "Let's check its type. I'll show you how", I say, trying to rescue the situation before thinking I've put them off coding for life. 

```python
>>> age = input("What is your age? ")
What is your age? 9
>>> print(age)
9 
>>> dog_years = age * 7
>>> print(dog_years)
9999999
type(dog_years)
<class 'str'>
>>>
```

At this point, she's looking at me confused. “It's clearly a number on the screen, and which number are you talking about anyway?”, she asks. 

Children are really good at asking "why?". 

In fact, my experience has taught me that they are relentless ninjas at asking why at least five times, even after offering your best answer. Oh, the innocence. 

I keep looking at the clock. Is the session nearly finished yet? It's so hot in here. 

"Let's change the type of variable 'age' into an integer number instead of a string, do you know how to do that?", I ask.

Phew, she finally gets the answer of 63. I'm relieved. But then another student next to her types in her age as 'nine'. I put my head into my hands this time. 

Oh, and there's the bell! 

"Great session team!", I exclaim, "Next week, we'll talk about reusing code and using functions". 

My car drive back to the office leaves me shuddering as I think about having to explain code indenting and whitespace next week. 

I get back to the office. "How did today's coding go then?", asks my boss, "And did you remember your five ways to answer the same question?". He smiles knowing I learned more about myself than they did about coding today. 


## A call to action

> You don't even need to consider yourself a specialist either if you can readily ask enquiring and supportive questions.

This article is a hats off to all the teachers and mentors I've had throughout my engineering career and Python hobby. It's for all the people who have inspired me and pushed me just that little bit further in my endeavours. They have all had one common character trait; that is being able to communicate well and with empathy. These are the rockstar developers and mentors to me.

We might all have different abilities now, but we were all beginners in the first place and looked to others for guidance and support in the early days just like the children in this code club. 

Why not make that a positive experience for beginners in the best way you can?

At the time of writing many of us will be locked down in our bubbles due to Covid-19. As we get through this and life returns to a new normal, I urge you to seek out your local opportunities to volunteer for an organisation like Code Club in your region. If working with children isn't your thing, perhaps go to a Python Meetup and explain something technically deep to an inexperienced audience, or even just try to explain something clearer at your next project meeting at work. Start high level, set the scene, go technically deep as your audience needs to and then summarise at that high level what you just spoke about. 

> Rockstar Python Developers need great communication skills too.

Remember that communication is as much about the receiver as it is the transmitter! It's another way to give back to the community if you like. You might find it very rewarding and enlightening about your own skills and development too. Let me know how it goes. What are your experiences?

All the best!

-- [Anthony](pages/guests.html#anthonylister)

(Cover photo by Rachel on Unsplash)

## Code Club

Code Club Aotearoa comes under the umbrella [Code Club organisation](https://codeclub.org/en/). Code Club volunteers join a local club and help children aged 9-13 learn to make games, animations and websites using the Code Club resources.

You don't even need to consider yourself a specialist either if you can readily ask enquiring and supportive questions. I'm certainly no expert in Python and suffer imposter syndrome as much as the next person. Also, students don't mind being shown how to search for answers if you don't know there and then, but be prepared to have your Google-Fu search skills shown up by these digital natives! 

There are a variety of projects provided to you as a volunteer in [the Code Club curriculum](https://projects.raspberrypi.org/en/codeclub). These include projects in Scratch, HTML/CSS, Python and Raspberry Pi, and even MicroPython on Lego Mindstorms. Code Club students are traditionally 9-13 years old. Very often students enter their first club with no prior coding experience so they will need to get started with the basics. However, Code Club students are from all varying levels of technical ability, ethnicity, gender and are all excited to learn to code!
