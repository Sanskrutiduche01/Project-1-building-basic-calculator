import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception:
        clear_field()
        text_result.insert(1.0, "error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x375")

# Display for the calculation
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=4)

# Button Layout
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, command=evaluate_calculation, width=5, font=("Arial", 18))
    elif text == "C":
        btn = tk.Button(root, text=text, command=clear_field, width=5, font=("Arial", 18))
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 18))
    btn.grid(row=row, column=col)

root.mainloop()