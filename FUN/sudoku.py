NO_OF_ROWS = 9
NO_OF_COLUMNS = 9
POSSIBILITIES = []
SETS = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def get_values(row, column):
    final_list = []
    row_set = []
    column_set = []

    temp_row = GAME[row]
    for val in temp_row:
        if val != 0:
            final_list.append(val)

    for i in range(NO_OF_ROWS):
        val = GAME[i][column]
        if val != 0:
            final_list.append(val)

    for i in SETS:
        if row in i:
            row_set = i

    for i in SETS:
        if column in i:
            column_set = i

    for r in row_set:
        for c in column_set:
            val = GAME[r][c]
            if val != 0:
                final_list.append(val)

    final_list.sort()
    res = [*set(final_list)]
    return res


def check_unique(row, column, value):
    flag = 1
    row_set = []
    column_set = []

    row_list = POSSIBILITIES[row]
    for n in range(NO_OF_ROWS):
        if n != column:
            lis = row_list[n]
            if value in lis:
                flag = 0

    for n in range(NO_OF_ROWS):
        if n != row:
            column_list = POSSIBILITIES[n][column]
            if value in column_list:
                flag = 0

    for i in SETS:
        if row in i:
            row_set = i

    for i in SETS:
        if column in i:
            column_set = i

    for r in row_set:
        for c in column_set:
            if r != row or c != column:
                temp = POSSIBILITIES[r][c]
                if value in temp:
                    flag = 0

    return flag


def initialize_possible():
    for _ in range(NO_OF_ROWS):
        POSSIBILITIES.append(list('0'*NO_OF_COLUMNS))

    for row in range(NO_OF_ROWS):
        for column in range(NO_OF_COLUMNS):
            POSSIBILITIES[row][column] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def initial_values(lis):
    row = lis[0] - 1
    column = lis[1] - 1
    value = lis[2]
    GAME[row][column] = value


def filter_input(string):
    a, b, c = map(int, string.strip().split(' '))
    return [a, b, c]


def list_possible():
    for row in range(NO_OF_ROWS):
        for column in range(NO_OF_COLUMNS):
            if GAME[row][column] == 0:
                values = get_values(row, column)
                for i in values:
                    if i in POSSIBILITIES[row][column]:
                        POSSIBILITIES[row][column].remove(i)
            else:
                POSSIBILITIES[row][column] = []


def update(row, column):
    if GAME[row][column] == 0:
        values = get_values(row, column)
        for i in values:
            if i in POSSIBILITIES[row][column]:
                POSSIBILITIES[row][column].remove(i)
    else:
        POSSIBILITIES[row][column] = []


def play():
    for row in range(NO_OF_ROWS):
        for column in range(NO_OF_COLUMNS):
            lis = POSSIBILITIES[row][column]
            length = len(lis)
            if length == 0:
                pass
            elif length == 1:
                value = POSSIBILITIES[row][column][0]
                GAME[row][column] = value
                POSSIBILITIES[row][column] = []


def print_game():
    for row in range(NO_OF_ROWS):
        if (row+1) % 3 != 0:
            string = ''
            for column in range(NO_OF_COLUMNS):
                if (column+1) % 3 != 0:
                    if GAME[row][column] == 0:
                        string += '\u001b[91m0 '
                    else:
                        string += f'\u001b[92m{GAME[row][column]} '
                else:
                    if GAME[row][column] == 0:
                        string += '\u001b[91m0 \u001b[97m| '
                    else:
                        string += f'\u001b[92m{GAME[row][column]} \u001b[97m| '
            print(string.strip())
        else:
            string = ''
            for column in range(NO_OF_COLUMNS):
                if (column+1) % 3 != 0:
                    if GAME[row][column] == 0:
                        string += '\u001b[91m0 '
                    else:
                        string += f'\u001b[92m{GAME[row][column]} '
                else:
                    if GAME[row][column] == 0:
                        string += '\u001b[91m0 \u001b[97m| '
                    else:
                        string += f'\u001b[92m{GAME[row][column]} \u001b[97m| '
            print(string.strip())
            print('-'*23)


def repeat(k):
    for _ in range(k):
        list_possible()
        play()
        list_possible()

    print_game()


def main():
    change = input('change: ')

    if change == 'stop':
        pass

    elif change != 'no':
        initial_values(filter_input(change))
        iterations = int(input('Enter no of iterations: '))
        repeat(iterations)
        main()

    else:
        iterations = int(input('Enter no of iterations: '))
        repeat(iterations)
        main()


GAME = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]

if __name__ == '__main__':
    initialize_possible()
    main()

"""            elif length > 1:
                for val in lis:
                    proceed = check_unique(row, column, val)
                    if proceed == 1:
                        GAME[row][column] = val
                        POSSIBILITIES[row][column].remove(val)"""

"""    for i in range(NO_OF_ROWS):
        string = input(f'line{i+1}: ')
        for index in range(NO_OF_COLUMNS):
            GAME[i][index] = int(string[index])"""