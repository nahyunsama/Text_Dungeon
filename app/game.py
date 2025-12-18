from .map import Map

class Game:

    def __init__(self):
        self.stage = 0

    def input_move(self):
        print("> choice your move")
        print("> left  : 1")
        print("> up    : 2")
        print("> down  : 3")
        print("> right : 4")
        print("")
        move_string = str(input())
        print("")

    def run(self):
        while True:
            if self.stage == 0:
                print("> Hello from text-dungeon!")
                print("> PRESS ANY KEY")
                print("")
                input()
            
                print("")
                print("> Game Start!")
                self.stage = 1
            elif self.stage == 1:
                self.map = Map.STAGE_1
                self.lore = Map.STAGE_1_LORE
                print(self.lore)
                Map.map_print(self.map)
                self.input_move()


