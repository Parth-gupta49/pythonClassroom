import tkinter as tk

def on_button_click(button_text):
    current_text = entry_var.get()
    entry_var.set(current_text + button_text)

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception as e:
        entry_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: on_button_click(b) if b != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', padx=20, pady=20, command=clear_entry).grid(row=row_val, column=col_val)

root.mainloop()
































# import tkinter as tk


# root = tk.Tk()  
# root.title("Standard Calculator")


# e = tk.Entry(root,width=35)
# e.grid(row=0, column=0, columnspan=3, padx=12, pady=12)


# def buttonClick(num):
#     temp = e.get()  
#     e.delete(0, tk.END)  
#     e.insert(0, temp + num)


# def buttonClear():  
#     e.delete(0, tk.END)


# def buttonGet(oper):  
#     global num1, math  
#     num1 = e.get()  
#     math = oper  
#     e.insert(tk.END, math)
#     try:
#         num1 = float(num1)
#     except ValueError:  
#         buttonClear()


# def buttonEqual():
#     inp = e.get()  
#     num2 = float(inp[inp.index(math) + 1:])  
#     e.delete(0, tk.END)
#     if math == '+':
#         e.insert(0, str(num1 + num2))
#     elif math == '-':
#         e.insert(0, str(num1 - num2))
#     elif math == 'x':  
#         e.insert(0, str(num1 * num2))
#     elif math == '/':  
#         try:
#             e.insert(0, str(num1 / num2))
#         except ZeroDivisionError:
#             e.insert(0, 'Undefined')


# b1 = tk.Button(root,text='1',padx=40,pady=10,command=lambda: buttonClick('1'),font='Calibri 12')
# b2 = tk.Button(root,text='2',padx=40,pady=10,command=lambda: buttonClick('2'),font='Calibri 12')
# b3 = tk.Button(root,text='3',padx=40,pady=10,command=lambda: buttonClick('3'),font='Calibri 12')
# b4 = tk.Button(root, text='4',padx=40,pady=10,command=lambda: buttonClick('4'),font='Calibri 12')
# b5 = tk.Button(root,text='5',padx=40,pady=10,command=lambda: buttonClick('5'),font='Calibri 12')
# b6 = tk.Button(root,text='6',padx=40,pady=10,command=lambda: buttonClick('6'),font='Calibri 12')
# b7 = tk.Button(root,text='7',padx=40,pady=10,command=lambda: buttonClick('7'),font='Calibri 12')
# b8 = tk.Button(root,text='8',padx=40,pady=10,command=lambda: buttonClick('8'),font='Calibri 12')
# b9 = tk.Button(root,text='9',padx=40,pady=10,command=lambda: buttonClick('9'),font='Calibri 12')
# b0 = tk.Button(root,text='0',padx=40,pady=10,command=lambda: buttonClick('0'),font='Calibri 12')
# bdot = tk.Button(root,text='.',padx=41,pady=10,command=lambda: buttonClick('.'),font='Calibri 12')
# badd = tk.Button(root,text='+',padx=29,pady=10,command=lambda: buttonGet('+'),font='Calibri 12')
# bsub = tk.Button(root,text='-',padx=30,pady=10,command=lambda: buttonGet('-'),font='Calibri 12')
# bmul = tk.Button(root,text='x',padx=30,pady=10,command=lambda: buttonGet('x'),font='Calibri 12')
# bdiv = tk.Button(root,text='/',padx=30.5,pady=10,command=lambda: buttonGet('/'),font='Calibri 12')
# bclear = tk.Button(root,text='AC',padx=20,pady=10,command=buttonClear,font='Calibri 12')
# bequal = tk.Button(root,text='=',padx=39,pady=10,command=buttonEqual,font='Calibri 12')


# b1.grid(row=3, column=0)
# b2.grid(row=3, column=1)
# b3.grid(row=3, column=2)
# badd.grid(row=3, column=3)


# b4.grid(row=2, column=0)
# b5.grid(row=2, column=1)
# b6.grid(row=2, column=2)
# bmul.grid(row=2, column=3)


# b7.grid(row=1, column=0)
# b8.grid(row=1, column=1)
# b9.grid(row=1, column=2)
# bdiv.grid(row=1, column=3)


# b0.grid(row=4, column=0)
# bdot.grid(row=4, column=1)
# bequal.grid(row=4, column=2)
# bsub.grid(row=4, column=3)


# bclear.grid(row=0, column=3)


# root.mainloop()