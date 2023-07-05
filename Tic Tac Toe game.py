import random

# Create an empty board
board = [' ' for _ in range(9)]

# Function to print the Tic Tac Toe board
def print_board():
    print('-------------')
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i+1], '|', board[i+2], '|')
        print('-------------')

# Function to check if any player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to perform the toss
def perform_toss(player1_name, player2_name):
    print("Performing a toss to determine who plays first...")
    toss_result = random.choice([player1_name, player2_name])
    print(toss_result + " won the toss and will play first!")
    return toss_result

# Function to play the game
def play_game(player1_name, player2_name):
    current_player = perform_toss(player1_name, player2_name)
    
    while True:
        print_board()
        move = int(input(current_player + ", enter your move (0-8): "))

        if board[move] == ' ':
            board[move] = 'X' if current_player == player1_name else 'O'
            
            if check_win(board[move]):
                print_board()
                print(current_player + " wins!")
                break
            elif is_board_full():
                print_board()
                print("It's a tie!")
                break

            current_player = player2_name if current_player == player1_name else player1_name
        else:
            print("Invalid move. Try again.")

# Prompt players for their names
player1_name = input("Enter the name of Player 1: ")
player2_name = input("Enter the name of Player 2: ")

# Start the game
play_game(player1_name, player2_name)
