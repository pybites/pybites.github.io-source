Title: Fast Emoji Lookup from the Command Line
Date: 2021-05-07 18:00
Category: Tools
Tags: poetry, emoji, pyperclip, pytest, command line, opensource
Slug: emojisearcher
Authors: PyBites
Summary: Today I share a nice little app I built they other day to search for emojis from the command line.
cover: images/featured/pb-special.png

Today I share a nice little app I built they other day to search for emojis from the command line.

This can be done via the OS, but I still find it useful to don't have to click anything in order to get my emojis. It also supports multiple emojis at once!

## Get the package

```
git clone git@github.com:PyBites-Open-Source/emojisearcher.git
cd emojisearcher
poetry install
poetry run emo
```

This last command (alias) actually works because I put this in the `pyproject.toml` file:

```
[tool.poetry.scripts]
emo = "emojisearcher.script:main"
```

Optionally you can make this even shorter by adding this shell alias (changing the path where you pulled it in):

```
$ alias emo
alias emo='cd YOUR_PATH/emojisearcher && poetry run emo'
```

## Folder structure

Thanks to `poetry new` the folder structure was put in place. I like the have the tests in a dedicated `tests/` directory.

## Libraries

I used the `emoji` library to find emojis leveraging its `EMOJI_UNICODE` constant:

```
...
EMOJI_MAPPING = EMOJI_UNICODE[LANGUAGE]

...
def get_emojis_for_word(
    word: str, emoji_mapping: dict[str, str] = EMOJI_MAPPING
) -> list[str]:
    # TODO: mypy says "Incompatible types in assignment"
    return [emo for name, emo in emoji_mapping.items() if word in name]
```

And I use `pyperclip` to copy to the OS' clipboard:

```
from pyperclip import copy
...
def copy_emojis_to_clipboard(matches: list[str]) -> None:
    all_matching_emojis = ' '.join(matches)
    print(f"Copying {all_matching_emojis} to clipboard")
    copy(all_matching_emojis)
```

## What if there are multiple matches?

In that case I enter user interactive mode with `user_select_emoji`.

I had to come up with a creative way to trigger this interactive mode for which I choose a dot: if a user's search string ends with this `SIGNAL_CHAR` it goes into interactive mode.

Here's why:

	[bobbelderbos@imac emojisearcher (master)]$ emo

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

We cannot go wrong with the snake emoji, but for flag it selects the first one by default (for "heart" there are 130 matches!), here I want to choose so typing a trailing `.` the program does just that.

## Testing

A few things here:

- `@pytest.mark.parametrize` is so nice to make your test code more DRY (_don't repeat yourself_).
- Breaking the code out into more functions makes it more reusable and easier to test.
- I tested interactive mode mocking out `input` with `@patch("builtins.input", side_effect=['a', 10, 2, 'q']`. The list in `side_effect` contains the arguments that "double" `input` one by one.
- A useful technique when testing your code is to remove any common leading whitespace. You can use `textwrap.dedent` for this but here I used the alternative `inspect.cleandoc`.

## PyPI

Thanks to some basic metadata in `[tool.poetry]` in the [toml file](https://github.com/PyBites-Open-Source/emojisearcher/blob/master/pyproject.toml), publishing to PyPI was just a matter of:

```
poetry build
poetry publish
```

(Use `--repository` first to try it on the test PyPI.)

You can learn more about this and much more in our [6 Key Ingredients of a Successful Pythonista](https://buildpythonapps.com/) free training.

---

Keep Calm and Code in Python!

- Bob
