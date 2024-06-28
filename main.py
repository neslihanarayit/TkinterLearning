import tkinter

# window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=500, height=700)
window.config(padx=20, pady=20)
# label
my_label = tkinter.Label(text="My Label", font=("Courier", 10, "bold"))
my_label.config(bg="light blue", fg="white")
my_label.place(x=150, y=0)

def click_button():
    print(my_entry.get())
    print(text.get("1.0", tkinter.END))

# button
my_button = tkinter.Button(text="My Button", command= click_button)
my_button.place(x=175-50, y=115)

#entry

my_entry = tkinter.Entry(width=20)
my_entry.place(x=175-88, y=150-11.5)

my_entry.update()
print(my_entry.winfo_height())
print(my_entry.winfo_width())

# text
text = tkinter.Text(width=20, height=5)
text.pack()

# scale
def scale_get(value):
    print(value)
my_scale = tkinter.Scale(from_=0, to=20, command=scale_get)
my_scale.place(x=175, y=200)

# spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = tkinter.Spinbox(from_=0, to=20, command=spinbox_selected)
my_spinbox.place(x=175, y=300)

#checkbutton
def checkbutton_selected():
    print(check_state.get())
check_state = tkinter.IntVar()
my_checkbutton = tkinter.Checkbutton(text="Check", variable=check_state, command=checkbutton_selected)
my_checkbutton.place(x=175, y=400)


# listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))
my_listbox = tkinter.Listbox()
name_list = ["A","B","C","D","E"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
my_listbox.bind('<<ListboxSelect>>', listbox_selected)
my_listbox.place(x=175, y=500)
window.mainloop()
