import tkinter as tk 
import pyautogui
# REMINDER that Label widget is for implementing text in python memory, Entry widget is for putting an entry box to type in stuff. .pack is literally putting it in the windows so that it is visible, which both widgets require.
def update_position():
    x, y = pyautogui.position() # returns mouse coordinates as a tuple, x and y variables both become the tuple's value
    label.config(text=f"X: {x}, Y: {y}", fg="purple") # f string that configures the label variable. {x} and {y} are the values and X: and Y: are the text. fg is foreground, AKA the text. changes text to purple
    # as a note, .config is actually part of the tkinter module, not a native python method
    root.after(100, update_position) # # after 100 miliseconds, use update_position.
    # root.after basically schedules what root is going to do after.

root= tk.Tk() # this is the main window, displays the whole window
root.title("Mouse Display") # title of the window
root.geometry("500x500") # how big the window is when you launch the program


text_Label = tk.Label(root, text="X and Y", font=('Arial', 14)) # shows you the text and font/font size. has a variable
text_Label.pack(pady=20) # takes the variable and gives it a pack, meaning it is now visible on the window


label = tk.Label(root,  font=('Arial', 14)) # the above label.config affects this line. basically shows you the x and y coordinates in real time.
label.pack(pady=50)  # this actually displays it on the window

button = tk.Button(root, text="Quit", font=('Arial', 20), command=root.destroy) # quit button
button.place(x=400, y=400) # places quit button at that coordinates on window



def move_Mouse():
    try:
        x = int(enter_x.get()) # this gets the value from enter_x, takes integers
        y = int(enter_y.get()) # this gets the value from enter_y, takes integers
        pyautogui.moveTo(x, y, duration=1) # this moves the mouse to the x,y coordinates in 1 second
    except ValueError: # gives an except so program keeps running after being given wrong values. ValueError is when python cannot convert what was inputted as whatever value you need it to be. 
        result_label.config("Please enter valid numbers") # this gives an error if you type in numbers that do not work


tk.Label(root, text="Enter X coordinates:", font=("Arial", 14)).pack() # label that is also packed, so you can see it. has no variable
enter_x = tk.Entry(root) # section where you enter numbers for x coordinates
enter_x.pack() # packed so that it is visible

tk.Label(root, text="Enter Y coordinates:", font=("Arial", 14)).pack() # label that is also packed, so you can see it. has no variable
enter_y = tk.Entry(root) # section where you enter numbers for y coordinates
enter_y.pack() # packed so that it is visible

entry_Button = tk.Button(root, text="Submit", font=("Arial", 14), command=move_Mouse) # button that executes the move_Mouse function
entry_Button.pack(pady=30)

result_label = tk.Label(root, text="") # this creates the label for results. so if you type in something wrong, it will give an error in terminal
result_label.pack(pady=50)


update_position() # pretty much shows you the mouse position after every 100 miliseconds





root.mainloop() # runs program on loop