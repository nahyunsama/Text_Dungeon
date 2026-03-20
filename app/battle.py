import random

WEIGHT_INT = (-4, 4)
AVOID_INT = (1, 6)
CRITICAL_MULTIPLIER = 2
DEFENSE_MULTIPLIER = 0.5
DEFENSE_SUCCESS_RATE = 0.3
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
        self.player_stun = False
        self.monster_stun = False
        self.player_extra_turn = False
        self.monster_extra_turn = False


    def start_battle(self, stage):
        print("> Battle Start!")
        print(f"> {self.player.name} VS {self.monster.name}")
        print("")
        while self.alive == 3:
            print(f"> {self.player.name} HP: {self.player.hp}")
            print(f"> {self.monster.name} HP: {self.monster.hp}")
            print("")

            monster_decison = self.monster_decision(stage)
            if self.monster_stun:
                print(f"> {self.monster.name} is Stunned and cannot move!")
                print("")
                self.monster_stun = False
            elif self.monster_extra_turn:
                self.monster_extra_turn = False
            else:
                match monster_decison:
                    case 1:
                        print(f"> {self.monster.name} chose Attack")
                        print("")
                        self.Attack_phase(self.monster, self.player)
                    case 2:
                        print(f"> {self.monster.name} chose Defense")
                        print("")
                        self.Defense_phase(self.monster, self.player)
                    case 3:
                        print(f"> {self.monster.name} chose Avoid")
                        print("")
                        self.Avoid_phase(self.monster, self.player)
            
            print(f"> {self.player.name} HP: {self.player.hp}")
            print(f"> {self.monster.name} HP: {self.monster.hp}")
            print("")
            
            if self.player.hp <= 0:
                print("> DEFATED...")
                print("")
                self.alive = 2
                return False

            if self.player_stun:
                print(f"> {self.player.name} is Stunned and cannot move!")
                print("")
                self.player_stun = False
            elif self.player_extra_turn:
                self.player_extra_turn = False
            else:
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
                        self.Attack_phase(self.player, self.monster)
                    case 2:
                        self.Defense_phase(self.player, self.monster)
                    case 3:
                        self.Avoid_phase(self.player, self.monster)

            if self.monster.hp <= 0:
                print("> YOU WIN!")
                print("")
                self.alive = 1
                return True

    def monster_decision(self, stage):
        if stage == 1:
            return 1
        else:
            return random.randint(1,3)

    def Attack_phase(self, actor, target):

        print("> Attack phase")
        print("")
        print(f"> {actor.name} attack: {target.name}")
        print(f"> {actor.name} attack power: {actor.atk}")
        print(f"> {target.name} defense power: {target.dfs}")
        weight = random.randint(WEIGHT_INT[0], WEIGHT_INT[1])
        print(f"> Attack weight: {weight}")
        print("")
        damage = max(actor.atk + weight - target.dfs, 1)
        print(f"> Attacker damage: {damage}")
        target.hp -= damage
        print(f"> {target.name} HP: {target.hp}")
        print("")
        print("================================")

    def Defense_phase(self, actor, target):
        print("> Defense phase")
        print("")
        print(f"> {actor.name} defense: {target.name}")
        print(f"> {actor.name} defense power: {actor.dfs}")
        print(f"> {target.name} attack power: {target.atk}")
        defense_success = random.random() < DEFENSE_SUCCESS_RATE
        if defense_success:
            print(f"> {actor.name} successfully defended!")
            actor.hp += int(DEFENSE_HEALING)
            print(f"> {actor.name} HP: {actor.hp}")
            print(f"> {target.name} got Stunned!")
            if actor == self.player:
                self.monster_stun = True
            else:
                self.player_stun = True
        else:
            print(f"> {actor.name} failed to defend!")
            damage = int(target.atk * DEFENSE_MULTIPLIER)
            print(f"> {target.name} attack damage: {damage}")
            actor.hp -= damage
            print(f"> {actor.name} HP: {actor.hp}")
        print("")
        print("================================")

    def Avoid_phase(self, actor, target):
        print("> Avoid phase")
        print("")
        print(f"> {actor.name} avoid: {target.name}")
        if actor == self.player:
            print("> choice: 1 ~ 6")
            input_int = int(input())
            if input_int not in range(1,7):
                print("> WRONG INPUT!")
                print("")
                return
        else:
            input_int = random.randint(AVOID_INT[0], AVOID_INT[1])
        
        avoid_target = random.randint(AVOID_INT[0], AVOID_INT[1])
        print(f"> DICE: {avoid_target}")
        if input_int == avoid_target:
            print(f"> {actor.name} successfully avoided!")
            print(f"> {actor.name} attack CRITICAL!")
            damage = actor.atk * CRITICAL_MULTIPLIER
            print(f"> {actor.name} attack damage: {damage}")
            target.hp -= damage
            print(f"> {target.name} HP: {target.hp}")
            if actor == self.player:
                self.monster_extra_turn = True
            else:
                self.player_extra_turn = True

        elif abs(input_int - avoid_target) == 1:
            print(f"> {actor.name} closely avoided!")
            if actor == self.player:
                self.monster_extra_turn = True
            else:
                self.player_extra_turn = True
        else:
            print(f"> {actor.name} failed to avoid!")
            print(f"> {actor.name} lost the balance")
            print(f"> {target.name} attack: {actor.name}")
            print(f"> {target.name} attack damage: {target.atk}")
            weight = random.randint(WEIGHT_INT[0], WEIGHT_INT[1])
            print(f"> Attack weight: {weight}")
            damage = target.atk + weight
            print(f"> {target.name} attack damage: {damage}")
            actor.hp -= damage
            print(f"> {actor.name} HP: {actor.hp}")
            if actor == self.player:
                self.monster_extra_turn = True
        
        print("")
        print("================================")