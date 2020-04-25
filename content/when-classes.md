Title: When to Write Classes in Python And Why it Matters
Date: 2020-04-25 18:30
Category: Concepts
Tags: OOP, classes, functions, data model, inheritance, clean code, DRY, games, design
Slug: when-classes
Illustration: blueprint.jpg
Authors: Bob
Summary: When people come to Python one of the things they struggle with is OOP (Object Oriented Programming). Not so much the syntax of classes, but more when and when not to use them. If that's you, read on. In this article I will give you some insights that will get you clarity on this.

When people come to Python one of the things they struggle with is OOP (Object Oriented Programming). Not so much the syntax of classes, but more when and when not to use them. If that's you, read on.

In this article I will give you some insights that will get you clarity on this.

Classes are incredibly useful and robust, but you need to know when to use them. Here are some considerations.

## 1. You need to keep state

For example, if you need to manage a bunch of students and grades, or when you build a game that keeps track of attempts, score etc ([Hangman example](https://github.com/pybites/challenges/blob/solutions/10/hangman-pb.py)).

Basically, when you have data and behavior (= variables and methods) that go together, you would use a class.

## 2. Bigger projects - classes favor code organization and reusability

I often use the example of a `Report` class. You can have a base class with shared attributes like report name, location and rows. But when you go into specifics like formats (xml, json, html), you could override a `generate_report` method in the subclass.

Or think about [vehicles](https://en.wikipedia.org/wiki/Vehicle):

> Vehicles include wagons, bicycles, motor vehicles (motorcycles, cars, trucks, buses), railed vehicles (trains, trams), watercraft (ships, boats), amphibious vehicles (screw-propelled vehicle, hovercraft), aircraft (airplanes, helicopters) and spacecraft.

When you see hierarchies like this, using classes leads to better code organization, less duplication, and reusable code.

This becomes specially powerful if you have hundreds of subclasses and you need to make a fundamental change. You can make a single change in the base class (parent) and all child classes pick up the change (keeping things DRY).

_Note_: although I like inheritance, composition is often preferred because it is more flexible. When I get to a real world use case, I will write another article about it ...

## 3. Encapsulation

You can separate internal vs external interfaces, hiding implementation details. You can better isolate or protect your data, giving consumers of our classes only certain access rights (think API design).

It's like driving a car and not having to know about the mechanics. When I start my car, I can just operate with the common interface I know and should operate with: gas, brake, clutch, steering wheel, etc. I don't have to know how the engine works.

Your classes can hide this complexity from the consumer as well, which makes your code easier to understand (elegant).

Another key benefit of this is that all related data is grouped together. It's nice to talk about `person.name`, `person.age`, `person.height`, etc. Imagine having to keep all this similar data in separate variables, it'll get messy and unmaintainable very quickly.

### Enforcing a contract

We gave an example [here](https://pybit.es/oop-primer.html) of _Abstract base classes (ABCs)_ which let you force derived classes to implement certain behaviors.

By applying [the `abstractmethod` decorator](https://docs.python.org/3/library/abc.html#abc.abstractmethod) to a method in your base class, you force subclasses to implement this method.

## BONUS: Better understanding of Python

Everything in Python is an object. Understanding classes and objects makes you better prepared to use Python's data model and full feature set, which will lead to cleaner and more "pythonic" code.

> ... the Python data model, and it describes the API that you can use to make your own objects play well with the most idiomatic language features. You can think of the data model as a description of Python as a framework. It formalizes the interfaces of the building blocks of the language itself, such as sequences, iterators, functions, classes, context managers, and so on. - [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/ch01.html)

Lastly, a lot of important design patterns are drawn from OOP, just Google "object oriented design patterns", even if you don't use classes day to day, you will read a lot of code that has them!

(Funny trivia: [today we extracted classes from standard library modules](https://codechalleng.es/bites/271/).)

---

## Main takeaway

Classes are great if you **need to keep state**, because they containerize data (variables) and behavior (methods) that act on that data and should logically be grouped together.

This leads to code that is better organized (cleaner) and easier to reuse.

### Avoid classes

With that said, OOP is not always the best solution. Here are some thoughts when to avoid classes:

1. The most straightforward reason is if your class has just a constructor and one method. Then just use a function (and watch this great talk: [Stop writing classes](https://www.youtube.com/watch?v=o9pEzgHorH0))

2. Small (one off) command line scripts probably don't need classes.

3. If you can accomplish the same with [a context manager](https://pybit.es/codechallenge09.html) or [a generator](https://pybit.es/generators.html), this might be cleaner and "Pythonic".

---

I hope this helps you decide when to use classes and when not.

Regardless you should have them in your arsenal.

And there is no better way to learn more about them through some of our resources:

1. Check out our articles: [How to Write a Python Class](https://pybit.es/python-classes.html) and [How to Write a Python Subclass](https://pybit.es/python-subclasses.html).

2. Don't spend more than 10-15 min on it though. The best way to learn is to ACTUALLY CODE! So [start our OOP learning path](https://codechalleng.es/bites/paths/oop) today and start to write classes / code OOP.

3. Once you get past the basics, read my article about Python's magic / special methods: [Enriching Your Python Classes With Dunder (Magic, Special) Methods](https://dbader.org/blog/python-dunder-methods)

4. As we said before, games make for good OOP practice. Try to to create a card game ([and submit it here](https://codechalleng.es/challenges/20/)).

Comment your wins below in the comments and hope to see you in the forums [on our platform](https://codechalleng.es) ...

-- Bob

(Photo by Daniel McCullough on Unsplash)
