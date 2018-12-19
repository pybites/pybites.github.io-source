Title: The Beauty of Python Virtualenvs
Date: 2016-12-22 22:11
Category: Tools
Tags: python, pip, virtualenv, venv
Slug: the-beauty-of-virtualenv
Authors: Julian
Summary: Python Virtualenvs are incredible yet sadly under utilised!
cover: images/featured/pb-article.png

Ever heard of a Python virtualenv? No? Neither had I, until I discovered them while following a video course on Python Flask.

A virtualenv (AKA venv) is essentially a Virtual Machine (VM) or sandbox environment that runs an independent and untouched Python environment.
When you create and activate the venv you no longer have access to the main Python environment running on your system.

The problem programmers have is that it can be hard to isolate problems in code when their primary environment is cluttered with imported modules and the like.
Best practice would be to create a venv within your project and use it to run your project.

## Step by Step

Let's create a venv called "awesome-test". You'd preferably run the following commands in your project root dir:

###Unix Commands
~~~~
# python3 -m venv awesome-test
# ls
awesome-test
~~~~

###Windows Commands
~~~~
# python -m venv awesome-test
# dir
awesome-test
~~~~

> In Python 3, virtualenvs come installed by default. In Python 2.7 you install them with pip install virtualenv.

The next step is to activate the venv.
Activating the venv puts you into a standalone Python instance that has pretty much nothing installed by default:

###Unix Commands
~~~~
# cd awesome-test
# ls
bin		include		lib		pyvenv.cfg
#
# source bin/activate
(awesome-test) #
(awesome-test) # echo YAY!
YAY!
~~~~

###Windows Commands
~~~~
# cd awesome-test
# dir
Include/	Lib/	pyvenv.cfg  Scripts/
# Scripts\activate
(awesome-test) #
(awesome-test) # echo YAY!
YAY!
~~~~

The *(awesome-test)* tag preceding your shell prompt indicates you're now in the venv.
Now list out the modules installed in this python instance:

~~~~
# pip list
pip (9.0.1)
setuptools (28.8.0)
#
~~~~

If you've been using Python already, you'll know that your main env would have a boat load of modules installed. It's nice to be able to run from a clean slate when desiging new code!

You can now play around and install whatever the heck you want without having to worry about corrupting or screwing up your primary environment. All modules installed in this venv will remain local to the venv.

When you're done using the venv you then exit (deactivate) it using the deactivate command:

###Unix Command
~~~~
(awesome-test) # deactivate
# 
~~~~

###Windows Command
~~~~
(awesome-test) # Scripts\deactivate
#
~~~~

> Note: All of changes you made in the venv will NOT be lost. It's all stored safely within the venv.

## Conclusion

The seasoned veteran out there will surely read this and call me a noob... and they'd be right! It's exactly why I'm so stoked to have discovered venvs!

If you're not using virtualenvs yet, install the package and give it a whirl.

Keep Calm and Code in Python!

-- Julian
