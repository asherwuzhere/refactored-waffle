import random

ROWS = 6
COLS = 7

# Initialize the board
def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

# Print the board
def print_board(board, first_move=False):
    for row in board:
        print(" | ".join(row))
    print("-" * (COLS * 4 - 1))
    if first_move:
        print("  ".join(map(str, range(1, COLS + 1))))

# Check if a column is not full
def is_valid_move(board, col):
    return board[0][col] == " "

# Drop a piece into the board
def drop_piece(board, col, piece):
    for row in reversed(range(ROWS)):
        if board[row][col] == " ":
            board[row][col] = piece
            return row, col
    return None

# Check for a win condition
def check_winner(board, piece):
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    # Check positively sloped diagonals
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    # Check negatively sloped diagonals
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    return False

# Get available columns
def get_valid_moves(board):
    return [c for c in range(COLS) if is_valid_move(board, c)]

# Check if the opponent has 3 in a row and can win next turn
def find_blocking_move(board, human):
    for col in get_valid_moves(board):
        temp_board = [row[:] for row in board]
        drop_piece(temp_board, col, human)
        if check_winner(temp_board, human):
            return col
    return None

# Check if the bot can win immediately
def find_winning_move(board, bot):
    for col in get_valid_moves(board):
        temp_board = [row[:] for row in board]
        drop_piece(temp_board, col, bot)
        if check_winner(temp_board, bot):
            return col
    return None

# Bot move logic
def bot_move(board, human, bot):
    win_move = find_winning_move(board, bot)
    if win_move is not None:
        return win_move
    block_move = find_blocking_move(board, human)
    if block_move is not None:
        return block_move
    valid_moves = get_valid_moves(board)
    central_moves = [c for c in [3, 4, 5, 2, 1, 6, 0] if c in valid_moves]
    return random.choice(central_moves)

# Play the game
def play_connect_four():
    board = create_board()
    human = "X"
    bot = "O"
    
    print("Welcome to Connect Four!")
    print_board(board, first_move=True)
    
    for turn in range(ROWS * COLS):
        if turn % 2 == 0:
            move = int(input("Enter your move (1-7): ")) - 1
            while move not in get_valid_moves(board):
                print("Invalid move, try again.")
                move = int(input("Enter your move (1-7): ")) - 1
            drop_piece(board, move, human)
        else:
            move = bot_move(board, human, bot)
            print(f"Bot chooses column {move + 1}")
            drop_piece(board, move, bot)
        
        print_board(board)
        
        if check_winner(board, human):
            print("You win!")
            return
        elif check_winner(board, bot):
            print("Bot wins!")
            return
    
    print("It's a draw!")

if __name__ == "__main__":
    play_connect_four()
