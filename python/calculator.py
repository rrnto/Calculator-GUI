import tkinter as tk
from tkinter import Toplevel


def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return None
    return a / b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b


selected_operation = "+"   # default


def open_icon_menu():
    """Creates a tiny pop-up window with icon options."""
    global menu_win

    # If menu is already open, close it
    if 'menu_win' in globals() and menu_win.winfo_exists():
        menu_win.destroy()

    # Create a popup near the button
    menu_win = Toplevel(root)
    menu_win.overrideredirect(True) 
    menu_win.configure(bg="#1e1e2e")

    # position next to operation button
    x = op_button.winfo_rootx()
    y = op_button.winfo_rooty() + op_button.winfo_height()
    menu_win.geometry(f"+{x}+{y}")

    # icons for operations
    icons = [
        ("+", "➕"),
        ("-", "➖"),
        ("×", "✖"),
        ("÷", "➗")
    ]

    for op, icon in icons:
        btn = tk.Button(
            menu_win,
            text=icon,
            font=("Arial", 18),
            width=3,
            bg="#45475a",
            fg="white",
            bd=0,
            activebackground="#89b4fa",
            command=lambda o=op, i=icon: select_operation(o, i)
        )
        btn.pack(fill="x")


def select_operation(op, icon):
    """Updates selected operation AND button icon."""
    global selected_operation

    selected_operation = op
    op_button.config(text=icon)

    # close the dropdown menu
    if 'menu_win' in globals():
        menu_win.destroy()


def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        result_label.config(text="❌ Invalid number!", fg="red")
        return

    if selected_operation == "+":
        result = addition(a, b)
    elif selected_operation == "-":
        result = subtraction(a, b)
    elif selected_operation == "×":
        result = multiplication(a, b)
    elif selected_operation == "÷":
        result = division(a, b)
        if result is None:
            result_label.config(text="❌ Division by zero!", fg="red")
            return

    result_label.config(text=f"Result: {result:.4f}", fg="white")



# ================= GUI =================

root = tk.Tk()
root.title("Icon Dropdown Calculator")
root.geometry("500x300")
root.configure(bg="#1e1e2e")
root.resizable(False, False)


title = tk.Label(
    root,
    text="Icon Dropdown Calculator",
    font=("Arial", 20, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
title.pack(pady=20)


input_frame = tk.Frame(root, bg="#1e1e2e")
input_frame.pack(pady=10)


entry_a = tk.Entry(input_frame, font=("Arial", 16), width=7, justify="center")
entry_a.grid(row=0, column=0, padx=10)


op_button = tk.Button(
    input_frame,
    text="➕",
    font=("Arial", 20),
    bg="#45475a",
    fg="white",
    width=3,
    bd=0,
    command=open_icon_menu
)
op_button.grid(row=0, column=1, padx=10)


entry_b = tk.Entry(input_frame, font=("Arial", 16), width=7, justify="center")
entry_b.grid(row=0, column=2, padx=10)


# Calculate button
calc_button = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 16),
    bg="#89b4fa",
    fg="black",
    activebackground="#74a0e6",
    activeforeground="white",
    command=calculate
)
calc_button.pack(pady=20)


# Result label
result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 16),
    bg="#1e1e2e",
    fg="white"
)
result_label.pack(pady=10)


root.mainloop()
