import tkinter as tk #import the tkinter module for GUI development

def add_task_clicked():
    print("Add Task button clicked!") # print a message to the console when the button is clicked

def create_gui(): # define a function to create the GUI window
    root = tk.Tk() # create a new Tkinter window
    root.title("Task Manager") # set the title of the window to "Task Manager"

    button = tk.Button(root, text='Add Task') # create a button widget with the text "Add Task"
    button.pack() # add the button to the window and make it visible
    button.config(command=add_task_clicked) # set the button's command to the add_task_clicked function
    task_entry = tk.Entry(root) # create an entry widget for task input
    task_entry.pack() # add the entry widget to the window and make it visible
    return root # return the created window object



app = create_gui() # call the create_gui function and assign the returned window object to the variable 'app'
app.mainloop() # start the Tkinter event loop, which keeps the window open and responsive to user interactions


