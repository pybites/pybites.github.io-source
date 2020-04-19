Title: Refactoring Opportunities That Will Boost the Quality of Your Code
Date: 2020-04-19 22:22
Category: Tips
Tags: refactoring, code quality, loose coupling, McCabe, cyclomatic complexity, classes, functions, testing, Django, design patterns, DRY, OOP, decorators
Slug: refactoring-opportunities
Authors: Bob
Illustration: multicolored-pins.jpg
Summary: Refactoring is all about making your code more maintainable. In this article I will provide you with Python and generic software tips to write better code.
cover: images/featured/pb-article.png

(Photo by Jonah Pettrich on Unsplash)

Refactoring is all about making your code easier to understand and more maintainable.

Remember, code runs on machines, but you write code for humans!

> One of the most important takeaways of McCabe’s cyclomatic complexity is that functions and methods that have the highest complexity tend to also contain the most defects. ([source](https://medium.com/unbabel/refactoring-a-python-codebase-using-the-single-responsibility-principle-ed1367baefd6))

Hence the challenge (art?) is to keep things as simple as possible so your code can evolve in a healthy way.

Previously we discussed [the importance of refactoring](https://pybit.es/refactoring.html). In this article we look at some refactoring opportunities.

## Keep it DRY

Don't repeat yourself. Avoid duplicated code at all costs.

> Number one on the stink parade is duplicated code. - Martin Fowler

With duplication you will inevitably forget to update one of the copies.

Extract repetitive code into helper functions or use [a decorator](https://pybit.es/decorators-by-example.html) if you need to apply the same functionality to multiple functions or methods.

## OOP vs functions

When you use a class and it has 1 or 2 functions and does not have to hold state, use a plain function (great talk: [stop writing classes](https://www.youtube.com/watch?v=o9pEzgHorH0)). 

Conversely, if a bunch of functions work on the same objects, turning them into a class can be really beneficial.

Class inheritance can be very powerful. For example, say you want to support multiple report formats. All reports have the same basic attributes and behaviors which can be reused, but each format is specific, which you can further define in subclasses.

Another design pattern to consider is [Composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance).

## Avoid deeply nested code

Follow the Zen of Python! One of my favorite principles is:

> Flat is better than nested.

Code with a lot of indenting is a red flag, extract code into helper functions, and use `continue` to reduce nesting or return early from a function.

As the quote at the start says, "functions and methods that have the highest complexity tend to also contain the most defects", so be conscious of the amount of decision points in your code!

## Loose coupling / modularize your code

As your code base grows, group similar functionality into modules, keeping things isolated. Or to quote the Zen of Python again: 

> Namespaces are one honking great idea -- let's do more of those!

Always separate concerns, so that the individual pieces of the system can easily be re-used and tested.

Last week I helped somebody with his data analysis app and we established a clear separation between:

1. obtaining the input data,

2. cleaning / analyzing it, and

3. generation of the output report.

Similarly in web frameworks like Django there is a clear split of responsibilities using the MVT pattern:

- Model (data access layer),

- View (business logic / kind of a broker between data and presentation),

- Template (presentation layer).

Code that is tightly coupled is harder to extend and test.

So ask yourself: how much should the components of the system know about each other? 

## Keep units small

Avoid long functions and (God) classes.

[SIG](https://www.softwareimprovementgroup.com/), who does a great job at [quantifying good software](https://www.softwareimprovementgroup.com/resources/ebook-building-maintainable-software/), recommends 15 lines max per function.

This can be tough, but remember shorter functions / methods are easier to test.

When you start to limit functions to one clear task, you'll soon realize you need to move stuff over into different functions / classes / modules which makes it easier to maintain.

## Control your interfaces

Interfaces meaning the parameters we pass between functions, classes, etc.

[SIG](https://www.softwareimprovementgroup.com/) recommends max. 4 or 5.

Again, it comes down to re-use and testability which is easier for units with fewer parameters.

So if you pass `**kwargs` between functions is that really explicit? Would you give the caller too much freedom?

What about 10 related args, would it be cleaner to pass in one object that has those args as attributes?

## Don't hardcode literals / config

Everytime you see a check of `var == 5` somewhere at line 127, it's a red flag.

At the least you should abstract the `5` into a constant. And if it's something that could change consider making it a config variable.

You could load those in as environment variables or from a (.env, yaml, etc) config file.

This makes the code more versatile, because consumers can now define these things independently of the code.

## Delete dead code

Remove code that is not called or commented out. It clutters up your modules and you can still retrieve it from version control.

## Pre-requisites

Before you can do any significant refactoring you need to have good test coverage in place. 

We write about testing [here](https://pybit.es/category/testing.html) and a great resource on the subject, and software development in general, is Brian Okken's [Test & Code podcast](https://testandcode.com/).

Documentation of both current and new feature code is crucial too. This can prevent badly designed code.

It often pays off big time to take a step back and (re-)think how everything ties together before starting to write code.

---

I hope this gave you some food for thought where to look for refactoring candidates.

-- Bob

---

** Level up your Python and Career **

With so many avenues to pursue in Python it can be tough to know what to do. 

If you're looking for some **direction**, [book a free strategy session with us now](https://pybit.es/pages/apply.html). We can help you!

---
