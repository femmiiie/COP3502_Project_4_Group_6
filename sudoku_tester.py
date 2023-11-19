from sudoku_generator import SudokuGenerator
from board import Board

def test_SudokuGenerator():
    instance = SudokuGenerator(9, 30)
    #Should Print 2D 9x9 list of 0's
    instance.print_board()

    instance.fill_values()

    #Should Print valid Sudoku Solution
    instance.print_board()


def test_Board():
    instance = Board(9, 9)
    instance.select(1,1)
    instance.place_number(4)
    print(instance.get_box(0,0))


if __name__ == "__main__":
    test_Board()
    