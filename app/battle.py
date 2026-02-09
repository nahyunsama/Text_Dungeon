import random
WEIGHT_INT = (-2, 2)
AVOID_INT = (1, 6)
CRITICAL_MULTIPLIER = 2
DEFENSE_MULTIPLIER = 2
DEFENSE_HEALING = 8

class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.alive = 3
        # alive var == 0: both death
        # alive var == 1: player alive
        # alive var == 2: monster alive
        # alive var == 3: both alive


    def start_battle(self, stage):
        print("> Battle Start!")
        print(f"> {self.player.name} VS {self.monster.name}")
        print("")
        player_HP = self.player.hp
        player_attack = self.player.atk
        player_defense = self.player.dfs
        monster_HP = self.monster.hp
        monster_attack = self.monster.atk
        monster_defense = self.monster.dfs
        while self.alive == 3:
            print(f"> {self.player.name} HP: {player_HP}")
            print(f"> {self.monster.name} HP: {monster_HP}")
            print("")

            monster_decison = self.monster_decision(stage)
            match monster_decison:
                case 1:
                    print(f"> {self.monster.name} chose Attack")
                    print("")
                    self.Attack_phase(monster_attack, player_defense, player_HP, self.monster.name, self.player.name)
                case 2:
                    print(f"> {self.monster.name} chose Defense")
                    print("")
                    self.Defense_phase(player_attack, monster_defense, monster_HP, self.player.name, self.monster.name)
                case 3:
                    print(f"> {self.monster.name} chose Avoid")
                    print("")
                    self.Avoid_phase(monster_attack, monster_defense, player_attack, player_defense, self.monster.name, self.player.name)
            
            print("> Choose your action")
            print("> Attack   : 1")
            print("> Defense  : 2")
            print("> Avoid    : 3")
            print("")
            player_decision = int(input())
            print("")

            if player_decision not in [1,2,3]:
                print("> WRONG INPUT!")
                print("")
                return

            
            match player_decision:
                case 1:
                    self.Attack_phase(player_attack, monster_defense, monster_HP, self.player.name, self.monster.name)
                case 2:
                    self.Defense_phase(monster_attack, player_defense, player_HP, self.monster.name, self.player.name)
                case 3:
                    self.Avoid_phase(monster_attack, monster_defense, player_attack, player_defense, self.monster.name, self.player.name)            
            if player_HP <= 0 and monster_HP <= 0:
                print("> LOVE SHOT!")
                print("")
                self.alive = 0
                break
            elif player_HP <= 0:
                print("> DEFATED...")
                print("")
                self.alive = 2
                break
            elif monster_HP <= 0:
                print("> YOU WIN!")
                print("")
                self.alive = 1
                break

    def monster_decision(self, stage):
        if stage == 1:
            return 1
        else:
            return random.randint(1,3)

    def Attack_phase(self, attaker_attack, defender_defense, defender_HP, attaker_name, defender_name):
        print("> Attack phase")
        print("")

    def Defense_phase(self, attaker_attack, defender_defense, defender_HP, attaker_name, defender_name):
        print("> Defense phase")
        print("")

    def Avoid_phase(self, attacker_attack, attacker_defense, defender_attack, defender_defense, attacker_name, defender_name):
        print("> Avoid phase")
        print("")