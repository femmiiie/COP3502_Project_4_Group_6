from cell import Cell

class Board:
    def __init__(self):
        self.board : list[list[Cell]] = []
        self.board_initialize()





    '''GETTERS FOR VALIDATION METHODS'''
    #Gets values from specified row as ints
    def get_row(self, num:int):
        lst = []
        for i in self.board[num]:
            if i.get_cell_value() == 0:
                lst.append(i.get_sketched_value())
            else:
                lst.append(i.get_cell_value())
        return lst

    