import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x460")
root.resizable(False, False)

# Main frame
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill="both", expand=True)

# State variables
precision = 2
fix_mode = False

# FIX label
fix_label = tk.Label(main_frame, text="Fix: 2", font=("Arial", 10))
fix_label.grid(row=0, column=0, columnspan=2, sticky="w")

# Entry display
entry = tk.Entry(main_frame, font=("Arial", 24),
                 bd=5, relief=tk.RIDGE, justify="right")
entry.grid(row=1, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

# ---------------- FUNCTIONS ---------------- #

def click(num):
    global fix_mode, precision

    # FIX mode handling
    if fix_mode:
        if num.isdigit():
            precision = int(num)
            fix_label.config(text=f"Fix: {precision}")
            fix_mode = False
        return  # stop normal input

    entry.insert(tk.END, num)

def clear():
    global fix_mode
    fix_mode = False
    entry.delete(0, tk.END)

def calculate():
    global fix_mode
    fix_mode = False

    try:
        result = eval(entry.get())

        if isinstance(result, float):
            result = round(result, precision)

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def activate_fix():
    global fix_mode
    fix_mode = True
    fix_label.config(text="Fix: _")

# ---------------- GRID CONFIG ---------------- #

for i in range(8):
    main_frame.rowconfigure(i, weight=1)
for i in range(4):
    main_frame.columnconfigure(i, weight=1)

# Button creator
def create_button(text, row, col, cmd,
                  bg=None, fg=None,
                  rowspan=1, columnspan=1):

    tk.Button(main_frame,
              text=text,
              command=cmd,
              font=("Arial", 14),
              bg=bg,
              fg=fg)\
        .grid(row=row, column=col,
              rowspan=rowspan,
              columnspan=columnspan,
              padx=5, pady=5,
              sticky="nsew")

# ---------------- BUTTONS ---------------- #

# Row 2 (brackets + controls)
create_button('(', 2, 0, lambda: click('('))
create_button(')', 2, 1, lambda: click(')'))
create_button('FIX', 2, 2, activate_fix, bg="#2196F3", fg="white")
create_button('C', 2, 3, clear, bg="red", fg="white")

# Row 3
create_button('7', 3, 0, lambda: click('7'))
create_button('8', 3, 1, lambda: click('8'))
create_button('9', 3, 2, lambda: click('9'))
create_button('/', 3, 3, lambda: click('/'))

# Row 4
create_button('4', 4, 0, lambda: click('4'))
create_button('5', 4, 1, lambda: click('5'))
create_button('6', 4, 2, lambda: click('6'))
create_button('*', 4, 3, lambda: click('*'))

# Row 5
create_button('1', 5, 0, lambda: click('1'))
create_button('2', 5, 1, lambda: click('2'))
create_button('3', 5, 2, lambda: click('3'))

# + (vertical span)
create_button('+', 5, 3, lambda: click('+'),
               rowspan=2)

# Row 6
create_button('0', 6, 0, lambda: click('0'))
create_button('.', 6, 1, lambda: click('.'))
create_button('-', 6, 2, lambda: click('-'))

# Row 7 (= full width)
create_button('=', 7, 0, calculate,
              bg="#4CAF50", fg="white", columnspan=4)

# Run
root.mainloop()