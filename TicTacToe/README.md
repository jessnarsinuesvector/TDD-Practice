# Tic Tac Toe

Requirements

`(a snippet)`
```
Tic – Tac – Toe
The requirements are:
a game is over when all fields are taken
a game is over when all fields in a column are taken by a player
a game is over when all fields in a row are taken by a player
a game is over when all fields in a diagonal are taken by a player
a player can take a field if not already taken
players take turns taking fields until the game is over

- Jim Gildea, et al.
```

Solution

provide a UI -> 3 columns, 3 rows

X-O input switching
X starts
each click in UI row x column will
    1. Change the display to X
    2. Change the next input to O
    3. Check if
        3.1 All slots are already taken
        3.2 A 3-in-a-row has been made

Sample Execution
> python main.py