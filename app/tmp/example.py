import random
import sys

class Unit:
    """플레이어와 몬스터의 공통 부모 클래스"""
    def __init__(self, name, hp, atk, dfs, row, col, icon):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.dfs = dfs
        self.row = row  # 세로 위치 (y)
        self.col = col  # 가로 위치 (x)
        self.icon = icon # 맵에 표시될 문자 (U, *)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(1, damage) # 최소 1의 데미지는 입음
        self.hp -= actual_damage
        return actual_damage

    def attack_target(self, target):
        # 랜덤 가중치 계산
        atk_weight = random.randrange(-2, 3)
        dfs_weight = random.randrange(-2, 3)
        
        final_atk = self.atk + atk_weight
        final_dfs = target.dfs + dfs_weight
        
        damage = final_atk - final_dfs
        if damage > 0:
            actual_dmg = target.take_damage(damage)
            print(f"{self.name} attacks! {target.name} took {actual_dmg} damage.")
        else:
            target.take_damage(1)
            print(f"{self.name} attacks but {target.name}'s defense is too high! (1 damage)")

class Map:
    """맵 데이터와 출력을 담당하는 클래스"""
    def __init__(self):
        # 초기 맵 설정
        self.grid = [
            ["=","=","=","=","="],
            ["="," "," "," ","="],
            ["="," "," "," ","="],
            ["=","=","=","=","="]
        ]
    
    def print_map(self, player, monster):
        # 맵을 출력할 때만 임시로 유닛들의 위치를 그려줍니다.
        # 원본 grid 데이터를 훼손하지 않기 위해 복사해서 출력하거나, 출력 시점에만 계산합니다.
        for r, row_list in enumerate(self.grid):
            line = ""
            for c, char in enumerate(row_list):
                if r == player.row and c == player.col:
                    line += player.icon
                elif r == monster.row and c == monster.col and monster.is_alive():
                    line += monster.icon
                else:
                    line += char
            print(line)

    def is_wall(self, row, col):
        # 맵 범위를 벗어나거나 벽(=)인 경우 True 반환
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]):
            return True
        return self.grid[row][col] == "="

class Game:
    """게임을 총괄하는 클래스"""
    def __init__(self):
        # 유닛과 맵 초기화
        self.player = Unit("Player", hp=100, atk=10, dfs=1, row=2, col=2, icon="U")
        self.monster = Unit("Monster", hp=100, atk=7, dfs=1, row=1, col=2, icon="*")
        self.game_map = Map()

    def battle(self):
        print("\n!!! ENCOUNTER !!! Let's Fight!")
        wrong_count = 0
        
        while self.player.is_alive() and self.monster.is_alive():
            if wrong_count >= 10:
                print("Too many wrong inputs! Game Over.")
                sys.exit()

            print(f"\n> {self.player.name} HP: {self.player.hp} / {self.monster.name} HP: {self.monster.hp}")
            print("1. Attack  2. Defense  3. Avoid")
            
            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Wrong Input!")
                wrong_count += 1
                continue

            # 플레이어 턴 처리
            if choice == 1: # Attack
                self.player.attack_target(self.monster)
            elif choice == 2: # Defense
                # 방어 로직 (단순화를 위해 여기서는 생략하거나 데미지 감소 로직 추가 가능)
                print("Player takes defensive stance.")
            elif choice == 3: # Avoid
                if random.randrange(1, 7) == 1:
                    print("Player avoided the attack!")
                    continue # 몬스터 턴 스킵
                else:
                    print("Avoid failed!")
            else:
                print("Please choose again")
                continue

            # 몬스터 턴 처리 (몬스터가 살아있다면)
            if self.monster.is_alive():
                # 간단하게 몬스터는 항상 공격한다고 가정 (원래 코드 로직 반영)
                self.monster.attack_target(self.player)

        # 전투 종료 처리
        if self.player.is_alive():
            print("YOU WIN!")
            self.monster.row = -1 # 맵에서 제거
        else:
            print("YOU DIED...")
            sys.exit()

    def move_player(self, direction):
        # 방향에 따른 변화량 (row, col)
        moves = {
            "1": (0, -1), # Left
            "2": (-1, 0), # Up
            "3": (1, 0),  # Down
            "4": (0, 1)   # Right
        }

        if direction in moves:
            d_row, d_col = moves[direction]
            new_row = self.player.row + d_row
            new_col = self.player.col + d_col

            if not self.game_map.is_wall(new_row, new_col):
                self.player.row = new_row
                self.player.col = new_col
            else:
                print("> Here is the wall!")
        else:
            print("Invalid direction.")

    def run(self):
        print("> Hello from text-dungeon (Refactored)!")
        print("> Game Start!\n")
        
        while True:
            self.game_map.print_map(self.player, self.monster)
            
            # 전투 조우 확인
            if self.player.row == self.monster.row and self.player.col == self.monster.col:
                if self.monster.is_alive():
                    self.battle()

            print("\n> Move: 1.Left 2.Up 3.Down 4.Right")
            move_input = input("Input: ")
            self.move_player(move_input)

if __name__ == "__main__":
    game = Game()
    game.run()