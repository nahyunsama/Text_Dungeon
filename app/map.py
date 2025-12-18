class Map:

    STAGE_1 = [["=","=","=","=","="],
               ["="," ","*"," ","="],
               ["="," ","U"," ","="],
               ["=","=","=","=","="]]

    STAGE_1_LORE = "Let's Tutrial"

    @staticmethod
    def map_print(map_list):
        print('\n'.join(map(''.join, map_list)))
