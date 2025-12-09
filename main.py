#TODO
#Need to check the fight function while

import random

def fight():
    player_HP = 100
    monster_HP = 100
    player_attack = 10
    monster_attack = 7
    player_defense = 1
    monster_defense = 1
    # alive var == 1: player alive
    # alive var == 2: monster alive
    # alive var == 3: both alive
    alive = 3
    wrong_count = 0
    while player_HP > 0 and monster_HP > 0:
        if wrong_count == 10:
            print("What's WRONG with YOU!")
            print("I'M OUT IT!")
            alive = 0
            break

        print(f"> player HP {player_HP}")
        print(f"> monster HP {monster_HP}")
        print("")
        print("> choice your action")
        print("> attack  : 1")
        print("> defense : 2")
        print("> Avoid   : 3")
        print("")
        print("")
        try:
            player_decision = int(input())
        except ValueError:
            print("WRONG INPUT!")
            print("")

            wrong_count = wrong_count + 1
            continue

        player_attack_weight = random.randrange(-2, 3)
        player_denfense_weight = random.randrange(-2, 3)
        monster_attack_weight = random.randrange(-2, 3)
        monster_denfense_weight = random.randrange(-2, 3)

        monster_defense_delta = monster_defense + monster_denfense_weight
        monster_attack_delta = monster_attack + monster_attack_weight
        player_defense_delta = player_defense + player_denfense_weight
        player_attack_delta = player_attack + player_attack_weight

        if player_decision == 1:
            print("player is attack")

            if player_attack_delta > monster_defense_delta:
                monster_HP = monster_HP + monster_defense_delta - player_attack_delta
                print(f"monster has gotten {player_attack_delta - monster_defense_delta} damage")
            else:
                print("monster defense is too high so take 1 damage")
                monster_HP = monster_HP - 1
            print("")

            print("monster is attack")
            if monster_attack_delta > player_defense_delta:
                player_HP = player_HP + player_defense_delta - monster_attack_delta
                print(f"player has gotten {monster_attack_delta - player_defense_delta} damage")
            else:
                print("player denfense is too high so take 1 damage")
                play_HP = player_HP - 1
            print("")

        elif player_decision == 2:
            print("player is denfense")
            if int(monster_attack_delta/2) > player_defense_delta:
                player_HP = player_HP + player_defense_delta - int(monster_attack_delta/2)
                print(f"player has gotten {int(monster_attack_delta/2) - player_defense_delta} damage")
            else:
                print("player denfense is too high so take 1 damage")
                play_HP = player_HP - 1
            print("")

        elif player_decision == 3:
            print("player is Avoid")
            player_avoid = random.randrange(1, 7)
            if player_avoid == 1:
                print("player avoid is success")
            else:
                print("player avoid is fail")
                if monster_attack_delta > player_defense_delta:
                    player_HP = player_HP + player_defense_delta - monster_attack_delta
                    print(f"player has gotten {monster_attack_delta - player_defense_delta} damage")
                else:
                    print("player denfense is too high so take 1 damage")
                    play_HP = player_HP - 1
            print("")
        else:
            print("please choice again")
        
        if player_HP > 0 and monster_HP > 0:
            alive = 3
        elif player_HP <= 0 and monster_HP > 0:
            alive = 2
        elif player_HP > 0 and monster_HP <= 0:
            alive = 1
        else:
            alive = 0
    return alive


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
    monster_x_y = [1,2]
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
            
        

        if monster_x_y[0] == user_x_y[0] and monster_x_y[1] == user_x_y[1]:
            print("Let's fight!!")
            alive = fight()

            if alive == 1:
                monster_x_y[0] = -1
                monster_x_y[1] = -1
                print("YOU WIN!")
                break
            elif alive == 2:
                print("Player Lose")
                break
            else:
                print ("GoodBYE!")
                break

        
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
