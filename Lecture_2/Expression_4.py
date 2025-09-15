import tkinter as tk

# Создание формы
root = tk.Tk()
root.title("Задание 3")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#232323")

# Рабочая область
frame = tk.Frame(root, padx=10, pady=20)
frame.pack(expand=True, fill="both", anchor="center")
frame.configure(bg="#333333")

# Стандартные настройки объектов
label_discripton = tk.Label(frame, font=20, justify="center", bg="#333333",
                            fg="white")
label_discripton.configure(text="Нажмите на кнопку")
label_answer = tk.Listbox(frame, font=20, justify="center",
                          bg="#333333", fg="white")
button = tk.Button(
    frame,
    justify="center",
    font=20,
    text="Узнать трехзначные простые числа",
    command=lambda: find_numbers()
)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=label_answer.yview)
label_answer.configure(yscrollcommand=scrollbar.set)

# Размещение объектов в рабочей зоне
label_discripton.grid(row=0, column=0, columnspan=2, sticky="ew")
label_answer.grid(row=2, column=0, sticky="nsew")
scrollbar.grid(row=2, column=1, sticky="ns")
button.grid(row=3, column=0, pady=10, sticky="nsew")


# Место подсчета
def find_numbers():
    number = 100
    numbers = []
    while number <= 999:
        before_number = 2
        is_simple = True
        while before_number < number:
            if number % before_number == 0:
                is_simple = False
                break
            before_number += 1
        if is_simple:
            numbers.append(number)
        number += 1
    for num in numbers:
        print(num)
        label_answer.insert(tk.END, num)


root.mainloop()
