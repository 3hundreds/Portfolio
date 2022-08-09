def great():
    print("Приветствуем вас в игре: ")
    print("-------------------------")
    print('"Крестики - нолики"')
    print("-------------------------")
    print("x,y - координаты для хода")


def show():
    print(f"  0 1 2")
    for i in range(3):
        row = " ".join(field[i])
        print(f"{i} {row}")

def ask():
    while True:
        cords = input("         Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите две координаты ")
            continue
        x,y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x,y = int(x),int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(f"Координаты {x}, {y} вне диапазона")
            continue
        if field[x][y] != " ":
            print(f"Клетка {x} {y} занята")
            continue
        return x, y

def win_check():
    for i in range(3):
        win = []
        for j in range(3):
            win.append(field[i][j])
        if win == ["X", "X", "X"]:
            return True
    for i in range(3):
        win = []
        for j in range(3):
            win.append(field[j][i])
        if win == ["X", "X", "X"]:
            return True

        win = []
        for i in range(3):
            win.append(field[i][i])
        if win == ["X", "X", "X"]:
            return True

        win = []
        for i in range(3):
            win.append(field[i][2 - i])
        if win == ["0", "0", "0"]:
            return False
        for i in range(3):
            win = []
            for j in range(3):
                win.append(field[i][j])
            if win == ["0", "0", "0"]:
                return False
        for i in range(3):
            win = []
            for j in range(3):
                win.append(field[j][i])
            if win == ["0", "0", "0"]:
                return False

            win = []
            for i in range(3):
                win.append(field[i][i])
            if win == ["0", "0", "0"]:
                return False

            win = []
            for i in range(3):
                win.append(field[i][2 - i])
            if win == ["0", "0", "0"]:
                return False
    return None

field = [[" "]*3 for i in range(3)]
great()
num = 0
while True:
    num += 1
    show()
    if win_check() == True:
        print("Выиграл крестик ")
        break
    if win_check() == False:
        print("Выиграл нолик")
        break
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x,y = ask()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if num == 9:
        print("Ничья!")
        break

