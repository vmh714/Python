class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.fill = 0
    def display(self):
        print(f"   0   1   2\n")
        for i, row in enumerate(self.grid):
            row_str = f"{i}  " + " | ".join(row)
            print(row_str)
            if i < 2:
                print("  ---+---+---  ")
    def update(self, row:int, col:int, symbol:str):
        self.grid[row][col] = symbol
        self.fill += 1
    def check_winner(self):
        lines = []                                         #khai bao list chua cac duong:doc, ngang, cheo
        lines.extend(self.grid)                                 #them cac duong ngang - theo hang
        for col in range(3):                                              #them cac duong doc - theo cot
            collum = [self.grid[row][col] for row in range(3)]
            lines.append(collum)
        #them cac duong cheo
        diag1 = [self.grid[i][i] for i in range(3)]
        diag2 = [self.grid[i][2-i] for i in range(3)]
        lines.append(diag1)
        #kiem tra tung duong xem co cac ki tu trung nhau khong
        lines.append(diag2)
        for line in lines:
            if line[0] != ' ' and line.count(line[0]) == 3:
                return line[0] #tra ve X hoac O

        return None
    def is_full(self):
        return self.fill == 9
    def is_empty(self, row:int, col:int):
        return self.grid[row][col] == ' '
'''
b = Board()
b.update(0,1,'X')
b.update(1,1,'O')
b.update(0,0,'X')
b.update(0,2,'X')
b.update(1,2,'O')

b.display()
print(b.check_winner())
print(b.is_full())
'''
