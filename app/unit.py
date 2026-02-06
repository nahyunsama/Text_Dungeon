# 유닛 이동 구현

class Unit:
    # 플레이어와 몬스터의 공통 부모 클래스
    def __init__(self, name, hp, atk, dfs, row, col, icon):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfs = dfs
        self.row = row
        self.col = col
        self.icon = icon

class Player(Unit):
    # 플레이어 전용 클래스
    def __init__(self, name, hp, atk, dfs, row, col, icon):
        super().__init__(name, hp, atk, dfs, row, col, icon)
    
class Monster(Unit):
    # 몬스터 전용 클래스
    def __init__(self, name, hp, atk, dfs, row, col, icon):
        super().__init__(name, hp, atk, dfs, row, col, icon)