class Map:

    STAGE_1 = [["=","=","=","=","="],
                ["="," ","*"," ","="],
                ["="," ","U"," ","="],
                ["=","=","=","=","="]]

    STAGE_1_LORE = "Let's Tutrial"

    @staticmethod
    def unit_xy(stage):
        match stage:
            case 1:
                user_x = 2
                user_y = 2
                user_x_before = 0
                user_y_before = 0
                monster_x = 1
                monster_y = 2
                #user_xy_before = [0,0]
                #user_xy = [2,2]
                #monster_xy = [1,2]
        
        return user_x, user_y, user_x_before, user_y_before, monster_x, monster_y

    @staticmethod
    def map_print(map_list):
        print('\n'.join(map(''.join, map_list)))
