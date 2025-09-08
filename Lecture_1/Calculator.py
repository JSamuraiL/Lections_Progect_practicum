import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Ошибка", "Неверное выражение")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Настройка окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#232323")

# Поле ввода
entry = tk.Entry(root, font=("Arial", 24), bg="#232323", fg="white", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

buttons = [
"sqrt", "X²", "C", "/",
"7", "8", "9", "×",
"4", "5", "6", "-",
"1", "2", "3", "+",
"0", ".", "=",
]

# Описание функционала символов и их приоритетов
operators = {(1, "+", lambda x, y: x + y), (1, "-", lambda x, y: x - y),
             (2, "×", lambda x, y: x * y), (2, "/", lambda x, y: x / y)}

# Обратная польская нотация
def polish_notation():
    

def create_button(text):
    return tk.Button(
        root, text=text, font=("Arial", 18), fg="white", bg="#3b3b3b",
        width=5, height=2, bd=0, activebackground="#555555", activeforeground="white"
    )

row = 1
col = 0

for button in buttons:
    btn = create_button(button)
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()