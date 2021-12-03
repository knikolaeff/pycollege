import tkinter as tk
from tkinter.constants import END


window = tk.Tk()
window.title("Parking App")

interfaceFrame = tk.Frame(window)
interfaceFrame.pack()

displayFrame = tk.Frame(window)
displayFrame.pack()

canvas = tk.Canvas(master=displayFrame, width=600, height=230)
canvas.pack()


class ParkingLot:
    def __init__(self, x1, y1, x2, y2, number):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.number = number
        canvas.create_rectangle(x1, y1, x2, y2)
        canvas.create_text(x1 + 55, y2 + 10, text="Lot %s" % (number))

    def TakeLot(self):
        self.regplate = canvas.create_text(self.x1 + 55, self.y2 +
                                           40, text=regplateEnt.get())
        regplateEnt.delete(0, END)
        lotEnt.delete(0, END)

    def EmptyLot(self):
        canvas.delete(self.regplate)
        regplateEnt.delete(0, END)
        lotEnt.delete(0, END)


parkingLots = {
    1: ParkingLot(5, 135, 115, 65, 1),
    2: ParkingLot(125, 135, 235, 65, 2),
    3: ParkingLot(245, 135, 355, 65, 3),
    4: ParkingLot(365, 135, 475, 65, 4),
    5: ParkingLot(485, 135, 595, 65, 5),
    6: ParkingLot(5, 215, 115, 145, 6),
    7: ParkingLot(125, 215, 235, 145, 7),
    8: ParkingLot(245, 215, 355, 145, 8),
    9: ParkingLot(365, 215, 475, 145, 9),
    10: ParkingLot(485, 215, 595, 145, 10),
}

regplateLbl = tk.Label(master=interfaceFrame, text="Registration number")
regplateLbl.grid(row=0, column=1)

lotLbl = tk.Label(master=interfaceFrame, text="Lot")
lotLbl.grid(row=0, column=4)

warningLbl = tk.Label(master=interfaceFrame, text="Full!", fg="red")

regplateEnt = tk.Entry(master=interfaceFrame, width=30)
regplateEnt.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

lotEnt = tk.Entry(master=interfaceFrame, width=5)
lotEnt.grid(row=1, column=4)

saveBtn = tk.Button(master=interfaceFrame, text="Save",
                    padx=5, command=lambda: parkingLots[int(lotEnt.get())].TakeLot())
saveBtn.grid(row=1, column=5, padx=5)

removeBtn = tk.Button(master=interfaceFrame, text="Remove", padx=5,
                      command=lambda: parkingLots[int(lotEnt.get())].EmptyLot())
removeBtn.grid(row=1, column=6, padx=5)

tk.mainloop()
