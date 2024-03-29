import tkinter as tk
import math

window = tk.Tk()
window.title("Calculator")
window.configure(bg="#72a3ea")
window.geometry("380x395")

entry = tk.Entry(window, width=50, borderwidth=4, bg="#d8fcff", fg="black")
entry.grid(row=0, column=0, columnspan=4, pady=5, ipady=5)

is_minus_clicked = False
is_extra_clicked = False
is_equal_clicked = False
action = None
first_number = None


def clean_input():
    entry.delete(0, "end")


def click(number):
    global is_equal_clicked

    if (is_equal_clicked):
        is_equal_clicked = False
        clean_input()

    curValue = entry.get()
    clean_input()
    entry.insert(0, curValue + str(number))


def add(number):
    global action
    global first_number
    action = "addition"
    first_number = float(number)
    clean_input()


def multiply(number):
    global action
    global first_number
    action = "multiplication"
    first_number = float(number)
    clean_input()


def divide(number):
    global action
    global first_number
    action = "division"
    first_number = float(number)
    clean_input()


def subtract(number):
    global action
    global first_number
    action = "subtraction"
    first_number = float(number)
    clean_input()


def power(number):
    global action
    global first_number
    action = "power"
    first_number = float(number)
    clean_input()


def root(number):
    global is_equal_clicked
    clean_input()
    entry.insert(0, math.sqrt(float(number)))
    # Makes next symbol disappear as if I pressed equal
    is_equal_clicked = True


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
        button_pi.grid(row=3, column=3)
        button_minus.grid(row=4, column=3)
    else:
        button_divide.grid(row=1, column=3)
        button_multiply.grid(row=2, column=3)
        button_subtract.grid(row=3, column=3)
        button_add.grid(row=4, column=3)
        button_power.grid_forget()
        button_root.grid_forget()
        button_pi.grid_forget()
        button_minus.grid_forget()


def minus():
    global is_minus_clicked
    is_minus_clicked = not is_minus_clicked

    if (is_minus_clicked):
        entry.insert(0, "-")
    else:
        entry.delete(0, 1)


def equal():
    global is_equal_clicked
    is_equal_clicked = True

    second_number = entry.get()
    clean_input()
    if action == "addition":
        entry.insert(0, first_number + int(second_number))
    elif action == "multiplication":
        entry.insert(0, first_number * float(second_number))
    elif action == "division":
        try:
            entry.insert(0, first_number / int(second_number))
        except ZeroDivisionError:
            entry.insert(0, "Division by zero!")
    elif action == "subtraction":
        entry.insert(0, first_number - int(second_number))
    elif action == "power":
        entry.insert(0, first_number ** int(second_number))


def make_cell_buttons():
    arr = []
    for t in range(1, 10):
        new_btn = tk.Button(window, text=str(t),
                            width=12, height=4,
                            bg="#72a3ea", fg="#000000",
                            command=lambda x=t: click(x))
        arr.append(new_btn)
    return arr


buttons1_9 = make_cell_buttons()

button0 = tk.Button(window, text="0", width=26, height=4,
                    bg="#72a3ea", fg="black", command=lambda: click(0))

button_equal = tk.Button(window, text="=", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: equal())

button_add = tk.Button(window, text="+", width=12, height=4,
                       bg="#7285ea", fg="black", command=lambda: add(entry.get()))

button_clear = tk.Button(window, text="Clear", width=26, height=4,
                         bg="#7285ea", fg="black", command=lambda: clean_input())

button_divide = tk.Button(window, text="/", width=12, height=4,
                          bg="#7285ea", fg="black", command=lambda: divide(entry.get()))
button_multiply = tk.Button(window, text="*", width=12, height=4,
                            bg="#7285ea", fg="black", command=lambda: multiply(entry.get()))
button_subtract = tk.Button(window, text="-", width=12, height=4,
                            bg="#7285ea", fg="black", command=lambda: subtract(entry.get()))
button_dot = tk.Button(window, text=".", width=12, height=4,
                       bg="#72a3ea", fg="black", command=lambda: click("."))
button_extra = tk.Button(window, text="Extra", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: extra())

button_power = tk.Button(window, text="bⁿ", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: power(entry.get()))
button_root = tk.Button(window, text="√", width=12, height=4,
                        bg="#7285ea", fg="black", command=lambda: root(entry.get()))
button_pi = tk.Button(window, text="π", width=12, height=4,
                      bg="#7285ea", fg="black", command=lambda: click(math.pi))
button_minus = tk.Button(window, text="+/-", width=12, height=4,
                         bg="#7285ea", fg="black", command=lambda: minus())


def fill_positions(buttons):

    buttonRowCol = {
        0: [1, 0],
        1: [1, 1],
        2: [1, 2],
        3: [2, 0],
        4: [2, 1],
        5: [2, 2],
        6: [3, 0],
        7: [3, 1],
        8: [3, 2],
    }

    for i, val in enumerate(buttons):
        val.grid(row=buttonRowCol[i][0], column=buttonRowCol[i][1])


fill_positions(buttons1_9)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)

button0.grid(row=4, column=0, columnspan=2)
button_dot.grid(row=4, column=2)


button_clear.grid(row=5, column=0, columnspan=2)
button_extra.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

#window.resizable(False, False)
window.mainloop()
