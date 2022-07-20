board=[" "for i in range(9)]
player="X"
a="It's {} turn, Select a place 1-9: "
game=True
def print_board():
    line="{0} | {1} | {2}"
    horizon_line="----------"
    for x in range(1,6):
        if x==1:
            print(line.format(board[0],board[1],board[2]))
        elif x==3:
            print(line.format(board[3],board[4],board[5]))
        elif x==5:
            print(line.format(board[6],board[7],board[8]))
        else:
            print(horizon_line)
def player_input(board):
    global player
    player_input_=input(a.format(player))
    if player_input_.isnumeric() and 1 <= int(player_input_)<=9:
        player_input_=int(player_input_)
        if board[player_input_-1]==" ":
            board[player_input_-1]= player
        else:
            print("This spot has been occupied. Please choose another place.")
            return player_input(board)
    else:
        print("Please enter number between 1 and 9!")
        return player_input(board)
def taking_turn():
    global player
    if player=="X":
        player="O"
    else:
        player="X"
def check_win_tie():
    global game
    win=[[board[0],board[1],board[2]],[board[3],board[4],board[5]],[board[6],board[7],board[8]],
        [board[0],board[3],board[6]],[board[1],board[4],board[7]],[board[2],board[5],board[8]],
        [board[0],board[4],board[8]],[board[2],board[4],board[6]]]
    for winner in win:
        if winner[0] == winner[1] == winner[2] !=" ":
            print_board()
            print(f"Congratulation, The winner is {player}.")
            game=False
    if " " not in board:
        print_board()
        print("You are tie!")
        game=False
def play_game():
    while game:
        print_board()
        player_input(board)
        check_win_tie()
        taking_turn()
def main():
    global game
    play_game()
    again=True
    while again:
        play_again = input("Would you like to play again? Y/N\n")
        if play_again.upper()=="Y":
            for x in range(len(board)):
                board[x]=" "
            game=True
            play_game()
        else:
            print("See you again!")
            again=False
        
if __name__=="__main__":
    main()
    
      
