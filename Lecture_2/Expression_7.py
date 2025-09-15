import tkinter as tk
from tkinter import messagebox


# Функция исключения нечисловых значений
def validate_digit_input(new_value):
    if new_value == "":
        return True
    elif new_value.isdigit():
        return True
    else:
        return False


# Создание формы
root = tk.Tk()
root.title("Задание 7")
root.geometry("350x400")
root.resizable(False, False)
root.configure(bg="#232323")
validate_digit_command = root.register(validate_digit_input)

# Рабочая область
frame = tk.Frame(root, padx=10, pady=20)
frame.pack(expand=True, fill="both", anchor="center")
frame.configure(bg="#333333")

# Стандартные настройки объектов
label_a = tk.Label(frame, font=20, justify="center", bg="#333333", fg="white")
label_a.configure(text="Введите a")
label_b = tk.Label(frame, font=20, justify="center", bg="#333333", fg="white")
label_b.configure(text="Введите b")
label_c = tk.Label(frame, font=20, justify="center", bg="#333333", fg="white")
label_c.configure(text="Введите c")
label_d = tk.Label(frame, font=20, justify="center", bg="#333333", fg="white")
label_d.configure(text="Введите d")
label_answer = tk.Label(frame, font=20, justify="center",
                        bg="#333333", fg="white")
entry_a = tk.Entry(frame, justify="center", font=20, validate="key",
                   validatecommand=(validate_digit_command, "%P"))
entry_b = tk.Entry(frame, justify="center", font=20, validate="key",
                   validatecommand=(validate_digit_command, "%P"))
entry_c = tk.Entry(frame, justify="center", font=20, validate="key",
                   validatecommand=(validate_digit_command, "%P"))
entry_d = tk.Entry(frame, justify="center", font=20, validate="key",
                   validatecommand=(validate_digit_command, "%P"))
button = tk.Button(
    frame,
    justify="center",
    font=20,
    text="Есть ли треугольник",
    command=lambda: find_numbers(entry_a.get(), entry_b.get(),
                                 entry_c.get(), entry_d.get())
)

# Размещение объектов в рабочей зоне
label_a.grid(row=0, column=0, sticky="ew")
entry_a.grid(row=0, column=1, pady=20, sticky="nsew")
label_b.grid(row=1, column=0, sticky="ew")
entry_b.grid(row=1, column=1, pady=20, sticky="nsew")
label_c.grid(row=2, column=0, sticky="ew")
entry_c.grid(row=2, column=1, pady=20, sticky="nsew")
label_d.grid(row=3, column=0, sticky="ew")
entry_d.grid(row=3, column=1, pady=20, sticky="nsew")
label_answer.grid(row=4, column=0, columnspan=2, sticky="nsew")
button.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")


# Место подсчета
def find_numbers(a, b, c, d):
    try:
        if a == "" or b == "" or c == "" or d == "" or \
                int(a) == 0 or int(b) == 0 or int(c) == 0 or int(d) == 0:
            raise ValueError("Пустое/нулевое значение в одной из строк")
        a, b, c, d = int(a), int(b), int(c), int(d)

        def F(fst, sec, trd):
            if fst + sec >= trd and fst + trd >= sec and sec + trd >= fst:
                return True
            else:
                return False
        if F(a, b, c) or F(b, c, d) or F(a, b, d) or F(a, c, d):
            label_answer.configure(text="YES")
        else:
            label_answer.configure(text="NO")
    except Exception as e:
        messagebox.showerror("Ошибка", e)


root.mainloop()
