# Solitaire Simulator

Solitaire Simulator is a simulator for the puzzle game, [Solitaire](https://en.wikipedia.org/wiki/Peg_solitaire). Not the card game!

I grew up playing this game, and have never looked up the solution to get just one piece (or peg, or marble) remaining. I've never figured it out or happened upon it by chance, either. My best score is two pieces remaining.

This is a side project I started ages ago out of curiosity -- whether the game could be solved randomly, or whether a more intelligent agent/player would be required to find a solution.

The code isn't very fast or elegant, but it's simple enough and it works.

## What does it do?

Solitaire Simulator lets you simulate solitaire games played by an automatic player.

You can write your own player with whatever algorithm you can come up with. The only restriction is to stick to legal moves. You'll get an error if you try to choose an illegal move.

Solitaire Simulator can run one or many games for one or many players at a time. It can print the full set of moves for each game, end states of each game (the default) or nothing at all apart from a summary of how each player did.

## How to run

Show all options:
```
python3 -m solitare --help
```

Run all players for one game each. Print the end state of each game and summary (the default).
```
python3 -m solitare
```

Run all players for one game each. Print all the moves along the way.
```
python3 -m solitare --print=all-moves
```

Run all players for 100 games of solitaire each, not printing anything apart from the summary:
```
python3 -m solitare --num-games 100 --print=summary
```

Run only the random player for 1000 games, not printing anything apart from the summary.
```
python3 -m solitaire --num-games 1000 --players random.RandomPlayer --print=summary
```

## How to build a 'player'

* Refer to the class `BasePlayer` in `solitaire/players/base.py`
* Create a new file in `players`, e.g. `players/myplayer.py`
* Create a class in the file that inherits from `BasePlayer` and implements the `get_next_move` method.
  * This method returns the desired next move, leaving you free to define whatever algorithm you want.
  * E.g.
    ```
    from solitaire.board import Move
    from solitaire.player.base import BasePlayer


    class MyPlayer(BasePlayer):

        def get_next_move(self) -> Move:
            # always choose the first available move in the list
            return self.board.get_moves()[0]
    ```
* Run `python3 -m solitaire --players myplayer.MyPlayer` and see what happens...!
  * To run a simulation with more games, try `python3 -m solitaire --players myplayer.MyPlayer --num-games 1000 --print=summary`