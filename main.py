# Define the game board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win
def check_win(player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to handle player moves
def player_move(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9) or 'q' to quit: ")
        if move.lower() == 'q':
            print(f"Player {player} has quit the game.")
            return False
        try:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = player
                return True
            else:
                print("This spot is already taken.")
        except (IndexError, ValueError):
            print("Invalid move. Please enter a number between 1 and 9 or 'q' to quit.")

# Main game loop
def main():
    current_player = 'X'
    while True:
        print_board()
        if not player_move(current_player):
            break
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
