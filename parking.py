import tkinter as tk
from tkinter.constants import END, DISABLED, ACTIVE
from tkinter import messagebox

window = tk.Tk()
window.title("Parking App")

interfaceFrame = tk.Frame(window)
interfaceFrame.pack()

displayFrame = tk.Frame(window)
displayFrame.pack()

canvas = tk.Canvas(master=displayFrame, width=600, height=230)
canvas.pack()

regplates = []


class ParkingLot:
    counter = 0
    def __init__(self, x1, y1, x2, y2):
        ParkingLot.counter += 1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        canvas.create_rectangle(x1, y1, x2, y2)
        canvas.create_text(x1 + 55, y2 + 10, text="Lot %s" % ParkingLot.counter)
        self.regplate = None

    def TakeLot(self):
        if not (self.regplate) and len(regplateEnt.get()) < 7:
            self.regplate = canvas.create_text(self.x1 + 55, self.y2 +
                                                40, text=regplateEnt.get())
            CleanEntries()
            regplates.append(self.regplate)
            IsFull()
        else:
            CleanEntries()
            messagebox.showerror("Error", "The regplate is too long!")
            
    def EmptyLot(self):
        canvas.delete(self.regplate)
        CleanEntries()
        self.regplate = None
        regplates.pop()
        IsFull()


def CleanEntries():
    regplateEnt.delete(0, END)
    lotEnt.delete(0, END)


def IsFull():
    if len(regplates) >= 2:
        canvas.itemconfigure(FullWarning, state="normal")
        saveBtn.config(state=DISABLED)
    elif len(regplates) < 2:
        canvas.itemconfigure(FullWarning, state="hidden")
        saveBtn.config(state=ACTIVE)

def CheckLot(**kwargs):
    try:
        key = int(lotEnt.get())
        if "take" in kwargs:
            ParkingLots[key].TakeLot()
        elif "empty" in kwargs:
            ParkingLots[key].EmptyLot()
    except ValueError:
        CleanEntries()
        messagebox.showerror("Error", "The lot does not exist!")


ParkingLots = {
    1: ParkingLot(5, 135, 115, 65),
    2: ParkingLot(125, 135, 235, 65),
    3: ParkingLot(245, 135, 355, 65),
    4: ParkingLot(365, 135, 475, 65),
    5: ParkingLot(485, 135, 595, 65),
    6: ParkingLot(5, 215, 115, 145),
    7: ParkingLot(125, 215, 235, 145),
    8: ParkingLot(245, 215, 355, 145),
    9: ParkingLot(365, 215, 475, 145),
    10: ParkingLot(485, 215, 595, 145),
}

# def BuildLots():
#     ParkingLots = {}
#     coord = [5, 135, 115, 65]
#     key = 1
#     for i in range(1, 6):
#         ParkingLots[key] = (coord[0] + 120, coord[1], coord[2] + 120, coord[3])


regplateLbl = tk.Label(master=interfaceFrame, text="Registration number (< 7 characters)")
regplateLbl.grid(row=0, column=1)

lotLbl = tk.Label(master=interfaceFrame, text="Lot")
lotLbl.grid(row=0, column=4)

regplateEnt = tk.Entry(master=interfaceFrame, width=30)
regplateEnt.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

lotEnt = tk.Entry(master=interfaceFrame, width=5)
lotEnt.grid(row=1, column=4)

FullWarning = canvas.create_text(
    300, 20, text="Parking is full!", fill="red", font="20", state="hidden")

saveBtn = tk.Button(master=interfaceFrame, text="Save",
                    padx=5, command=lambda: CheckLot(action="take"))
saveBtn.grid(row=1, column=5, padx=5)

removeBtn = tk.Button(master=interfaceFrame, text="Remove", padx=5,
                      command=lambda: CheckLot(action="empty"))
removeBtn.grid(row=1, column=6, padx=5)


tk.mainloop()
