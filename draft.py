values = []
i = 0
while i < 3:
    value = input(f'value number {i+1} >')
    if not value:
        print('You must type a valid input')
        # The loop will re-prompt for the same value of 'i'
    else:
        values.append(value)
        i += 1 # Only increment 'i' if a valid input is received
print(values)