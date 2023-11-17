from sudoku_generator import SudokuGenerator

if __name__ == "__main__":
    instance = SudokuGenerator(9, 30)
    #Should Print 2D 9x9 list of 0's
    instance.print_board()

    instance.fill_values()

    #Should Print valid Sudoku Solution
    instance.print_board()