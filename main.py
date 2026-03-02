import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password

def generate():
    try:
        length = int(length_entry.get())
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_numbers, use_symbols)
        result_label.config(text=password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter Length:").pack()

length_entry = tk.Entry(root)
length_entry.pack()

numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()