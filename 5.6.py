first_player = input("Игрок №1, как вас зовут? ")
second_player = input("Игрок №2, как вас зовут? ")

def hello():
    print("-------------------")
    print(f" Привет, {first_player} и {second_player}! Давайте играть в 'крестики-нолики'! ")
    print(f" {first_player}, Вы играете крестиками, а Вы, {second_player} - ноликами!")
    print("-------------------")

def show():
    print(f"    0 * 1 * 2")
    for i in range(3):
        print(f"{i} * {game[i][0]} * {game[i][1]} * {game[i][2]} *")
    print()

def play():
    while True:
        cords = input("ваш ход: ").split()
        print()

        if len(cords) != 2:
            print("для продолжения игры нужны две координаты, попробуйте снова")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("координаты должны быть числами, попробуйте снова")
            continue

        x, y = int(x), int(y)

        if x<0 or x>2 or y<0 or y>2:
            print("ячейки игрового поля от 0 до 2, попробуйте снова")
            continue

        if game[x][y] != ' ':
            print("ячейка поля уже занята, попробуйте снова")
            continue

        return x, y

def win():
    win_combination = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_combination:
        symbols = []
        for c in cord:
            symbols.append(game[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(f"Выиграл {first_player}!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f"Выиграл {second_player}!")
            return True
    return False

hello()
game = [[' '] * 3 for i in range (3)]
count = 0
while count != 10:
    count += 1
    show()
    if count % 2 == 0:
        print(f" {second_player}, ")
    else:
        print(f" {first_player}, ")

    x, y = play()

    if count % 2 == 0:
        game[x][y] = "0"
    else:
        game[x][y] = "Х"

    if win():
        break

    if count == 9:
        print("Ничья!")
        break