from cell import Cell
import pygame
class Board:

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.board = [[Cell(0, i, j) for i in range(width)] for j in range(height)]
        self.selected_cell = (9, 9)
        self.original_board = self.board

    def set_reset_board(self, board:list[list[Cell]]):
        self.reset_board = board
            
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
    def get_col(self, num:int)->list[int]:
        value_list = []
        for i in range(len(self.board)):
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

    # Reset all cells in the board to their original values.
    def reset_to_original(self):
        self.board = self.reset_board
        self.set_selected(9, 9)

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
        solved_rows = 0
        for i in range(0, 9):
            found_nums = 0
            for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if num in set(self.get_row(i)):
                    found_nums += 1
            if found_nums == 9:
                solved_rows += 1
        if solved_rows == 9:
            return True
        else:
            return False

    def check_col(self):
        solved_cols = 0
        for i in range(0, 9):
            found_nums = 0
            for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if num in set(self.get_col(i)):
                    found_nums += 1
            if found_nums == 9:
                solved_cols += 1
        if solved_cols == 9:
            return True
        else:
            return False

    def check_box(self):
        solved_boxes = 0
        for r in range(0, 3):
            for c in range(0, 3):
                found_nums = 0
                for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if num in set(self.get_box(r, c)):
                        found_nums += 1
                if found_nums == 9:
                    solved_boxes += 1
        if solved_boxes == 9:
            return True
        else:
            return False

    def check_board(self):
        if self.check_box and self.check_row and self.check_col:
            return True
        return False
        
