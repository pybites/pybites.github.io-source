Title: Introduction to Python Functions
Date: 2020-02-11 22:13
Category: Learning
Tags: learning, code, programming, python, functions, beginners
Slug: python-functions
Authors: Julian
Summary: In this article I'm going to break down what a function is and how you can use them to be a better coder.
cover: images/featured/pb-article.png

While seemingly "simple" to comprehend and use, functions can definitely be a bit of a hurdle to overcome when you're new to Python or programming in general.
In this article I'm going to break down what a function is and how you can use them to be a better coder.

## What is a function?

Straight to the point, I like it.

Let's just say that a function is a reusable bit of code. It could be a single line of code or it could be many. It'll only have one purpose and it'll do it well.

Pretty vague right? Well that's kind of unavoidable. When you understand the ideology behind a function, then you'll start to get it.


## Let's put the FUN in function!

Excuse the sub-header, I just had to say it.

First, let's look at why we need functions. Why do we need reusable bits of code?

The quickest answer is that it makes repetition easy.

For a moment, let's replace the word "function" with the word *task*. Think of a repetitive task that you have in your daily life. How about *taking a shower*.

If we break down taking a shower into a series of steps we could say that a shower consists of:

1. Turning on the water.
2. Using shampoo.
3. Using soap.
4. Rinsing off.
5. Turning off the water.

If we were to write that in Python code it could look like this:

~~~~
print("Turned on the water.")
print("Used shampoo.")
print("Used soap.")
print("Rinsed off.")
print("Turned off the water.")
~~~~

Nice! We have the code to print out the steps or actions required for taking a shower.

Here's the thing though. What if, as part of a video game a player can choose to "take a shower" when certain things happen? Am I really going to write out the code for taking a shower every single time it's needed? That's five lines of code that I'd have to include for every scenario where they could choose to take a shower.


## Bring on the fun(ction)!

This is why functions are so amazing. We can take those five repetitive steps for taking a shower and wrap them up in a nice little ball to be called whenever needed.

Here's what a function for taking a shower would look like:

~~~~
def take_a_shower():
    print("Turned on the water.")
    print("Used shampoo.")
    print("Used soap.")
    print("Rinsed off.")
    print("Turned off the water.")
~~~~

To break it down:

1. The `def` is how we indicate we're writing a function.
2. We give the function a nice, user friendly name.
3. The empty `()`s allow you to specify any objects/variable you want to pass into the function. We don't need any right now so don't worry about that for now.
4. Any code that is considered to be part of our function needs to be indented by 4 spaces. Thus, all of our print statements are in our `take_a_shower` function.


## Calling the function

We have a `take_a_shower` function that contains our steps. Now what?

Well, any time a player chooses to take a shower, we can just *call* the `take_a_shower` function and it'll print out our actions for taking a shower. The way to call a function is to just use the function's name:

~~~~
take_a_shower()
~~~~

It makes more sense when you use it. We could add it to a game like this:

~~~~
if player == "stinky":
    take_a_shower()
else:
    print("You smell fantastic! Let's go eat some chocolate!")
~~~~

In this scenario, if the player is stinky, then the game calls the `take_a_shower` function. Otherwise the player gets to go eat some chocolate.
When the `take_a_shower` function is called, it *executes* the lines of code we put in the function, i.e., our 5 print statements.


## Simplistic but powerful

I know this seems inane and simplistic but I wanted to demonstrate it with something relatable.

The reality here is we can break down just about anything into chunks and create functions out of them, ready to be called whenever necessary.

Rather than having a long page of code, try breaking your code up into functions that can be called at any time.

When you're starting out with Python and creating really basic programs for yourself, some easy functions to create for yourself could include:

- Basic math, e.g.: a + b
- A text menu system for your program
- Collecting user input
- Different aspects/tasks of a text based game
- Randomisation
- Timers
- Date Calculation

The list is essentially endless but you get the point.


## Take Action

If you're new to Python and functions, go look at any code you've written to date and see how you can [*refactor*](https://pybit.es/refactoring.html) your code and use functions instead.

Once done, leave a comment below and tell us about the functions you created!

Keep Calm and Code in Python!

-- Julian

<div class="ctaBox">
	<p>With so many avenues to pursue in Python it can be tough to know what to do. If you're looking for some <strong>direction</strong> or want to take your Python code and career to the next level, <a href="https://pybit.es/pages/apply.html" target="_blank">schedule a call with us now</a>. We can help you!</p>
</div>
