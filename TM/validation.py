total_failures = 0

def handle_easter_egg(value):
    special_numbers = {
        69: 'Nice! But... Not... a valid priority.',
        420: 'Blaze it! But... Not... a valid priority.',
        1337: 'Leet! But... Not... a valid priority.',
        42: 'The answer to the ultimate question of life, the universe, and everything! But... Not... a valid priority.',
        67: 'Tell me you were born after 2000 without telling me you were born after 2000.',
        666: 'Sus, but... Not... a valid priority.',
        1738: 'Good Vibes. But... Not... a valid priority.',
        0: 'Zero? Really? Not... a valid priority.',
        -1: 'Negative? Are we going into the upside down?'}
    
    return special_numbers.get(value)

def handle_invalid_input(user_input, attempts, was_numeric, numeric_value):
    if not was_numeric:
        return 'Use the Number Pad!'
    easter_egg_responses = handle_easter_egg(numeric_value)
    if easter_egg_responses:
        return easter_egg_responses
    if numeric_value < 1 or numeric_value > 5:
        if attempts == 1:
            return 'Bro.... 1 through 5.'
        elif attempts == 2:
            return '... Seriously? 1 through 5. It\'s not that hard.'
        elif attempts == 3:
            return 'That was your last chance. And you blew it. Now we start over...'
        
def get_valid_priority():
    global total_failures
    attempts = 0
    while attempts < 3 :
        user_input = input('Enter task priority (1-5): ')
        attempts += 1

        try:
            numeric_value = int(user_input)
            was_numeric = True
        except ValueError:
            was_numeric = False
            numeric_value = None
        
        if was_numeric and 1 <= numeric_value <= 5:
            if attempts == 3:
                print('... Finally!')
            return numeric_value
        
        message = handle_invalid_input(user_input, attempts, was_numeric, numeric_value)
        print(message)

    total_failures += 1

    if total_failures == 1:
        print('When you come back! Be ready to enter a valid priority.')
    elif total_failures == 2:
        print('Oh this is getting concerning. Again...')
    elif total_failures == 3:
        print('This is becoming a pattern.')
    return None

def get_valid_status():
    status_options = ['not started', 'in progress']
    while True:
        status = input('Enter task status (not started, in progress): ').lower()
        if status in status_options:
            return status
        else:
            print('. . . No, chose from the options provided. . . not started or in progress. . .')

            global total_failures
            total_failures += 1
            