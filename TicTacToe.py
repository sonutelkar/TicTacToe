# write your code here
def check_board(user):
    global valid
    win_conditions = [user[:3], user[3:6], user[6:], user[0:7:3],
    user[1:8:3], user[2:9:3], user[0:9:4], user[2:7:2]]
    if abs(user.count('X') - user.count('O')) > 1 or ('XXX' in win_conditions and 'OOO' in win_conditions):
        print('Impossible')
        return True
    elif 'XXX' in win_conditions:
        print('X wins')
        valid = False 
    elif 'OOO' in win_conditions:
        print('O wins')
        valid = False 
    else:
        if ' ' in user:
            print('Game not finished')
        else:  
            print('Draw')
            valid = False 


def display_board(usr):
    print('---------')
    print('|', usr[0], usr[1], usr[2], '|')
    print('|', usr[3], usr[4], usr[5], '|')
    print('|', usr[6], usr[7], usr[8], '|')
    print('---------')


user =[' ',' ',' ',' ',' ',' ',' ',' ',' ']
tokken = ['X','O']
display_board(user)
mapping = {'1 1': 6, '1 2': 3, '1 3': 0,
           '2 1': 7, '2 2': 4, '2 3': 1,
           '3 1': 8, '3 2': 5, '3 3': 2}
valid = True
turn_count = 0
while valid:
    coordinates = input('Enter coordinates > ')
    try:
        x, y = coordinates.split()
        if not (1 <= int(x) <= 3) or not (1 <= int(y) <= 3):
            print('Coordinates should be from 1 to 3!')

        elif user[mapping[coordinates]] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            turn = 0 if (turn_count% 2) == 0 else 1
            user[mapping[coordinates]] = tokken[turn]
            display_board(user)
            if check_board(''.join(map(str,user))):
                user[mapping[coordinates]] = ' '

                display_board(user)
            else:
                turn_count += 1
    except (ValueError, IndexError):
        print('You should enter numbers!')