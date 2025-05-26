import tkinter as tk

base = tk.Tk()
base.geometry("180x200")
base.title("Counter")

x = 0

def plus():
    global x
    x += 1
    val.config(text=str(x),fg="Green")

def minus():
    global x
    x -= 1
    val.config(text=str(x),fg="Blue")

def reset():
    global x
    x = 0
    val.config(text=str(x),fg="Red")

val = tk.Label(base, text=str(x), font=("Arial", 24), fg="blue")
val.grid(row=0, column=0, columnspan=3, pady=20)

inc = tk.Button(base, text="+", width=5, font=("Arial", 12), command=plus)
inc.grid(row=1, column=0, padx=15)

dec = tk.Button(base, text="-", width=5, font=("Arial", 12), command=minus)
dec.grid(row=1, column=2, padx=10)

res = tk.Button(base, text="Reset", width=10, font=("Arial", 12), command=reset)
res.grid(row=2, column=0, columnspan=3, pady=20)

base.mainloop()
