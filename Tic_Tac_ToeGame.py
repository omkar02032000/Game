def take_input():
    cont = True
    while cont:
        py1 = input('\nPick a marker "X" or "O": ').upper()
        if py1 == 'X':
            cont = False
            py2 = 'O'
            print('\nPlayer 1 going to play First')
        elif py1 == 'O':
            cont = False
            py2 = 'X'
            print('\nPlayer 2 going to play First\n')
        else:
            print('\n!Woops! Enter correct input --> Try Again\n')
    print('\nThe player 1 marker is: ' + py1 + '\nThe player 2 marker is: ' + py2)
    return (py1, py2)

def show_board(l):
    print(l[1] + '    |    ' + l[2] + '    |    ' + l[3])
    print('---------------------')
    print(l[4] + '    |    ' + l[5] + '    |    ' + l[6])
    print('---------------------')
    print(l[7] + '    |    ' + l[8] + '    |    ' + l[9])

def place_marker(b, m, p):
    if b[p] not in ['X', 'O']:
        b[p] = m
    else:
        print('# HEY # \nA mark is already there \nChoose another position')
        take_position(b, m)
    return b

def win_check(b, m):
    return ((b[1] == b[2] == b[3] == m) or (b[4] == b[5] == b[6] == m) or (b[7] == b[8] == b[9] == m) or (b[3] == b[5] == b[7] == m) or
               (b[1] == b[4] == b[7] == m) or (b[2] == b[5] == b[8] == m) or (b[3] == b[6] == b[9] == m) or (b[1] == b[5] == b[9] == m))

def take_position(b, m):
    pos = 0
    cont = True
    while cont:
        if pos not in [1,2,3,4,5,6,7,8,9]:
            pos = int(input("\nEnter the to place your mark: "))
            al = place_marker(b, m, pos)
            return al

def replay():    
    return input('\nDo you want to play again? Enter Yes or No: ').lower().startswith('y')


print('!!! Welcome to the Tic - Tac - Toe game !!!')

while True:
    theboard = ['  ']*10
    player1 , player2 = take_input()
    turn = False

    if player1 == 'X':
        turn = True
    play_game = input('\nAre you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True

    else:
        game_on = False
    
    while game_on:
        
        if turn:
            show_board(theboard)
            theboard = take_position(theboard, player1)
            if win_check(theboard, player1):
                show_board(theboard)
                print('Congratulations! Player1 have won the game!')
                game_on = False
            turn = False

        else:
            show_board(theboard)
            theboard = take_position(theboard, player2)
            if win_check(theboard, player2):
                show_board(theboard)
                print('\nCongratulations! Player2 have won the game!\n')
                game_on = False
            turn = True

        if theboard.count('  ') == 1:
            show_board(theboard)
            print('\nThe game is a draw!\n')
            break

    if not replay():
        print('\n---Bye--- Come Again to play\n') 
        break
