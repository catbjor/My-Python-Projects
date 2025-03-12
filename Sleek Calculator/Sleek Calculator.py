import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear():
    display.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Sleek Calculator")
window.configure(bg="#73494A")  # Set lavender background color

# Create the display
display = ttk.Entry(window, font=("Poppins", 12))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons with glass effect
style = ttk.Style()
style.configure("TButton", font=("Poppins", 16), background="#FFFFFF", relief="flat", borderwidth=0)
style.map("TButton", background=[("pressed", "#FFFFFF"), ("active", "#E0E0E0")])

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3)
]

for button in buttons:
    text, row, col = button
    button = ttk.Button(window, text=text, command=lambda text=text: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create the "=" button with glass effect and bind the calculate() function
equal_button = ttk.Button(window, text="=", command=calculate)
equal_button.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

# Create clear button with glass effect
clear_button = ttk.Button(window, text="C", command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

# Configure grid to center the calculator and make it responsive
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Run the main loop
window.mainloop()
