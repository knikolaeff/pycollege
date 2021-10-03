import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.configure(bg="#72a3ea")
window.geometry("370x355")

entry = tk.Entry(window, width=38, borderwidth=3, bg="#d8fcff", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5, ipady=5)

def click(number):
    curValue = entry.get()
    entry.delete(0, "end")
    entry.insert(0, curValue + str(number))

def add(number):
    global action
    global first_number
    action = "addition"
    first_number = int(number)
    entry.delete(0, "end")
    

def sum():
    second_number = entry.get()
    entry.delete(0, "end")
    

    if action == "addition":
        entry.insert(0, first_number + int(second_number))

#creating all the buttons (for loop is a bad idea because of buttons scaling)
button1 = tk.Button(window, text="1", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(1))
button2 = tk.Button(window, text="2", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(2))
button3 = tk.Button(window, text="3", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(3))
button4 = tk.Button(window, text="4", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(4))
button5 = tk.Button(window, text="5", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(5))
button6 = tk.Button(window, text="6", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(6))
button7 = tk.Button(window, text="7", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(7))
button8 = tk.Button(window, text="8", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(8))
button9 = tk.Button(window, text="9", padx=40, pady=20, bg="#72a3ea", fg="black", command=lambda: click(9))
button0 = tk.Button(window, text="0", padx=87, pady=20, bg="#72a3ea", fg="black", command=lambda: click(0))

button_equal = tk.Button(window, text="=", padx=40, pady=20, bg="#7285ea", fg="black", command=lambda: sum())

button_add = tk.Button(window, text="+", padx=40, pady=20, bg="#7285ea", fg="black", command=lambda: add(entry.get()))

#to make code smaller, I didn't use separate function 
button_clear = tk.Button(window, text="Clear", padx=76, pady=20, bg="#7285ea", fg="black", command=lambda: entry.delete(0, "end"))

button_divide = tk.Button(window, text="/", padx=42, pady=20, bg="#7285ea", fg="black", command=lambda: click(1))
button_multiply = tk.Button(window, text="*", padx=41, pady=20, bg="#7285ea", fg="black", command=lambda: click(1))
button_subtract = tk.Button(window, text="-", padx=42, pady=20, bg="#7285ea", fg="black", command=lambda: click(1))
button_dot = tk.Button(window, text=".", padx=42, pady=20, bg="#72a3ea", fg="black", command=lambda: click(1))
button_extra = tk.Button(window, text="Extra", padx=28, pady=20, bg="#7285ea", fg="black", command=lambda: click(1))

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button0.grid(row=4, column=0, columnspan=2)
button_dot.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0, columnspan=2)
button_extra.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

window.resizable(False, False)
window.mainloop()