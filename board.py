from cell import Cell

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[Cell(0, i, j) for i in range(width)] for j in range(height)]
        self.selected_cell = (0, 0)

    # Draws the board
    def draw(self):
        cell_size = 50
        bold_line_width = 3
        normal_line_width = 1
        margin = 10

        for i in range(self.width + 1):
            if i % 3 == 0:
                line_width = bold_line_width
            else:
                line_width = normal_line_width

            pygame.draw.line(self.screen, (0, 0, 0), (margin + i * cell_size, margin),
                             (margin + i * cell_size, margin + self.height * cell_size), line_width)

        for j in range(self.height + 1):
            if j % 3 == 0:
                line_width = bold_line_width
            else:
                line_width = normal_line_width

            pygame.draw.line(self.screen, (0, 0, 0), (margin, margin + j * cell_size),
                             (margin + self.width * cell_size, margin + j * cell_size), line_width)
            
        for i in range(self.width):
            for j in range(self.height):
                cell = self.cells[i][j]
                cell_rect = pygame.Rect(margin + i * cell_size, margin + j * cell_size, cell_size, cell_size)

                if cell.original:
                    pygame.draw.rect(self.screen, (200, 200, 200), cell_rect)
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), cell_rect)

                if cell.value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(cell.value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=cell_rect.center)
                    self.screen.blit(text, text_rect)

                # Draw sketch if available
                if cell.sketch:
                    sketch_font = pygame.font.Font(None, 18)
                    sketch_text = sketch_font.render(str(cell.sketch), True, (150, 150, 150))
                    sketch_text_rect = sketch_text.get_rect(topleft=(cell_rect.left + 5, cell_rect.top + 5))
                    self.screen.blit(sketch_text, sketch_text_rect)

        pygame.display.flip()
            
    #Marks boards
    def select(self, row, col):
        self.selected_cell = (row, col)

    #Clicks or returns none
    def click(self, x, y):
        cell_size = 50
        margin = 10

        if margin <= x <= margin + self.width * cell_size and margin <= y <= margin + self.height * cell_size:
            row = (x - margin) // cell_size
            col = (y - margin) // cell_size
            return int(row), int(col)
        else:
            return None
    
    #Clears the cells
    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].value = 0

    #Sketches the cells
    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].sketch = value

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

    
    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        pass

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
        
