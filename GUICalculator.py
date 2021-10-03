import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.configure(bg="#72a3ea")
window.geometry("370x355")

entry = tk.Entry(window, width=38, borderwidth=3, bg="#d8fcff", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5, ipady=5)


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
    first_number = int(number)
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
    first_number = int(number)
    clean_input()


def equal():
    global is_equal_clicked
    is_equal_clicked = True

    second_number = entry.get()
    clean_input()

    if action == "addition":
        entry.insert(0, first_number + int(second_number))

    if action == "multiplication":
        entry.insert(0, first_number * int(second_number))

    if action == "division":
        entry.insert(0, first_number / int(second_number))

    if action == "subtraction":
        entry.insert(0, first_number - int(second_number))

def make_cell_buttons():
    arr = []
    for t in range(1, 10):
        new_btn = tk.Button(window, text=str(t),
                            padx=40, pady=20,
                            bg="#72a3ea", fg="black",
                            command=lambda x=t: click(x))
        arr.append(new_btn)
    return arr


buttons1_9 = make_cell_buttons()

button0 = tk.Button(window, text="0", padx=88, pady=20,
                    bg="#72a3ea", fg="black", command=lambda: click(0))

button_equal = tk.Button(window, text="=", padx=40, pady=20,
                         bg="#7285ea", fg="black", command=lambda: equal())

button_add = tk.Button(window, text="+", padx=40, pady=20,
                       bg="#7285ea", fg="black", command=lambda: add(entry.get()))

button_clear = tk.Button(window, text="Clear", padx=77, pady=20,
                         bg="#7285ea", fg="black", command=lambda: clean_input())

button_divide = tk.Button(window, text="/", padx=42, pady=20,
                          bg="#7285ea", fg="black", command=lambda: divide(entry.get()))
button_multiply = tk.Button(window, text="*", padx=41, pady=20,
                            bg="#7285ea", fg="black", command=lambda: multiply(entry.get()))
button_subtract = tk.Button(window, text="-", padx=42, pady=20,
                            bg="#7285ea", fg="black", command=lambda: subtract(entry.get()))
button_dot = tk.Button(window, text=".", padx=42, pady=20,
                       bg="#72a3ea", fg="black", command=lambda: click("."))
button_extra = tk.Button(window, text="Extra", padx=28, pady=20,
                         bg="#7285ea", fg="black", command=lambda: click(1))


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

button0.grid(row=4, column=0, columnspan=2)
button_dot.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0, columnspan=2)
button_extra.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

window.resizable(False, False)
window.mainloop()
