import random
positions= ['first','second']
game_board = []
def choose_position():
    while True:
        user_position = input('Go firt or second ? (F) (S)\n>')  
        if user_position.isalpha():
            user_position = user_position.upper()
            if user_position == 'F':
                user_position = 'first'
                is_playing = True
                break
            if user_position == 'S':
                user_position = 'second'
                is_playing = False
                break
            else : 
                print('Wrong input.')
        else:
            print('Wrong input.')
    return  is_playing

def choose_amount():
    while True:
        amount = input('How many numbers do you wish to enter?\n')
        try:
            amount = int(amount)
            if len(game_board) == 18:
                if 1 <= amount <= 2:
                    return amount
                else:
                    print('Type a value between 1 and 2')
            elif len(game_board) == 19:
                if amount ==1 :
                    return amount
                else:
                    print('Type a value between 1 and 2')
            else:
                if 1 <= amount <= 3 :
                    return amount
                else :
                    print('Type a value between 1 and 3')
        except ValueError:
            print('Type a numeral value')

def choose_values(amount):
    print('Enter your values')
    input_values = []
    i=0
    while i<amount :
        value = input(f'Value {i+1} >')
        try:
            value = int(value)
            if not value:
                print('You must type a valid input')
            else:
                input_values.append(value)
                i+=1
        except ValueError:
            print('Type a numeral value')
    return input_values

def check_consecutive(board):
    is_consecutive_counter = 0
    if len(board) ==1:
        is_consecutive_counter = 0
    else:
        for i in range(len(board)-1):
            if board[i+1] - board[i] !=1:
                is_consecutive_counter += 1
           
    return is_consecutive_counter     

def game():
    is_playing = choose_position()
    while len(game_board) < 20 :
        if is_playing == True:
            print('\nYour turn\n')
            amount = choose_amount()
            input_values = choose_values(amount) 
            consecutive = check_consecutive(input_values)
            if consecutive == 0:
                if not game_board:
                    for i in range(len(input_values)):
                        game_board.append(input_values[i])
                else:
                    if input_values[0] != game_board[-1]+1:
                        print('Your values are not following the sequence. You lost !')
                        print(f'Expected : {game_board[-1]+1} as first value')
                        break
                    for i in range(len(input_values)):
                        game_board.append(input_values[i])
            else:
                print('Your values are not crescent consecutives. You lost !')
                break         
            is_playing = False
        else:
            if len(game_board) == 18:
                amount = random.randint(1,2)
            elif len(game_board) == 19:
                amount = 1
            else:
                amount = random.randint(1,3)
            cpu_values=[]
            if not game_board:
                for i in range(amount):
                    game_board.append(i+1)
            else :
                for i in range(amount):
                    cpu_values.append(game_board[-1]+1)
                    game_board.append(cpu_values[i])
            is_playing = True
            print(f'Order of input after Computer turn is :\n {game_board}')
    if is_playing == True:
        print('The player ends on 21. Player lost !')
    elif is_playing == False:
        print('The computer ends on 21. Player win !')

    
game()

