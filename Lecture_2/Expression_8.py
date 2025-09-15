import math
import tkinter as tk

# Создание формы
root = tk.Tk()
root.title("Задание 3")
root.geometry("350x350")
root.resizable(False, False)
root.configure(bg="#232323")

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
label_answer = tk.Label(frame, font=20, justify="center",
                        bg="#333333", fg="white")
entry_a = tk.Entry(frame, justify="center", font=20)
entry_b = tk.Entry(frame, justify="center", font=20)
entry_c = tk.Entry(frame, justify="center", font=20)
button = tk.Button(
    frame,
    justify="center",
    font=20,
    text="Тупой ли треугольник",
    command=lambda: find_numbers(int(entry_a.get()), int(entry_b.get()),
                                 int(entry_c.get()))
)

# Размещение объектов в рабочей зоне
label_a.grid(row=0, column=0, sticky="ew")
entry_a.grid(row=0, column=1, pady=20, sticky="nsew")
label_b.grid(row=1, column=0, sticky="ew")
entry_b.grid(row=1, column=1, pady=20, sticky="nsew")
label_c.grid(row=2, column=0, sticky="ew")
entry_c.grid(row=2, column=1, pady=20, sticky="nsew")
label_answer.grid(row=4, column=0, columnspan=2, sticky="nsew")
button.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")


# Место подсчета
def find_numbers(a, b, c):
    # Нет учета, что треугольника может не быть
    def F(fst, sec, trd):
        values = [fst, sec, trd]
        max_value_step = max(values) ** 2
        values.remove(math.sqrt(max_value_step))
        summakv = 0
        for val in values:
            summakv += val ** 2
        if summakv < max_value_step:
            return True
        else:
            return False
    if F(a, b, c):
        label_answer.configure(text="Треугольник тупоугольный")
    else:
        label_answer.configure(text="Треугольник не тупоугольный")


root.mainloop()
