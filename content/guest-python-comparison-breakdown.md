Title: Under the Hood: Python Comparison Breakdown
Date: 2019-10-24 23:20
Category: Concepts
Tags: guest, learning, dis, precedence, chaining
Slug: guest-python-comparison-breakdown
Authors: AJ Kerrigan
Summary: Use Python's "dis" module to see how Python evaluates two similar comparison operations.
cover: images/featured/pb-guest.png

PyBites community member `fusionmuck` asked an interesting question in the Slack channel recently:

>I am trying to get my head around the order of precedence. The test code is listed without brackets. In the second portion, I add brackets to test my understanding of precedence and I get a return value of True. I am missing something here...

Followed by this code sample:

```python
>>> lst = [2, 3, 4] 
>>> lst[1] * -3 < -10 == 0 
False 

>>> (((lst[1]) * (-3)) < (-10)) == 0 
True
```

I love this question because there are a few different concepts colliding, but fusionmuck still has a clear question - "Why does Python do _this_ when I expect it to do _that_?"

When I saw the question, I thought I understood at least part of what was going on. I needed to run some checks to be sure though, and this is fun stuff to play with. So let's do it together!

1. [Simplify](#simplify)
1. [Read or Experiment?](#read-or-experiment)
1. [Avengers... Disassemble!](#avengers-disassemble)
1. [Bonus Round: Outside Python](#bonus-round-outside-python)
1. [Takeaways and Related Reading](#takeaways-and-related-reading)

## Simplify

I mentioned that there were a few concepts colliding in the original question. It can be helpful to break down the code that we're trying to understand, and strip out as much noise as possible. So let's remove some elements like:

* Pulling items from a list
* Using 0 as a boolean (True/False) value
* Negative numbers

And come up with a pair of simpler comparisons that still demonstrate the behavior from the original question:

```python
>>> 3 < 1 == False
False 

>>> (3 < 1) == False
True
```

We still might not be able to explain what's going on yet, but we have a much more focused question.

## Read or Experiment?

The original question was about operator precedence in Python. One way to answer that question is to check the official Python documentation. The sections on [operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) and [comparison chaining](https://docs.python.org/3/reference/expressions.html#comparisons) are definitely helpful:

>Note that comparisons, membership tests, and identity tests, all have the same precedence and have a left-to-right chaining feature as described in the Comparisons section.

And:

>Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

>Formally, if a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators, then a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z, except that each expression is evaluated at most once.)

Applying that to our question, that means for a comparison like this:

```python
3 < 1 == False
```

Python treats it like this:

```python
3 < 1 and 1 == False
```

That makes things a lot clearer! Adding parentheses helps turn a chained comparison into separate, explicitly ordered operations.

But... what if we want to see that difference in action? What happens under the hood when we add those parentheses? We can't break down the code any more while preserving the behavior we're trying to observe, so `print()` statements or Python debuggers are of limited use. But we still have ways to look closer.

## Avengers... Disassemble!

Python's [dis](https://docs.python.org/3/library/dis.html) module can help us break down Python code into the internal instructions ([bytecode](https://docs.python.org/3/glossary.html#term-bytecode)) that the CPython interpreter sees. That can be very helpful for understanding how Python code works. Reading disassembled output can be tricky at first, but you don't need to understand every detail to spot differences between two pieces of code.

So let's look at some bytecode for these two comparisons. And if this is your first time looking at disassembled Python code, don't panic! Focus on how much longer the first block of instructions is:

```python
>>> import dis
>>> dis.dis('3 < 1 == False')
  1           0 LOAD_CONST               0 (3)
              2 LOAD_CONST               1 (1)
              4 DUP_TOP
              6 ROT_THREE
              8 COMPARE_OP               0 (<)
             10 JUMP_IF_FALSE_OR_POP    18
             12 LOAD_CONST               2 (False)
             14 COMPARE_OP               2 (==)
             16 RETURN_VALUE
        >>   18 ROT_TWO
             20 POP_TOP
             22 RETURN_VALUE

>>> dis.dis('(3 < 1) == False')
  1           0 LOAD_CONST               0 (3)
              2 LOAD_CONST               1 (1)
              4 COMPARE_OP               0 (<)
              6 LOAD_CONST               2 (False)
              8 COMPARE_OP               2 (==)
             10 RETURN_VALUE
```

Those extra instructions in the first block are the work Python has to do to manage [chained comparisons](https://docs.python.org/3/reference/expressions.html#comparisons). Have some fun playing with `dis` - send it some code you understand, or some that you don't (yet)!

Here are some homespun animations that loop through the bytecode instructions, showing the evaluation stack along the way. If you want to follow along with a reference, [this section](https://docs.python.org/3/library/dis.html#python-bytecode-instructions) of the `dis` documentation explains how each bytecode instruction interacts with the evaluation stack.

Here's the breakdown of `3 < 1 == False` ([full size]({filename}/images/comparison-anim-no-parens-full.gif)):

![evaluation stack animation - no parentheses]({filename}/images/comparison-anim-no-parens-small.gif)

And here's `(3 < 1) == False` ([full size]({filename}/images/comparison-anim-with-parens-full.gif)):

![evaluation stack animation - with parentheses]({filename}/images/comparison-anim-with-parens-small.gif)

That was a lot of words and pictures to break down two comparison operations, but I hope you had fun along the way.

## Bonus Round: Outside Python

One tricky aspect of this question is that `==` and `<` have the same precedence. Often this isn't relevant, because you would be unlikely to type:

```python
if a < b == False:
    ...
```

when you could use the simpler:

```python
if a >= b:
    ...
```

or:

```python
if not a < b:
    ...
```

If you're coming to Python from another language though, Python's operator precedence rules can catch you off guard. In languages such as C, C#, Java and JavaScript, relational comparisons like `<` have higher precedence than equality checks like `==`. That makes `3 < 1 == false` functionally equivalent to `(3 < 1) == false`. [Rust](https://doc.rust-lang.org/1.22.1/reference/expressions/operator-expr.html#comparison-operators) sidesteps this confusion entirely by forcing you to be explicit:

>Parentheses are required when chaining comparison operators. For example, the expression a == b == c is invalid and may be written as (a == b) == c.

## Takeaways and Related Reading

The thing I hope people take away from this post is that if you're not sure what a line of Python code is doing, try disassembling it. It can't hurt, and it might lead to some fun discoveries.

The post that inspired _me_ to pull out the `dis` module more often was:

[Weird Python Integers Part II: Constants in Bytecode](https://kate.io/blog/2017/08/24/python-constants-in-bytecode/) by Kate Murphy

---

Thanks for reading! Please leave any questions or comments below, especially if you know of a better way to create evaluation stack animations from Python bytecode.

Keep calm and code in Python!

-- AJ
