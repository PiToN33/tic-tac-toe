def display_board(board):
    print("\n"*100)
    
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("------")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("------")
    print(board[1] + "|" + board[2] + "|" + board[3])

def player_input():
    marker = " "
    while marker != "x" and marker != "o":
        marker = input("Player 1, choose x or o: ")
        player1 = marker
        if player1 == "x":
            player2 = "o"
        else:
            player2 = "x"
        return(player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return "PLayer1"
    else:
        return "Player2"

def space_check(board, position):
    board[position] == " "

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
        return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))
    
    return position

def replay():
    choice = input("PLay again? Enter Yes or No")
    return choice == "Yes"

print("Welcome to Tic Tac Toe!")

while True:
    board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game = input("Ready to play? y or n: ")
    if play_game == "y":
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == "Player1":
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display_board(board)
                print("Player1 has won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "Player2"
        else:
              if turn == "Player2":    
                    display_board(board)
                    position = player_choice(board)
                    place_marker(board, player2_marker, position)
            
              if win_check(board, player2_marker):
                display_board(board)
                print("Player2 has won")
                game_on = False
    else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is draw")
                    game_on = False
                else:
                    turn = "Player1"
                         
    if not replay():
        break