human_turn = 'rock'
computer_turn = 'paper'

if human_turn == computer_turn:
    print ('Draw!')

elif human_turn == 'rock and' and computer == 'scissors':
    print ('Human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print ('Human wins!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print ('Human wins!')
else:
    print ('Computer wins!')
