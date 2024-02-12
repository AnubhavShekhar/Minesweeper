# Minesweeper Game

This is a simple implementation of the classic Minesweeper game in Python.

## Introduction

Minesweeper is a single-player puzzle game in which the player must uncover all non-bomb cells without detonating any bombs. The game board is a grid of cells, some of which contain bombs. The player uncovers cells by "digging" them, revealing either a bomb or a number indicating the number of neighboring cells containing bombs.

## Features

- Customizable game board size and number of bombs.
- ASCII-based interface for easy gameplay.
- Recursive cell uncovering to reveal neighboring cells.

## Getting Started

1. **Clone the repository:**

    ```
    git clone https://github.com/example/minesweeper.git
    ```

2. **Navigate to the project directory:**

    ```
    cd minesweeper
    ```

3. **Run the game:**

    ```
    python minesweeper.py
    ```

4. **Follow the on-screen instructions to play the game.**

## Gameplay Instructions

- The game board is represented as a grid of cells.
- Enter the coordinates of the cell you want to dig in the format `row, col`.
- If the cell contains a bomb, the game is over.
- If the cell is empty, it will reveal a number indicating the number of neighboring cells containing bombs.
- Keep digging until all non-bomb cells are uncovered or a bomb is detonated.
