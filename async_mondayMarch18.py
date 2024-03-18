#def countLettters():
 #   userCharacters = input('Count Number Of Characters.')
  #  characters = round(userCharacters)
   # print(characters)
#countLettters()
 

def winner(Computer_Move,Player_Move):
    if Computer_Move == Player_Move:
        print('Tie')
    elif Player_Move == 'Rock' and Computer_Move == 'paper':
        winner = 'computer'
    elif Player_Move == 'paper' and Computer_Move == 'Scissor':
        winner = 'Computer'
    elif Player_Move == 'Scissor' and Computer_Move == 'Rock':
        winner = 'Computer'
    elif Player_Move == 'paper' and Computer_Move == 'Rock':
        winner = 'Player'
    else:
        print('Computer Win.')

winner('paper','Rock')
