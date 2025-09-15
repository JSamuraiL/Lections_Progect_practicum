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
root.title("Задание 3")
root.geometry("300x450")
root.resizable(False, False)
root.configure(bg="#232323")
validate_digit_command = root.register(validate_digit_input)

# Рабочая область
frame = tk.Frame(root, padx=10, pady=20)
frame.pack(expand=True, fill="both", anchor="center")
frame.configure(bg="#333333")

# Стандартные настройки объектов
label_discripton = tk.Label(frame, font=20, justify="center", bg="#333333",
                            fg="white")
label_discripton.configure(text="Введите верхнее значение n")
label_answer = tk.Listbox(frame, font=20, justify="center",
                          bg="#333333", fg="white")
entry = tk.Entry(frame, justify="center", font=20, validate="key",
                 validatecommand=(validate_digit_command, "%P"))
button = tk.Button(
    frame,
    justify="center",
    font=20,
    text="Найти числа",
    command=lambda: find_numbers(entry.get())
)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=label_answer.yview)
label_answer.configure(yscrollcommand=scrollbar.set)

# Размещение объектов в рабочей зоне
label_discripton.grid(row=0, column=0, columnspan=2, sticky="ew")
entry.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")
label_answer.grid(row=2, column=0, sticky="nsew")
scrollbar.grid(row=2, column=1, sticky="ns")
button.grid(row=3, column=0, pady=10, sticky="nsew")


# Место подсчета
def find_numbers(n):
    try:
        label_answer.delete(0, tk.END)
        if n == "" or int(n) == 0:
            raise ValueError("Пустое/нулевое значение в одной из строк")
        n_number = int(n)
        number = 1
        numbers = []
        while number <= n_number:
            is_divine = True
            for n_element in n:
                digit = int(n_element)
                if digit != 0 and number % digit != 0:
                    is_divine = False
                    break
            if is_divine:
                numbers.append(number)
            number = number + 1
        for num in numbers:
            label_answer.insert(tk.END, num)
    except Exception as e:
        messagebox.showerror("Ошибка", e)


root.mainloop()
