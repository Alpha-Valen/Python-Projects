from datetime import datetime
from validation import get_valid_priority, get_valid_status

tasks = []
completed_tasks = []
status_options = ['not started', 'in progress', 'completed']

def display_tasks_by_priority(tasks): 
    displayed_tasks = []
    printed_any = False
    task_number = 1

    for priority in range(1, 6):
        bucket_tasks = [task for task in tasks if task['priority'] == priority]

        if bucket_tasks:
            printed_any = True
            print(f'\n=== PRIORITY {priority} ===')
            for task in bucket_tasks:
                print(f"{task_number}. {task['task']} [{task['status']}]")
                task_number += 1
                displayed_tasks.append(task)
        
    if not printed_any:
        print('\n Wiggle Party! Stop looking for something to do and go relax!')

    return displayed_tasks  
    
def add_task():
    task = input('Oh, What are we doing? Tell me: ').strip()

    while not task:
        print('Don\'t start. . . enter something, anything.')
        task = input('Let\'s try again. Tell me what you want to do: ').strip()

    status = get_valid_status()
    priority = get_valid_priority()
    if priority is None:
        print('... I said valid priority. . .')
        return
    
    tasks.append({'task': task, 'status': status, 'priority': priority})
    print(f'Task "{task}" added with status "{status}" and priority {priority}. . . Good job!')

def add_one_task_at_a_time():
    while True:
        add_task()
        while True:
            continue_input = input('Do you want to add another? (y/n/maybe): ').lower()
            continue_input = continue_input.strip()
            if continue_input == 'y':
                break
            elif continue_input == 'n':
                print('Well, that/s a choice. . .')
                return
            elif continue_input == 'maybe':
                print('Okay, I will answer for you. . .  Add another.')
                break
            else:
                print('This is a yes, no, or maybe question . . .')
                continue

def add_multiple_tasks():
    batch_input = input('Enter tasks separated by "|": ')
    batch_tasks = [t.strip() for t in batch_input.split('|') if t.strip()]

    for task in batch_tasks:
        status = get_valid_status()
        priority = get_valid_priority()
        tasks.append({'task': task, 'status': status, 'priority': priority})
        print(f'Task "{task}" added with status "{status}" and priority {priority}. . . Good job!')
    
def save_task():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['status']},{task['priority']}\n")

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                task, status, priority = line.strip().split(',')
                tasks.append({'task': task, 'status': status, 'priority': int(priority)})
    except FileNotFoundError:
        print('I hope you are ready for some productivity...')

load_tasks()

def edit_task():
    displayed_tasks = display_tasks_by_priority(tasks)
    task_to_edit = int(input('Which task did we forget to do? '))
    task_to_edit_index = task_to_edit - 1
    if 0 <= task_to_edit_index < len(displayed_tasks):
        task = displayed_tasks[task_to_edit_index]
        print(f'Editing task: {task["task"]} [{task["status"]}]')
        new_status = get_valid_status()
        task['status'] = new_status
        print(f'Task "{task["task"]}" updated to status "{new_status}".')
    
        if task['status'] == 'completed':
            completed_tasks.append(task)
            tasks.remove(task)
            print(f'Task "{task["task"]}" marked as completed and moved to completed tasks.') # add sass
        else:
            print(f'Task "{task_to_edit}" not found.')

def view_completed_tasks():
    completed_tasks = [task for task in tasks if task['status'] == 'completed']
    display_tasks_by_priority(completed_tasks)
    
def view_active_tasks():
    active_task = [task for task in tasks if task['status'] != 'completed']
    display_tasks_by_priority(active_task)

def view_all_tasks():
    all_tasks = [task for task in tasks if task['status'] in ['not started', 'in progress', 'completed']]
    display_tasks_by_priority(all_tasks)

def edit_task():
    displayed_tasks = display_tasks_by_priority(tasks)
    task_to_edit = int(input('What are we changing? Enter task number: '))
    task_to_edit_index = task_to_edit -1
    if 0 <= task_to_edit_index < len(displayed_tasks):
        selected_task = displayed_tasks[task_to_edit_index]
        new_task = input('New task description (Leave it to keep it the same): ').strip()
        if new_task:
            selected_task['task'] = new_task
    new_status = input('New status (not started, in progress, completed) (Leave it to keep it the same): ').strip().lower()
    if new_status in status_options:
        selected_task['status'] = new_status
    new_priority = input('New priority (1-5) (Leave it to keep it the same): ').strip()
    if new_priority.isdigit() and 1 <= int(new_priority) <= 5:
        selected_task['priority'] = int(new_priority) 
        if new_priority:
            if not new_priority.isdigit() or not (1 <= int(new_priority) <= 5):
                print('Please. . . 1 through 5 😑')

