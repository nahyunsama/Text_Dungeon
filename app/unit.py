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
    
    def get_next_pos(self, direction):
        # left: 1, up: 2, down: 3, right: 4
        match direction:
            case "1":
                return self.row, self.col -1
            case "2":
                return self.row -1, self.col
            case "3":
                return self.row +1, self.col
            case "4":
                return self.row, self.col +1
            
    def move(self, row, col):
        self.row = row
        self.col = col
    
class Player(Unit):
    # 플레이어 전용 클래스
    def __init__(self, name, hp, atk, dfs, row, col, icon):
        super().__init__(name, hp, atk, dfs, row, col, icon)
    
class Monster(Unit):
    # 몬스터 전용 클래스
    def __init__(self, name, hp, atk, dfs, row, col, icon):
        super().__init__(name, hp, atk, dfs, row, col, icon)