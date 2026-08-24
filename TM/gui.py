from asyncio import tasks
import tkinter as tk #import the tkinter module for GUI development
import main #import the main module for task management functions



def add_task_clicked(task_entry, status_var, priority_var): # define a function to handle the button click event for adding a task
    task_text = task_entry.get().strip() # get the text from the task_entry widget and remove leading/trailing whitespace
    status = status_var.get() # get the selected status from the status_var StringVar
    priority = int(priority_var.get()) # get the selected priority from the priority_var StringVar

    if not task_text: # check if the task text is empty
        print("No task entered.") # print a message to the console if no task was entered
        return
    
    main.tasks.append({'task': task_text, 'status': status, 'priority': priority}) # add the task text to the task list
    print(f'Task "{task_text}" added. . . Good job!') # print a message to the console confirming the task was added
    print(f'All tasks:', main.tasks) # print the current list of tasks to the console

    task_entry.delete(0, tk.END) # clear the task_entry widget after adding the task

def create_gui(): # define a function to create the GUI window
    root = tk.Tk() # create a new Tkinter window
    root.title("Task Manager") # set the title of the window to "Task Manager"

    task_entry = tk.Entry(root) # create an entry widget for task input
    task_entry.pack() # add the entry widget to the window and make it visible

    status_var = tk.StringVar(root) # create a StringVar to hold the selected status value 
    status_var.set('not started') # set the default value to 'not started'
    status_menu = tk.OptionMenu(root, status_var, *main.status_options) # create an option menu for selecting task status
    status_menu.pack() # add the status menu to the window and make it visible

    priority_var = tk.StringVar(root) # create a StringVar to hold the selected priority value
    priority_var.set('1') # set the default value to '1'
    priority_menu = tk.OptionMenu(root, priority_var, *[str(i) for i in range(1, 6)]) # create an option menu for selecting task priority
    priority_menu.pack() # add the priority menu to the window and make it visible


    search_entry = tk.Entry(root) # create an entry widget for search input
    search_entry.pack() # add the search entry widget to the window and make it visible

    button = tk.Button(root, text='Add Task', command=lambda: add_task_clicked(task_entry, status_var, priority_var)) # create a button widget with the text "Add Task"
    button.pack() # add the button to the window and make it visible
                                      
    return root # return the created window object



app = create_gui() # call the create_gui function and assign the returned window object to the variable 'app'
app.mainloop() # start the Tkinter event loop, which keeps the window open and responsive to user interactions


