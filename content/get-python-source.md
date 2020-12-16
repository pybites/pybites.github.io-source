Title: Get to Python source code instantly using importlib and inspect
Date: 2020-12-14 19:05
Category: Tools
Tags: importlib, inspect, vim, bash, source code, pathlib, Standard Library, argparse, pydoc
Slug: get-python-source
Authors: Bob
Summary: Have you ever wondered how to get Python source code quickly? It turns out the Standard Library can do this pretty effortlessly. Here is some code to read more Python source.
cover: images/featured/pb-article.png

Have you ever wondered how to get Python source code quickly? It turns out the Standard Library can do this pretty effortlessly. Here is some code to read more Python source.

## The code

The source / project is [here](https://github.com/PyBites-Open-Source/pysource):

	import argparse
	import importlib
	import inspect
	import pydoc

Here is where the magic happens (credit to [this Stack Overflow](https://stackoverflow.com/a/8790232) thread): we use `importlib` to import the module from a string and get the class or function from this imported module using `getattr`:

	# src/pysource.py
	def get_callable(arg):
		module_str, name = arg.rsplit(".", 1)
		module = importlib.import_module(module_str)
		return getattr(module, name)

Then we print it out. By default we use `print`, but if `pager` is `True` we use `pydoc.pager` which works like Unix `more`: it waits for you to press spacebar and you can use `/` for searching / string matching, pretty cool!

	# src/pysource.py
	def print_source(func, pager=False):
		output = pydoc.pager if pager else print
		output(inspect.getsource(func))

---

To make it stick, check out [another example of `importlib.import_module`](https://codechalleng.es/tips/import-module-from-a-string) and [here is another example of `inspect`](https://codechalleng.es/tips/read-in-source-code).

---

Lastly in `src/__main__.py` we handle command line arguments. We require a `module(.submodule).name` for which we want to see the source and we have an optional `pager` argument. Then we call the two functions:

	# src/__main__.py
	def main():
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

I stored this script in my `$HOME/bin` folder and [Michael](https://michaelabrahamsen.com/) was so kind to come up with an alias to use it in Vim:

	autocmd FileType python map <leader>py :exec '!python3.9 $HOME/bin/pysource.py -m <C-R><C-A> -p'<CR>

He even made this nice little gif demo how it calls the script when you press `<leader>py` when you are on `module.class` or `module.function`:

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

## PyPI

I turned it into a package and [uploaded it to PyPI](https://pypi.org/project/pybites-pysource/1.0.0/) (if you're curious how you can do this, check out [this article](https://pybit.es/opensource-package-pypi.html)).

By the way, lesson learned: [call your source folder something relevant](https://github.com/PyBites-Open-Source/pysource/commit/7a2b8dae046280530e3e558a52a141d52422e435) because that is how it ends up in your virtual environment's `site-packages` folder.

Try it out yourself! Just install it like `pip install pybites-pysource` (not to be confused with `pysource` which is another / unrelated package on PyPI, thanks Nils).

---

This is still experimental but I hope it will already make it easier for you to read more Python (Standard Library) code.

Keep Calm and Code in Python!

-- Bob
