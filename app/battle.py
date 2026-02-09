import random

class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.alive = 3
        # alive var == 0: both death
        # alive var == 1: player alive
        # alive var == 2: monster alive
        # alive var == 3: both alive

    def start_battle(self):
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
                    self.attack_phase(player_attack, player_defense, monster_attack, monster_defense)
                case 2:
                    self.Defense_phase(player_attack, player_defense, monster_attack, monster_defense)
                case 3:
                    self.Avoid_phase(player_attack, player_defense, monster_attack, monster_defense)
            
            if player_HP <= 0 and monster_HP <= 0:
                print("> LOVE SHOT!")
                self.alive = 0
                break
            elif player_HP <= 0:
                print("> DEFATED...")
                self.alive = 2
                break
            elif monster_HP <= 0:
                print("> YOU WIN!")
                self.alive = 1
                break

    def attack_phase(self, player_attack, player_defense, monster_attack, monster_defense):
        print("> Attack phase")
    def Defense_phase(self, player_attack, player_defense, monster_attack, monster_defense):
        print("> Defense phase")
    def Avoid_phase(self, player_attack, player_defense, monster_attack, monster_defense):
        print("> Avoid phase")