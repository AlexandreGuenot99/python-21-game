positions= ['first','second']
is_playing = False
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
                break
            else : 
                print('Wrong input.')
        else:
            print('Wrong input.')
    return user_position,is_playing

user_position,is_playing = choose_position()

while True:
    if is_playing == True:
        print('Player turn')
        values = input('Choose values\n>')
        is_playing = False
    else:
        print('Computer turn')
        print('Computer is choosing values')
        print([1,2,3])
        is_playing = True

