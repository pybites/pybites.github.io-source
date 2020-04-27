Title: Exploring the Modern Python Command-Line Interface
Date: 2020-04-27 22:00
Category: 
Tags: python, unix, cli, history, argparse, click, typer
Slug: guest-exploring-python-clis
Illustration: mixer.jpg
Authors: Erik O'Shaughnessy
summary: Delve into the why and the how of writing command-line tools using Python. 
cover: images/featured/pb-article.png

# Exploring the Modern Python Command-Line Interface

The goal here is simple: help the new Python developer with some of
the history and terminology around [command-line interfaces][20] (CLIs)
and explore how we write these useful programs in Python.

## In the Beginning...

First, a [Unix][11] persepective on command-line interface design.

Unix is a computer operating system and is the ancestor of Linux
and MacOS (and [many other operating systems][11] as well).  Before
graphical user interfaces, the user interacted with the computer
via a command-line prompt (think of today's [bash][21]
environment). The primary language for developing these programs
under Unix is [C][12], which has amazing power for both [good][23] and
[evil][22].

>
>      "C get's sh*t done."
>
>          - a handsome and yet strangely anonymous C programmer
>

So it behooves us to at least understand the basics of a [C program][0] .

Assuming you didn't read that, the basic architecture of a C program
is a function called **`main`** whose signature looks like:

```C
   int main(int argc, char **argv)
   {
   ...
   }
```

This shouldn't look too strange to a Python programmer. C functions
have a return type first, a function name, and then the typed
arguments inside the parenthesis. Lastly, the body of the function
resides between the curly braces. The function name **`main`** is
how the [runtime linker][24] (the program that constructs and runs
programs) decides where to start executing your program. If you
write a C program and it doesn't include a function named
**`main`**, it will not do anything. Sad.

The function argument variables `argc` and `argv` together describe
a list of strings which were typed by the user on the command-line
when the program was invoked. In typical terse Unix naming
tradition, `argc` means _argument count_ and `argv` means _argument
vector_. Vector sounds cooler than list and `argl` would have
sounded like a strangled cry from help. We are Unix system
programmers and we do not cry for "help". We make _other_ people cry
for help.

### Moving On

```console
$ ./myprog foo bar -x baz
```

If `myprog` is implemented in C, `argc` will have the value 5 and
`argv` will be an array of pointers to characters with five entries
(don't worry if that sounds super-technical, it's a list of five
strings). The first entry in the vector, `argv[0]`, will be the
name of the program. The rest of `argv` will contain the arguments:

```C
   argv[0] == "./myprog"
   argv[1] == "foo"
   argv[2] == "bar"
   argv[3] == "-x"
   argv[4] == "-baz"
   
   /* Note: not valid C */
``` 

In C, we have many choices to handle the strings in `argv`. We could
loop over the array `argv` _manually_ and interpret each of the
strings according to the needs of the program. This is relatively
easy, but leads to programs with wildly different interfaces as
different programmers have different ideas about what is "good".

```C
include <stdio.h>

/* A simple C program that prints the contents of argv */

int main(int argc, char **argv) {
    int i;
    
    for(i=0; i<argc; i++)
      printf("%s\n", argv[i]);
}
```

### Early Attempts to Standardize the Command-Line

The next weapon in the command-line arsenal is a [C standard
library][14] function called [`getopt`][15]. This function allows the
programmer to parse switches, arguments with a dash preceeding it like
`-x` and optionally pair follow-on arguments with their
switches. Think about command invocations like `/bin/ls -alSh`,
`getopt` is the function originally used to parse that argument
string. Using `getopt` makes parsing the command-line pretty easy and
improves the user experience (UX).

```
#include <stdio.h>
#include <getopt.h>

#define OPTSTR "b:f:"

extern char *optarg;

int main(int argc, char **argv) {
    int opt;
    char *bar = NULL;
    char *foo = NULL;
    
    while((opt=getopt(argc, argv, OPTSTR)) != EOF)
       switch(opt) {
          case 'b':
              bar = optarg;
              break;
          case 'f':
              foo = optarg;
              break;
          case 'h':
          default':
              fprintf(stderr, "Huh? try again.");
              exit(-1);
              /* NOTREACHED */
       }
    printf("%s\n", foo ? foo : "Empty foo");
    printf("%s\n", bar ? bar : "Empty bar");
}
```

On a personal note, I *wish* Python had switches but that will
[never][25] [happen][26].


### The GNU Generation

The [GNU][1] project came along and introduced longer format
arguments for their implementations of traditional Unix
command-line tools, things like `--file-format foo`. Of course we
_real_ Unix programmers hated that because it was too much to type,
but like the dinosaurs we are, we lost because the users _liked_
the longer options. I never wrote any code using the GNU-style
option parsing, so no code example.

GNU-style arguments also accepted short names like `-f foo` that
had to be supported too.  All of this choice resulted in more
workload for the programmer who just wanted to know what the user
was asking for and get on with it.  But the user got an even more
consistent UX; long and short format options and automatically
generated help that often kept the user from attempting to read
infamously difficult-to-parse [manual][2] pages (see [`ps`][18] for
a particularly egregious example).

## But We're Talking About Python?

You have now been exposed to enough (too much?) command-line
history to have some context about how to approach CLIs written
with our favorite language. Python gives us a similar number of
choices for command-line parsing; do it yourself, a
batteries-included option and a [plethora][29] of third-party
options. Which one you choose depends on your particular
circumstances and needs.

### First, Do It Yourself

We can get our program's arguments from the [`sys`][16]
module. 

```python
import sys

if __name__ == '__main__':
   for value in sys.argv:
       print(value)
```

