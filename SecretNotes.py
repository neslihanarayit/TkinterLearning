import tkinter as tk
from tkinter import messagebox

from cryptography import fernet
from cryptography.fernet import Fernet

window.title("Secret Notes ")
window.config(pady=30, padx=30)
window.minsize(width=400, height=700)

title_label = tk.Label(text="Enter Your Title")
title_label.pack()

title_entry = tk.Entry(width=20)
title_entry.pack()

secret_label = tk.Label(text="Enter Your Secret")
secret_label.pack()

secret_text = tk.Text(width=40, height=25)
secret_text.pack()

key_label = tk.Label(text="Enter Master Key")
key_label.pack()

key_entry = tk.Entry(width=20)
key_entry.pack()

key_save = {}
def opening_file():
    file = open('secret.txt','a')

def save_button():
    if title_entry.get() == "":
        var = messagebox.showwarning(title="warning", message="Please enter a title")
        print(var)
    elif secret_text.get("1.0", tk.END) == "":
        var = messagebox.showwarning(title="warning", message="Please enter a secret")
        print(var)
    elif key_entry.get() == "":
        var = messagebox.showwarning(title="warning", message="Please enter a key")
        print(var)
    else:
        opening_file()
        with open('secret.txt', mode='a') as secret_file:
            secret_file.write(title_entry.get())
            key = Fernet.generate_key()
            print(key)
            fernet = Fernet(key)
            print(fernet)
            enc_message = fernet.encrypt(secret_text.get("1.0",tk.END).encode())
            secret_file.write(f"\n {enc_message}\n")
            key_save[enc_message] = key_entry.get()
encrypt_button = tk.Button(text="Save & Encrypt", command=save_button)
encrypt_button.pack()

def decrypted_message():
    if key_entry.get() == "":
        var = messagebox.showwarning(title="warning", message="Please enter a key")
        print(var)
    elif secret_text.get("1.0", tk.END) == "":
        var = messagebox.showwarning(title="warning", message="Please enter a secret")
        print(var)
    else:
        opening_file()
        with open('secret.txt', mode='r') as secret_file:
            #if str(key_entry.get()) == key_save[secret_text.get("1.0", tk.END)]:

            passwordChosen = fernet.decrypt(secret_text.get("1.0", tk.END) )
            decryptedPasswordDB = passwordChosen.decode('utf-8')
            print(decryptedPasswordDB)
decrypt_button = tk.Button(text="Decrypt", command=decrypted_message)
decrypt_button.pack()
print(decrypted_message())


window.mainloop()
