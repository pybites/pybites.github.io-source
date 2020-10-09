Title: 10 Things We Picked Up From Code Reviewing
Date: 2020-09-24 18:43
Category: Tips
Tags: clean code, software development, best practices, software quality, code reviewing
Slug: code-reviewing
Authors: Bob
Summary: Here are some things we picked up from code reviews that when addressed can make your code a lot cleaner.
cover: images/featured/pb-article.png

_We originally sent the following 10 tips to our [Friends List](https://pybit.es/pages/friends) and we received requests to post it here for reference, so here you go ..._

Ever wondered what you could learn from a code review?

Here are some things we picked up from code reviews that when addressed can make your code a lot cleaner:

1. Break long functions (methods) into multiple smaller ones - this will make your code more reusable and easier to test.

	Remember each function should do only **one** thing. Example: a function that parses a csv file, builds up a result list and prints the results does 3 things and should be split accordingly.

2. Move _magic numbers_ sprinkled in your code, to constants (at the top of your module) - again easier to reuse, more readable, less surprises later on.

3. Watch out for anything that you put in the global scope, localize variables (data) as much as possible and you'll have less unexpected side consequences.

4. Use `flake8` (or `black`) - more consistent, ([PEP8](https://pep8.org/) compliant code) is easier to read and earns you more respect from fellow developers (also remember: "how you do the small things determines how you do the big things" - very true with software development).

	This  goes back to developers writing code not only for machines, but also (and more importantly) for other developers. E.g.: really long lines might annoy your colleagues that use vsplit to look at multiple code files at once.

5. Keep `try/except` blocks narrow (ask yourself: "Are all those lines in between really going to throw this exception?!") and avoid _bare exceptions_ or just using pass or reraising an exception without additional error handling code (e.g. at least log the error).

6. Leverage the Python language (_Pythonic code_) - for example replace a `try/finally` with a `with` statement, don't overly check conditions (_leaping_), just `try/except` (_ask for forgiveness_). Here is a great article on this topic: [Idiomatic Python: EAFP versus LBYL](https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/).

	Another example is relying on Python's concept of _truthiness_ (e.g. just do `if my_list` instead of `if len(my_list) > 0`).

7. Use the right data structure - if you check for membership in a big collection it's often better to use a `set` over a `list` which would be scanned sequentially and is therefor slower.

8. Leverage the [Standard Library](https://docs.python.org/3/library/) - you don't have to reinvent the wheel.

	For example if you have a `collections.Counter` object you don't need to use max on it, you can use its `most_common` method. Counting values manually? You can use sum that receives an iterable. The `all`/`any` builtins are wonderful. Or for more complex operations, `itertools` is an excellent module.

9. Long `if-elif-elif-elif-elif-else`'s are quite ugly and hard to maintain. You can beautifully refactor those using dictionaries (mappings) - less lines of code, easier to maintain.

10. Flat is better than nested ([Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python). Go send `import this` to your printer now and keep it handy) - closely related to number 1., but worth emphasizing: if you have a `for` in a `for`, and the inner for has a bunch of nested ifs, it's time to rethink what you are trying to do. This code will be very hard to test and maintain in the future.

Hope that helps! What cool tips have you learned from going through code reviews? Comment below ...

---

Keep calm and code in Python!

-- Bob
