game_array: list[list[str]] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def ask_user_position(input_value: str) -> tuple[int,int]:
    is_valid = False
    while not is_valid:
        try:
            row_input = int(input(f'\n{input_value} which row(1-3)?: ')) - 1
            column_input = int(input(f'\n{input_value} which column(1-3)?: ')) - 1
            is_valid = True
        except:
            print("\nTry to put a number between (1-3)")
            continue
    return row_input, column_input


def add_value(input_value: str, row: int, column: int) -> bool:
    global game_array
    if game_array[row][column] == ' ':
        game_array[row][column] = input_value
        return True
    else:
        print('Place is occupied, try to put somewhere else.')
        return False


def write_game_table() -> None:
    for row_num in range(len(game_array)):
        row = game_array[row_num]
        for value in range(len(row)):
            if value != 2:
                print(row[value], '| ', end='')
            else:
                print(row[value], end='')
        if row_num != 2:
            print('\n----------')
    print('\n')


def write_on_table(input_value: str) -> None:
    is_available = False
    while not is_available:
        row_input, column_input = ask_user_position(input_value)
        try:
            is_available = add_value(input_value, row_input, column_input)
        except:
            print("\nTry to put a number between (1-3)")
            continue


def is_finished() -> bool:
    """Checks is game finished and who won"""
    global game_array
    for num in range(len(game_array)):
        if game_array[0][num] == game_array[1][num] and game_array[0][num] == game_array[2][num] and game_array[0][num] != ' ':
            print(f'\n{game_array[0][num]} won.')
            return True
        if game_array[num][0] == game_array[num][1] and game_array[num][0] == game_array[num][2] and game_array[num][0] != ' ':
            print(f'\n{game_array[num][0]} won.')
            return True

    if game_array[0][0] == game_array[1][1] and game_array[0][0] == game_array[2][2] and game_array[0][0] != ' ':
        print(f'{game_array[0][0]} won.')
        return True
    if game_array[0][2] == game_array[1][1] and game_array[0][2] == game_array[2][0] and game_array[0][2] != ' ':
        print(f'{game_array[0][2]} won.')
        return True


def main() -> None:
    counter = 0
    while True:
        counter += 1
        write_game_table()
        write_on_table('X')
        print("\n")
        write_game_table()
        if is_finished():
            break
        # If no one wins until there is no space left. Breaks the loop with message tie
        if counter == 5:
            print('Tie')
            break

        write_on_table('O')
        write_game_table()
        if is_finished():
            break
        print('\n')


if __name__ == '__main__':
    main()
