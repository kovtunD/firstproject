from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator')

activeStr = '' # для текущего числа
stack = [] # для предыдущего числа

def calculate():
    global stack
    global Num
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '*':
        result = operand1 * operand2
    elif operation == '/':
        if not (operand2 == 0) :
            result = operand1 / operand2
    if operation == '/' and operand2 == 0 :
        Num.configure(text="error")
    else :
        Num.configure(text=str(result))

def click(text):
    global activeStr
    global stack
    global prNum
    global operation
    if text == 'C':
        stack.clear()
        activeStr = ''
        Num.configure(text='')
        prNum.configure(text='')
        operation.configure(text='')
    elif '0' <= text <= '9':
        activeStr += text
        Num.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            Num.configure(text=activeStr)
    else: # знаки операций
        #if(operation['text']
        if len(stack) >= 2:
            stack.append(Num['text'])
            calculate()
            stack.clear()
            stack.append(Num['text'])
            activeStr = ''
            prNum.configure(text=Num['text'])
            Num.configure(text='')
            operation.configure(text=text)
            if text != '=':
                stack.append(text)
            else:
                operation.configure(text='')
        else:
            if text != '=':
                stack.append(Num['text'])
                stack.append(text)
                prNum.configure(text=Num['text'])
                activeStr = ''
                Num.configure(text='')
                operation.configure(text = text)
            #else :
             #   activeStr = str(Decimal(stack.pop()))
              #  label.configure(text = activeStr)




buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           ) # "массив" с текстами кнопок

Num = Label(root, text='', width=80, height = 5, font = 'consolas 14') # строка текущего состояния
Num.grid(row=1, column=0, columnspan=4, sticky="nsew")
prNum = Label(root, text='', width=60, height = 5, font = 'consolas 14')
prNum.grid(row=0, column=0, columnspan=3)
operation = Label(root, text='', width=20, height = 5, font = 'consolas 14')
operation.grid(row = 0, column = 3) 

button = Button(root, text='C', command=lambda text='C': click(text))
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col], height = 5, font = 'consolas 14',
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 3, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()


