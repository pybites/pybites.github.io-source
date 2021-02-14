Title: Naughts and Crosses gets a little help
Date: 12 February 2021
Category: Concepts
Tags: guest, games theory, ai, tic-tac-toe, python
Slug: guest-naughts-and-crosses
Authors: Geoff Riley
summary: Naughts and Crosses (Tic-Tac-Toe to some audiences) is a popular skill game often played by children. It can also be usefully employed to distract dial up computers, at NORAD for example, rather than allowing the 'playing' of Global Thermonuclear War.  Would you like to play a game?
cover: images/featured/pb-guest.png


![Header image: Naughts and Crosses, Os and Xs, Tic Tac Toe](images/guest-naughts-and-crosses-ai/title-bar.png)
<!-- Indexes are always a good start! -->
## Index
* [Introduction](#introduction)
  * [Game concept](#game-concept)
* [Basic game implementation](#basic-game-implementation)
  * [Starting the code](#starting-the-code)
* [References](#references)
  
<a name="introduction"></a>
## Introduction

![Would you like to play a game?](images/guest-naughts-and-crosses-ai/like-to-play.png)[^WG]

If you happen to have recently hacked into [NORAD (North American Aerospace Defense Command)](https://www.norad.mil/) 
then it is quite possible that you are stuck in the 1980s and are looking to play **Global Thermonuclear War**[^WG], 
take it from me: it really won't turn out hope you hope.

On the other hand if you are looking for what is arguably the simplest of all strategy games, then you've come to the
right place. This article was inspired by the _PyBites Coding Challenge 12_—**Build a Tic-tac-toe Game**[^PCC12].

<a name="game-concept"></a>
### Game concept

![Image of naughts and crosses grid](images/guest-naughts-and-crosses-ai/grid-blank.png)

Traditionally, naughts and crosses[^WP] is a pencil and paper game for two players: one playing the symbol 'O', 
pronounced 'naught' or 'oh', and the other playing 'X', pronounced 'cross' or 'ex'. The game begins with a 3x3 grid of 
nine cells, and the players take turns at drawing their symbols into one of the empty cells. The aim is to achieve the 
occupation of three cells in a row, horizontally, vertically or diagonally, with their own symbol, whilst _at the same 
time_ interfering with their opponents attempts to do likewise. There are eight possible winning lines are shown in the 
figure below.

![Image of winning positions](images/guest-naughts-and-crosses-ai/winning-positions.png)

<a name="basic-game-implementation"></a>
## Basic game implementation

The first thing that is necessary in implementing _any_ game is deciding how it should be represented both to the player
and when it is held in the computer memory. We are working with fixed a three by three grid in this game, so it is easy 
to see that a series of nine consecutive elements of an array can be used. Like this:

![Image of array of nine memory cells numbered zero to nine](images/guest-naughts-and-crosses-ai/memory-cells.png)

These memory cells, in turn, map to the three rows of three cells that will be displayed to the player.  To help the
player to associate the positions of the cells, however, it is convenient to give a different _external_ mapping that
is based upon something familiar.  A familiar three by three grid is found on the keyboard numeric keypad, but this is 
'upside down' compared to how we have suggested the internal representation will be achieved.

This difference in representation can be handled in a few different ways:

* change the internal representation to match the external representation;
* change the external representation to match the internal representation; or
* find a way to translate between the two representations as and when needed.

There are implications for each of these options. Firstly, if the internal representation is changed, it wil be 
necessary to extract the details for the grid when it is being displayed in a non-sequential order. This is not an 
impossible situation, but adds a layer of complexity that is probably undesirable. Secondly, if the external 
representation is changed, then it inconveniences the player who will have to think more about the value of the cell
rather than the position. Thirdly, and finally, translating between the two systems allows the positives of both 
representations to be exercised with a minor inconvenience of ensuring that the interface between the two sides is 
patrolled appropriately.

Assuming that the third option is taken we have the following representations:

![Image of internal cell numbering](images/guest-naughts-and-crosses-ai/numbering-internal.png) 
![Image of external cell numbering](images/guest-naughts-and-crosses-ai/numbering-external.png)


<a name='starting-the-code'></a>
### Starting the code

It is always wise to start off a Python file with a descriptive comment about the file, who wrote it, any copyright
declarations, the place within a project that it belongs and what the weather is like when you write the code, possibly
less likely on that last one. So, we begin our project and, as it is going to be a single file, just comment on what
the whole project is about.  If this was to be a one of a number of files then the description would focus upon the 
functionality of this particular file.
```python
"""
    Proper name: 'Naughts and Crosses'
    Irish name: 'Xs and Os'
    American name: 'Tic Tac Toe'
    Reason: Who on Earth has a clue?  It's an historical thing.
"""
```
Lovely. That'll do nicely.  Not much coding going on there though.  There are going to be some `import`s of various 
modules to help us with the coding, straight off the bat we know that we are going to be dealing with some kind of
memory cells, this brings to mind that we'll need coding hints for things like `List` and perhaps `Union` so 
we'll add those in for a starter.  Later on we'll add more in at this place in the file.
```python
from typing import List, Union
```

There are a number of elements of the game that can be usefully given names to help to document the code as we go along.
The extra advantage to defining things by name at this point is that if we want to change things later on, then any 
changes made here automatically reflect through the whole code. (Hurrah!)

So, what elements need to be defined? We have already identified that there are internal and external 
representations involved, therefore those should be defined along with the mapping between the two.  Externally we know 
that we're going to have 'O' and 'X' to show the symbols—that much is obvious—but there is a third symbol too: the 
blank. The blank could be just a space character, but that isn't very _visible_ if you want to **see** the grid, 
particular when it is empty, but also when working out which row and column a single symbol might be on. For this reason
we'll use the underscore ('_') to represent a blank space.
```python
# External representations of the playing symbols 
BLANK_SYM: str = '_'
O_SYM: str = 'O'
X_SYM: str = 'X'
```
That will make any grids clear:
```text
 ___     _X_     ___
 ___     ___     _O_
 ___     ___     ___
Blank / One X / One O
```
What about internal representations? Does it matter? We could use the same symbols, however we _do_ know that string
comparisons are slower than integer comparisons, and so it would probably be better to use the quicker of the two 
given that there are a lot of comparisons that will be made. Let us keep it simple and just use the values zero to two.
```python
# Internal representations of the playing symbols 
BLANK_VALUE: int = 0
O_VALUE: int = 1
X_VALUE: int = 2
```
Now that we have those defined, we can create a couple of dictionaries that map between the two systems:
```python
# Translation between systems
VAL_TO_SYM: dict = {
  BLANK_VALUE: BLANK_SYM,
  O_VALUE: O_SYM,
  X_VALUE: X_SYM,
}
SYM_TO_VAL: dict = {
  BLANK_SYM: BLANK_VALUE,
  O_SYM: O_VALUE,
  X_SYM: X_VALUE,
}
```
The chances are that whilst we are going through checking for winning lines and such like, we might want a quick way
to refer to the opponent of the current player; we might not need it, but it could prove useful:
```python
OPPONENT: dict = {
  O_VALUE: X_VALUE,
  X_VALUE: O_VALUE,
}
```
Just a couple of other things that need to be taken care of: the translation of internal to external grid positions,
and vise versa.  Looking at the graphical images of the two representations, it is easy to write out a couple of
dictionary constants mapping between the two:

![Image of internal and external representations of grid](images/guest-naughts-and-crosses-ai/numbering-int-and-ext.png)
```python
INTERNAL_TO_EXTERNAL: dict = {
  0: 7, 1: 8, 2: 9, 
  3: 4, 4: 5, 5: 6, 
  6: 1, 7: 2, 8: 3
}
EXTERNAL_TO_INTERNAL: dict = {
  7: 0, 8: 1, 9: 2, 
  4: 3, 5: 4, 6: 5, 
  1: 6, 2: 7, 3: 8
}
```


<!-- add your closer here! -->

-- [Geoff Riley](pages/guests.html#geoff-riley)


<a name='references'></a>
## References
* [^WG]: [Wargames (1983)](https://www.imdb.com/title/tt0086567/)
* [^WP]: [Wikipedia article on Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
* [^PCC12]: [PyBites coding challenge 12](https://codechalleng.es/challenges/12/)

Markdown:[Markdown extended reference](https://www.markdownguide.org/extended-syntax/)

```python
from collections import defaultdict
from functools import reduce
from itertools import cycle
from operator import mul
from typing import List, Union

# Definition of game elements
# External representation of grid is numbered 1 to 9;
# internal representation of grid is numbered 0 to 8.
# Working with a 3 x 3 grid represented as a linear array of nine cells
# initialise to `DEFAULT`
# External representations of the playing symbols 
BLANK_SYM: str = '_'
O_SYM: str = 'O'
X_SYM: str = 'X'
# Internal representations of the playing symbols 
BLANK_VALUE: int = 2
O_VALUE: int = 3
X_VALUE: int = 5
# Translation between systems
VAL_TO_SYM: dict = {
  BLANK_VALUE: BLANK_SYM,
  O_VALUE: O_SYM,
  X_VALUE: X_SYM,
}
SYM_TO_VAL: dict = {
  BLANK_SYM: BLANK_VALUE,
  O_SYM: O_VALUE,
  X_SYM: X_VALUE,
}
OPPONENT: dict = {
  O_VALUE: X_VALUE,
  X_VALUE: O_VALUE,
}
EXTERNAL_TO_INTERNAL = {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}
INTERNAL_TO_EXTERNAL = {0: 7, 1: 8, 2: 9, 3: 4, 4: 5, 5: 6, 6: 1, 7: 2, 8: 3}
# Visualise the board cells numbered as:
#  7  8  9
#  4  5  6
#  1  2  3
# (Just like a numeric keypad!)
VALID_POSITIONS: List[int] = list(range(1, 10))
# A winning combination exists for three symbols in a row:
WINNING_COMBINATIONS = (
  (6, 7, 8), (3, 4, 5), (0, 1, 2),
  (6, 3, 0), (7, 4, 1), (8, 5, 2),
  (0, 4, 8), (6, 4, 2),
)
WINNING_PROD = {
  O_VALUE: 18,
  X_VALUE: 50,
}


class BlockedCell(Exception):
  pass


class InvalidMove(Exception):
  pass


class TicTacToe:
  _board: List[int]

  def __init__(self):
    """Constructor, allocate the blank board"""
    # Create an array of cells to hold the grid positions.
    self._board = [BLANK_VALUE] * len(VALID_POSITIONS)
    self._turn_cycle = cycle([O_VALUE, X_VALUE])
    self._turn = self._next_turn()
    self._move = 0

  def _next_turn(self):
    return next(self._turn_cycle)

  def __str__(self):
    """Print the board"""
    return ' ' + '\n---+---+---\n '.join(
      ' | '.join(VAL_TO_SYM[c]
                 for c in self._board[s * 3:(s + 1) * 3])
      for s in range(3))

  @staticmethod
  def _ndx_to_cell_(ndx: int) -> int:
    return EXTERNAL_TO_INTERNAL[ndx]

  @staticmethod
  def _cell_to_ndx_(cell: int) -> int:
    return INTERNAL_TO_EXTERNAL[cell]

  def player_move(self, target_position: int):
    """
    Attempt to place the player move

    May raise exceptions: BlockCell, InvalidMove
    """
    if target_position in VALID_POSITIONS:
      cell = self._ndx_to_cell_(target_position)
      if self._board[cell] is BLANK_VALUE:
        self._board[cell] = self._turn
      else:
        raise BlockedCell(
          f'Cannot play at {target_position}, it is already held by {VAL_TO_SYM[self._board[cell]]}')
    else:
      raise InvalidMove(f'Invalid move, {target_position} not available')

  def next_player(self) -> str:
    self._turn = self._next_turn()
    return VAL_TO_SYM[self._turn]

  def find_winner(self) -> Union[int, None]:
    """Find a winner, 'O', 'X' or None"""
    for s in [O_VALUE, X_VALUE]:
      if any(all(self._board[c] == s for c in combo) for combo in WINNING_COMBINATIONS):
        return s
    return None

  @property
  def win(self) -> bool:
    """Test if the game is won"""
    return self.find_winner() == self._turn

  @property
  def lose(self) -> bool:
    """Test if the game is lost"""
    return self.find_winner() == OPPONENT[self._turn]

  @property
  def draw(self) -> bool:
    """Test if the game is a draw"""
    return not (any(c == BLANK_VALUE for c in self._board))

  @property
  def win_draw_lose(self) -> bool:
    """Test if the game is still in play"""
    return self.win or self.lose or self.draw

  @property
  def player(self) -> str:
    return VAL_TO_SYM[self._turn]

  def ai_move(self) -> str:
    return str(self._cell_to_ndx_(self._ai_move()))

  def _ai_move(self) -> int:
    """Work out a move for the computer"""
    # Working from the Strategy presented on Wikipedia
    #       [https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy]
    # 1. Win: If the player has two in a row, they can place a
    #       third to get three in a row.
    #
    # Using 3 and 5 for 'O' and 'X' and 2 for empty means that
    # in order to identify a 'winning' line we can take the
    # product of the values to work out what if an appropriate
    # gap is present.
    # (Distinct) Possible products are:
    #   _ _ _ → 2 x 2 x 2 = 8
    #   O _ _ → 3 x 2 x 2 = 12
    #   O O _ → 3 x 3 x 2 = 18 [Winning O line]
    #   O O O → 3 x 3 x 3 = 27
    #   O X _ → 3 x 5 x 2 = 30
    #   O O X → 3 x 3 x 5 = 45
    #   X _ _ → 5 x 2 x 2 = 20
    #   X X _ → 5 x 5 x 2 = 50 [Winning X line]
    #   X X X → 5 x 5 x 5 = 125
    #   X X O → 5 x 5 x 3 = 75
    # Therefore it can be seen that there is a single value
    # indicating a winning line for either Os or Xs
    winning_lines = defaultdict(set)
    for line in WINNING_COMBINATIONS:
      prod = reduce(mul, [self._board[c] for c in line])
      winning_lines[prod].add(line)

    # Let's see if there is a winning line for the current player
    if winning_lines[WINNING_PROD[self._turn]]:
      # find the blank in the first winning line.
      line = winning_lines[WINNING_PROD[self._turn]].pop()
      return [n for n in line if self._board[n] == BLANK_VALUE][0]

    # 2. Block: If the opponent has two in a row, the player
    #       must play the third themselves to block the opponent.
    if winning_lines[WINNING_PROD[OPPONENT[self._turn]]]:
      # find the blank to play a block.
      line = winning_lines[WINNING_PROD[OPPONENT[self._turn]]].pop()
      return [n for n in line if self._board[n] == BLANK_VALUE][0]

    # 3. Fork: Create an opportunity where the player has two
    #       ways to win (two non-blocked lines of 2).

    # 4. Blocking an opponent's fork:
    #       If there is only one possible fork for the opponent,
    #       the player should block it.
    #       Otherwise, the player should block all forks in any
    #       way that simultaneously allows them to create two
    #       in a row.
    #       Otherwise, the player should create a two in a row
    #       to force the opponent into defending, as long as it
    #       doesn't result in them creating a fork.
    #       For example, if "X" has two opposite corners and
    #       "O" has the center, "O" must not play a corner move
    #       in order to win. (Playing a corner move in this
    #       scenario creates a fork for "X" to win.)

    # 5. Center: A player marks the center. (If it is the first
    #       move of the game, playing a corner move gives the
    #       second player more opportunities to make a mistake
    #       and may therefore be the better choice; however, it
    #       makes no difference between perfect players.)
    if self._board[4] == BLANK_VALUE:
      return 4

    # 6. Opposite corner: If the opponent is in the corner, the
    #       player plays the opposite corner.
    for x, y in [(0, 8), (2, 6), (6, 2), (8, 0)]:
      if self._board[x] == OPPONENT[self._turn] and self._board[y] == BLANK_VALUE:
        return y

    # 7. Empty corner: The player plays in a corner square.
    for x in [0, 2, 6, 8]:
      if self._board[x] == BLANK_VALUE:
        return x

    # 8. Empty side: The player plays in a middle square on any
    #       of the 4 sides.
    for x in [1, 3, 5, 7]:
      if self._board[x] == BLANK_VALUE:
        return x

    raise InvalidMove(f"Couldn't identify a move to make for AI controlled {self.player}")


if __name__ == "__main__":
  while True:
    game = TicTacToe()
    print("Let's play Naughts and Crosses!")
    while not game.win_draw_lose:
      print('\nCurrent state of game:')
      print(game)
      try:
        if game.player == O_SYM:
          mv = input(f'Where would you like to play your {game.player}? ')
        else:
          mv = game.ai_move()
          print(f'\nComputer chooses to play {game.player} at {mv}.')
        position = int(mv)
        game.player_move(position)
        if game.win:
          print(game)
          print(f'**WIN** We have a WINNER!!  Well done {game.player}.')
          break
        if game.draw:
          print(game)
          print('**DRAW** That was a little pointless in the end.')
          break
        game.next_player()
      except InvalidMove as exc:
        print(f'Poor choice, Grasshopper, "{mv}" is not and acceptable move: use the numeric keypad layout!')
        print(f'DEBUG: {exc}')
      except BlockedCell as exc:
        print(f'Sorry that spot is already taken.')
        print(f'DEBUG: {exc}')
      except ValueError as exc:
        print(f'Please indicate position as though it were the numeric keypad.')
        print(f'DEBUG: {exc}')
```