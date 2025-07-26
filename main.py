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

def game():
    is_playing = choose_position()
    while True:
        if is_playing == True:
            print('Your turn')
            amount = choose_amount()
            input_values = choose_values(amount)
            print(f'Your chosen values  : {input_values}')
            for i in range(0,len(input_values)):
                game_board.append(input_values[i])
            is_playing = False
        else:
            print('Computer turn')
            amount = random.randint(1,3)
            print(f'Computer choose {amount} values')
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
    
game()

