Title: A Python Orientation - How to Get Started
Date: 2018-08-17 09:41
Category: Concepts
Tags: guest, 2vs3, CPython, PyPy, MicroPython, pip, pipenv, venv, virtualenv, Conda, editors, Pythonic, Pythonista, Zen of Python, pycon, PSF, BDFL, overview, reference
Slug: guest-python-orientation
Authors: Andrew Knight
Summary: Python is a wonderful language for both beginners and expert programmers, but getting started can be daunting. Which version should I use? Which editors are best? What do you mean there are different implementations and environments? Here's a guide to help navigate these big FAQs.
cover: images/featured/pb-guest.png

Python is a wonderful language for both beginners and expert programmers, but getting started can be daunting. Which version should I use? Which editors are best? What do you mean there are different implementations and environments? Here's a guide to help navigate these big FAQs.

tl;dr
-----

For most people:

*   Use the latest version of **Python 3**.
*   Use the **CPython** implementation.
*   Use **pipenv **to manage packages and installations.
*   Use **Visual Studio Code** or **PyCharm** for editing code.

Which Version?
--------------

Python 2 and Python 3 are actually different languages. The differences go deeper than just print statements. The [What's New in Python](https://docs.python.org/3/whatsnew/) page on the official doc site lists all the gory details, and decent articles showcasing differences can be found [here](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html), [here](https://www.digitalocean.com/community/tutorials/python-2-vs-python-3-practical-considerations-2), and [here](https://blog.appdynamics.com/engineering/the-key-differences-between-python-2-and-python-3/). Although Python 3 is newer, Python 2 remains prevalent. Most popular packages use [Python packaging tools](https://packaging.python.org/distributing/#packaging-your-project) to support both versions. The [Python Wiki](https://wiki.python.org/moin/Python2orPython3) makes it clear that **Python 3 is the better choice**:

> _Python 2.x is legacy, Python 3.x is the present and future of the language_

Furthermore, **Python 2 will reach end-of-life in 2020**. The Python team will continue to provide bug fixes for 2.7 until 2020 ([PEP 373](https://www.python.org/dev/peps/pep-0373/)), but there will be no new language features and no 2.8 ([PEP 404](https://www.python.org/dev/peps/pep-0404/)). (Originally, end-of-life was planned for 2015, but it was pushed back by 5 years.) There is even a [Python 2.7 Countdown](https://pythonclock.org/) clock online.

Which Implementation?
---------------------

In purest terms, "Python" is a language specification. An implementation provides the language processing tools (compiler, interpreter, etc.) to run Python programs. [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/) has a great article entitled [Picking an Interpreter](http://docs.python-guide.org/en/latest/starting/which-python/) that provides a good summary of available interpreters. Others are listed on [python.org](https://www.python.org/download/alternatives/) and the [Python Wiki](https://wiki.python.org/moin/PythonImplementations). The table below provides a quick overview of the big ones.


[CPython](https://en.wikipedia.org/wiki/CPython)

*   most widely used implementation
*   the [reference implementation](https://en.wikipedia.org/wiki/Reference_implementation)
*   has the most libraries and support
*   implemented in C
*   supports Python 2 and 3

[PyPy](http://pypy.org/)

*   much faster than CPython
*   much more memory efficient
*   implemented in RPython
*   supports Python 2 and 3

[Jython](http://www.jython.org/)

*   implemented in Java
*   runs on the JVM
*   supports Python 2
*   only a [sandbox](https://github.com/jython/jython3) for Python 3
*   no project updates since May 2015

[IronPython](http://ironpython.net/)

*   implemented for .NET
*   lets Python libs call .NET and vice versa
*   supports Python 2

[Python for .NET](http://pythonnet.github.io/)

*   integrates CPython with .NET/Mono runtime
*   supports Python 2 and 3

[Stackless Python](https://bitbucket.org/stackless-dev/stackless/wiki/Home)

*   branch of CPython with real threading

[MicroPython](http://micropython.org/)

*   optimized for microcontrollers
*   uses a subset of the standard library

Unless you have a very specific reason, **just use CPython**. In fact, most people are referring to CPython when they say "Python." CPython has the most compatibility, the widest package library, and the richest support. If you really need speed, consider PyPy.

Managing Installations
----------------------

[pip](https://pip.pypa.io/en/stable/) is the standard tool for installing Python packages. The simplest way to install Python is to install it "globally" for the system. In fact, some operating systems like macOS and Ubuntu have Python pre-installed. However, global installation has limitations:

1.  You may want to develop packages for both versions 2 and 3.
2.  You may not have permissions to add new packages globally.
3.  Different projects may require different versions of packages.

These problems can be solved by using "virtual" environments. A [virtual environment](https://www.python.org/dev/peps/pep-0405/) is like a local Python installation with a specific package set. For example, I have created virtual environments for Python as part of [Jenkins](https://jenkins.io/) build jobs, since I did not have permission to install special automation packages globally on the Jenkins slaves.

The standard virtual environment tool for Python is [venv](https://docs.python.org/3/library/venv.html), which has been packaged with (C)Python since 3.3. (_venv_ had a command line wrapper named _pyvenv_, but this was deprecated in 3.6.) Another older but still popular third-party tool is [virtualenv](https://virtualenv.pypa.io). As explained in [this Reddit post](https://www.reddit.com/r/learnpython/comments/4hsudz/pyvenv_vs_virtualenv/), _venv _is the Python-sanctioned replacement for _virtualenv_. However, _virtualenv_ supports Python 2, whereas _venv_ does not. [Conda](https://conda.io/docs/) is an environment manager popular with the science and data communities, and it can support other languages in addition to Python.

That being said, there is a relatively new package manager taking the Python world by storm: [pipenv](https://docs.pipenv.org/). Pipenv combines _pip_, _Pipfile_, and _virtualenv_ into an easy workflow with simple commands. Personally, I find it to be very helpful. However, it has caused some controversy (see [Reddit](https://np.reddit.com/r/Python/comments/8jd6aq/why_is_pipenv_the_recommended_packaging_tool_by/)), and it may not be applicable for all scenarios (see [Chris Warrick's article](https://chriswarrick.com/blog/2018/07/17/pipenv-promises-a-lot-delivers-very-little/)). My recommendation is to **use _pipenv_ for new projects** if it meets your needs.

Editors and IDEs
----------------

After setting up your Python environment, you are ready to start programming! There are two routes to take for text editing: _source code editors_ and _integrated development environments_.

Source code editors are lightweight but often include basics like syntax highlighting and basic auto-completion. They're great for quick edits and light scripting. Many have plugins. Popular choices are [Visual Studio Code](https://code.visualstudio.com/), [Sublime](https://www.sublimetext.com/), [Atom](https://atom.io/), and [Notepad++](https://notepad-plus-plus.org/). **My current favorite is Visual Studio Code** because the Python extensions are stellar and settings are simple - just remember to install the extensions you need! I use it personally for [Django development](http://automationpanda.com/2018/02/08/django-projects-in-visual-studio-code/).

For more intense development, I highly recommend an IDE like [JetBrains PyCharm](https://www.jetbrains.com/pycharm/), [PyDev](http://www.pydev.org/) for [Eclipse](https://eclipse.org/), [Wing Python IDE](https://wingware.com/), or [Eric](http://eric-ide.python-projects.org/). IDEs provide rich development support, especially for larger apps that use frameworks like [Django](https://www.djangoproject.com/), [Pyramid](https://trypyramid.com/), and [SQLAlchemy](https://www.sqlalchemy.org/). They also make testing easier with plugins for test frameworks like [pytest](http://doc.pytest.org/en/latest/), [behave](https://pypi.org/project/behave/), and others. PyCharm and PyDev are particularly nice because they can integrate into their larger IDEs (IntelliJ IDEA and Eclipse, respectively) to handle more languages. Personally, **I prefer PyCharm**, but advanced features require a paid license.

Pythonese
---------

The Python community throws around a few terms you should know:

[Pythonic](https://docs.python-guide.org/writing/style/)

*   describes idiomatic code for Python
*   closely related to conciseness, readability, and elegance
*   highly recommended to use
*   follow style guidelines

[Pythonista](http://binhminhcs.blogspot.com/2011/12/python-pythonic-pythoneer-pythonist.html)

*   someone who loves the Python language
*   often an advanced Python programmer

[Pythoneer](http://binhminhcs.blogspot.com/2011/12/python-pythonic-pythoneer-pythonist.html)

*   a programmer who uses Python to solve problems

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

*   the list of guiding principles for Python's design
*   run "import this" to see them

[The Python Software Foundation](https://www.python.org/psf/) (PSF)

*   non-profit org
*   keeps Python going strong
*   support them!

[PyCon](https://us.pycon.org/)

*   the annual Python conference held in North America
*   _GO_ \- it will [change your life](http://automationpanda.com/2018/05/20/pycon-2018-reflections/)!
*   several other conferences are held [worldwide](https://www.python.org/community/workshops/)

[Benevolent Dictator for Life](https://en.wikipedia.org/wiki/Guido_van_Rossum)(BDFL)

*   Guido van Rossum
*   the inventor of Python
*   resigned in July 2018 but remains BDFL Emeritus

_This article was originally posted at [AutomationPanda.com](https://automationpanda.com/2017/02/07/which-version-of-python-should-i-use/) and has been reposted here with permission._

---
Keep Calm and Code in Python!

[Andy](pages/guests.html#andrewknight)
