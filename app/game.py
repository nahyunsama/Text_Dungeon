## TODO: User input vaildation, game over, multiple stages, avoid logic, monster AI, Serveral monsters

from .map import Map
from .unit import Player, Monster
from .battle import Battle

class Game:

    def __init__(self):
        self.stage = 0
        self.init_flag = 0
        self.map_manager = Map()
        self.invalid_input = 0

        self.player = Player("Player", hp=100, atk=15, dfs=2, row=2, col=2, icon="U")
        self.monster = Monster("Monster", hp=120, atk=10, dfs=3, row=1, col=2, icon="M")

    def input_move(self):
        print("> choice your move")
        print("> left  : 1")
        print("> up    : 2")
        print("> down  : 3")
        print("> right : 4")
        print("")
        move_string = str(input())
        print("")
        if move_string not in ["1","2","3","4"]:
            print("> WRONG INPUT!")
            print("")
            self.invalid_input = self.invalid_input + 1
            if self.invalid_input > 10:
                print("> What's wrong with you?")
                print("I'm out!")
                exit()
            return
        next_row, next_col = self.player.get_next_pos(move_string)
        if not self.map_manager.is_wall(next_row, next_col):
            prev_row, prev_col = self.player.row, self.player.col
            self.player.move(next_row, next_col)
            self.map_manager.update_map(prev_row, prev_col, next_row, next_col, self.player.icon)
        else:
            print("> Here is the wall!")
            print("")
        
        if self.player.row == self.monster.row and self.player.col == self.monster.col:
            self.invalid_input = 0
            print("> Welcome to Enter the Dungeon!")
            print("")
            battle = Battle(self.player, self.monster)
            Victory = battle.start_battle(self.stage)
            if Victory:
                self.stage = 2
            else:
                exit()



    def run(self):
        while True:
            if self.stage == 0:
                print("> Hello from Text-Dungeon!")
                print("> PRESS ANY KEY")
                print("")
                input()
                print("")
                print("> Game Start!")
                self.stage = 1
                self.init_flag = 1
            elif self.stage == 1:
                if self.init_flag == 1:
                    self.lore = Map.STAGE_1_LORE
                    print(self.lore)
                    self.map_manager.update_map(self.player.row, self.player.col, self.player.row, self.player.col,self.player.icon)
                    self.map_manager.update_map(self.monster.row, self.monster.col, self.monster.row, self.monster.col,self.monster.icon)
                    self.init_flag = 0
                else:
                    self.map_manager.show()
                    self.input_move()
            elif self.stage == 2:
                print("> Congratulations! You cleared the game!")
                exit()


