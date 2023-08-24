import tkinter as tk

class Screen:

    def __init__(self):
        self.window = tk.Tk()
        self.label_miles = tk.Label()
        self.label_equal = tk.Label()
        self.label_km = tk.Label()
        self.label_calculated = tk.Label()
        self.entry_miles = tk.Entry(width=10)
        self.button = tk.Button()
        self.window_setup()

    def window_setup(self):
        self.window.title("mile to km converter")
        self.window.minsize(width=60, height=30)

        self.label_miles.config(text="miles")
        self.label_miles.grid(padx=10, pady=10, column=2, row=0)

        self.label_equal.config(text="is equal to: ")
        self.label_equal.grid(padx=10, pady=10, column=0, row=1)

        self.label_km.config(text="km")
        self.label_km.grid(padx=10, pady=10, column=2, row=1)

        self.label_calculated.config(text="0")
        self.label_calculated.grid(padx=10, pady=10, column=1, row=1)

        self.entry_miles.insert(index=0, string="0")
        self.entry_miles.grid(padx=10, pady=10, column=1, row=0)

        self.button.config(text="Calculate", command=self.calculate)
        self.button.grid(column=1, row=2)

    def calculate(self):
        calculated = round(int(self.entry_miles.get())*1.6, 2)
        self.label_calculated.config(text=str(calculated))
