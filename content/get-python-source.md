Title: Get to Python source code instantly using inspect and importlib
Date: 2020-12-14 19:05
Category: Tools
Tags: importlib, inspect, vim, bash, source code, pathlib, Standard Library, argparse, pydoc
Slug: get-python-source
Authors: Bob
Summary: Have you ever wondered how to get Python source code quickly? It turns out the Standard Library can do this pretty effortlessly. Here is some code to read more Python source.
cover: images/featured/pb-article.png

Have you ever wondered how to get Python source code quickly? It turns out the Standard Library can do this pretty effortlessly. Here is some code to read more Python source.

## The code

The source is [here](https://gist.github.com/pybites/87318a06c8cfef8b40ddd1967768a446):

	#!/usr/bin/env python3.9
	import argparse
	import importlib
	import inspect
	import pydoc

Here is where the magic happens (credit to [this Stack Overflow](https://stackoverflow.com/a/8790232) thread): we use `importlib` to import the module from a string and get the class or function from this imported module using `getattr`:

	def get_callable(arg):
		module_str, name = arg.rsplit(".", 1)
		module = importlib.import_module(module_str)
		return getattr(module, name)

Then we print it out. By default we use `print`, but if `pager` is `True` we use `pydoc.pager` which works like Unix `more`: it waits for you to press spacebar and you can use `/` for searching / string matching, pretty cool!

	def print_source(func, pager=False):
		output = pydoc.pager if pager else print
		output(inspect.getsource(func))

---

To make it stick, check out [another example of `importlib.import_module`](https://codechalleng.es/tips/import-module-from-a-string) and [here is another example of `inspect`](https://codechalleng.es/tips/read-in-source-code).

---

Lastly [under `if __name__ == "__main__":`](https://codechalleng.es/tips/if-name-main) we handle command line arguments. We require a `module(.submodule).name` for which we want to see the source and we have an optional `pager` argument. Then we call the 2 functions.

	if __name__ == "__main__":
		parser = argparse.ArgumentParser(description='Read Python source.')
		parser.add_argument("-m", "--module", required=True, dest='module',
							help='module(.submodule).name')
		parser.add_argument("-p", "--pager", action='store_true', dest='use_pager',
							help='page output (like Unix more command)')
		args = parser.parse_args()

		func = get_callable(args.module)
		print_source(func, pager=args.use_pager)

(I used `sys.argv` in my first iteration, but `argparse` makes this so much more cleaner and extensible! Of course [there are more options](https://pybit.es/guest-exploring-python-clis.html) as well ...)

## Calling it from within Vim

I stored this script in my `$HOME/bin` folder and [Michael](https://michaelabrahamsen.com/) was so kind to come up with this alias and gif demo:

	autocmd FileType python map <leader>py :exec '!$HOME/bin/pysource.py <C-R><C-A>'<CR>

So when you are on a `module.class` or `module.function` it calls the script:

![demo of this script]({filename}/images/pysource-example.gif)

Here we actually wanted to know how `pathlib` did operator overloading (answer: it implements `__truediv__`).

Of course you can also just call it from the command line:

	$ pysource -m re.match
	def match(pattern, string, flags=0):
		"""Try to apply the pattern at the start of the string, returning
		a Match object, or None if no match was found."""
		return _compile(pattern, flags).match(string)

Or when using paging:

	$ pysource -m pathlib.PurePath -p

## Deployment

I will write some test code and ([put it on PyPI](https://pybit.es/opensource-package-pypi.html)) soon so you can just `pip install` it.

---

This is still experimental but I hope it will already make it easier for you to read more Python (Standard Library) code.

Keep Calm and Code in Python!

-- Bob
