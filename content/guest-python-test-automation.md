Title: Why Python is Great for Test Automation
Date: 2018-07-25 21:52
Category: Testing
Tags: guest, test, testing, automation, tdd, selenium, automation, pytest, IDE
Slug: guest-python-test-automation
Authors: Andrew Knight
Summary: Testing in Python is consistently growing in popularity. In this article our friend Andrew Knight from Automation Panda walks through 10 reasons why Python is great for Test Automation.
cover: images/featured/pb-guest.png

Testing in Python is consistently growing in popularity. In this article our friend Andrew Knight from Automation Panda walks through 10 reasons why Python is great for Test Automation.

----------------

[Python](http://automationpanda.com/python/) is an incredible programming language. As Dan Callahan said in [his PyCon 2018 keynote](https://youtu.be/ITksU31c1WY?t=409), "Python is the second best language for anything, and that's an amazing aspiration." For test automation, however, I believe it is one of _the_ best choices. Here are ten reasons why:

##1: The Zen of Python

The Zen of Python, as codified in [PEP 20](https://www.python.org/dev/peps/pep-0020/), is an _ideal_ guideline for test automation. Test code should be a natural bridge between plain-language test steps and the programming calls to automate them. Tests should be readable and descriptive because they describe the features under test. They should be explicit in what they cover. Simple steps are better than complicated ones. Test code should add minimal extra verbiage to the tests themselves. Python, in its concise elegance, is a powerful bridge from test case to test code. (Want a shortcut to the Zen of Python? Run `import this` at the Python interpreter.)
<br>

##2: pytest

[pytest](http://automationpanda.com/2017/03/14/python-testing-101-pytest/) is one of the best test frameworks currently available in _any_ language, not just for Python. It can handle any functional tests: unit, integration, and end-to-end. Test cases are written simply as functions (meaning no side effects as long as globals are avoided) and can take parametrized inputs. Fixtures are a generic, reusable way to handle setup and cleanup operations. Basic "assert" statements have automatic introspection so failure messages print meaningful values. Tests can be filtered when executed. Plugins extent pytest to do code coverage, run tests in parallel, use Gherkin scenarios, and integrate with other frameworks like Django and Flask. Other Python test frameworks are great, but pytest is by far the best-in-show. (Pythonic frameworks always win in Python.)
<br>

##3: Packages

For all the woes about the [CheeseShop](https://wiki.python.org/moin/CheeseShop), Python has a rich library of useful packages for testing: [pytest](https://docs.pytest.org/en/latest/), [unittest](https://docs.python.org/3/library/unittest.html), [doctest](https://docs.python.org/3/library/doctest.html), [tox](https://tox.readthedocs.io/en/latest/), [logging](https://docs.python.org/3/library/logging.html), [paramiko](http://www.paramiko.org/), [requests](https://requests.readthedocs.io/en/master/), [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/), [Splinter](https://splinter.readthedocs.io/en/latest/), [Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html), and others are available as off-the-shelf ingredients for custom automation recipes. They're just a "pip install" away. No reinventing wheels here!
<br>

##4: Multi-Paradigm

Python is object-oriented _and_ functional. It lets programmers decide if functions or classes are better for the needs at hand. This is a major boon for test automation because (a) stateless functions avoid side effects and (b) simple syntax for those functions make them readable. pytest itself uses functions for test cases instead of shoehorning them into classes (à la JUnit).
<br>

##5: Typing Your Way

Python's out-of-the-box dynamic duck typing is great for test automation because most feature tests ("above unit") don't need to be picky about types. However, when static types are needed, projects like [mypy](http://mypy-lang.org/), [Pyre](https://pyre-check.org/), and [MonkeyType](https://github.com/Instagram/MonkeyType) come to the rescue. Python provides typing both ways!
<br>

##6: IDEs

Good IDE support goes a long way to make a language and its frameworks easy to use. For Python testing, [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) supports [visual testing](https://www.youtube.com/watch?v=FjojZxDZscQ) with pytest, unittest, and doctest out of the box, and its Professional Edition includes support for BDD frameworks (like pytest-bdd, behave, and lettuce) and Web development. For a lighter offering, [Visual Studio Code](https://code.visualstudio.com/docs/languages/python) is taking the world by storm. Its Python extensions support all the good stuff: snippets, linting, environments, debugging, testing, and a command line terminal right in the window. [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/), [PyDev](http://www.pydev.org/), and [Notepad++](https://notepad-plus-plus.org/) also get the job done.
<br>

##7: Command Line Workflow

Python and the command line are like peanut butter and jelly - a match made in heaven. The entire test automation workflow can be driven from the command line. [Pipenv](http://automationpanda.com/2018/04/16/pipenv-python-packagement-for-champions/) can manage packages and environments. Every test framework has a console runner to discover and launch tests. There's no need to "build" test code first because Python is an interpreted language, further simplifying execution. Rich command line support makes testing easy to manage manually, with tools, or as part of build scripts / CI pipelines. As a bonus, automation modules can be called from the Python REPL interpreter. What does this mean? Automation-assisted exploratory testing! Imagine using Python calls to automatically steer a Web app to a point that requires a manual check. Python makes it possible.
<br>

##8: Ease of Entry

Python has always been friendly to beginners thanks to its Zen, whether those beginners are programming newbies or expert engineers. This gives Python a big advantage as an automation language choice because tests need to be done quickly and easily. Nobody wants to waste time when the features are in hand and just need to be verified. Plus, many manual software testers (often without programming experience) are now starting to do automation work (by choice or by force) and benefit from Python's low learning curve.
<br>

##9: Strength for Scalability

Even though Python is great for beginners, it's also no toy language. Python has industrial-grade strength because its design always favors one right way to get a job done. Development can scale thanks to meaningful syntax, good structure, modularity, and a rich ecosystem of tools and packages. Command line versatility enables it to fit into any tool or workflow. The fact that Python may be [slower than other languages](https://medium.com/@anthonypjshaw/why-is-python-so-slow-e5074b6fe55b) is not an issue for feature tests because system delays (such as response times for Web pages and REST calls) are orders of magnitude slower than language-level performance hits.
<br>

##10: Popularity

Python is one of _the_ most popular programming languages in the world today. It is consistently ranked near the top on [TIOBE](https://www.tiobe.com/tiobe-index/), [Stack Overflow](https://insights.stackoverflow.com/survey/2018/), and [GitHub](https://octoverse.github.com/) (as well as [GitHut](http://githut.info/)). It is a beloved choice for Web developers, infrastructure engineers, data scientists, and test automationeers alike. The Python community also powers it forward. There is no shortage of Python developers, nor is there any dearth of support online. Python is not going away anytime soon. (Python 3, that is.)
<br>

##Other Languages?

The purpose of this article is to highlight what makes Python great for test automation based on its own merits. Although I strongly believe that Python is one of the best automation languages, other choices like Java, C#, and Ruby are also viable. Check out my article [The Best Programming Language for Test Automation](http://automationpanda.com/2017/01/21/the-best-programming-language-for-test-automation/) for a comparison.  
  
_This article was posted with the author's permission on both [Automation Panda](https://automationpanda.com/) and [PyBites](https://pybit.es/)._

---
Keep Calm and Code in Python!

[Andy](pages/guests.html#andrewknight)
