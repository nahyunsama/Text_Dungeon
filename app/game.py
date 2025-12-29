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
        match move_string:
            case "1":
                self.user_xy_before = self.user_xy
                self.user_xy[1] = self.user_xy[1] - 1
                if self.map[self.user_xy[0]][self.user_xy[1]] != "=":
                    self.map[self.user_xy[0]][self.user_xy[1]] = "U"
                    self.map[self.user_xy_before[0]][self.user_xy_before[1]] = " "
                    self.user_xy_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    self.user_xy = self.user_xy_before.copy()
                    self.user_xy_before = [0, 0]
            
            case "2":
                self.user_xy_before = self.user_xy.copy()
                self.user_xy[0] = self.user_xy[0] - 1
                if self.map[self.user_xy[0]][self.user_xy[1]] != "=":
                    self.map[self.user_xy[0]][self.user_xy[1]] = "U"
                    self.map[self.user_xy_before[0]][self.user_xy_before[1]] = " "
                    self.user_xy_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    self.user_xy = self.user_xy_before.copy()
                    self.user_xy_before = [0, 0]

            case "3":
                self.user_xy_before = self.user_xy.copy()
                self.user_xy[0] = self.user_xy[0] + 1
                if self.map[self.user_xy[0]][self.user_xy[1]] != "=":
                    self.map[self.user_xy[0]][self.user_xy[1]] = "U"
                    self.map[self.user_xy_before[0]][self.user_xy_before[1]] = " "
                    self.user_xy_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    self.user_xy = self.user_xy_before.copy()
                    self.user_xy_before = [0, 0]

            case "4":
                self.user_xy_before = self.user_xy.copy()
                self.user_xy[1] = self.user_xy[1] + 1
                if self.map[self.user_xy[0]][self.user_xy[1]] != "=":
                    self.map[self.user_xy[0]][self.user_xy[1]] = "U"
                    self.map[self.user_xy_before[0]][self.user_xy_before[1]] = " "
                    self.user_xy_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    self.user_xy = self.user_xy_before.copy()
                    self.user_xy_before = [0, 0]
        return self.user_xy, self.user_xy_before

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
                (self.user_x, self.user_y, self.user_x_before, self.user_y_before,
                 self.monster_x, self.monster_y)= Map.unit_xy(self.stage)
                Map.map_print(self.map)
                self.input_move()


