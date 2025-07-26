board = [1,2,3,4,5,7]

def consecutive(board):
    for i in range(len(board)-1):
        if board[i+1] - board[i] !=1:
            print(f'{board[i]} and {board[i+1]} are not consecutives')
            is_consecutive = False
        else:
            print(f'{board[i]} and {board[i+1]} are consecutives')
            is_consecutive = True

    return is_consecutive

is_consecutive = consecutive(board)

print(is_consecutive)