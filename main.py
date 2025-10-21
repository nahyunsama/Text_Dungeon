def map_print(map_list):
    print('\n'.join(map(''.join, map_list)))
    
def stage_1():
    print("> Let's Tutrial")
    stage_1_map = [["=","=","=","=","="],
                   ["="," ","*"," ","="],
                   ["="," ","U"," ","="],
                   ["=","=","=","=","="]]
    map_print(stage_1_map)
    user_x_y_before = [0,0]
    user_x_y = [2,2]
    print("")
    while(True):
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
            
                user_x_y_before = user_x_y.copy()
                user_x_y[1] = user_x_y[1] - 1
            
                if stage_1_map[user_x_y[0]][user_x_y[1]] != "=":
                    stage_1_map[user_x_y[0]][user_x_y[1]] = "U"
                    stage_1_map[user_x_y_before[0]][user_x_y_before[1]] = " "
                    user_x_y_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    user_x_y = user_x_y_before.copy()
                    user_x_y_before = [0, 0]

                map_print(stage_1_map)
            
            case "2":

                user_x_y_before = user_x_y.copy()
                user_x_y[0] = user_x_y[0] - 1
            
                if stage_1_map[user_x_y[0]][user_x_y[1]] != "=":
                    stage_1_map[user_x_y[0]][user_x_y[1]] = "U"
                    stage_1_map[user_x_y_before[0]][user_x_y_before[1]] = " "
                    user_x_y_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    user_x_y = user_x_y_before.copy()
                    user_x_y_before = [0, 0]

                map_print(stage_1_map)

            case "3":

                user_x_y_before = user_x_y.copy()
                user_x_y[0] = user_x_y[0] + 1
            
                if stage_1_map[user_x_y[0]][user_x_y[1]] != "=":
                    stage_1_map[user_x_y[0]][user_x_y[1]] = "U"
                    stage_1_map[user_x_y_before[0]][user_x_y_before[1]] = " "
                    user_x_y_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    user_x_y = user_x_y_before.copy()
                    user_x_y_before = [0, 0]

                map_print(stage_1_map)

            case "4":

                user_x_y_before = user_x_y.copy()
                user_x_y[1] = user_x_y[1] + 1
            
                if stage_1_map[user_x_y[0]][user_x_y[1]] != "=":
                    stage_1_map[user_x_y[0]][user_x_y[1]] = "U"
                    stage_1_map[user_x_y_before[0]][user_x_y_before[1]] = " "
                    user_x_y_before = [0, 0]
                else:
                    print("> Here is the wall!")
                    print("")
                    user_x_y = user_x_y_before.copy()
                    user_x_y_before = [0, 0]

                map_print(stage_1_map)
        
    
    

def main():
    print("> Hello from text-dungeon!")
    print("> Please Enter the 1 to start")
    print("")
    menu_string = str(input())
    if menu_string == "1":
        print("")
        print("> Game Start!")
        stage_1()


if __name__ == "__main__":
    main()
