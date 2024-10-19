def create_board():
    return [['.' for _ in range(10)] for _ in range(10)]
def display_board(board):
    print('   ' + ' '.join(str(i) for i in range(10)))
    for row_index, row in enumerate(board):
        print(f'{row_index}  ' + ' '.join(row))
    print()
board = create_board()
def get_player_move(board):
    while True:
        try:
            row = int(input('Введите номер строки (0-9): '))
            col = int(input('Введите номер столбца (0-9): '))
            if row < 0 or row >= 10 or col < 0 or col >= 10:
                print('Координаты должны быть в пределах от 0 до 9.')
            elif board[row][col] != '.':
                print('Эта клетка уже занята. Попробуйте другую.')
            else:
                return row, col
        except ValueError:
            print('Введите число.')
def make_move(board, row, col, mark):
    board[row][col] = mark
def game_loop():
    current_player = 'X'
    while True:
        display_board(board)
        print(f'Ход игрока {current_player}:')
        row, col = get_player_move(board)
        make_move(board, row, col, current_player)
        if check_for_chain(board, row, col):
            print(f'Игрок {current_player} проиграл!')
            display_board(board)
            break
        current_player = 'O' if current_player == 'X' else 'X'
DIRECTIONS = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1),
    (1, -1), (1, 1)
]
def check_for_chain(board, row, col):
    if board[row][col] == '.':
        return False
    for dr, dc in DIRECTIONS:
        chain_length = 1
        r, c = row + dr, col + dc
        while 0 <= r < 10 and 0 <= c < 10 and board[r][c] != '.':
            chain_length += 1
            r += dr
            c += dc
        r, c = row - dr, col - dc
        while 0 <= r < 10 and 0 <= c < 10 and board[r][c] != ".":
            chain_length += 1
            r -= dr
            c -= dc
        if chain_length >= 3:
            return True
    return False
game_loop()