According to the [Zen of Python](https://www.python.org/dev/peps/pep-0020/), "There should be one-- and preferably only one --obvious way to do it." It’s a good principle for designing a program--the more ways there are of doing something, the more confusing the software becomes, along with a host of other problems. In reality, though, there almost always is more than one way to accomplish something. The quotation even displays this fact: it places the dash in two different ways, neither of which are the obvious way.

Scroll through a few bite threads on PyBites, and you’ll quickly see that for some bites, no two solutions are exactly the same. Some might be easier to understand, some might be faster, or use less memory, or fewer lines of code. Typically, there are tradeoffs involved. Understanding those tradeoffs and how they apply to the requirements for our code is an important part of programming.

I encourage you to, after solving a bite, think carefully about the other solutions in the bite thread. How do they differ from yours? Do they run faster? Use less memory? Are they more readable? Why? Asking yourself these questions will give you the tools to evaluate code and decide whether it works for your requirements.

There are many reasons that influence how we arrive at a solution to a problem. For example, I was struggling with a bite that involved numbers. I tried several approaches, but kept failing to find the right solution. In the end, I took a completely different approach--there’s a calculator website that already did what the bite wanted me to do, so I just wrote a function to query that website and scraped the result off of it. That’s not what the bite was trying to teach me, but I still learned a lot in the process. It’s a small example, but in the real world, sometimes it is best to know when a problem is readily solved by something that already exists.

For reference, here’s that code, slightly edited to remove spoilers.

```
from urllib.parse import urlencode
from urllib.request import urlopen
import re


API_URL = (
  "url"
)

ANSWER_FINDER = re.compile(r"<br>(.*?)<br>")


def solution(decimal_number):
    if not isinstance(decimal_number, int) or not 0 < decimal_number < 4000:
        raise ValueError

    data = {
        "num": str(decimal_number),
        "action": "solve",
        "page_id": "MTU3NDgxNzMyNw==",
    }
    data = urlencode(data).encode("utf-8")
    response = urlopen(API_URL, data=data)
    response_data = response.read().decode()
    
    return ANSWER_FINDER.findall(response_data)[1].split(" = ")[1]

```
My initial solution to this used `requests` and `BeautifulSoup` to get the answer, but those aren’t available on this bite, so I had to learn how to use the built-in `urllib` and `re`, instead.

Another example is when I copied somewhere around a thousand lines of code from an open source "Abstract Syntax Tree to source code" program, Astor, into my solution, because I wanted to use the built-in AST parser in my solution, but needed a way to turn the AST back into source code. Working with limitations like that often leads to creativity.

So, next time you’re solving a bite, try to think of alternative methods. It’s also a great idea to go back to ones you have already solved and retry them to learn new lessons. Have fun with it, experiment with new ways of doing things, and remember to share what you learn!
