from datetime import datetime

total_failures = 0
tasks = []

tasks.append({'task': 'make task manager', 'status': 'in progress', 'priority': 1})
tasks.append({'task': 'write documentation', 'status': 'not started', 'priority': 2})
tasks.append({'task': 'test application', 'status': 'not started', 'priority': 3}) 


def display_tasks(tasks):
    printed_any = False

    for priority in range(1, 6):
        bucket_tasks = [task for task in tasks if task['priority'] == priority and task['status'] != 'completed']
        if bucket_tasks:
            printed_any = True
            print(f'\n=== PRIORITY {priority} ===')
            for task in bucket_tasks:
                print(f"- {task['task']} [{task['status']}]")
    if not printed_any:
        print('\n Wiggle Party! Stop looking for something to do and go relax!')

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

def add_task():
    task = input('Enter what needs to be done: ').strip()
    status = get_valid_status()
    priority = get_valid_priority()
    tasks.append({'task': task, 'status': status, 'priority': priority})
    print(f'Task "{task}" added with status "{status}" and priority {priority}. . . Good job!')

def get_valid_status():
     status_options = ['not started', 'in progress', 'completed']
     while True:
        status = input('Enter task status (not started, in progress, completed): ').lower()
        if status in status_options:
            return status
        else:
            print('. . . No, chose from the options provided. . . not started, in progress, completed. . .')

def save_task():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f'{task['task']},{task['status']},{task['priority']}\n')

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                task, status, priority = line.strip().split(',')
                tasks.append({'task': task, 'status': status, 'priority': int(priority)})
    except FileNotFoundError:
        print('I hope you are ready for some productivity...')

load_tasks()
while True:
    add_task()
    display_tasks(tasks)
    print('-----------------------')

    continue_input = input('Do you want to add another? (yes/no/maybe): ').lower()

    if continue_input == 'yes':
        continue
    elif continue_input == 'maybe'
        print('I mean... I can\'t force you to add more tasks, but it would be good for you to practice entering valid input. . .')
        continue
    elif continue_input == 'no':
        print('Well fine then!')
        break
    else:
        print('This is a yes or no question . . .')
        continue


display_tasks(tasks)
save_task()


# TODO:
# 1. create special easter eggs function for certain priority numbers, like 69 or 420, that print a joke instead of an error message. (D)
# 2. expand handle_invalid_input to check for these easter eggs and return the joke instead of an error message when they are entered. (D)
# 3. create add_task function that prompts the user for task details (task, status, priority) and adds the task to the tasks list. (D)
# 3.1 Use get_valid_priority to ensure the priority is valid. (D)
# 4. create the status options as a predefined list and validate user input against it when adding a task. (D)
# 5. create get_valid_status function that prompts the user for a valid status and returns it. (D)

# 6. implement a loop in the main program that allows the user to add multiple tasks until they choose to stop.  
# 6.1 make a batch entry option that allows the user to enter multiple tasks at once, separated by '|' and parse the input to add each task accordingly.
# 7. add functionality to display tasks sorted by priority, with clear formatting. 
# 8. implement a feature to mark tasks as completed and move them to a separate completed tasks list.
# 9. add error handling for edge cases, such as empty task descriptions or invalid status entries.
# 10. create a function to save tasks to a file and load them back when the program starts, allowing for persistence between sessions. (D)
