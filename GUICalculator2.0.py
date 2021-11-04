import tkinter as tk
import math
import sys
# Creating a window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#72a3ea")
# The window looks differently on different OS so I specify sizes here
if sys.platform.startswith('win'):
    window.geometry("380x395")
else:
    window.geometry('500x460')
# This entry will show all the user input
entry = tk.Entry(window, width=50,  borderwidth=4, bg="#d8fcff", fg="black")
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)

is_extra_clicked = False

# This function will clean the entry 
def clean_input():
    entry.delete(0, "end")

# "Click" function registers a button user clicks and shows it's value. 
def click(number):

    curValue = entry.get()
    clean_input()
    entry.insert(0, curValue + str(number))

# Using the sqrt method from math package, this function calculates square root of an entered value
def root(number):
    clean_input()
    entry.insert(0, math.sqrt(float(number)))

# This function toggles "extra" tab by showing and hiding the buttons on the right
def extra():

    global is_extra_clicked
    is_extra_clicked = not is_extra_clicked

    if (is_extra_clicked):
        button_divide.grid_forget()
        button_multiply.grid_forget()
        button_subtract.grid_forget()
        button_add.grid_forget()
        button_power.grid(row=1, column=3)
        button_root.grid(row=2, column=3)
        button_opBracket.grid(row=3, column=3)
        button_clBracket.grid(row=4, column=3)
    else:
        button_divide.grid(row=1, column=3)
        button_multiply.grid(row=2, column=3)
        button_subtract.grid(row=3, column=3)
        button_add.grid(row=4, column=3)
        button_power.grid_forget()
        button_root.grid_forget()
        button_opBracket.grid_forget()
        button_clBracket.grid_forget()

# This function calculates input in the entry and prints the result. Also, it handles errors
# Eval is a dangerous method, because it executes everything inside the entry without filtering it,
# but this program will work only on user's machine so using is justified 
def equal():

    try:
        calculation = eval(str(entry.get()))
        clean_input()
        entry.insert(0, calculation)
    except ZeroDivisionError:
        clean_input()
        entry.insert(0, "Division by zero!")
    except ValueError:
        clean_input()
        entry.insert(0, "Strings are not allowed!")
    except OverflowError:
        clean_input()
        entry.insert(0, "The number is too big!")
    except SyntaxError:
        clean_input()
        entry.insert(0, "Something went wrong!")

# This function declares buttons from 1 to 9. Every attribute of these buttons is the same except command and text 
def make_cell_buttons():
    lst = []
    for t in range(1, 10):
        new_btn = tk.Button(window, text=str(t),
                            width=12, height=4,
                            bg="#72a3ea", fg="#000000",
                            command=lambda x=t: click(x))
        lst.append(new_btn)
    return lst

# Declaring all the extra buttons manually because sizes are "hit or miss" in tkinter 
buttons1_9 = make_cell_buttons()

button0 = tk.Button(window, text="0", width=26, height=4,
                    bg="#72a3ea", fg="black", command=lambda: click(0))

button_equal = tk.Button(window, text="=", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: equal())

button_add = tk.Button(window, text="+", width=12, height=4,
                       bg="#7285ea", fg="black", command=lambda: click("+"))

button_clear = tk.Button(window, text="Clear", width=26, height=4,
                         bg="#7285ea", fg="black", command=lambda: clean_input())

button_divide = tk.Button(window, text="/", width=12, height=4,
                          bg="#7285ea", fg="black", command=lambda: click("/"))

button_multiply = tk.Button(window, text="*", width=12, height=4,
                            bg="#7285ea", fg="black", command=lambda: click("*"))

button_subtract = tk.Button(window, text="-", width=12, height=4,
                            bg="#7285ea", fg="black", command=lambda: click("-"))

button_dot = tk.Button(window, text=".", width=12, height=4,
                       bg="#72a3ea", fg="black", command=lambda: click("."))

button_extra = tk.Button(window, text="Extra", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: extra())

button_power = tk.Button(window, text="bⁿ", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: click(" ** "))

button_root = tk.Button(window, text="√", width=12, height=4,
                        bg="#7285ea", fg="black", command=lambda: root(entry.get()))

button_clBracket = tk.Button(window, text=")", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: click(")"))

button_opBracket = tk.Button(window, text="(", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: click("("))

# Using dictionary, filling buttons from 1 to 9 into grid
def fill_positions(buttons):

    buttonRowCol = {
        0: [3, 0],
        1: [3, 1],
        2: [3, 2],
        3: [2, 0],
        4: [2, 1],
        5: [2, 2],
        6: [1, 0],
        7: [1, 1],
        8: [1, 2],
    }

    for i, val in enumerate(buttons):
        val.grid(row=buttonRowCol[i][0], column=buttonRowCol[i][1])


fill_positions(buttons1_9)

# Filling everything that left
button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)

button0.grid(row=4, column=0, columnspan=2)
button_dot.grid(row=4, column=2)


button_clear.grid(row=5, column=0, columnspan=2)
button_extra.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

# This will not break the window by accidentaly resizing it
window.resizable(False, False)
window.mainloop()