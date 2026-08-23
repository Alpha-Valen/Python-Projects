import tkinter as tk #import the tkinter module for GUI development
task = [] # create an empty list to store tasks

def add_task_clicked(task_entry): # define a function to handle the button click event for adding a task
    task_text = task_entry.get().strip() # get the text from the task_entry widget and remove leading/trailing whitespace
    if not task_text: # check if the task text is empty
        print("No task entered.") # print a message to the console if no task was entered
        return
    
    task.append(task_text) # add the task text to the task list
    print(f'Task "{task_text}" added. . . Good job!') # print a message to the console confirming the task was added
    print(f'All tasks:', task) # print the current list of tasks to the console

    task_entry.delete(0, tk.END) # clear the task_entry widget after adding the task

def create_gui(): # define a function to create the GUI window
    root = tk.Tk() # create a new Tkinter window
    root.title("Task Manager") # set the title of the window to "Task Manager"

    task_entry = tk.Entry(root) # create an entry widget for task input
    task_entry.pack() # add the entry widget to the window and make it visible

    button = tk.Button(root, text='Add Task', command=lambda: add_task_clicked(task_entry)) # create a button widget with the text "Add Task"
    button.pack() # add the button to the window and make it visible

    return root # return the created window object



app = create_gui() # call the create_gui function and assign the returned window object to the variable 'app'
app.mainloop() # start the Tkinter event loop, which keeps the window open and responsive to user interactions


