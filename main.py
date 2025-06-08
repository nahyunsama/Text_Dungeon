def map_print(map_list):
    print('\n'.join(map(''.join, map_list)))
    
def stage_1():
    print("> Let's Tutrial")
    stage_1_map = [["=","=","=","=","="],
                   ["="," ","*"," ","="],
                   ["="," ","U"," ","="],
                   ["=","=","=","=","="]]
    map_print(stage_1_map)
    user_coordinate_before = [0,0]
    user_coordinate = [2,2]
    print("")
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
            
            user_coordinate_before = user_coordinate.copy()
            user_coordinate[1] = user_coordinate[1] - 1
            
            if stage_1_map[user_coordinate[0]][user_coordinate[1]] != "=":
                stage_1_map[user_coordinate[0]][user_coordinate[1]] = "U"
                stage_1_map[user_coordinate_before[0]][user_coordinate_before[1]] = " "
                user_coordinate_before = [0, 0]
            else:
                print("> Here is the wall!")
                user_coordinate = user_coordinate_before.copy()
                user_coordinate_before = [0, 0]

            map_print(stage_1_map)
            
        # case "2":

        # case "3":

        # case "4":

    
    

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
