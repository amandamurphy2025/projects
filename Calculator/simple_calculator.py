import tkinter as tk 

calculation = ""

def add_to_calculation(symbol):
    global calculation

    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        calculation = ""
    except:
        clear_field()
        text_result.inset(1.0, "Error")

def clear_field():
    global calculation

    calculation = ""
    text_result.delete(1.0, "end")

#declare GUI dimensions, etc. Bookended by creating object and running mainloop
root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=20, font=("Arial", 24))
text_result.grid(row=0, columnspan=5)

#add number buttons
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

#add calculation buttons: + - x / ( ) = clear
btn_p = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_p.grid(row=2, column=4)

btn_m = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_m.grid(row=3, column=4)

btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=4, column=4)

btn_d = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_d.grid(row=5, column=4)

btn_l = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_l.grid(row=5, column=1)

btn_r = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_r.grid(row=5, column=3)

btn_c = tk.Button(root, text="clear", command=lambda: clear_field(), width=10, font=("Arial", 14))
btn_c.grid(row=6, column=1, columnspan=2)

btn_e = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width=10, font=("Arial", 14))
btn_e.grid(row=6, column=3, columnspan=2)

root.mainloop()
