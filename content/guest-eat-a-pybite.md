Title: There's no wrong way... to eat a Bite of Py
Date: 2019-11-27 12:02
Category: Tips
Tags: guest, pybites, learning, tips
Slug: guest-eat-a-pybite
Authors: AJ Kerrigan
Summary: There are many ways to tackle a Bites of Py exercise, try them all!
cover: images/featured/pb-guest.png

The [Bites of Py](https://codechalleng.es/bites/) exercises from PyBites are a wonderful way to improve your Python skills in short, focused practice sessions. You can even work on them right from your browser! Of course, that's not the _only_ way.

Here are a few different ways I might work on a bite. I hope some of these are useful - please share your own habits in the comments!

* [Quickstart: Working Directly in the Browser](#quickstart-working-directly-in-the-browser)
* [Interactive Exploration: Using a REPL](#interactive-exploration-using-a-repl)
* [Testing/Debugging Support: A Full-Featured Editor](#testingdebugging-support-a-full-featured-editor)
  * [First-time setup](#first-time-setup)
  * [Per-bite setup](#per-bite-setup)
* [Test Bites: A New Spin](#test-bites-a-new-spin)
* [There's No Wrong Way...](#theres-no-wrong-way)

### Quickstart: Working Directly in the Browser

If a bite appears to have a short solution with reasonably straightforward test cases, I'll probably give it a try right in the browser. PyBites uses the [Ace](https://github.com/ajaxorg/ace) editor with some nice Python-specific additions such as:

* Code linting with [flake8](https://pypi.org/project/flake8/)
* Auto-formatting with [black](https://black.readthedocs.io/en/stable/)

This is a great way to start coding. It's pleasant to use, with no requirements beyond a capable browser.

If a bite deals with concepts or modules that I'm not familiar with though, I often want to work more interactively. I'm not just submitting code for tests in that case - I'm also reading documentation and experimenting to get a better feel for the concepts in the bite. The browser editor falls short for me in those cases, so I might switch to...

### Interactive Exploration: Using a REPL

As long as you have Python installed on your local machine, you'll be able to run `python` to launch the Python interpreter in interactive mode. This gives you a helpful REPL (Read-Eval-Print Loop) where you can explore, try things out, and see the output in real-time.

Depending on the bite you're working on, you might need to install additional packages. It pays to do a little bit of work to keep your PyBites environment isolated, by following steps like these:

* Prepare a new `pybites` virtual environment. [Real Python](https://realpython.com/) has a [primer](https://realpython.com/python-virtual-environments-a-primer/) on virtual environments that can help you get started.
* Install required packages inside your `pybites` virtual environment. The specific requirements vary from bite to bite, but here are some packages that you'll need eventually:
  * requests
  * bs4 - for BeautifulSoup/web scraping bites
  * feedparser
  * python-dateutil
  * pandas

Aside from running `python`, there are a number of alternative REPLs available. This includes local tools such as [bpython](https://bpython-interpreter.org/) or [ptpython](https://github.com/prompt-toolkit/ptpython/), and web-based options like [repl.it](https://repl.it/). My REPL of choice is the `ptipython` component of [ptpython](https://github.com/prompt-toolkit/ptpython/), with vim keybindings. This is mostly personal preference though, so find the experience that best fits your style!

Sometimes after I've done some exploring and feel comfortable with the concepts of a bite, I find that I'm getting hung up with a few failing tests. In that case I am looking for a smoother flow for testing and debugging. I might jump over to...

### Testing/Debugging Support: A Full-Featured Editor

With an editor like [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/docs/languages/python), you can run the same tests locally that PyBites runs in the browser. However, locally you've got a quicker test cycle _and_ you can debug along the way!

When I set up my editor of choice (currently VS Code) to work on a bite, it goes something like this:

#### First-time setup

* Set up a directory where pybites code will live. For me, that is `~/code/pybites`.
* Activate the same `pybites` virtual environment I created for use with my REPL. Microsoft has some [helpful guidance](https://code.visualstudio.com/docs/python/environments) for working with virtual environments in VS Code.

#### Per-bite setup

* Create a directory for the bite. In my case, code for bite `20` goes into `~/code/pybites/20`.
* Copy the code and test files. Again using [bite 20](https://codechalleng.es/bites/20/) as an example, this means I have code in `~/code/pybites/20/account.py` and tests in `~/code/pybites/20/test_account.py`.
* Configure tests. This means enabling `pytest` and using the bite directory (such as `~/code/pybites/20`) as the test root as described in the [documentation](https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework).

With the setup steps done, I can [discover](https://code.visualstudio.com/docs/python/testing#_test-discovery), [run](https://code.visualstudio.com/docs/python/testing#_run-tests) and [debug](https://code.visualstudio.com/docs/python/testing#_debug-tests) tests quickly.

### Test Bites: A New Spin

Now that [Test Bites](https://pybit.es/launch-pytest-bites.html) are live, there's an extra wrinkle to the coding and testing workflow. If you've already got a local environment set up though, you've already laid the groundwork for testing your tests! The last piece you need is the [MutPy](https://github.com/mutpy/mutpy) [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing) tool. With that installed, you can run your mutation tests locally just like [Bob](author/bob.html) did in the [launch post](https://pybit.es/launch-pytest-bites.html)!

### There's No Wrong Way...

If you're practicing on PyBites, you'll definitely be submitting code from the browser. But what other tools will help you along the way? The options are endless - so go nuts, find something that works for you, and share your own tips in the comments!

Thanks for reading!

-- [AJ](pages/guests.html#ajkerrigan)
