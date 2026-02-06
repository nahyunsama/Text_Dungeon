import copy

class Map:

    STAGE_1 = [["=","=","=","=","="],
                ["="," "," "," ","="],
                ["="," "," "," ","="],
                ["=","=","=","=","="]]

    STAGE_1_LORE = "Let's Tutrial"

    def __init__(self):
        self.grid = copy.deepcopy(self.STAGE_1)
    
    def is_wall(self, row, col):
        if self.grid[row][col] == "=":
            return True
        else:
            return False
    
    def update_map(self, prev_row, prev_col, new_row, new_col, icon):
        self.grid[prev_row][prev_col] = " "
        self.grid[new_row][new_col] = icon

    def show(self):
        print('\n'.join(map(''.join, self.grid)))