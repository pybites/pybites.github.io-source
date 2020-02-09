Title: Exploring the Mutpy Library and How PyBites Uses it to Verify Test Code
Date: 2020-02-09 10:00
Category: Testing
Tags: guest, mutpy, pytest, coverage, bites of py, platform, mutants
Slug: guest-mutpy-exploration
Authors: Harrison Morgan
Summary: A while back we launched [our Test Bites](https://pybit.es/launch-pytest-bites.html). In this follow up article Harrison explains the [MutPy mutation testing tool](https://pypi.org/project/MutPy/) in depth and how we use it to verify test code on our platform. Enter Harrison.
cover: images/featured/pb-guest.png

A while back we launched [our Test Bites](https://pybit.es/launch-pytest-bites.html). In this follow up article Harrison explains the [MutPy mutation testing tool](https://pypi.org/project/MutPy/) in depth and how we use it to verify test code on our platform. Enter Harrison.

# Table of Contents
1. [What Is Mutation Testing?](#what-is-mutation-testing)
2. [What Is Mut.py?](#what-is-mutpy)
3. [Example of Mut.py's Output](#example-output)
4. [Killing Mutants](#killing-mutants)
5. [Summary of Results](#summary-of-results)
6. [Typical Workflow](#typical-workflow)
7. [Tips for Completing Test Bites](#tips)

<a name="what-is-mutation-testing"></a>
# What Is Mutation Testing?

Mutation testing is a way of testing your tests. It should be used after you already have tests that cover your code well.

In the case of a [Test Bite on PyBites](https://codechalleng.es/bites/paths/pytest), that means you should have [100% code coverage first](https://pypi.org/project/pytest-cov/).

The way it works is by subtly changing, in various ways, the source code being tested, then rerunning the tests for each change.

If the tests continue to pass, then the change was not caught. The idea is that if a random change can be made to the code without causing a failure, then either the tests are not specific enough, or they don't cover enough.

Thus, mutation testing can help you identify areas where your tests are weak and need improvement. Beyond the improvements to your tests, I believe one of the main benefits is the depth of understanding of the code being tested that you often develop. I'll talk more about that later.

Mutation testing has been around for a long time, but because it can be slow, it only recently has started to become more popular. If your tests take a long time to run already, adding mutation testing will increase that time by quite a bit. 

Some people also argue that a reason not to use it is that sometimes the mutations are not useful in improving tests. Sometimes you deliberately do not want to test a particular line of code--but to make the mutation tester happy, you either have to test that line or add a comment to tell it not to mutate that line, which doesn't look very nice and can be distracting.

I think it does have pros and cons, so use your discretion in whether to make mutation testing a regular part of a project. For PyBites, where the code is short and the tests are fast, mut.py is a good way to test Test Bites.

Some common terminology in mutation testing inludes: **mutant**, **killed**, **incompetent**, and **survived**:

1. **Mutant**: this refers to a changed copy of the original code.

2. **Killed**: a killed mutant is one that causes one of your tests to fail.

3. **Incompetent**: an incompetent mutant causes the code to raise an error, before your tests even run. You can consider it killed.

4. **Survived**: a mutant that survives did not cause your tests to fail, so the change was not caught.

I like to use an analogy of a lab experimenting on mutant mice. Imagine you're in charge of the last line of defence security system preventing the mutants from escaping and wreaking havoc on society.

A bunch of mutants break out and try to escape. If an escaping mutant survives, your security system needs to be improved. If one is killed, your security system did its job. An incompetent mutant accidentally drank poison before it even got to your security system.

<a name="what-is-mutpy"></a>
# What is Mut.py?

Mut.py is a mutation tester for Python programs. There also exist Mutmut and Cosmic Ray, which you can explore for your own use, but these require multiple commands to run and review results, so they were not ideal for the PyBites environment.

Mut.py makes changes to your Python programs by applying various operations to [Abstract Syntax Trees](https://greentreesnakes.readthedocs.io/en/latest/). There are a lot of powerful options -- the complete list can be found in [the repository](https://github.com/mutpy/mutpy#command-line-arguments) -- which can be used to customize how mutants are generated, types of output, and more. 

<a name="example-output"></a>
## How to Read Mut.py's Output

There are four sections in Mut.py's output, which are marked by `[*]`:

- The section starting with `Start mutation process` loads the code and tests.

- The section starting with `3 tests passed`, which runs the tests with the original (unmutated) code. 

- `Start mutants generation and execution` marks the main section, where the mutants are actually generated and tested.

- The section starting with `Mutation score` summarizes the results of the mutations.

The first two sections are fairly self-explanatory, and for the most part you won't need to look at them. So, we'll focus on the third and fourth sections.

Here's an example of Mut.py's output from a partially-completed [Bite 241](https://codechalleng.es/bites/241/):

```
=== 2. MutPy output ===
=== $ mut.py --target numbers_to_dec --unit-test test_numbers_to_dec.py --runner pytest -m ===

[*] Start mutation process:
   - targets: numbers_to_dec
   - tests: /tmp/test_numbers_to_dec.py
[*] 3 tests passed:
   - test_numbers_to_dec [0.32171 s]
[*] Start mutants generation and execution:
   - [#   1] COD numbers_to_dec: [0.11618 s] incompetent
   - [#   2] COD numbers_to_dec: [0.11565 s] killed by test_numbers_to_dec.py::test_out_of_range
   - [#   3] COI numbers_to_dec: [0.11298 s] incompetent
   - [#   4] COI numbers_to_dec: [0.11256 s] killed by test_numbers_to_dec.py::test_out_of_range
   - [#   5] COI numbers_to_dec: [0.11287 s] killed by test_numbers_to_dec.py::test_out_of_range
   - [#   6] CRP numbers_to_dec: [0.11643 s] killed by test_numbers_to_dec.py::test_correct
   - [#   7] CRP numbers_to_dec: 
--------------------------------------------------------------------------------
  14:     """
  15:     for num in nums:
  16:         if (isinstance(num, bool) or not (isinstance(num, int))):
  17:             raise TypeError
- 18:         elif not (num in range(0, 10)):
+ 18:         elif not (num in range(0, 11)):
  19:             raise ValueError
  20:
  21:     return int(''.join(map(str, nums)))
--------------------------------------------------------------------------------
[0.11324 s] survived

   - [#   8] CRP numbers_to_dec: [0.13675 s] killed by test_numbers_to_dec.py::test_correct
   - [#   9] LCR numbers_to_dec: [0.11509 s] killed by test_numbers_to_dec.py::test_wrong_type
[*] Mutation score [1.50227 s]: 85.7%
   - all: 9
   - killed: 6 (66.7%)
   - survived: 1 (11.1%)
   - incompetent: 2 (22.2%)
   - timeout: 0 (0.0%)
```

<a name="killing-mutants"></a>
## Killing Mutants

The third section of the output gives us all the information we need to start killing mutants, but it can be confusing.

Let's break down a few lines to see what each part means, and which parts are relevant to killing mutants.

`- [#   1] COD numbers_to_dec: [0.11618 s] incompetent`

- `[#   1]` is the mutation number. It identifies the mutation and allows you to rerun Mut.py with only that mutation to make debugging faster, using the `--mutation-number MUTATION_NUMBER` flag.

- `COD` is the mutation operator. It stands for “conditional operator deletion.” The mutation operator tells you what Mut.py did to mutate the code. The full list of mutation operators can be found in the readme.

- `numbers_to_dec` is the module being mutated.

- `[0.11618 s]` is how long the tests took for this mutation. Sometimes, a mutation will result in an infinite loop, or otherwise cause the tests to take a long time. Mut.py tracks the time for each mutation and compares it to the baseline tests it ran before mutations started, so it can detect and end tests that take much longer than the baseline.

- `incompetent` is the result of the mutation. More on this later!

---

`- [#   2] COD numbers_to_dec: [0.11565 s] killed by test_numbers_to_dec.py::test_out_of_range`

This is an example of a mutation that was killed. It includes the test module and the specific function from that module which killed the mutant. So, what that means is that`test_out_of_range` was the first test to fail.

Note that both this mutation and the previous one would normally print out more information, but PyBites shortens the output to make it clearer. You don't need the extra information for these mutations because they're already done. However, if you run the same command locally, the output will be much more verbose.

---

`- [#   7] CRP numbers_to_dec: … [0.11324 s] survived`

Here's a mutant that survived.

It contains the same information the other mutants do, as well as outputting the diff that shows the exact change that was made. The line starting with `- 18:` is the original code, and the line starting with `+ 18:` is the mutation. The rest is just there for context. In this case, we can see that Mut.py replaced the constant `10` with `11`.

With this information, we have what we need to make a test that fails. The test has to make sure that the `range` doesn't change. Doing that can be tricky, and a lot of people have struggled with this particular mutant.
s
In order to make sure it doesn't change at all, you have to know what it does. This is one of the benefits of testing with Mut.py, as I mentioned above: it forces you to think: what exactly does this code do? Then: how do I test this code to make sure it does exactly what it is supposed to do?

Pretty useful questions!

<a name="summary-of-results"></a>
## Summary of Results

The final section summarizes the results, telling us how many mutations there were and the percentage that didn't survive. There are also four ways a mutation can be categorized: killed, survived, incompetent, or timeout.

In this case, 6 mutants were killed, 1 survived, 2 were incompetent, and 0 timed out. Keeping in mind that the goal of your tests is to fail when a mutant is applied, here's an explanation of the categories. We already talked about the **killed**, **survived**, and **incompetent** categories, so that just leaves...

**Timeout** mutants took too long to run. The cutoff is at 10x longer than the baseline of how long the tests took to run on the unmutated code, so probably what happened is that a loop got broken and started going for infinity or just taking way longer. These ones don't count against us.

<a name="typical-workflow"></a>
# Typical workflow

1. Write code. (Doesn't apply to PyBites test bites -- the code is already written!)

2. Write tests.

3. Run mut.py.

4. Focus on a mutation that survived.

5. Write/modify a test to fail when the mutation is applied.

6. Repeat 3-5 until all mutations are killed.

<a name="tips"></a>
# Tips for Completing Test Bites

Some mutants can be particularly, frustratingly stubborn! Sometimes the best thing to do is to step away from the problem for a while and come back to it later. When that doesn't work, here are some tips to help:

- Think about these questions:

	- “What exactly does this line of code do?”

	- “In what way does this mutation change what this line of code does?”

	- “How can I write a test that passes for the original line of code, but fails when it is mutated?”

- Refresh your memory about how mutation testing works. The process can be especially confusing when you're testing that the code raises errors when it's supposed to, like in the example from Bite 241. You have to write a test that causes the code to fail and the test to pass in the normal (unmutated) case, but causes the code to pass and the test to fail when mutated. Thinking through the workflow may help keep things straight.

- Ask for help on the [PyBites Slack channel](https://pybit.es/pages/community.html) ([#pytest channel](https://pybites.slack.com/archives/CB387MV44)). There's almost always someone around who will be willing to help. Knowing when to ask for help is part of the learning process, too!

---

Keep Calm and Code in Python!

-- [Harrison](pages/guests.html#harrisonmorgan)

