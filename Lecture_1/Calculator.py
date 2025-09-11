import tkinter as tk
from tkinter import messagebox
import math

# Ивенты, происходящие при нажатии на кнопки
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            label.configure(text=entry.get()+"=")
            result = polish_notation(entry.get().replace("×","*"))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Ошибка", "Неверное выражение")
    elif text in wrapping_operators:
        entry.insert(0, text+"(")
        entry.insert(tk.END, ")")
    elif text == "x²":
        entry.insert(0, "(")
        entry.insert(tk.END, ")^2")
    elif text == "x^y":
        entry.insert(0, "(")
        entry.insert(tk.END, ")^")
    elif text == "|x|":
        entry.insert(0, "abs(")
        entry.insert(tk.END, ")")
    elif text == "C":
        entry.delete(0, tk.END)
        label.configure(text="")
    else:
        entry.insert(tk.END, text)

# Настройка окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#232323")

# Место для хранения формулы
label = tk.Label(root, font=("Arial", 24), bg="#232323", fg="#535353", bd=0, justify="right", anchor="e")
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
    "ln", "|x|", "0", ".", "="
]

# Описание функций (символы и мат.операции) и их приоритетов
operators = {"+": (1, lambda x, y: x + y), 
             "-": (1, lambda x, y: x - y),
             "*": (2, lambda x, y: x * y), 
             "/": (2, lambda x, y: x / y),
             "^": (3, lambda x, y: x ** y),
             "sin": (4, lambda x: math.sin(x)),
             "cos": (4, lambda x: math.cos(x)),
             "tg": (4, lambda x: math.tan(x)),
             "ctg": (4, lambda x: 1/math.tan(x)),
             "sqrt": (4, lambda x: math.sqrt(x)),
             "log": (4, lambda x: math.log10(x)),
             "ln": (4, lambda x: math.log(x)),
             "rad": (4, lambda x: math.radians(x)),
             "abs": (4, lambda x: abs(x)),
             "minus": (4, lambda x: -x)
             }

math_symbols = "1234567890."
brackets = "()"
wrapping_operators = ["log", "ln", "sin", "cos", "tg", "ctg", "sqrt", "rad", "abs"]

# Обратная польская нотация
def polish_notation(expression):

    #Парсер, принимает строку и отделяет числа от символов
    def parser_numbers(expression):
        number = ''
        letter = 0
        allow_minus = True 
        while letter < len(expression):
            symbol = expression[letter]
            # Место, где создается число
            if symbol in math_symbols:
                number += symbol
                allow_minus = False
            # Если нечисловое значение, то заканчивается создание номера, происходит сброс
            else:
                if number:
                    yield float(number)
                    number = ''
                found_function = False
                for function in wrapping_operators:
                    if expression.startswith(function, letter):
                        yield function
                        letter += len(function) - 1
                        allow_minus = True
                        found_function = True
                        break
                if not found_function:
                    if symbol == "-" and allow_minus:
                        yield "minus"
                        allow_minus = False
                    elif symbol in operators or symbol in brackets:
                        yield symbol
                    if symbol in operators or symbol == "(":
                        allow_minus = True
                    else:
                        allow_minus = False
            letter += 1
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
            # Вынос числовых значений как есть   
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
                if element in wrapping_operators or element == "minus":
                    x = elements.pop()
                    elements.append(operators[element][1](x))
                else:
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