from cell import Cell
import pygame
import copy
class Board:

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.board = [[Cell(0, i, j) for i in range(width)] for j in range(height)]
        self.selected_cell = (9, 9)
        self.solved_board = self.board


    def get_int_list(self)->list[list[int]]:
        board_list = []
        for i in range(len(self.board)):
            board_list.append(self.get_row(i))
        return board_list


    def set_reset_board(self, board:list[list[Cell]]):
        self.reset_board = self.get_int_list()
    

    # Reset all cells in the board to their original values.
    def reset_to_original(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].set_cell_value(self.reset_board[i][j])
                self.board[i][j].set_sketched_value(0)

        self.set_selected(9, 9)
            
    #Marks boards
    def set_selected(self, row, col):
        self.selected_cell = (row, col)

    def get_selected(self):
        return self.selected_cell

    #Clears the cells
    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].value = 0

    '''GETTERS FOR VALIDATION METHODS'''
    #Gets values from specified row as ints
    def get_row(self, num:int)->list[int]:
        value_list = []
        for i in self.board[num]:
            if i.get_cell_value() == 0:
                value_list.append(i.get_sketched_value())
            else:
                value_list.append(i.get_cell_value())
        return  value_list


    #Get values from specified col as ints
    def get_col(self, num: int) -> list[int]:
        value_list = []
        for i in range(len(self.board)):
            if self.board[i][num].get_cell_value() == 0:
                value_list.append(self.board[i][num].get_sketched_value())
            value_list.append(self.board[i][num].get_cell_value())
        return value_list


    #Gets value from specified box as int list in reading order
    def get_box(self, row_start:int, col_start:int)->list[int]:
        value_list = []
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if self.board[i][j].get_cell_value() == 0:
                    value_list.append(self.board[i][j].get_sketched_value())
                else:
                    value_list.append(self.board[i][j].get_cell_value())
        return  value_list

    # Sets the value of the current selected cell equal to user entered value.
    def place_number(self, value):
        self.board[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(value)


    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        for r in range(0, 9):
            for c in range(0, 9):
                if self.board[r][c].get_cell_value() == 0:
                    return False
        return True

    # Finds the first empty cell and returns as tuple
    def find_empty(self):
        for r in range(0, 9):
            for c in range(0, 9):
                if self.board[r][c].get_cell_value() == 0:
                    return r, c

    # Check row, col, and box function make sure that each number is found in each. Combined in check_board

    def check_row(self):
        for i in range(0, 9):
            found_nums = 0
            current_row = self.get_row(i)
            for num in range(1,10):
                if num in current_row:
                    found_nums += 1

                    try:
                        current_row.remove(num)
                    except:
                        return False

            if len(current_row) != 0:
                return False

        return True

    def check_col(self):
        for i in range(0, 9):
            found_nums = 0
            current_col = self.get_col(i)
            for num in range(1,10):
                if num in current_col:
                    found_nums += 1

                    try:
                        current_col.remove(num)
                    except:
                        return False

            if len(current_col) != 0:
                return False

        return True
        

    def check_box(self):
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                current_box = self.get_box(r, c)

                for num in range(1,10):
                
                    if num in current_box:
                        try:
                            current_box.remove(num)
                        except:
                            return False
                        
                if len(current_box) != 0:
                    return False
        
        return True

    def check_board(self):
        if self.check_box() and self.check_row() and self.check_col():
            return True
        return False
        