def search():
    keyword = input('Whatcha lookin for?').strip().lower()
    found_tasks = [task for task in tasks if keyword in task['task'].lower() or keyword in task['status'].lower()]
    if found_tasks:
        print(f'FOUND IT! Here are the tasks that match "{keyword}":')
        display_tasks_by_priority(found_tasks)
    else:
        print(f'Nope nothing here for "{keyword}". Want to add it?')
        add_it = input('Add it? (y/n): ').strip().lower()

        if add_it == 'y':
            add_task()
        else:
            return

def delete_task():
    displayed_tasks = display_tasks_by_priority(tasks)
    if not displayed_tasks:
        print('No tasks to delete.')
        return

    task_to_delete = input("Which task do you want to delete? Enter task number: ").strip()
    if not task_to_delete.isdigit():
        print('This is a number pad situation.')
        return

    task_to_delete_index = int(task_to_delete) - 1

    if 0 <= task_to_delete_index < len(displayed_tasks):
        selected_task = displayed_tasks[task_to_delete_index]
        confirm = input(f'Are you sure you want to delete "{selected_task["task"]}"? (y/n): ').strip().lower()
        if confirm == 'y':
            tasks.remove(selected_task)
            print(f'Task "{selected_task["task"]}" has been deleted.')
        else:
            print('Deletion canceled.')
    else:
        print('Invalid task number.')
        
def main_menu():
    print("Welcome to your Task Manager!")
    print('=' * 15)
    print('Please choose an option:')
    print('1. Add a single task')
    print('2. Add multiple tasks')
    print('3. Edit tasks')
    print('4. View completed tasks')
    print('5. View active tasks')
    print('6. View all tasks')
    print('7. Save tasks')
    print('8. Search tasks')
    print('9. Exit')

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input('Enter your choice (1-9): ').strip()
        if choice == '1':
            add_one_task_at_a_time()
        elif choice == '2':
            add_multiple_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            view_completed_tasks()
        elif choice == '5':
            view_active_tasks()
        elif choice == '6':
            view_all_tasks()
        elif choice == '7':
            save_task()
            print('Tasks saved!')
        elif choice == '8':
            search()
        elif choice == '9':
            print('Byyyyyyyyeeeee. Until next time!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 9.')
        print('-----------------------')

    save_task()

# TODO:
# 1. create special easter eggs function for certain priority numbers, like 69 or 420, that print a joke instead of an error message. (D)
# 2. expand handle_invalid_input to check for these easter eggs and return the joke instead of an error message when they are entered. (D)
# 3. create add_task function that prompts the user for task details (task, status, priority) and adds the task to the tasks list. (D)
# 3.1 Use get_valid_priority to ensure the priority is valid. (D)
# 4. create the status options as a predefined list and validate user input against it when adding a task. (D)
# 5. create get_valid_status function that prompts the user for a valid status and returns it. (D)

# 6. implement a loop in the main program that allows the user to add multiple tasks until they choose to stop. (D)
# 6.1 make a batch entry option that allows the user to enter multiple tasks at once, separated by '|' and parse the input to add each task accordingly. (D)
# 7. add functionality to display tasks sorted by priority, with clear formatting.(D)
# 8. implement a feature to mark tasks as completed and move them to a separate completed tasks list.(D)
# 8.1 Create a main menu that allows users to choose between adding tasks, viewing tasks, marking tasks as completed, and viewing completed tasks. (D)
# 9. add error handling for edge cases, such as empty task descriptions or invalid status entries. (D)

# 10. create a function to save tasks to a file and load them back when the program starts, allowing for persistence between sessions. (D)
# 11. Implement a feature to display the overall status of tasks, indicating whether there are any tasks still in progress or if all tasks are completed.(VETO - redundant with completed task feature)
# 12. Add a feature to allow users to edit existing tasks, including changing the task description, status, or priority.(D)
# 13. Implement a search functionality that allows users to find tasks based on keywords in the task description or by status. (D)
# 14. Create a feature to delete tasks from the list, with confirmation prompts to prevent accidental deletions. (D)
# 15. Add a feature to categorize tasks into different projects or categories, allowing users to filter and view tasks based on these categories.

# 16. Implement a feature to set deadlines for tasks and display upcoming deadlines, with notifications for overdue tasks.
# 17. Create a user-friendly interface with clear instructions and prompts, making it easy for users to navigate and manage their tasks effectively.
# 18. Add a feature to export tasks to different formats, such as CSV or PDF, for easy sharing and reporting.
# 19. Allow users to customize the priority levels and status options, providing flexibility to adapt the task management system to their specific needs.
# 20. Implement a feature to track the time spent on each task, allowing users to log their work and analyze productivity over time.
# 21. Create a feature to generate reports and statistics on task completion rates, average time spent on tasks, and other relevant metrics to help users improve their productivity.

# 22. Add a feature to integrate with calendar applications, allowing users to sync their tasks and deadlines with their preferred calendar platform for better time management.
# 23. Colorize terminal output based on task priority or status to enhance visual clarity and user experience.