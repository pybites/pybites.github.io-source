Title: 15 Refactoring Tips That Will Improve The Quality of Your Code
Date: 2020-04-19 11:00
Category: Tips
Tags: pythonic, refactoring, coding, beautiful code, code quality, testing, loose coupling, McCabe, cyclomatic complexity, classes, functions, data structures
Slug: python-refactoring
Authors: Bob
Illustration: content/images/multicolored-pins.jpg
Summary: Refactoring is all about making your code more maintainable. In this article I provide you with 15 tips to write better code.
cover: images/featured/pb-article.png

(Photo by Jeff Frenette on Unsplash)

> Whenever I have to think to understand what the code is doing, I ask myself if I can refactor the code to make that understanding more immediately apparent. ― Martin Fowler

Refactoring is all about making your code more maintainable.

> One of the most important takeaways of McCabe’s cyclomatic complexity is that functions and methods that have the highest complexity tend to also contain the most defects. [source](https://medium.com/unbabel/refactoring-a-python-codebase-using-the-single-responsibility-principle-ed1367baefd6)

And keeping things relatively simple so code can evolve in a healthy way.

In this article some of my favorite techniques. Notice how I originally aimed for 20 Pythonic tips, but they became more software generic as I progressed. 

So the good news is that once you grasp these concepts you can use them in any programming endeavor.

1. Use lookup tables

If you have a long sequence of if / elif / ... / else (or a `switch` statement in other languages), you can probably rewrite it by keeping a mapping of (key, value) pairs, retrieving the value by looking up the key. This is much cleaner and easier to extend.

2. Looping

Programmers coming from C tend to a lot of acrobatics like `for i in range(len(durations)):`. In Python you can just do `for i in durations:` ([thanks Julian](https://pybit.es/refactoring.html)).

3. Know the standard library

`enumerate` gives you a free counter variable in the loop, for example if names is `['bob', 'julian', 'martin', 'AJ']` and you want to print them with a counter, you can do so with `for i, name in enumerate(names, 1): ...`

Python has batteries included and every week I discover new things, but some noticeable things if you're new to Python: `max`, `min`, `sum`, `all`, `any`, `sort(ed)`'s `key` for robust sorting. Or use `zip` to iterate over multiple sequences at once.

The point is that using those builtin constructs lead to shorter, more readable, and oftentimes faster code.

Plenty of features you can discover and practice in [our Bites](https://codechalleng.es/bites).

Keep up with new features, for example since 3.7 we have `dataclasses` which eliminate a lot of boilerplate / setup code.

4. Data structures

Know your data structures.

Sets and dicts are much faster than lists for membership checking.

Check out the `collections` module sooner rather than later: `namedtuple`s lead to more readable code, `defaultdict`s are very convenient to stop looking for keys in a dict before adding values, `Counter` is very Pythonic, and depending your use of lists, consider a `deque`.

5. Keep it DRY

Don't repeat yourself. Avoid duplicated code at all costs.

With duplication you will inevitably forget to update one of the copies.

Extract repetitive code into helper functions or use a decorator if you need to apply the same functionality to multiple functions or methods.

6. Context managers

Every time you manage a resource of some kind (e.g. files) use a context manager or `with` statement so the clean up step, or freeing up of the resource, runs automatically.

If you see a `try/except/else/finally`, this could be a candidate to use a `with` statement instead: more elegant/ readable, less code.

7. OOP vs functions

When you use a class and it has 1 or 2 functions and does not have to hold state, use a plain function ([stop writing classes](https://www.youtube.com/watch?v=o9pEzgHorH0)), conversely if a bunch of functions work on the same objects, turning them into a class can be really beneficial.

Class inheritance can be very powerful, for example if you want to support multiple report formats. All reports have the same basic attributes and behaviors which can be re-used, but each format is specific, which you can refine in its subclass.

Another deisgn pattern to consider is [Composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance).

8. Deeply nested code

Follow the Zen of Python!

One of my favorite principles is "Flat is better than nested". 

Code with a lot of indenting is a red flag, extract code into helper functions, and use `continue` to reduce nesting or return early from a function.

As the quote at the start says: "One of the most important takeaways of McCabe’s cyclomatic complexity is that functions and methods that have the highest complexity tend to also contain the most defects", so be concious of the amount of decision points in a function/method!

9. Loose coupling / modularize your code

As your code base grows, group similar functionality into modules, this keeps things isolated or to quote the Zen of Python again: "Namespaces are one honking great idea -- let's do more of those!"

Always separate concerns, so that the individual pieces of the system can easily be re-used and tested. Last week I helped somebody with his data analysis app and we established a clear separation between: 1. obtaining the input data, 2. cleaning / analyzing it, and 3. generation of the output report.

Similarly in web frameworks like Django there is a clear split of responsabilities via MVT / Model (data access layer) - View (business logic / kind of a broker between data and presentation) - Template (presentation layer).

Code that is tightly coupled is harder to extend. So ask yourself: how much should the component of the system know about each other?

A loosely coupled system is one in which each of its components has, or makes use of, little or no knowledge of the definitions of other separate components (Wikipedia)

10. Length matters

Avoid long functions and (God) classes.

[SIG](https://www.softwareimprovementgroup.com/) recommends 15 lines per function which can be tough, but remember shorter functions / methods are easier to test.

When you start to limit functions to one clear task you'll soon realize you need to move stuff over into different functions / classes / modules. Easier to maintain and extend, happier developers.

11. Keep interfaces small

[SIG](https://www.softwareimprovementgroup.com/), who do a great job at [quantifying good software](https://www.softwareimprovementgroup.com/resources/ebook-building-maintainable-software/), recommends 4 or 5 max.

Again, it comes down to re-use and testability which is easier for units with fewer parameters.

So if you pass `**kwargs` between functions is that really explicit? Would you give the caller too much freedom?

What about 10 related args, would it be cleaner to pass in one object that has those args as attributes?

12. Exception handling

Another golden nugget from the Zen of Python: "Errors should never pass silently. Unless explicitly silenced."

How often have I lost valuable time debugging silent errors.

[Try/except/pass is one of the worst anti-patterns](https://pybit.es/error_handling.html). Name and catch explicit exceptions (conditions).

Also keep your try blocks small to prevent catch-all scenarios.

Here is a bit more on [exception handling](https://pybit.es/error_handling.html).

13. Don't hardcode literals / config

Everytime you see a check of `var == 5` somewhere at line 127, it's a red flag.

At the least you should abstract the `5` into a _constant_ and if it's something that could change consider making it a config variable.

You could load those in as environment variables or from a (.env, yaml, etc) config file.

This makes the code more versatile because consumers can now define these things without relying on modifying the code.

14. Leverage Git

Huh? Yeah, we don't have to leave code commented in our code base.

You can delete it and make a meaningful commit. Your code will still be under version control and can be pulled back any time.

15. Bonus: dev best practices

Not really a refactoring tip per se, but any refactoring starts with having good test coverage, and a good understanding of the code base.

Documentation of current functionality and good specification of new features prevent a lot of code that gets written without truly understanding what needs to happen.

It often pays off big time to take a step back and (re-)think how everything ties together.

---

What refactoring tips can you add to the mix? Comment below.

- Bob

<div class="ctaBox">
▸␣␣␣<p>With so many avenues to pursue in Python it can be tough to know what to do. If you're looking for some <strong>direction</strong> or want to take your Python code and career to the next level, <a href="https://pybit.es/pages/apply.html" target="_blank">schedule a call with us now</a>. We can help you!</p>
</div>
