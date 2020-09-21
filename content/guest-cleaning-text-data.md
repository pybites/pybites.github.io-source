Title: Cleaning Text Data With Python
Date: 2020-09-17 23:00
Category: Data Science
Tags: guest, tokenisation, case, punctuation, stop words, spelling, urls, email, stemming, lemmatisation
Slug: guest-clean-text-data
Authors: David Colton
Summary: Machine Learning is super powerful if your data is numeric. What do you do, however, if you want to mine text data to discover hidden insights or to predict the sentiment of the text. What, for example, if you wanted to identify a post on a social media site as cyber bullying. In this article we introduce some methods to clean your text and prepare it for modelling.
cover: images/featured/pb-guest.png
status: draft

# Table of Contents

1. [Cleaning Text Data with Python](#cleaning-text)
2. [Tokenisation](#tokenisation)
3. [Normalising Case](#normalising-case)
4. [Remove All Punctuation](#remove-punctuation)
5. [Stop Words](#stop-words)
6. [Spelling and Repeated Characters (Word Standardisation)](#word-standardisation)
7. [Remove URLs, Email Addresses and Emojis](#remove)
8. [Stemming and Lemmatisation](#stemming-lemmatisation)
9. [A Simple Demonstration](#demonstration)

<a name="cleaning-text"></a>

# Cleaning Text Data with Python

Machine Learning is super powerful if your data is numeric. What do you do, however, if you want to mine text data to discover hidden insights or to predict the sentiment of the text. What, for example, if you wanted to identify a post on a social media site as cyber bullying. 

One way to analyse text is to use a measure called Term Frequency - Inverse Document Frequency (TF-IDF). A full explanation of TF-IDF is beyond the scope of this quick introduction, however, a detailed background and explanation of TF-IDF, including some Python examples, is given here [Analyzing Documents with TF-IDF](https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf). Suffice it to say that TF-IDF will assign a value to every word in every document you want to analyse and, the higher the TF-IDF value, the more important or predictive the word will typically be.

However, before you can use TF-IDF you need to clean up your text data. But why do we need to clean text, can we not just eat it straight out of the tin? The answer is yes, you can use the raw data exactly as you've received it, however, cleaning your data will increase the accuracy of your model. This guide is a very basic introduction to some of the approaches used in cleaning text data. Some techniques are simple, some more advanced. For the more advanced concepts, consider their inclusion here as pointers for further personal research. 

In the following sections I'm assuming that you have plain text and your text is not embedded in HTML or Markdown or anything like that. If that is the case you should handle this first to get access to the raw text before proceeding.

<a name="tokenisation"></a>

## Tokenisation

Typically the first thing to do is to tokenise the text. This is just a fancy way of saying split the data into individual words that can be processed separately. Tokenisation is also usually as simple as splitting the text on white-space. It's important to know how you want to represent your text when it is dived into blocks. By this I mean are you tokenising and grouping together all words on a line, in a sentence, all words in a paragraph or all words in a document. The simplest assumption is that each line a file represents a group of tokens but you need to verify this assumption. BTW I said you should do this first, I lied. A lot of the tutorials, sample code on the internet talks about tokenising your text immediately. This then has the downside that some of the simpler clean up tasks, like converting to lowercase and removing punctuation for example, need to be applied to each token and not on the text block as a whole. Something to consider.

<a name="normalising-case"></a>

## Normalising Case

This is just a fancy way of saying convert all your text to lowercase. If using Tf-IDF `Hello` and `hello` are two different tokens. This has the side effect of reducing the total size of the vocabulary, or corpus, and some knowledge will be lost such as Apple the company versus eating an apple. In all cases you should consider if each of these actions actually make sense to the text analysis you are performing. If you are not sure, or you want to see the impact of a particular cleaning technique try the before and after text to see which approach gives you a more predictive model. Sometimes, in text mining, there are multiple right answers.

<a name="remove-punctuation"></a>

## Remove All Punctuation

Punctuation doesn't bring anything to the table when text mining so just remove it all. In fact sentence structure and word order is irrelevant when using TF-IDF.  Word of caution though. If you are also going to remove URLs and Email addresses you might want to the do that before removing punctuation characters otherwise they'll be a bit hard to identify. Another consideration is hashtags which you might want to keep so you may need a rule to remove `#` unless it is the first character of the token.

<a name="stop-words"></a>

## Stop Words

[Stop Words](https://en.wikipedia.org/wiki/Stop_word) are the most commonly used words in a language. You could consider them the glue that binds the important words into a sentence together. Sample stop words are `I, me, you, is, are, was` etc. Removing stop words have the advantage of reducing the size of your corpus and your model will also train faster which is great for tasks like Classification or Spam Filtering. However, another word or warning. If you are doing sentiment analysis consider these two sentences:

* _this movie was not good_
* _movie good_

By removing stop words you've changed the sentiment of the sentence. Who said NLP and Text Mining was easy.

<a name="word-standardisation"></a>

## Spelling and Repeated Characters (Word Standardisation)

Fixing obvious spelling errors can both increase the predictiveness of your model and speed up processing by reducing the size of your corpora. A good example of this is on Social Media sites when words are either truncated, deliberately misspelt or accentuated by adding unnecessary repeated characters. Consider:

* `love, luv, lovvvvv, lovvveeee`

To an English speaker it's pretty obvious that the single word that represents all these tokens is `love`. Standardising your text in this manner has the potential to improve your model significantly. 

<a name="remove"></a>

## Remove URLs, Email Addresses and Emojis

Depending on your modelling requirements you might want to either leave these items in your text or further preprocess them as required. A general approach though is to assume these are not required and should be excluded. Consider if it is worth converting your emojis to text, would this bring extra predictiveness to your model? Regular expressions are the go to solution for removing URLs and email addresses.

<a name="stemming-lemmatisation"></a>

## Stemming and Lemmatisation

Stemming is a process by which derived or inflected words are reduced to their stem, sometimes also called the base or root. Using the words `stemming` and `stemmed` as examples, these are both based on the word `stem`. **Stemming** algorithms work by cutting off the end or the beginning of the word, taking into account a list of common prefixes and suffixes that can be found in an inflected word.

**Lemmatisation** in linguistics, is the process of grouping together the different inflected forms of a word so they can be analysed as a single item. In languages, words can appear in several inflected forms. For example, in English, the verb 'to walk' may appear as 'walk', 'walked', 'walks', 'walking'. The base form, 'walk', that one might look up in a dictionary, is called the lemma for the word.

So stemming uses *predefined rules* to transform the word into a *stem* whereas lemmatisation uses *context* and *lexical library* to derive a *lemma*. The *stem* doesn’t always have to be a valid word whereas *lemma* will always be a valid word because *lemma* is a dictionary form of a word.

<a name="demonstration"></a>

## A Simple Demonstration

Let have a look at some simple examples. We start by creating a string with five lines of text:

```python
In [1]: data = """This is the first line
    ...: This is the 2nd line
    ...: The third line, this line, has punctuation.
    ...: THE FORTH LINE I we and you are not wanted
    ...: I lovveee email fred@flintsones.ie"""
```

At this point we could split the text into lines and split lines into tokens but first lets covert all the text to lowercase (line 4), remove that email address (line 5) and punctuation (line 6) and then split the string into lines (line 7).

```Python
In [2]: import re
In [3]: import string
In [4]: data = data.lower()
In [5]: data = re.sub(r'\S*@\S*\s*', '', data)
In [6]: data = data.translate(str.maketrans('', '', string.punctuation))
In [7]: lines = data.split('\n')
In [8]: lines
Out[8]:
['this is the first line',
 'this is the 2nd line',
 'the third line this line has punctuation',
 'the forth line i we and you are not wanted',
 'i lovveee email rocks']
```

Line 8 now shows the contents of the data variable which is now a list of 5 strings).

Next we'll tokenise each sentence and remove stop words. Normally you's use something like NLTK (Natural Language Toolkit) to remove stop words but in this case we'll just use a list of prepared tokens (words)

```python
In [9]: tokens = [[word for word in line.split() if word not in stop_words] for line in lines]

In [10]: tokens
Out[10]:
[['first', 'line'],
 ['2nd', 'line'],
 ['third', 'line', 'line', 'punctuation'],
 ['forth', 'line', 'wanted'],
 ['lovveee', 'email', 'rocks']]
```

The final data cleansing example to look is spell checking and word normalisation. If we look at the list of tokens above you can see that there are two potential misspelling candidates `2nd` and `lovveee`. Rather then fixing them outright, as every text mining scenario is different a possible solution to help identify the misspelt words in your corpus is shown. This would then allow you determine the percentage of words that are misspelt and, after analysis or all misspellings or a sample if the number of tokens is very large, an appropriate substituting algorithm if required.

```python
In [1]: from spellchecker import SpellChecker

In [2]: spell = SpellChecker()

In [3]: misspelled = ['lovve', 'lovee', 'lovvee', 'lovveee', '2nd']

In [4]: for word in misspelled:
    ...:    print(f'{word}: \t{spell.correction(word)} \t{spell.candidates(word)}')
    ...:
lovve:	  love	  {'love'}
lovee:	  love	  {'lover', 'love', 'levee', 'loved', 'lovey', 'loves'}
lovvee:	  love	  {'lover', 'lovage', 'ovver', 'love', 'levee', ... 'loves', 'loaves'}
lovveee:	lovveee	{'lovveee'}
2nd:	    and	    {'mnd', 'und', 'ond', 'nd', 'cnd', 'ind', 'bnd', 'and', 'hnd', 'end'}
```

In lines 1 and 2 a [Spell Checker](https://pypi.org/project/pyspellchecker/) is imported and initialised. Line 3 creates a list of misspelt words. Then in line 4 each misspelt word, the corrected word, and possible correction candidate are printed. This is not suggested as an optimised solution but only provided as a suggestion.

