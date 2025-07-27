from game import Game

def main():
    print("Chao mung ban den voi Tik Tac Toe duoc thiet ke boi vmh")
    name1 = input("Hay nhap ten cua nguoi choi 1: ")
    name2 = input("Hay nhap ten cua nguoi choi 2: ")
    game = Game(name1,name2)
    game.play()

if __name__ == "__main__":
    main()