You can see the C heritage in this short program. There's a reference
to `main` and `argv`. The name `argc` is missing since the Python [list][27]
class incorporates the concept of length (or count) internally. If
you are writing a quick throw-away script, this is definitely your
go-to move.

### Batteries Included

There have been several implementations of argument parsing modules
in the Python standard library; [`getopt`][3], [`optparse`][4], and
most recently [`argparse`][5]. `Argparse` allows the programmer to
provide the user with a consistent and helpful UX, but like it's
GNU antecedents it takes a lot of work and ['boilerplate code'][17]
on the part of the programmer to make it "good".

```python
from argparse import ArgumentParser

if __name__ == '__main__':

   argparser = ArgumentParser(description='My Cool Program')
   argparser.add_argument('--foo', '-f', help='A user supplied foo')
   argparser.add_argument('--bar', '-b', help='A user supplied bar')
   
   results = argparser.parse_args()
   print(results.foo, results.bar)
```

The payoff for the user is automatically generated help available
when the user invokes the program with `--help`. But what about the
advantage of [batteries included][28]? Sometimes the circumstances
of your project dictate that you have limited or no access to
third-party libraries, and you have to "make do" with the Python
standard library.

### A Modern Approach to CLIs

And then there was [Click][6]. The`Click` framework uses a
[decorator][7] approach to building command-line parsing. All of
the sudden it's fun and easy to write a rich command-line
interface. Much of the complexity melts away under the cool and
futuristic use of decorators and users marvel at the automatic
support for keyword completion as well as contextual help. All
while writing less code than previous solutions.  Any time you can
write less code and still get things done is a "win". And we all
want "wins".

```python
import click

@click.command()
@click.option('-f', '--foo', default='foo', help='User supplied foo.')
@click.option('-b', '--bar', default='bar', help='User supplied bar.')
def echo(foo, bar):
    """My Cool Program
    
    It does stuff. Here is the documentation for it.
    """
    print(foo, bar)
    
if __name__ == '__main__':
    echo()
```

You can see some of the same boilerplate code in the `@click.option`
decorator as you saw with `argparse`. But the "work" of creating and
managing the argument parser has been abstracted away. Now our function
`echo` is called _magically_ with the command-line arguments parsed and
the values assigned to the function arguments.

Adding arguments to a `click` interface is as easy as adding another
decorator to the stack and adding the new argument to the function
definition.

## But Wait, There's More!

Built on top of `Click`, [`Typer`][8] is an even _newer_ CLI
framework which combines the functionality of `Click` with modern
Python [type hinting][10]. One of the drawbacks of using `Click` is
the stack of decorators that have to be added to a function. CLI
arguments have to be specified in two places; the decorator and the
function argument list. `Typer` [DRYs][9] out CLI specifications,
resulting in code that's easier to read and maintain.

```python
import typer

typer = typer.Typer()

@typer.command()
def echo(foo: str = 'foo', bar: str = 'bar'):
    """My Cool Program
    
    It does stuff. Here is the documentation for it.
    """
    print(foo, bar)
    
if __name__ == '__main__':
    typer.run()
```

## Time to Start Writing Some Code

Which one of these approaches is right? It depends on _your_ use
case. Are you writing a quick and dirty script that only you will
use? Use `sys.argv` directly and drive on. Do you need more
robust command-line parsing?  Maybe `argparse` is enough. Maybe you
have lots of subcommands and complicated options and your team is
going to use it daily? Now you should definitely consider `Click`
or `Typer`. Part of the fun of being a programmer is hacking out
alternate implementations to see which one suits you best. 

Finally, there are _many_ third-party packages for parsing
command-line arguments in Python. I've only presented the ones I like
or have used. It is entirely fine and expected for you to like and/or use
different packages. My advice is to start with these and see where you
end up.

Go write something cool.

-- [Erik](pages/guests.html#erikoshaughnessy)

(Cover photo by Dylan McLeod on Unsplash)

<!-- URLS -->
[0]: https://opensource.com/article/19/5/how-write-good-c-main-function
[1]: https://www.gnu.org
[2]: https://en.wikipedia.org/wiki/Man_page
[3]: https://docs.python.org/2/library/getopt.html
[4]: https://docs.python.org/2/library/optparse.html
[5]: https://docs.python.org/3/library/argparse.html
[6]: https://click.palletsprojects.com/en/7.x/
[7]: https://wiki.python.org/moin/PythonDecorators
[8]: https://typer.tiangolo.com
[9]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
[10]: https://docs.python.org/3/library/typing.html
[11]: https://en.wikipedia.org/wiki/Unix
[12]: https://en.wikipedia.org/wiki/C_(programming_language)
[14]: https://en.wikipedia.org/wiki/C_standard_library
[15]: http://man7.org/linux/man-pages/man3/getopt.3.html
[16]: https://docs.python.org/3/library/sys.html
[17]: https://en.wikipedia.org/wiki/Boilerplate_code
[18]: http://man7.org/linux/man-pages/man1/ps.1.html
[19]: https://en.wikipedia.org/wiki/Guido_van_Rossum
[20]: https://en.wikipedia.org/wiki/Command-line_interface
[21]: https://www.gnu.org/software/bash/
[22]: https://www.radford.edu/ibarland/Manifestoes/whyC++isBad.shtml
[23]: https://www.toptal.com/c/after-all-these-years-the-world-is-still-powered-by-c-programming
[24]: https://en.wikipedia.org/wiki/Dynamic_linker
[25]: https://www.python.org/dev/peps/pep-0275/
[26]: https://www.python.org/dev/peps/pep-3103/
[27]: https://docs.python.org/3/tutorial/datastructures.html
[28]: https://www.python.org/dev/peps/pep-0206/
[29]: https://www.youtube.com/watch?v=-mTUmczVdik
