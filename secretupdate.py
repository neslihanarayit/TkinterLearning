import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

window = tk.Tk()
window.title("Secret Notes")
window.config(pady=30, padx=30)
window.minsize(width=400, height=700)

title_label = tk.Label(text="Enter Your Title")
title_label.pack()

title_entry = tk.Entry(width=20)
title_entry.pack()

secret_label = tk.Label(text="Enter Your Secret")
secret_label.pack()

secret_text = tk.Text(width=40, height=10)
secret_text.pack()

key_label = tk.Label(text="Enter Master Key")
key_label.pack()

key_entry = tk.Entry(width=20)
key_entry.pack()

key_save = {}

def save_button():
    if title_entry.get() == "":
        messagebox.showwarning(title="Warning", message="Please enter a title")
        return
    if secret_text.get("1.0", tk.END).strip() == "":
        messagebox.showwarning(title="Warning", message="Please enter a secret")
        return
    if key_entry.get() == "":
        messagebox.showwarning(title="Warning", message="Please enter a key")
        return

    else:
        key = Fernet.generate_key()
        fernet = Fernet(key)


        enc_message = fernet.encrypt(secret_text.get("1.0", tk.END).encode())

        with open('secret.txt', mode='a') as secret_file:
            secret_file.write(f"{title_entry.get()}:{enc_message.decode('utf-8')}\n")
        with open('secret_keys.txt', mode='a') as secret_key_file:
            secret_key_file.write(f"{key_entry.get()} : {key.decode('utf-8')}\n")






def decrypted_message():
    if key_entry.get() == "":
        messagebox.showwarning(title="Warning", message="Please enter a key")
        return
    else:
        with open("secret_keys.txt", mode="r") as secret_keys_file:
            for line in secret_keys_file:
                if line.startswith(key_entry.get()):
                    parts = line.split(":")
                    key = parts[1].strip()
                    fernet = Fernet(key)
                    # print(f"key : { key},")

                    try:
                        decrypted_message = fernet.decrypt(secret_text.get("1.0",tk.END)).decode('utf-8')
                        messagebox.showinfo(title="Decrypted Message", message=decrypted_message)
                    except Exception as e:
                        messagebox.showerror(title="Decryption Error", message="Failed to decrypt message")





encrypt_button = tk.Button(text="Save & Encrypt", command=save_button)
encrypt_button.pack()

decrypt_button = tk.Button(text="Decrypt", command=decrypted_message)
decrypt_button.pack()

window.mainloop()
