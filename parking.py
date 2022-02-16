import tkinter as tk
from tkinter.constants import END, DISABLED, ACTIVE
from tkinter import messagebox

# Constants for colors. I can change these three instead of rewriting colors in HEX for every object
color_primary = "#f8f9fa"
color_warning = "#dc3545"
color_taken = "#28a745"
color_outline = "#6c757d"

# Creating window, title and filling the window with color
window = tk.Tk()
window.title("Parking")
window.configure(bg=color_primary)

# This frame has all the interface objects - entries, buttons
interfaceFrame = tk.Frame(window, bg=color_primary)
interfaceFrame.pack()

# This frame stores canvas inside.
# Canvas is used to draw lots and text
displayFrame = tk.Frame(window, bg=color_primary)
displayFrame.pack()

canvas = tk.Canvas(master=displayFrame, width=596,
                   height=200, bg=color_primary)
canvas.pack()

# This list stores regplates. The program checks if the list has < 10 elements. 
# If more - parking is full
regplates = []


class ParkingLot:
    # Counter is needed to create text with the instance number lately
    counter = 0
    # Every instance has a rectangle, built on 4 coordinates with the related text on top
    def __init__(self, x1, y1, x2, y2):
        ParkingLot.counter += 1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.box = canvas.create_rectangle(x1, y1, x2, y2, width=1, outline=color_outline)
        canvas.create_text(x1 + 55, y2 + 10, font="Verdana 10", text="Lot %s" %
                           ParkingLot.counter)
        # This attribute stores regplates to check whether parking is full 
        # and helps avoiding duplicates
        self.isLotTaken = False

    def TakeLot(self):
        # Gets the inputed regplate
        regplate = regplateEnt.get()  

        # Checks if regplate already exists
        if ( (regplate not in regplates)

            # Checks if regplate length is too long 
            and (len(regplate) <= 7)

            # Checks if the lot is busy
            and self.isLotTaken == False):

            # Create texts with the regplate inside lot
            self.reg_text = canvas.create_text(self.x1 + 55, self.y2 + 
                                               35, text=regplate, 
                             
                                               font="verdana 15")

            canvas.itemconfigure(self.box, fill=color_taken)
            CleanEntries()
            regplates.append(regplate)
            self.isLotTaken = True
            IsFull()

        # Handling in case if any condition fails
        elif len(regplate) > 7:
            CleanEntries()
            messagebox.showerror(
                "Error", "The regplate is too long!")
  
        elif regplate in regplates:
            CleanEntries()
            messagebox.showerror(
                "Error", "The regplate already exists!")

        elif self.isLotTaken == True:
            CleanEntries()
            messagebox.showerror(
                "Error", "The lot is taken!")

    def EmptyLot(self):
        try:
            canvas.delete(self.reg_text)
            canvas.itemconfigure(self.box, fill=color_primary)
            CleanEntries()
            regplates.remove(regplate)
            self.isLotTaken = False
            IsFull()
        except IndexError:
            messagebox.showerror("Error", "Nothing to remove!")

# As the name states, cleans everything. I use it so often so it's a better tone to have a separate function for this
def CleanEntries(): 
    regplateEnt.delete(0, END)
    lotEnt.delete(0, END)



# Checking whether parking is full and prints a warning label if so. Also, blocks button until at least one lot is free
def IsFull(): 
    if len(regplates) >= 10:
        canvas.itemconfigure(FullWarning, state="normal")
        saveBtn.config(state=DISABLED)
    elif len(regplates) < 10:
        canvas.itemconfigure(FullWarning, state="hidden")
        saveBtn.config(state=ACTIVE)



def CheckLot(*args): # Checking whether the lot exists and determining what to do with it next
    try:
        key = int(lotEnt.get())
        # I use args to route the program to the particular route: to save or to remove
        if "take" in args:
            ParkingLots[key].TakeLot()
        elif "empty" in args:
            ParkingLots[key].EmptyLot()
        # Exception handling if incorrect lot is entered
    except ValueError:
        CleanEntries()
        messagebox.showerror("Error", "The lot does not exist!")
    except KeyError: 
        CleanEntries()
        messagebox.showerror("Error", "The lot does not exist!")


# Every instance declaration makes a lot (a box), 4 parameters are coordinates
ParkingLots = {
    1: ParkingLot(5, 105, 115, 35),
    2: ParkingLot(125, 105, 235, 35),
    3: ParkingLot(245, 105, 355, 35),
    4: ParkingLot(365, 105, 475, 35),
    5: ParkingLot(485, 105, 595, 35),
    6: ParkingLot(5, 185, 115, 115),
    7: ParkingLot(125, 185, 235, 115),
    8: ParkingLot(245, 185, 355, 115),
    9: ParkingLot(365, 185, 475, 115),
    10: ParkingLot(485, 185, 595, 115),
}

# Declaring buttons, entries and labels: everything is located on the top part of an interface
regplateLbl = tk.Label(master=interfaceFrame,
                       text="Registration number (< 7 characters)", bg=color_primary, font="verdana 9")
regplateLbl.grid(row=0, column=1)

lotLbl = tk.Label(master=interfaceFrame, text="Lot",
                  bg=color_primary, font="verdana 9")
lotLbl.grid(row=0, column=4)

regplateEnt = tk.Entry(master=interfaceFrame, width=40)
regplateEnt.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

lotEnt = tk.Entry(master=interfaceFrame, width=5)
lotEnt.grid(row=1, column=4)

# Creates text and imeditially hides it until parking is full
FullWarning = canvas.create_text( 
    300, 20, text="Parking is full!", fill=color_warning, font="20", state="hidden")

saveBtn = tk.Button(master=interfaceFrame, text="Save",
                    padx=5, command=lambda: CheckLot("take"))
saveBtn.grid(row=1, column=5, padx=5)

removeBtn = tk.Button(master=interfaceFrame, text="Remove",
                      command=lambda: CheckLot("empty"))
removeBtn.grid(row=1, column=6, padx=2)


tk.mainloop()
