Title: Assertions about Exceptions with pytest.raises()
Date: 2020-05-16 20:20
Category: Concepts
Tags: guest, pybites, pytest, testing, contextmanagers
Slug: guest-pytest-raises
Authors: AJ Kerrigan
Summary: It's useful to test for exceptions exceptions in your code. A handy feature of pytest makes that fun and flexible!
cover: images/featured/pb-guest.png

I got some feedback related to [Bite 243](https://codechalleng.es/bites/243/) recently. Since that's a [testing bite](https://pybit.es/launch-pytest-bites.html), it means working with [pytest](https://docs.pytest.org) and specifically checking for exceptions with `pytest.raises()`. The comment got me to look at this handy feature of pytest with fresh eyes, and it seemed like a trip worth sharing!

### `pytest.raises()` as a Context Manager

We can uses `pytest.raises()` to assert that a block of code raises a specific exception. Have a look at this sample from the [pytest documentation](https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions):

```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
```

Is that test reasonably clear? I think so. But see how that `assert` is outside the `with` block? The first time I saw that sort of assertion, it felt odd to me. After all, my first exposure to the `with` statement was opening files:

```python
with open('my_delicious_file.txt') as f:
    data = f.read()
```

When we get comfortable using `open()` in a [with](https://docs.python.org/2.5/whatsnew/pep-343.html) block like that, we pick up some lessons about context manager behavior. Context managers are good! They handle runtime context like opening and closing a file for us, sweeping details under the rug as any respectable abstraction should. As long as we only touch `f` inside that `with` block, our lives are long and happy. We probably don't try to access `f` _outside_ the block, and if we do things go awry since the file is closed. `f` is effectively dead to us once we leave that block.

I didn't realize how much I had internalized that subtle lesson until the first time I saw examples of `pytest.raises`. It felt wrong to use `excinfo` after the `with` block... like an _animal_! But when you think about it, that's the only way it can work. We're testing for an _exception_ after all - once an exception happens we get booted out of that block. The pytest docs explain this well in a note [here](https://docs.pytest.org/en/latest/reference.html#pytest-raises):

> **Note**
> 
> When using pytest.raises as a context manager, it’s worthwhile to note that normal context manager rules apply and that the exception raised must be the final line in the scope of the context manager. Lines of code after that, within the scope of the context manager will not be executed. For example:

```python
>>> value = 15
>>> with raises(ValueError) as exc_info:
...     if value > 10:
...         raise ValueError("value must be <= 10")
...     assert exc_info.type is ValueError  # this will not execute
```

> Instead, the following approach must be taken (note the difference in scope):

```python
>>> with raises(ValueError) as exc_info:
...     if value > 10:
...         raise ValueError("value must be <= 10")
...
>>> assert exc_info.type is ValueError
```

### Under the Covers

What I didn't think about until recently is how the `open()`-style context manager and the `pytest.raises()` style are mirror-world opposites:
  
|                | open('file.txt') as f                    | pytest.raises(ValueError) as excinfo                 |
| -------------- | ---------------------------------------- | ---------------------------------------------------- |
| inside `with`  | `f` is useful                            | `excinfo` is present but useless (empty placeholder) |
| outside `with` | `f` is present but useless (file closed) | `excinfo` has exception details                      |

<br />

How does this work under the covers? As the [Python documentation](https://docs.python.org/3/reference/datamodel.html#context-managers) notes, entering a `with` block invokes a context manager's `__enter__` method and leaving it invokes `__exit__`. [Check out](https://github.com/pytest-dev/pytest/blob/efada09da2a01b55206801568b3427a38acc153a/src/_pytest/python_api.py#L716-L726) what happens when the context manager gets created, and what happens inside `__enter__`: 

```python
def __init__(
    self,
    expected_exception: Union["Type[_E]", Tuple["Type[_E]", ...]],
    message: str,
    match_expr: Optional[Union[str, "Pattern"]] = None,
) -> None:
    ... snip ...
    self.excinfo = None  # type: Optional[_pytest._code.ExceptionInfo[_E]]

def __enter__(self) -> _pytest._code.ExceptionInfo[_E]:
    self.excinfo = _pytest._code.ExceptionInfo.for_later()
    return self.excinfo
```

So that `excinfo` attribute starts empty - good, there's no exception yet! But in a nod to clarity, it gets a placeholder `ExceptionInfo` value thanks to a `for_later()` method! `Explicit is better than implicit` indeed!

So what happens [later](https://github.com/pytest-dev/pytest/blob/efada09da2a01b55206801568b3427a38acc153a/src/_pytest/python_api.py#L732-L751) when we leave the `with` block?

```python
    def __exit__(
        self,
        exc_type: Optional["Type[BaseException]"],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        ... snip ...
        exc_info = cast(
            Tuple["Type[_E]", _E, TracebackType], (exc_type, exc_val, exc_tb)
        )
        self.excinfo.fill_unfilled(exc_info)
        ... snip ...
```

Pytest checks for the presence and type of an exception, and then it delivers on its `for_later()` promise by filling in `self.excinfo`.

### A Summary in Three Parts

With all that background out of the way, we can see the three-act play of `excinfo`'s life - from nothing, to empty, to filled:

```python
def __init__(...):
    self.excinfo = None  # type: Optional[_pytest._code.ExceptionInfo[_E]]

def __enter__(...):
    self.excinfo = _pytest._code.ExceptionInfo.for_later()
    return self.excinfo

def __exit__(...):
    self.excinfo.fill_unfilled(exc_info)
```

Which shows up in our test code as:

```python
with pytest.raises(RuntimeError) as excinfo:  # excinfo: None
    # excinfo: Empty
    def f():
        f()

    f()
# excinfo: Filled
assert "maximum recursion" in str(excinfo.value)
```

And that's a beautiful thing!

### References

[With Statement Context Managers (python docs)](https://docs.python.org/3/reference/datamodel.html#context-managers)
[pytest.raises (pytest docs)](https://docs.pytest.org/en/latest/reference.html#pytest-raises)
[Assertions about excepted exceptions (pytest docs)](https://docs.pytest.org/en/latest/assert.html#assertraises)
[PEP 343 - The "with" statement](https://www.python.org/dev/peps/pep-0343/)
