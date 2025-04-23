def print_board(b):
    for row in b:
        print(' '.join(row))

def check_winner(b):
    lines = b + list(map(list, zip(*b))) + [[b[i][i] for i in range(3)], [b[i][2-i] for i in range(3)]]
    for line in lines:
        if line == ['X']*3: return 'X'
        if line == ['O']*3: return 'O'
    return 'D' if all(c in 'XO' for row in b for c in row) else None

def minimax(b, is_max):
    winner = check_winner(b)
    if winner: return {'X': -1, 'O': 1, 'D': 0}[winner], None
    best = (-2, None) if is_max else (2, None)
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'O' if is_max else 'X'
                score, _ = minimax(b, not is_max)
                b[i][j] = ' '
                if (is_max and score > best[0]) or (not is_max and score < best[0]):
                    best = (score, (i, j))
    return best

def play():
    board = [[' '] * 3 for _ in range(3)]
    while True:
        print_board(board)
        r, c = map(int, input("Enter row col (0-2): ").split())
        if board[r][c] != ' ':
            print("Invalid move."); continue
        board[r][c] = 'X'
        if check_winner(board): break
        _, move = minimax(board, True)
        if move: board[move[0]][move[1]] = 'O'
        if check_winner(board): break
    print_board(board)
    print("Winner:", check_winner(board))

play()
