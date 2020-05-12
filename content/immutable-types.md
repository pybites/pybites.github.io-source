Title: Mutable vs Immutable Data Types in Python
Date: 2020-04-27 22:53
Category: Concepts
Tags: mutable, immutable, types, data integrity, strings, lists, functional programming, javascript, react
Slug: immutable-types
Authors: Bob
Illustration: ripple.jpg
Summary: Knowing the difference between mutable and immutable types in Python is important. In this article I will give you some practical examples of both and show you some of the advantages of using immutable types. We even look at JS / React / functional programming a bit towards the end.
cover: images/featured/pb-article.png

Have you ever wondered why there are mutable and immutable types in Python?

Have you ever encountered this error in Python?

	>>> s = 'hello'
	>>> s[0] = 'H'
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

In this article I will give you some practical examples and show you some of the advantages of using immutable types. 

## Types

As per Python's [language reference's Data model section](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types):

> The value of some objects can change. Objects whose value can change are said to be **mutable**; objects whose value is unchangeable once they are created are called **immutable** ... An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

Let's look at some examples.

## String building

When I started Python I was not too concerned with string concatenations. I would have long chains of string building code of:

	>>> s = 'hello'
	>>> s += 'world'
	>>> s += ...

However if we look at the `id`s of `s` after each concatenation we discover:

	>>> s = 'hello'
	>>> id(s)
	4341555696
	>>> s += 'world'
	>>> id(s)
	4341545584  => new object created!

This is not efficient. So here you want to use a mutable type:

	>>> l = ['hello']
	>>> id(l)
	4341463496
	>>> l.append('world')
	>>> id(l)
	4341463496  => same object

Lists are cheaper here, because you can change the size of this type of object on the fly.

On the other hand, the size of immutable types is known in memory from the start, which makes them quicker to access (interesting read: [Tuples tend to perform better than lists](https://stackoverflow.com/a/22140115)).

This can really add up as [Michael Kennedy shows here featuring \_\_slots\_\_](https://www.youtube.com/watch?v=FUJf-eEF1GY).

## Immutability

Another advantage of immutables is the guarantee that these objects will never change.

Mutable types have a risk of being unexpectedly modified anywhere in your program:

	>>> l
	['hello', 'world']
	>>> ll = l  # somewhere a shallow copy was made
	>>> l[0] = 'spam'
	>>> l
	['spam', 'world']
	>>> ll
	['spam', 'world']  # oops!

Or here are some more insidious problems:

- [Mutable default arguments](https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments), a common [anti-pattern](https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html)

- [Compound objects](https://pybit.es/mutability.html)

- Multiple threads modifying an object (although [you can use _locking_](https://www.oreilly.com/content/python-cookbook-concurrency/))

- Mutable objects / shared state (OOP) can lead to race conditions ([example given here](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0))

Further reading: [5 Benefits of Immutable Objects Worth Considering for Your Next Project](https://hackernoon.com/5-benefits-of-immutable-objects-worth-considering-for-your-next-project-f98e7e85b6ac)

## Grain of salt

Notice that _immutable_ is sometimes not 100% guaranteed. For instance, you can have a tuple with a list inside of it:

	>>> a = (1, [2, 3], 4)
	>>> a[0] = 2
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment
	>>> a[1].append(3.5)
	>>> a
	(1, [2, 3, 3.5], 4)

Not 100% immutable. Just something to be wary of.

---

**Update**: somebody on FB added something interesting to be aware of:

> The example about list being an element of a tuple is right - on the surface. It is perfectly in line with tuple immutability notion. Tuple holds a reference to a list - so that list may be modified, but cannot be replaced by another list. Yes, tuple can hold a reference to a mutable - it does not contradict the notion of its immutability.

Researching a bit more, I stumbled upon Luciano Ramalho's ["Python tuples: immutable but potentially changing" article](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html) which is an interesting read in this context:

> What is immutable is the physical content of a tuple, consisting of the object references only. The value of the list referenced by dum[1] changed, but the referenced object id is still the same. A tuple has no way of preventing changes to the values of its items, which are independent objects and may be reached through references outside of the tuple, like the skills name we used earlier. Lists and other mutable objects inside tuples may change, but their ids will always be the same.

---

## React & functional programming

Huh? Yes, let's move onto JS for a bit. If you want to learn more about the paradigms of immutability and functional programming it's interesting [to look at React](https://blog.logrocket.com/immutability-in-react-ebe55253a1cc):

> It’s easier to test if two objects are equal if they are immutable and React takes advantage of this concept to make some performance optimizations.

Further reading: [Master the JavaScript Interview: What is Functional Programming?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)

> Functional code tends to be more concise, more predictable, and easier to test than imperative or object oriented code — but if you’re unfamiliar with it and the common patterns associated with it, functional code can also seem a lot more dense, and the related literature can be impenetrable to newcomers.

---

I hope this makes you think about mutable vs immutable and what it means for your code ...

Keep Calm and Code in Python!

-- Bob

(Cover photo by Linus Nylund on Unsplash)
