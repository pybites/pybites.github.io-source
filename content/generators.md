Title: Generators are Awesome, Learning by Example
Date: 2017-03-17 9:00
Category: Concepts
Tags: python, tips, code, pybites, generators, iteration, yield
Slug: generators
Authors: Julian
Summary: Learn what a Generator is and check out some different examples.
cover: images/featured/pb-article.png

Playing around with context managers for last week’s [Challenge 09](http://pybit.es/codechallenge09.html) introduced me to Python Generators and I’ll be forever grateful. They’re exactly what I didn’t know I needed!

First, for the uninitiated, what is a Generator? (If you’re already across Generators, feel free to skip this next part!).


##What is a Generator?

Well, there’s actually not much to it. A generator is just a function that generates values specifically when called with *next()*. Take this absolutely simple generator for example:

~~~~
>>> def num_gen():
...     yield 1
...     yield 2
...     yield 3
... 
>>> 
>>> demo_gen = num_gen()
>>> next(demo_gen)
1
>>> next(demo_gen)
2
>>> next(demo_gen)
3
>>> next(demo_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
~~~~

As you can see, we have a function *num_gen()* which uses *yield* to return the numbers 1, 2 and 3.

Normally you’d return these numbers via some sort of loop or with 3x print() functions which would print the numbers 1, 2 and 3 all at once.

With a generator however, the numbers are only returned when called using the *next()* function. Here’s what the code does:

1. We take *num_gen()* and assign it to a variable *demo_gen* to make this easier on us.

2. We use the *next()* function on *demo_gen* to request the “next” iteration of the demo_gen function. This results in **the first yield only** being returned.

3. Notice we then have to run *next(demo_gen)* two more times to see the next iteration in the code.

4. Once we’ve exhausted all of the yields within *num_gen()* running *next()* again results in a *StopIteration* error.

> The StopIteration error appears because there are no more yield statements in the function. Calling next on the generator after this does not cause it to loop over and start again.


##Generator Performance Gains

One of the main reasons for using a generator is to avoid having performance issues. For this example it isn’t an issue to work with our 3 numbers in memory but what if we were to be dealing with lists of millions of numbers? 

The performance hit for building lists of millions of numbers within memory isn’t mind blowingly bad but it’s definitely not a great practice.

Generators on the other hand get around the memory hogging by only loading the code into memory that’s returned by *yield*. That is, you’re not processing and storing the entire chunk of code/function in memory, just the next iteration you’re requesting with *next()*.



##Using a For Loop in a Generator

You can use Generators in all sorts of ways. Here’s one that uses a For Loop to double the value of the number I throw into the generator. I can specify how many times the loop is going to run too:

~~~~
>>> def double_nums(num, loops=5):
...     for i in range(loops):
...         num += num
...         yield num
... 
>>> 
>>> demo_gen = double_nums(2)
>>> 
>>> next(demo_gen)
4
>>> next(demo_gen)
8
>>> next(demo_gen)
16
>>> next(demo_gen)
32
>>> next(demo_gen)
64
>>> next(demo_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
~~~~


##Using a While Loop within a Generator

Now let’s say we want it to indefinitely double every number but only when we want to. The generator is necessary otherwise you’d run out memory and crash your machine.

~~~~
>>> def num_gen(num):
...     while True:
...         num += num
...         yield num
... 
>>> 
>>> 
>>> demo_gen = num_gen(2)
>>> 
>>> next(demo_gen)
4
>>> next(demo_gen)
8
>>> next(demo_gen)
16
>>> next(demo_gen)
32
>>> next(demo_gen)
64
>>> next(demo_gen)
128
…
~~~~

This code will continue doubling the number but only when *next()* asks for the number. Nothing is sitting in memory waiting to just return a number.


##Some more examples: Generators for chaining

Here are some examples from our [challenges repo (solutions branch)](https://github.com/pybites/challenges):

* Get all permutations of a draw in a simple game:

		def _get_permutations_draw(draw):
			for i in range(1, 8):
				yield from list(itertools.permutations(draw, i))

	Note that yield from requires [>= 3.3](https://docs.python.org/3/whatsnew/3.3.html).

	Related: [5 cool things you can do with itertools](http://pybit.es/itertools-examples.html)

* Get similar tags:

		def get_similarities(tags):
			for pair in product(tags, tags):
				pair = tuple(sorted(pair))  
				similarity = SequenceMatcher(None, *pair).ratio()
				if SIMILAR < similarity < IDENTICAL:
					yield pair

We grep on yield in our [blog code repo](https://github.com/pybites/blog_code) quite a bit:

* A tweet pipeline:

		def get_tweets(search):
			for tweet in tweepy.Cursor(api.search,
									q=search,
									rpp=100,
									result_type="recent",
									include_entities=True,
									lang="en").items():
				if not tweet.retweeted and 'RT @' not in tweet.text:
					yield tweet

* Get all our challenges repo's forks:

		def get_forks():
			page_num = 0
			while True:
				page_num += 1
				url = FORK_URL + str(page_num)
				response = requests.get(url)
				d = response.json()
				if not d:
					return
				for row in d:
					url = row['html_url']
					updated = row['updated_at']
					pushed = row['pushed_at']
					yield Fork(url, updated, pushed)


##Using a Generator to SSH to Multiple Hosts Idea

I came up with a [useful SSH script](https://github.com/pybites/challenges/blob/solutions/09/with_ssh.py) for last week’s context manager challenge.

It works great but it’s only for one host.

A cool idea from here (that I’ll probably use for work now that I think about it!) would be to make a generator to create a list of node IP addresses to use with the ssh code.

The catch would be the SSH authentication for each server if your credentials aren’t the same across your fleet.

Simplistically but potentially it could look like this:

	net = input('Input your IP net, e.g. 192.168.0')

	# define the generator
	def get_nodes(net):
		for i in range(1, 256):
			yield '{}.{}'.format(net, i)

	# consume it
	for node in get_nodes(net):
		print('Checking IP {}'.format(node))
		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(node, username=username, password=password)
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/hostname')
			yield ssh_stdout.readlines()
		finally:
			ssh.close()
		
		confirm = input(‘Do you want to continue? ')
		...

Output (assuming 'net' was entered as 192.168.0):

	Checking IP 192.168.0.1
	-- output --
	Checking IP 192.168.0.2
	-- output --
	Checking IP 192.168.0.3
	-- output --
	...
	...
	Checking IP 192.168.0.253
	-- output --
	Checking IP 192.168.0.254
	-- output --
	Checking IP 192.168.0.255
	-- output --

(Note the lack of StopIteration. This is because the for loop catches that for you).

##Conclusion

Generators are extremely useful for keeping memory usage low. Not a huge deal for your run of the mill script at home or on your laptop but definitely worth keeping in mind and learning for your coding arsenal.

> There are many ways to skin a… actually, we’re animal lovers here. There are many ways to code a solution! As I wrote the SSH script above I was thinking it’d be much easier to do it differently (not force the generator) but I wanted to for the sake of this post.

Do you use generators in any creative ways? Maybe you can *generate* some interest with your solutions…  pun intended! [I’m here all week!](https://www.youtube.com/watch?v=bcYppAs6ZdI).

## next(PyBites_Generators)

The next step (ha!) is to learn ’send' (yes, you can send data into a generator, how cool is that?!) -> coroutines -> asyncio ... So much to learn, so little time!


Keep Calm and Code in Python!

— Julian
