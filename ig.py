import tkinter as tk

def validate_number(new_value):
    if new_value.isdigit():
        return True
    else:
        return False

root = tk.Tk()

spinbox = tk.Spinbox(root, from_=0, to=100, validate="key", validatecommand=(root.register(validate_number), '%P'))
spinbox.pack()

root.mainloop()
