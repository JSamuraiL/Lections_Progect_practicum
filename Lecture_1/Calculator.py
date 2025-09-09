import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = polish_notation(entry.get().replace("×","*"))
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
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#232323")

# Место для хранения формулы
label = tk.Label(root, text="test", font=("Arial", 24), bg="#232323", fg="#535353", bd=0, justify="right", anchor="e")
label.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 0), sticky="ew")
# Поле ввода
entry = tk.Entry(root, font=("Arial", 24), bg="#232323", fg="white", bd=0, justify="right")
entry.grid(row=1, column=0, columnspan=5, padx=10, pady=(0, 10), sticky="ew")

buttons = [
    "sin", "cos", "tg", "ctg", "rad",
    "(", ")", "x²", "C", "/",
    "sqrt", "7", "8", "9", "×",
    "x^y", "4", "5", "6", "-",
    "log", "1", "2", "3", "+",
    "ln", "+/-", "0", ".", "="
]

# Описание функций (символы и мат.операции) и их приоритетов
operators = {"+": (1, lambda x, y: x + y), 
             "-": (1, lambda x, y: x - y),
             "*": (2, lambda x, y: x * y), 
             "/": (2, lambda x, y: x / y)}

# Обратная польская нотация
def polish_notation(expression):

    #Парсер, принимает строку и отделяет числа от символов
    def parser_numbers(expression):
        number = ''
        for symbal in expression:
            # Место, где создается число
            if symbal in '1234567890.':
                number += symbal
            # Если нечисловое значение, то заканчивается создание номера, происходит сброс
            else:
                if number:
                    yield float(number)
                    number = ''
                if symbal in operators or symbal in '()':
                    yield symbal
        # Вывод числа при его создании
        if number:
            yield float(number)

    # Парсер, принимает прошлое выражение и разносит функции по приоритету
    def parser_functions(parsed_expression):
        elements = []
        for element in parsed_expression:
            # Если выражение вне скобок, добавляем его справа от списка:
            if element in operators:
                 while (elements and elements[-1] != '(' and 
                       operators[element][0] <= operators[elements[-1]][0]):
                    yield elements.pop()
                 elements.append(element)
            # Если нашлась закрывающаяся скобка, проходимся по всем элементам в обратном порядке до открывающейся скобки    
            elif element == ")":
                while elements:
                    check_bracket = elements.pop()
                    if check_bracket == "(":
                        break
                    yield check_bracket
            # Если скобка открывается, добавляется к списку элементов
            elif element == "(":
                elements.append(element)
            # Вынос числовых значений вне списка    
            else:
                yield element
        while elements:
            yield elements.pop()
    
    # Функция подсчета на основе польской нотации
    def calculation(polish_expression):
        elements = []
        for element in polish_expression:
            # Если операция, то идет ее выполнение по инструкции
            if element in operators:
                y, x = elements.pop(), elements.pop()
                elements.append(operators[element][1](x, y))
            # Если число, то идет его фиксация для подсчета
            else:
                elements.append(element)
        # Результат подсчета - единственный элемент списка
        return elements[0]
    
    # Подсчет по польской нотации
    return calculation(parser_functions(parser_numbers(expression)))
    
    
    
# Создание кнопки
def create_button(text):
    btn = tk.Button(
        root, text=text, font=("Arial", 14), fg="white", width=5, height=2, bd=0, activebackground="#555555", 
        activeforeground="white"
    )    
    if text == "=":
        btn.configure(bg="#678afc", activebackground="#80B9FF")
    else:
        btn.configure(bg="#3b3b3b")
    return btn

row = 2
col = 0

for button in buttons:
    btn = create_button(button)
    btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 4:
        col = 0
        row += 1

for i in range(7):
    root.grid_columnconfigure(i, weight=1)
for i in range(8):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()