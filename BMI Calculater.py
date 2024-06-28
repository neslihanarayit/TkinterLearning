import tkinter as tk
window = tk.Tk()
window.title("BMI Calculater")
window.minsize(width=300, height=300)
window.config(padx=30,pady=30)

weight_text = tk.Label(text="Enter Your Weight (kg)")
weight_text.config(font=("Ariel",10,"normal"))
weight_text.pack()

def kg_entry_take():

    try:
        return int(kg_entry.get())
    except ValueError as err:
        print("Please write your weight in numbers")


kg_entry = tk.Entry(width=15)
kg_entry.pack()

height_text = tk.Label(text="Enter Your Height (cm)")
height_text.config(font=("Ariel",10,"normal"))
height_text.pack()

def cm_entry_take():
    try:
        return int(cm_entry.get())
    except ValueError as err:
        print("Please write your height in numbers")

cm_entry = tk.Entry(width=15)
cm_entry.pack()

def calculation():
    kg = kg_entry_take()
    cm = cm_entry_take()
    result = kg / ((cm/100) * (cm/100))
    if result < 18.4:
        print("You are underweight!")
    elif result >= 19.4 and result < 24.9:
        print("You are in normal weight")
    elif result >= 24.9 and result < 30.9:
        print("You are overweight!")
    else:
        print("You might be obese!!!")
Calculate = tk.Button(text="Calculate", bg="light green", command=calculation)
Calculate.pack()


window.mainloop()
