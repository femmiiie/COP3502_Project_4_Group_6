

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched = 0
    
    #Sets Definite Value of cell
    def set_cell_value(self, value):
        self.value = value

    #Sets User Inputted Value of cell
    def set_sketched_value(self, value):
        self.sketched = value
    
    def draw(self):
        pass

    