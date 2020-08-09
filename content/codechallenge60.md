Title: Code Challenge 60 - Working With PDF Files in Python
Date: 2019-01-08 12:40
Category: Challenge
Tags: code challenge, challenges, PDF, text parsing, data mining, data cleaning, PyPDF2, pdftables, PDFMiner, PyPI
Slug: codechallenge60
Authors: PyBites
Summary: Hey Pythonistas, in this challenge you will learn how to work with PDF documents. Enjoy!
cover: images/featured/pb-challenge.png

> There is an immense amount to be learned simply by tinkering with things. - Henry Ford

Hey Pythonistas, in this challenge you will learn how to work with PDF documents. Enjoy!

## The Challenge

For the NLTK challenge (PCC58/59) we stumbled upon a hurdle: episode 1-150 of [Tim Ferriss' transcripts](https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/) are PDF files. And we're not alone, in the comments somebody stated:

> These are much appreciated. I do wonder, however, why they are all not a downloadable PDF and only the first 150. Perhaps just a marketing thing, but it would be nice to be able to grab them all to have an easily searchable database. Ah well, you have to work for what you want!

Challenge accepted! You can try this too or use another data set, it's up to you!

Googling for this challenge we stumbled upon a Pycon proposal: [Liberating tabular data from the clutches of PDFs](https://in.pycon.org/cfp/2017/proposals/liberating-tabular-data-from-the-clutches-of-pdfs~dRjwd/):

> Budget Documents are moral documents that represent the priorities and values of the states and its governing bodies. Unfortunately these documents are published in unstructured PDF formats which makes it difficult for researchers, economists and general public to analyse and use this crucial data. In this session will delve into how we can create a data pipeline and leverage computer vision techniques to parse these documents into clean machine-readable formats by leveraging libraries like OpenCV, numpy, pandas, PyPDF2, tabula and poppler-pdf-to-text

Which goes to show that:

1. There are a lot of interesting resources that are still in PDF format that are waiting to be converted ...
2. In this Data Science age, there is a lot of focus on the data algorithms and visualization, the fun stuff, but it is _data cleaning_ that actually allows for this, so this is a relevant skill to have.

If you can't find a use case for data extraction, feel free to do the inverse: generate a nice looking PDF file from a bunch of data sources.

You probably want to use a 3rd party package for this: [PyPDF2](https://pythonhosted.org/PyPDF2/), [pdftables](https://github.com/okfn/pdftables) (if you need to extract tables), and/or [PDFMiner](https://github.com/euske/pdfminer). Or search [_the cheese shop_](https://pypi.org/search/?q=extract+text+from+pdf) ...

Have fun and use Python!

## Ideas and feedback

If you have ideas for a future challenge or find any issues, open a [GH Issue](https://github.com/pybites/challenges/issues) or reach out via [Twitter](https://twitter.com/pybites), [Slack](https://codechalleng.es/settings/) or [Email](mailto:support@pybit.es).

Last but not least: there is no best solution, only learning more and better Python. Good luck!

## Become a Python Ninja

At PyBites you get to [*master Python* through Code Challenges](https://pybit.es/special-learning-python.html):

* Subscribe to our blog (sidebar) to periodically get new PyBites Code Challenges (PCCs) in your inbox.

* Apart from this blog code challenge we have a growing collection which you can check out [on our platform](https://codechalleng.es/challenges/). 

* Prefer coding bite-sized Python exercises, using effective Test-Driven Learning, and in the comfort of your browser? Try our growing collection of _[Bites of Py](https://codechalleng.es/bites/)_ on our platform.

	<iframe width="560" height="315" src="https://www.youtube.com/embed/5AQg2UxvXbI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* Want to do the [#100DaysOfCode](https://twitter.com/hashtag/100DaysOfCode?src=hash&lang=en) but not sure what to work on? Take [our course](https://talkpython.fm/100days?utm_source=pybites) and/or start logging your 100 Days progress using our _Progress Grid Feature_ [on our platform](https://codechalleng.es/100days/) (you can also use the Grid to do 100 Bite exercises in 100 days, earning a die hard PyBites Ninja Certificate!)

---

	>>> from pybites import Bob, Julian

	Keep Calm and Code in Python!
