'''
                            [Random Password Generator {RPG}]
                            Programming language used --> Python  
'''
import tkinter as tk
import random
import string

def rpg():
    length = pass_len.get()
    chars = ""

    if use_uppercase.get():
        chars += string.ascii_uppercase
    if use_lowercase.get():
        chars += string.ascii_lowercase
    if use_special_chars.get():
        chars += string.punctuation
    if use_numerics.get():
        chars += string.digits

    if not chars:
        result_label.config(text="!! Error !! : Select at least one check box.")
        return

    generated_password = "".join(random.choice(chars) for _ in range(length))
    result_label.config(text=f"Password Generated : \n \n {generated_password}")


# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("600x500")  
root.resizable(False, False)

# creates label widgets with a text
input_label = tk.Label(root, text="!! Random Password Generator !!",font=("Arial",10))
input_label.pack(padx=30, pady=30)


# Password length
pass_head = tk.Label(root, text="Enter password length ", font=("Arial",10))
pass_head.pack(pady=10)
pass_len = tk.IntVar()
length_spinbox = tk.Spinbox(root, from_= 8, to_= 32, textvariable=pass_len, width = 24, font=("Arial",10))
length_spinbox.pack()

# Strength options
use_uppercase = tk.BooleanVar()
use_lowercase = tk.BooleanVar()
use_special_chars = tk.BooleanVar()
use_numerics = tk.BooleanVar()

input_label = tk.Label(root, text="(Select atleast one check box)",font=("Arial",10))
input_label.pack(padx=10, pady=20)

tk.Checkbutton(root, text="CASE 1 : Uppercase", variable=use_uppercase).pack()
tk.Checkbutton(root, text="CASE 2 : Lowercase", variable=use_lowercase).pack()
tk.Checkbutton(root, text="CASE 3 : Numeric Values", variable=use_numerics).pack()
tk.Checkbutton(root, text="CASE 4 : Special Characters", variable=use_special_chars).pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=rpg)
generate_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

'''********************END OF THE CODE********************'''