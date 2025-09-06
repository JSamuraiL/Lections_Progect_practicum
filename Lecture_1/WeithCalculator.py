import tkinter as tk
from tkinter import messagebox

# Функция подсчета ИМТ 
def calculate_index(height, weight):
    kg = weight
    m = height/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)

    if bmi <= 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi <= 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi <= 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  

# Функция исключения нечисловых значений
def validate_digit_input(new_value): 
    if new_value == "": 
        return True 
    elif new_value.isdigit(): 
        return True 
    else: 
        return False 

# Создание формы калькулятора
root = tk.Tk()
root.title("Калькулятор индекса массы тела")
root.geometry("500x300")
root.configure(bg="#1e1e1e")
root.resizable(False, False)
validate_digit_command = root.register(validate_digit_input)

# Надпись с описанием действий
disc_message = tk.Label(root,text="Введите свои данные", font=("Arial", 24), bg="#1e1e1e", fg="white", bd=0,anchor="center")
disc_message.pack(pady=40)

# Блок взаимодействия с формой
frame = tk.Frame(
   root,
   padx=10,
   pady=10
)
frame.pack(expand=True, anchor="n")
frame.configure(bg="#333333")

# Блок веса
disc_weight = tk.Label(frame, text="Вес (в кг):")
disc_weight.grid(row=1, column=0)
disc_weight.configure(bg="#333333",fg="white", font=20)

weigth = tk.Entry(frame, validate="key", validatecommand=(validate_digit_command,"%P"))
weigth.grid(row=1, column=1)
weigth.configure(font=20)

#Блок роста
disc_height = tk.Label(frame, text="Рост (в см):")
disc_height.grid(row=2, column=0,pady=10)
disc_height.configure(bg="#333333",fg="white", font=20)

height = tk.Entry(frame, validate="key", validatecommand=(validate_digit_command,"%P"))
height.grid(row=2, column=1,pady=10)
height.configure(font=20)

#Кнопка подсчета
calc_index = tk.Button(frame, text="Подсчитать", command=lambda: calculate_index(int(height.get()), int(weigth.get())))
calc_index.grid(row=3, column=0, columnspan=2)
calc_index.configure(font=20)

root.mainloop()