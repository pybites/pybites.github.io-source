Title: How to Deploy Your Open Source Package to PyPI
Date: 2020-08-31 12:05
Category: Packages
Tags: opensource, tips, packaging, opensource, setup.py, classes, pypi
Slug: opensource-package-pypi
Authors: Bob
Summary: In this post I share some useful things I learned deploying an open source package to PyPI.
cover: images/featured/pb-article.png

In this post I share some useful things I learned deploying [an open source](https://github.com/PyBites-Open-Source/pybites-tips) package [to PyPI](https://pypi.org/project/pybites-tips/).

## The app

I built a small `PyBitesTips` class to consume our Python tips from the command line. The code (project) is [here](https://github.com/PyBites-Open-Source/pybites-tips/blob/master/pytip/tips.py)

Speaking of tips, here are some cool things I learned / re-used:
- Make a class _callable_ using the `__call__` dunder (magic) method.
- Use `namedtuple`s and instantiate them with ** keyword args: `[Tip(**tip) for tip in resp.json()]`
- Use _paging_ of results with `pydoc.pager`.
- Break down output creation and printing in different methods (and helpers) which made testing the code easier.

## Testing

I put [the tests](https://github.com/PyBites-Open-Source/pybites-tips/blob/master/tests/test_tips.py) in a separate `tests/` subdirectory. This way it's easier to omit them from the package build (see further down).

I also mocked out `requests.get`, providing a static `tips_payload` list, and `builtins.input` to simulate a user searching for various tips.

As mentioned before the abstraction of an individual tip output using `_generate_tip_output` made it easy to write `test_tip_output(pb_tips)`.

Another thing worth mentioning is the `conftest.py` I added to the main package folder `pytip` which has `pytest` added to `sys.path`. With that change I could just run `pytest` in the top project folder ([more info](https://docs.pytest.org/en/stable/pythonpath.html)).

## License

This is as simple as copying an existing one and updating the Copyright banner ([MIT example](https://github.com/PyBites-Open-Source/pybites-tips/blob/master/LICENSE)). For more info, check out [Choosing a License](https://docs.python-guide.org/writing/license/).

## setup.py

This file is your key to making your project _pip installable_. As per [the official documentation](https://packaging.python.org/tutorials/packaging-projects/), a basic `setuptools.setup` will do the trick. A few things to highlight as well as extra features I used for [my setup.py](https://github.com/PyBites-Open-Source/pybites-tips/blob/master/setup.py):

- In `classifiers` you set the Python versions you support, here I use Python 3.x
- In `packages` you specify which directories to bundle up, here it's just `pytip`. Note that I called it `pytip` instead of `src`. I discovered that is how it ends up in your virtual environment's `site-packages`.
- In `install_requires` you specify any 3rd party dependencies, in this case `requests`. Note that this makes `requirements.txt` redundant, because `python setup.py install` will now pull it in automatically.
- And one of the coolest things I learned: [__main__.py](https://stackoverflow.com/questions/4042905/what-is-main-py), it allows you to run your package as a console script. So here `entry_points` > `console_scripts` makes an alias `pytip` that points to `pytip` directory (package) > `__main__` module > `main` function which has some `argparse` logic to make this a CLI app (read much more about this in Erik's [Exploring the Modern Python Command-Line Interface](https://pybit.es/guest-exploring-python-clis.html)). So when you pip install this package, you can just run `pytip`, how cool is that, no?!

## Wheels and PyPI

This is 80% of the battle. Uploading it to PyPI is actually very easy.

1. Make 2 accounts: [PyPI](https://pypi.org/) and [Test PyPI](https://test.pypi.org/).
2. Get API tokens for both. Note them down because they only show them once.
3. I highly recommend making this file so you can authenticate to both servers without entering a password ever again:

		$ cat ~/.pypirc
		[distutils]
		index-servers =
			pypi
			testpypi

		[pypi]
		username: __token__
		password: ...

		[testpypi]
		repository: https://test.pypi.org/legacy/
		username: __token__
		password: ...

4. pip install `setuptools`, `wheel` and `twine`.

5. Create your distribution: `python setup.py sdist bdist_wheel`. This will put a `tar.gz` and a `.whl` (_wheel_) in a `dist/` folder (which you should add to `.gitignore`).

6. Always first upload your package to the Test PyPI to make sure it all works: `twine upload --repository testpypi dist/*`. This is important because version numbers can only be uploaded once, so it better work before uploading it to the real PyPI.

7. `pip install` the package from the test index to see if you are happy with the results (here I found out about the "pytip vs src directory name" thing by looking at what got installed in `site-packages`. And here I tested out if my `pytip` alias, as defined in `console_scripts`, actually worked.

8. If all good, upload it to the real PyPI server: `twine upload dist/*` (no need to specify `repository` as PyPI is the default).

And that's it, a new open source project on [PyPI](https://pypi.org/project/pybites-tips/).

## Resources

These resources really helped me going through this process end-to-end:

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/) - specially the console entry point / alias trick I picked up from here.
- [Configuring a .pypirc File for Easier Python Packaging](https://truveris.github.io/articles/configuring-pypirc/)

## "Modern" Python

Setup.py is still the way to go in many cases, but [Poetry](https://python-poetry.org/) and the standardized `toml` file is a strong contender.

Check it out for yourself:

- [What the heck is pyproject.toml](https://snarky.ca/what-the-heck-is-pyproject-toml/)
- [We (Patrick G) used it in our own Karmabot](https://github.com/PyBites-Open-Source/karmabot)


---

Keep Calm and Code in Python!

-- Bob
