from tkinter import *


def mile_to_km():
    mile = float(mile_input.get())
    km = mile * 1.609
    kilometer_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calc_button = Button(text="calculate", command=mile_to_km)
calc_button.grid(column=1, row=2)

window = mainloop()
