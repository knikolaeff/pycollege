import tkinter as tk

regplates = []
window = tk.Tk()
interfaceFrame = tk.Frame(window)
interfaceFrame.pack()
displayFrame = tk.Frame(window)
displayFrame.pack()

regplateLbl = tk.Label(master=interfaceFrame, text="Registration number")
regplateLbl.grid(row=0, column=2)

warningLbl = tk.Label(master=interfaceFrame, text="Full!", fg="red")

regplateEnt = tk.Entry(master=interfaceFrame, width=50)
regplateEnt.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

regplateSave = tk.Button(master=interfaceFrame, text="Save", padx=5, command=lambda: saveplate(regplateEnt.get())) 
regplateSave.grid(row=1, column=5, padx=5)

regplateInfo = tk.Button(master=interfaceFrame, text="Display all the cars", command=lambda: displayplates())
regplateInfo.grid(row=1, column=6, padx=5)

def displayplates():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    for i in regplates:
        plate = tk.Label(master=displayFrame, text=i)
        plate.pack()


def saveplate(plate):
    regplates.append(plate)
    regplateEnt.delete(0, tk.END)
  
    if len(regplates) == 10:
        warningLbl.grid(row=0, column=5)

tk.mainloop()