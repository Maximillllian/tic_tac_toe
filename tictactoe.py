# Игра в крестики нолики


def put_coord(field, mark):  # Функция отвечает за ввод координат
    while True:
        coords = input('Enter the coordinates: ').split()
        if len(coords) != 2:
            print('Enter two numbers!')
            continue
        coord_1 = coords[0]
        coord_2 = coords[1]
        if not coord_1.isnumeric() or not coord_2.isnumeric():
            print('You should enter numbers!')
            continue
        coord_1, coord_2 = int(coord_1), int(coord_2)
        if not (1 <= coord_1 <= 3) or not (1 <= coord_2 <= 3):
            print('Coordinates should be from 1 to 3!')
            continue
        coord_1 -= 1
        if field[-coord_2][coord_1] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        field[-coord_2][coord_1] = mark
        return


def result(field):  # Функция отвечает за проверку результата игры
    lst_string = [i for j in field for i in j]
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    winner = ''
    for i in win_coord:
        if lst_string[i[0]] == lst_string[i[1]] == lst_string[i[2]] and lst_string[i[0]] != '_':
            return f'{lst_string[i[0]]} wins'
    if not ('_' in lst_string):
        return 'Draw'
    return


def print_field(field):  # Функция отвечает за вывод игрового поля
    print('-' * 9)
    for i in field:
        print('| ', end='')
        for j in i:
            print(j, end=' ')
        print('|')
    print('-' * 9)


def tictactoe():  # Функция отвечает за сам процесс игры
    counter = 1
    user_field = [['_' for i in range(3)] for j in range(3)]
    print(result(user_field))
    print_field(user_field)
    while not result(user_field):
        mark = 'X'
        if counter % 2 == 0:
            mark = 'O'
        put_coord(user_field, mark)
        counter += 1
        print_field(user_field)
    print(result(user_field))


if __name__ == '__main__':
    tictactoe()
