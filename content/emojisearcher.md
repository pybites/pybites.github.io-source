Title: Fast Emoji Lookup from the Command Line
Date: 2021-05-07 18:45
Category: Tools
Tags: poetry, emoji, pyperclip, pytest, command line, opensource, mocking, PyPI, packaging, project
Slug: emojisearcher
Authors: Bob
Summary: Today I wanted to share a little app I built the other day to search emojis from the command line.
cover: images/featured/pb-article.png

Today I wanted to share a little app I built the other day to search emojis from the command line.

This surely can be done via the OS (and Slack is the absolute winner for their emoji autocomplete!), but at times I still find it more useful (faster) to don't have to click anything in order to get my emojis.

And the tool supports copying multiple matching emojis to the OS clipboard at once:

```text
$ emo

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> snake beer fire ninja
Copying 🐍 🍺 🔥 🥷 to clipboard

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> q
Bye
```

At this point I have all 4 emojis on my clipboard so voilà, typing Cmd+v here they are: 🐍 🍺 🔥 🥷

Pretty cool, no?

## Install and run the package

```text
git clone git@github.com:PyBites-Open-Source/emojisearcher.git
cd emojisearcher
poetry install
poetry run emo
```

If you are new to `poetry`, check out our training [here](https://vimeo.com/534397924), this tool makes dependency management a breeze == happier developer life.

This last command (alias) actually works because I put this in the `pyproject.toml` file:

```
[tool.poetry.scripts]
emo = "emojisearcher.script:main"
```

Optionally you can make the invocation command even shorter (like I had in the first example) by adding this shell alias:

```
$ alias emo
alias emo='cd YOUR_PATH/emojisearcher && poetry run emo'
```

(Change `YOUR_PATH` to the path where you pulled the project.)

## Folder structure

Thanks to `poetry new` the folder structure was put in place from the start following [what's considered best practice](https://docs.python-guide.org/writing/structure/).

I like the have the tests in a dedicated `tests/` folder.

## Libraries

I used the [`emoji` library](https://pypi.org/project/emoji/) to find emojis leveraging its [`EMOJI_UNICODE` constant](https://github.com/carpedm20/emoji/tree/master/emoji/unicode_codes):

```
...
EMOJI_MAPPING = EMOJI_UNICODE[LANGUAGE]

...
def get_emojis_for_word(
    word: str, emoji_mapping: dict[str, str] = EMOJI_MAPPING
) -> list[str]:
    return [emo for name, emo in emoji_mapping.items() if word in name]
```

And I use [`pyperclip`](https://pypi.org/project/pyperclip/) to copy to the OS' clipboard:

```
from pyperclip import copy
...
def copy_emojis_to_clipboard(matches: list[str]) -> None:
    all_matching_emojis = ' '.join(matches)
    print(f"Copying {all_matching_emojis} to clipboard")
    copy(all_matching_emojis)
```

A very cool package I have used multiple times already, thanks [Al](https://pypi.org/user/AlSweigart/).

## What if there are multiple emoji matches?

In that case I enter interactive mode via [the `user_select_emoji` function](https://github.com/PyBites-Open-Source/emojisearcher/blob/master/emojisearcher/script.py#L57).

I had to come up with a creative way to trigger this interactive mode for which I choose a signal character (`SIGNAL_CHAR`): if a user's search string ends with a dot (`.`) it goes into interactive mode.

Here's why:

```text
$ emo

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> snake
Copying 🐍 to clipboard

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> flag
Copying 🏴 to clipboard

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> flag.
1 🏴
2 🏁
3 📪
4 📫
5 🎌
6 ⛳
7 📭
8 📬
9 🏴‍☠️
10 🏳️‍🌈
11 🏳️‍⚧️
12 🚩
13 🏳
Select the number of the emoji you want: 12
Copying 🚩 to clipboard

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> q
Bye
```

We cannot go wrong with the snake emoji, but for flag it selects the first of the 12 matches by default (for "heart" we get 130 matching emojis!), here I want to choose one manually so typing a trailing `.`, the program lets me do that.

## Testing

A few things here:

- `@pytest.mark.parametrize` is so nice to make your test code more DRY (_don't repeat yourself_).

- Breaking the code out into more functions makes it more reusable and easier to test.

- I tested interactive mode mocking out `input` with `@patch("builtins.input", side_effect=['a', 10, 2, 'q']`. The list in `side_effect` contains the arguments that "double" `input` one by one. So this would be equivalent to the following (after typing `tree.`):

```text
$ emo

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> tree.
1 🎄
2 🌳
3 🌲
4 🌴
5 🎋
Select the number of the emoji you want: a
a is not an integer.
1 🎄
2 🌳
3 🌲
4 🌴
5 🎋
Select the number of the emoji you want: 10
10 is not a valid option.
1 🎄
2 🌳
3 🌲
4 🌴
5 🎋
Select the number of the emoji you want: 2
Copying 🌳 to clipboard

------------------------------------------------------------------------------------
Type one or more emoji related words ...
End a word with a . if you want to select an emoji if there are multiple
matches, otherwise the first match will be picked. Type 'q' to exit.
> q
Bye
```

- A useful technique when testing your code is to remove any common leading white space. You can use `textwrap.dedent` for this but here I used the alternative `inspect.cleandoc`.

## Upload to PyPI

Thanks to some basic metadata in `[tool.poetry]` in the [toml file](https://github.com/PyBites-Open-Source/emojisearcher/blob/master/pyproject.toml), publishing to PyPI was just a matter of:

```
poetry build
poetry publish
```

(Use the `--repository` of `publish` first to try it on the test PyPI to see if it all looks good.)

You can learn more about this and much more in our [6 Key Ingredients of a Successful Pythonista](https://buildpythonapps.com/) free training.

That's it, if you like this project, [give it a star on Github](https://github.com/PyBites-Open-Source/emojisearcher) and happy to receive contributions to add features and what not ...

---

Keep Calm and Code in Python!

-- Bob
