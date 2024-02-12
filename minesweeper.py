import random
import re
from typing import List, Set, Tuple

class Board:
    def __init__(self, dim_size: int, num_bombs: int) -> None:
        """
        Initializes a new game board.

        Args:
            dim_size (int): The dimension size of the square game board.
            num_bombs (int): The number of bombs to be placed on the board.
        """
        self.dim_size: int = dim_size
        self.num_bombs: int = num_bombs

        self.board: List[List[str]] = self.make_new_board()
        self.assign_values_to_board()

        self.dug: Set[Tuple[int, int]] = set()

    def make_new_board(self) -> List[List[str]]:
        """
        Creates a new game board with randomly placed bombs.

        Returns:
            List[List[str]]: The generated game board.
        """
        board: List[List[str]] = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted: int = 0
        while bombs_planted <= self.num_bombs:
            loc: int = random.randint(0, self.dim_size ** 2 - 1)
            row: int = loc // self.dim_size
            col: int = loc % self.dim_size

            if board[row][col] == "*":
                continue

            board[row][col] = "*"
            bombs_planted += 1

        return board

    def assign_values_to_board(self) -> None:
        """Assigns values to non-bomb cells on the board, indicating the number of neighboring bombs."""
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

    def get_num_neighbouring_bombs(self, row: int, col: int) -> int:
        """
        Counts the number of neighboring bombs for a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of neighboring bombs.
        """
        num_neighbouring_bombs: int = 0

        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs

    def __str__(self) -> str:
        """
        Returns a string representation of the game board.

        Returns:
            str: The string representation of the game board.
        """
        visible_board: List[List[str]] = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

        string_rep: str = ''
        # get max column widths for printing
        widths: List[int] = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices: List[int] = [i for i in range(self.dim_size)]
        indices_row: str = '   '
        cells: List[str] = []
        for idx, col in enumerate(indices):
            format_str: str = '%-' + str(widths[idx]) + "s"
            cells.append(format_str % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format_str: str = '%-' + str(widths[idx]) + "s"
                cells.append(format_str % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len: int = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep

    def dig(self, row: int, col: int) -> bool:
        """
        Performs a dig operation on the specified cell.

        Args:
            row (int): The row index of the cell to dig.
            col (int): The column index of the cell to dig.

        Returns:
            bool: True if the dig operation is successful, False if a bomb is encountered.
        """
        self.dug.add((row, col))

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

def play(dim_size: int = 10, num_bombs: int = 10) -> None:
    """
    Function to start and play the game.

    Args:
        dim_size (int): The dimension size of the game board (default is 10x10).
        num_bombs (int): The number of bombs to be placed on the board (default is 10).
    """
    board = Board(dim_size, num_bombs)

    safe: bool = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(",(\\s)*", input("Where would you like to dig? Input as row, col : "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid input!! Try again.")
            continue

        safe = board.dig(row, col)

        if not safe:
            break

    if safe:
        print("CONGRAGULATIONS! YOU ARE VICTORIOUS")
    else:
        print("SORRY, GAME OVER!")
        board.dug = {(r, c) for r in range(board.dim_size) for c in range(board.dim_size)}
        print(board)

if __name__ == "__main__":
    play()
