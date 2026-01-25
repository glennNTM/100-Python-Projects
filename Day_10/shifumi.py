from random import choice

player_move = int(input("Select your move (1 for Rock(🪨), 2 for Paper(📜), 3 for Scissors(✂️)):"))

computer_move = choice((1, 2, 3))

if computer_move == 1 and player_move == 1:
    print("Computer chose Rock. It's a tie!")
elif computer_move == 1 and player_move == 2:
    print("Computer chose Rock. You win!")
elif computer_move == 1 and player_move == 3:
    print("Computer chose rock. You lose!")


if computer_move == 2 and player_move == 2:
    print("Computer chose Paper. It's a tie!")
elif computer_move == 2 and player_move == 1:
    print("Computer chose Paper. You lose!")
elif computer_move == 2 and player_move == 3:
    print("Computer chose Paper. You win!")

if computer_move == 3 and player_move == 3:
    print("Computer chose Scissor. It's a tie!")
elif computer_move == 3 and player_move == 2:
    print("Computer chose Scissor. You lose!")
elif computer_move == 3 and player_move == 1:
    print("Computer chose Scissor. You win!")