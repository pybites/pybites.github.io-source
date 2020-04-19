Title: Refactoring Opportunities That Will Boost the Quality of Your Code
Date: 2020-04-19 17:00
Category: Tips
Tags: refactoring, coding, beautiful code, refactoring, code quality, testing, loose coupling, McCabe, cyclomatic complexity, classes, functions, data structures, decorators, context managers, with statement, exception handling, Zen of Python
Slug: python-refactoring
Authors: Bob
Illustration: content/images/multicolored-pins.jpg
Summary: Refactoring is all about making your code more maintainable. In this article I will provide you with Python and generic software tips to write better code.
cover: images/featured/pb-article.png

(Photo by Jeff Frenette on Unsplash)

> Whenever I have to think to understand what the code is doing, I ask myself if I can refactor the code to make that understanding more immediately apparent. ― Martin Fowler

Refactoring is all about making your code easier to understand and more maintainable.

Remember, code runs on machines, but you write code for humans!

> One of the most important takeaways of McCabe’s cyclomatic complexity is that functions and methods that have the highest complexity tend to also contain the most defects. ([source](https://medium.com/unbabel/refactoring-a-python-codebase-using-the-single-responsibility-principle-ed1367baefd6))

Hence the challenge (art?) is to keep things as simple as possible so your code can evolve in a healthy way.

In this article some techniques that can help you with that.

In the first half I'll cover some "Pythonic" tips.

n the second half I go into more software generic practices. 

I hope you see your code improve as you abide by those principles, specially the second half of them which are universal.

# Python Code

## Use dictionaries (lookup tables)

If you have a long sequence of `if / elif / ... / else` conditions (a `switch` scenario), you can probably rewrite it by keeping a mapping of (key, value) pairs, retrieving the value by looking up the key.

This is much cleaner and easier to extend.

Note that `dict`s have a `get` method which lets you specify a default value. Really elegant.

## Pythonic looping

Programmers coming from C tend to a lot of acrobatics like `for i in range(len(durations)):`. In Python you can just do `for i in durations:` = _for-each_ loops ([thanks Julian](https://pybit.es/refactoring.html)).

If you need to repeat an action N times, no need to keep a counter, you can just use `for _ in range(10)` (where `_` is a throwaway variables).

Lastly, `enumerate` gives you a free counter variable in the loop, for example if names is `['bob', 'julian', 'martin', 'AJ']` and you want to print them with a counter, you can do so with `for i, name in enumerate(names, 1): ...`

## Leverage the standard library

Python comes with batteries included and after years of usage (a lot of which we distilled in our [Bite Exercises](https://codechalleng.es/bites/)), I still regularly discover new things.

If you're relatively new to Python, checkout the [built-ins](https://docs.python.org/3/library/functions.html) and check out [the docs](https://docs.python.org/3/library/) (but make sure you [exercise often](https://codechalleng.es/bites) so it becomes second nature). 

What has this to do with refactoring? Well, sometimes we see clumsy code to do summing, sorting, finding the max, loop over multiple sequences, etc.

Only to find out it can be written more concisely using `sum(...)`, `sorted(sequence, key=...)`, `max(...)`, `zip(...)`.

Using builtin constructs leads to shorter, more readable, and oftentimes faster code as they use [_lazy loading_](https://en.wikipedia.org/wiki/Lazy_evaluation).

What does this mean? Mentioned `zip` for example takes one element from each iterable it gets passed in, and returns them in a tuple.

It doesn’t construct an in-memory list and exhaust all the input iterators before returning. Instead tuples are constructed and returned only if they’re requested ([source](https://docs.python.org/3/howto/functional.html#built-in-functions)).

Lastly, keep up with new features, e.g. `dataclasses` and [`f-strings`](https://pybit.es/string-formatting.html) which lead to way more concise code.

## Know your data structures.

First there is performance gains from knowing which data structures to use.

For lookups [use `dict`s/ `set`s](https://stackoverflow.com/a/513906).

Beyond the basic data structures, for refactoring there are some gems in the `collections` module:

- `namedtuple`s lead to more readable code,
- `defaultdict`s are very convenient to stop looking for keys in a dict before adding values,
- `Counter` is a very Pythonic way to get most common occurrences,
- and depending on prepending/appending `list`s, a `deque` can be more performant.

---

Check out our [`collections` Learning Path](https://codechalleng.es/bites/paths/collections). Once you grasp these, you'll wonder how you could live without them ...

---

## Context managers

Every time you manage a resource of some kind (e.g. files) use a context manager or `with` statement so the clean up step, or freeing up of the resource, runs automatically.

If you see a `try/except/else/finally`, this could be a candidate to use a `with` statement instead: more elegant/ readable, less code.

To quote Raymond Hettinger (via [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/ch15.html)):

> Context managers may end up being almost as important as the subroutine itself. We’ve only scratched the surface with them. […] Basic has a with statement, there are with statements in lots of languages. But they don’t do the same thing, they all do something very shallow, they save you from repeated dotted [attribute] lookups, they don’t do setup and tear down. Just because it’s the same name don’t think it’s the same thing. The with statement is a very big deal.

--- 

Take your Python to next level with our [Decorators and Context Managers Learning Path](https://codechalleng.es/bites/paths/decorators-context). 

---

## Exception handling

Another golden nugget from the [Zen of Python](https://www.python.org/dev/peps/pep-0020/):

> Errors should never pass silently. Unless explicitly silenced.

How often have I lost valuable time debugging silent errors.

[Try/except/pass is one of the worst anti-patterns](https://pybit.es/error_handling.html). Name and catch explicit exceptions (conditions).

Also keep your try blocks small to prevent catch-all scenarios.

Here is a bit more on [exception handling](https://pybit.es/error_handling.html).

I feel this needs more coverage here still, comment below if interested and what you're struggling with ...

---

# Beyond Python

And now onto the generic software principles.

## Keep it DRY

Don't repeat yourself. Avoid duplicated code at all costs.

> Number one on the stink parade is duplicated code. - Martin Fowler

With duplication you will inevitably forget to update one of the copies.

Extract repetitive code into helper functions or use [a decorator](https://pybit.es/decorators-by-example.html) if you need to apply the same functionality to multiple functions or methods.

## OOP vs functions

When you use a class and it has 1 or 2 functions and does not have to hold state, use a plain function (great talk: [stop writing classes](https://www.youtube.com/watch?v=o9pEzgHorH0)). 

Conversely, if a bunch of functions work on the same objects, turning them into a class can be really beneficial.

Class inheritance can be very powerful, for example if you want to support multiple report formats. All reports have the same basic attributes and behaviors which can be reused, but each format is specific, which you can refine in its subclass.

Another design pattern to consider is [Composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance).

## Avoid deeply nested code

Follow the Zen of Python!

One of my favorite principles is:

> Flat is better than nested.

Code with a lot of indenting is a red flag, extract code into helper functions, and use `continue` to reduce nesting or return early from a function.

As the quote at the start says: "One of the most important takeaways of McCabe’s cyclomatic complexity is that functions and methods that have the highest complexity tend to also contain the most defects", so be conscious of the amount of decision points in a function/method!

## Loose coupling / modularize your code

As your code base grows, group similar functionality into modules, this keeps things isolated or to quote the Zen of Python again: 

> Namespaces are one honking great idea -- let's do more of those!

Always separate concerns, so that the individual pieces of the system can easily be re-used and tested. Last week I helped somebody with his data analysis app and we established a clear separation between: 1. obtaining the input data, 2. cleaning / analyzing it, and 3. generation of the output report.

Similarly in web frameworks like Django there is a clear split of responsibilities via MVT / Model (data access layer) - View (business logic / kind of a broker between data and presentation) - Template (presentation layer).

Code that is tightly coupled is harder to extend. So ask yourself: how much should the component of the system know about each other?

A loosely coupled system is one in which each of its components has, or makes use of, little or no knowledge of the definitions of other separate components (Wikipedia)

## Keep units small

Avoid long functions and (God) classes.

[SIG](https://www.softwareimprovementgroup.com/) recommends 15 lines per function which can be tough, but remember shorter functions / methods are easier to test.

When you start to limit functions to one clear task you'll soon realize you need to move stuff over into different functions / classes / modules. Easier to maintain and extend, happier developers.

## Control your interfaces

[SIG](https://www.softwareimprovementgroup.com/), who does a great job at [quantifying good software](https://www.softwareimprovementgroup.com/resources/ebook-building-maintainable-software/), recommends 4 or 5 max.

Again, it comes down to re-use and testability which is easier for units with fewer parameters.

So if you pass `**kwargs` between functions is that really explicit? Would you give the caller too much freedom?

What about 10 related args, would it be cleaner to pass in one object that has those args as attributes?

## Don't hardcode literals / config

Everytime you see a check of `var == 5` somewhere at line 127, it's a red flag.

At the least you should abstract the `5` into a _constant_ and if it's something that could change consider making it a config variable.

You could load those in as environment variables or from a (.env, yaml, etc) config file.

This makes the code more versatile because consumers can now define these things without relying on modifying the code.

---

## Before refactoring

Not really a refactoring tip per se, but any refactoring starts with having good test coverage, and a good understanding of the code base.

Documentation of current functionality and good specification of new features prevent a lot of code that gets written without truly understanding what needs to happen.

It often pays off big time to take a step back and (re-)think how everything ties together.

---

Well, that's it for now. We have to start somewhere.

I'd like this to be a work in progress though. So feel free to PR additional ones or comment below.

-- Bob

---

** Level up your Python and Career **

With so many avenues to pursue in Python it can be tough to know what to do or how to do it effectively.

If you're looking for some **direction**, [book a Strategy Session with us](https://pybit.es/pages/apply.html) and we dig in where you are, where you want to go, and how we can help you.

---
