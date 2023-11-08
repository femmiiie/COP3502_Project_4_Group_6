
#Class for a singular cell in the sudoku board
#If the cell does not have a given value then value will be 0
#Sketched and Value should never both have a real value at the same time
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched = 0
    
    #Gets Definite Value of cell
    def get_cell_value(self):
        return self.value

    #Sets Definite Value of cell
    def set_cell_value(self, value):
        self.value = value
    
    #Gets Sketched Value of cell
    def get_sketched_value(self):
        return self.sketched

    #Sets User Inputted Value of cell
    def set_sketched_value(self, value):
        self.sketched = value
    
    def draw(self):
        pass

    