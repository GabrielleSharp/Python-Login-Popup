import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

stored_username="AdminKev1n"
stored_password="97531leuveueu"


def validate_password(new_pwd):
    if len(new_pwd) < 8 or len(new_pwd) > 16:
        return False, "Password must be between 8-16 characters long."
    
    if not any(ch.isdigit() for ch in new_pwd):
        return False, "Password must contain at least one number."
    
    if not any(ch.isupper() for ch in new_pwd):
        return False, "Password must contain at least one uppercase letter."
    
    symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
    if not any(ch in symbols for ch in new_pwd):
        return False, "Password must contain at least one symbol."
    return True, "Password is valid." 

def validate_username(new_usn):
    if len(new_usn) < 5:
        return False, "Username must be longer than 5 characters."
    
    if not any(ch.isdigit() for ch in new_usn):
        return False, "Username must contain at least one number."
    
    if not any(ch.isupper() for ch in new_usn):
        return False, "Username must contain at least one uppercase letter."
    
    symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
    if any(ch in symbols for ch in new_usn):
        return False, "Username cannot contain any symbols."
    return True, "Username is valid."

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

tk.Label(root, text="Welcome back, please login.", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack(pady=5)
username_entry= tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry=tk.Entry(root)
password_entry.pack()

button_frame=tk.Frame(root)
button_frame.pack(pady=10)

reset_button=tk.Button(button_frame, text="Reset Password")
reset_button.pack(side="left", padx=5)
reset_button.pack_forget()

reset_user_button=tk.Button(button_frame, text="Reset Username")
reset_user_button.pack(side="left", padx=5)
reset_user_button.pack_forget()

def login():
    global stored_password
    user=username_entry.get()
    pwd=password_entry.get()
    if user == stored_username and pwd == stored_password:
        messagebox.showinfo("Login Success", f"Welcome {user}!")
        root.destroy()
    elif user==stored_username and pwd != stored_password:
        messagebox.showinfo(f"Login Unsuccessful {user}.", "Password is incorrect. Retry, or reset your password.")
        reset_button.pack(pady=5)
    elif user != stored_username and pwd == stored_password:
        messagebox.showinfo(f"Login Unsuccessful {user}.", "Password is incorrect. Retry, or reset your password.")
        reset_button.pack(pady=5)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Try Again")



def reset_password():
    global stored_password
    while True:
      new_pwd = simpledialog.askstring("Reset Password", "Enter new Password:")
      if not new_pwd:
          break
      confirm_pwd = simpledialog.askstring("Reset Password", "Confirm new password")
      if confirm_pwd != new_pwd:
          messagebox.showerror("Error", "Passwords do not match")
          continue
      valid, msg = validate_password(new_pwd)
      if valid:
         stored_password = new_pwd
         messagebox.showinfo("Success", "Password reset successfully!")
         break
      else:
         messagebox.showerror("Error", msg)

def reset_username():
    global stored_username
    while True:
      new_usn = simpledialog.askstring("Reset Username", "Enter new Username:")
      if not new_usn:
          break
      confirm_usn = simpledialog.askstring("Reset Username", "Confirm new username")
      if confirm_usn != new_usn:
          messagebox.showerror("Error", "Passwords do not match")
          continue
      valid, msg = validate_username(new_usn)
      if valid:
         stored_password = new_usn
         messagebox.showinfo("Success", "Username reset successfully!")
         break
      else:
         messagebox.showerror("Error", msg)
# def exit_app():
#     root.destroy()

reset_button.config(command=reset_password)
reset_user_button.config(command=reset_username)
tk.Button(button_frame, text="Enter", command=login).pack(side="left", pady=5)
# tk.Button(root, text="Exit", command=exit_app).pack()

root.mainloop()