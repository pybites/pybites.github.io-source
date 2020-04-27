Title: Mutable vs Immutable Data Types in Python and When to Use Them
Date: 2020-04-27 10:00
Category: Concepts
Tags: mutable, immutable, data integrity, strings, lists, hashable
Slug: immutable-types
Authors: Bob
Illustration: locked.jpg
Summary: Knowing the difference between mutable and immutable types in Python is important. In this article I give you some practical examples and show you some of the advantages of using immutable types. 
cover: images/featured/pb-article.png

Have you ever wondered why there are mutable and immutable in Python? In this article I give you some practical examples and show you some of the advantages of using immutable types. 

As per Python's [language reference's Data model section](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types):

> The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable ... An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

Even as a beginner, you have seen this. You touch this every day. You probably have hit this one or more times:

	>>> a = (1, 2, 3)
	>>> a[0] = 4
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

In this short article I want to ask you if you have ever used mutables instead of immutables and vice versa?

## String building

When I started Python I would not really think this to be a concern:

>>> s = 'hello'
>>> s += 'world'

However if we look at the id of s after each concatenation we discover:

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

Lists are cheaper here, because you can change the size of the object on the fly.

Immutable objects are expensive to modify, because you'd create a whole new object every time.

On the other hand, the size of immutable types is known in memory from the start, which makes them quicker to access.

## Fewer side effects

Another advantage of immutables type is the guarantee that these objects will never change. 

This makes them good friends with dicts and sets:

> Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally [docs](https://docs.python.org/3/glossary.html#term-hashable)

Even in the example above we could do `+=` on an immutable string, but (!) it returned a new object, the original object was unmodified.

Mutable types on the other hand are riskier because they **might change in multiple locations** throughout your code:

	>>> l
	['hello', 'world']
	>>> ll = l
	>>> l[0] = 'spam'
	>>> l
	['spam', 'world']
	>>> ll
	['spam', 'world']  # oops

However mutable types have a risk to be unexpectedly modified anywhere in your program.

	>>> l
	['hello', 'world']
	# imagine somewhere else:
	>>> ll = l
	>>> l[0] = 'spam'
	>>> l
	['spam', 'world']
	>>> ll
	['spam', 'world']

A good example here is the [_anti-pattern_ of mutable using default arguments](https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html):

	def append(number, number_list=[]):
		number_list.append(number)
		print(number_list)
		return number_list

	append(5) # expecting: [5], actual: [5]
	append(7) # expecting: [7], actual: [5, 7]
	append(2) # expecting: [2], actual: [5, 7, 2]

The immutability is also an advantage when [working with threads](5 Benefits of Immutable Objects Worth Considering for Your Next Project):

> If one thread needs a new version or altered version of that object, it must create a new one therefore any other threads will still have the original object.

### Bonus: some resources

1. It's always interesting to look at code in the REPL. Here is the difference in interface for list vs tuple:

	>>> for attr in vars(list):
	...     if callable(getattr(list, attr)) and not attr.startswith('__'):
	...             print(attr)
	...
	clear
	copy
	append
	insert
	extend
	pop
	remove
	index
	count
	reverse
	sort
	>>> for attr in vars(tuple):
	...     if callable(getattr(tuple, attr)) and not attr.startswith('__'):
	...             print(attr)
	...
	index
	count

2. Tuples are awesome but you would index them by numeric indices. `namedtuple`s are a great alternative. Here is [a quick intro](https://www.youtube.com/watch?v=dsGwfjZxp9A).

3. Another efficiency tip related to immutable types is `__slots__`, check out Michael Kennedy's [Tip #2 Hacking Python's memory with __slots__](https://www.youtube.com/watch?v=FUJf-eEF1GY) for an interesting example.

4. The fewer side effects (predictability) of immutable types is an important concept to grasp and it's hot in the JS world with frameworks like React leveraging its benefits. Although a JS resource, this is a really interesting resource: [Master the JavaScript Interview: What is Functional Programming?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0), specially if you contrast it with [OOP](https://pybit.es/when-classes.html).

> Just a few years ago, few JavaScript programmers even knew what functional programming is, but every large application codebase I’ve seen in the past 3 years makes heavy use of functional programming ideas.

5. Here is another article that sums up the benefits of working with immutable objects: [5 Benefits of Immutable Objects Worth Considering for Your Next Project](https://hackernoon.com/5-benefits-of-immutable-objects-worth-considering-for-your-next-project-f98e7e85b6ac)
---

It's important to keep in mind which types are mutable vs immutable in Python and the gains you can have using the latter. 

(Photo by Masaaki Komori on Unsplash)

---

Keep Calm and Code in Python!

-- Bob
