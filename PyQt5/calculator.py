import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Cool Calculator")
        master.geometry("300x400")
        master.configure(bg="#2C3E50")

        self.equation = tk.StringVar()
        self.entry_value = ''

        # Create the display
        entry = tk.Entry(master, textvariable=self.equation, justify='right', font=('Arial', 20))
        entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")
        entry.configure(bg="#34495E", fg="white", bd=0, highlightthickness=1, highlightcolor="#3498DB")

        # Button layout
        buttons = [
            'C', '←', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '±', '0', '.', '='
        ]

        # Create buttons
        row_val = 1
        col_val = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=5, height=2, font=('Arial', 14),
                      bg="#34495E", fg="white", activebackground="#2980B9", bd=0,
                      highlightthickness=1, highlightcolor="#3498DB").grid(row=row_val, column=col_val, padx=2, pady=2)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.entry_value)
                self.equation.set(result)
            except:
                messagebox.showerror("Error", "Invalid Input")
                self.equation.set("")
            self.entry_value = str(result)
        elif key == 'C':
            self.entry_value = ''
            self.equation.set("")
        elif key == '←':
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)
        elif key == '±':
            if self.entry_value and self.entry_value[0] == '-':
                self.entry_value = self.entry_value[1:]
            else:
                self.entry_value = '-' + self.entry_value
            self.equation.set(self.entry_value)
        else:
            self.entry_value += str(key)
            self.equation.set(self.entry_value)

root = tk.Tk()
calculator = Calculator(root)

# Bind keyboard events
root.bind('<Return>', lambda event: calculator.click('='))
root.bind('<BackSpace>', lambda event: calculator.click('←'))
root.bind('<Escape>', lambda event: calculator.click('C'))

root.mainloop()