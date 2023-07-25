import tkinter as tk
# Create the main application window
root = tk.Tk()
root.title(" Codsoft Task-1: Calculator")

# Entry widget to display the calculations
record = tk.Entry(root, width=25, font=("Arial Narrow", 22))
record.grid(row=0, column=0, columnspan=4, padx=12, pady=12)

# Buttons
buttons = [
    ("C", 1, 0), ("/", 1, 2), ("del", 1, 1), 
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 1, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 2, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 3, 3),
    ("0", 5, 0), ("00", 5,1), (".", 5, 2), ("=", 5, 3), 
]
def click_button(event):
    user_input = event.widget.cget("text")  
    if user_input == "=":
        try:
            result = eval(record.get())
            record.delete(0, tk.END)
            record.insert(tk.END, str(result))
        except Exception as e:
            record.delete(0, tk.END)
            record.insert(tk.END, "Can not Divide by 0")
    elif user_input == "C":
        record.delete(0, tk.END)
    elif user_input == "del":
        present_value = record.get()
        new_value = present_value[:-1]  # Remove the last character
        record.delete(0, tk.END)
        record.insert(tk.END, new_value)
    else:                              
        record.insert(tk.END, user_input)

for (user_input, row, col) in buttons:
    button = tk.Button(root, text=user_input, font=("Arial Narrow", 17), relief="ridge")
    button.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")
    button.bind("<Button-1>", click_button)

# Make the columns and rows expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
