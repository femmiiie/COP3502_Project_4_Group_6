from cell import Cell

class Board:
    def __init__(self):
        self.board : list[list[Cell]] = []
        self.board_initialize()





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
        