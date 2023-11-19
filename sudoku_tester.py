from sudoku_generator import SudokuGenerator
from board import Board

def test_SudokuGenerator():
    instance = SudokuGenerator(9, 30)

        #PRINT FUNCS ARE WORKING
        #BY EXTENSION GET BOARD WORKS
    instance.print_board()
    print()

        #VALIDITY FUNCS ARE WORKING
    #print(instance.valid_in_row(0,6))
    #print(instance.is_valid(0,0, 6))
    instance.fill_values()

    #Should Print valid Sudoku Solution
    instance.print_board()
    print()

    #Should appropriately remove 30 cells
    instance.remove_cells()
    instance.print_board()



def test_Board():
    instance = Board(9, 9)
    instance.select(1,1)
    instance.place_number(4)
    print(instance.get_row(0))

if __name__ == "__main__":
    test_SudokuGenerator()
    #test_Board()
    