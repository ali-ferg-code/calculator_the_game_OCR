# Calculator: The Game OCR
A personal python project to solve levels in a fun yet infuriating phone game - Calculator: The Game on [Android](https://play.google.com/store/apps/details?id=com.sm.calculateme) and [ios](https://itunes.apple.com/us/app/calculator-the-game/id1243055750). 

This implementation reads screenshots of the game, performs some OCR on the image and solves the puzzle.
Any sensible resolution screenshots should work, but the character recognition works best at resolutions of 1920x1080 or larger.

# Usage
```
>python image_to_solution.py --image level_91.png
Reading image path: level_91.png
Detected the following buttons: ['x9', '4', '3=>5', 'x3', 'SUM']
Detected number of moves:        5
Detected goal number:            45
Detected starting number:        0
Solving...

                START:          0
                GOAL:           45
                MOVES:          5
                BUTTONS:        [Times 9.0, Append 4.0, Button: Replace 3=>5, Times 3.0, Button: Sum]
                SEARCH SPACE:   3125 Combinations

                SOLUTION:       (Append 4.0, Times 3.0, Button: Sum, Button: Replace 3=>5, Times 9.0)
```
