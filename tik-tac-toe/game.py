from board import Board
from player import Player
class Game:
    def __init__(self, name1: str, name2: str):
        self.board = Board()
        self.players = [Player(name1, "X"), Player(name2, "O")]
        self.current_turn = 0
    def get_move(self):
        while True:
            try:
                row_str, col_str = input("Hãy nhập tọa độ ô bạn muốn đi (ví dụ: 1 2): ").split(" ")
                row, col = int(row_str), int(col_str)
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if self.board.is_empty(row, col):
                        break
                    else:
                        print("Toa do tren da duoc dien roi, hay dien lai")
                else:
                    print("Tọa độ ngoài phạm vi! Vui lòng nhập lại.")
            except ValueError:
                print("Sai định dạng! Vui lòng nhập lại theo cú pháp: X(space)Y")
        return row, col
    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        while True:
            self.board.display()
            print(f"Dang la luot choi cua: {self.players[self.current_turn].name} ({self.players[self.current_turn].symbol})")
            row, col = self.get_move()
            self.board.update(row, col, self.players[self.current_turn].symbol)
            if self.board.is_full():
                self.board.display()
                print("Tran dau da ket thuc voi ket qua Hoa")
                break
            elif self.board.check_winner() != None:
                self.board.display()
                print(f"Xin chuc mung {self.players[self.current_turn].name} ({self.players[self.current_turn].symbol}) da chien thang")
                break
            else:
                self.switch_turn()

