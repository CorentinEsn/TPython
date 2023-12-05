import getpass
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

def create_account_console():
    login = input("Enter your login: ")
    password = getpass.getpass("Enter your password: ")

    # Add salt to the password
    salted_password = add_salt(login, password)

    # Hash the password
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    # Store the login and hashed password in a text file
    with open("user_accounts.txt", "a") as file:
        file.write(f"{login} {hashed_password}\n")

    print("Account created successfully.")

def add_salt(password, salt):
    # Use a fixed string as part of the salt
    return password + salt

def create_account_gui():
    def save_account():
        login = login_var.get()
        password = password_var.get()

        # Add salt to the password
        salted_password = add_salt(login, password)

        # Hash the password
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        # Store the login and hashed password in a text file
        with open("user_accounts.txt", "a") as file:
            file.write(f"{login} {hashed_password}\n")

        result_label.config(text="Account created successfully.")

    root = Tk()
    root.title("Create Account")

    login_label = Label(root, text="Login:")
    login_label.pack()

    login_var = StringVar()
    login_entry = Entry(root, textvariable=login_var)
    login_entry.pack()

    password_label = Label(root, text="Password:")
    password_label.pack()

    password_var = StringVar()
    password_entry = Entry(root, show="*", textvariable=password_var)
    password_entry.pack()

    create_button = Button(root, text="Create Account", command=save_account)
    create_button.pack()

    result_label = Label(root, text="")
    result_label.pack()

    root.mainloop()

def login_user_console():
    login = input("Enter your login: ")
    password = getpass.getpass("Enter your password: ")

    # Check if the login and hashed password are present in the file
    with open("user_accounts.txt", "r") as file:
        for line in file:
            stored_login, stored_hashed_password = line.strip().split(" ")

            # Add salt to the provided password for verification
            salted_password = add_salt(login, password)

            # Hash the password for verification
            hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

            # Check if the login and hashed password match
            if login == stored_login and hashed_password == stored_hashed_password:
                print("Login successful.")
                return

    print("Invalid login or password.")

def login_user_gui():
    def verify_login():
        login = login_var.get()
        password = password_var.get()

        # Check if the login and hashed password are present in the file
        with open("user_accounts.txt", "r") as file:
            for line in file:
                stored_login, stored_hashed_password = line.strip().split(" ")

                # Add salt to the provided password for verification
                salted_password = add_salt(login, password)

                # Hash the password for verification
                hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

                # Check if the login and hashed password match
                if login == stored_login and hashed_password == stored_hashed_password:
                    result_label.config(text="Login successful.")
                    return

        result_label.config(text="Invalid login or password.")

    root = Tk()
    root.title("Login")

    login_label = Label(root, text="Login:")
    login_label.pack()

    login_var = StringVar()
    login_entry = Entry(root, textvariable=login_var)
    login_entry.pack()

    password_label = Label(root, text="Password:")
    password_label.pack()

    password_var = StringVar()
    password_entry = Entry(root, show="*", textvariable=password_var)
    password_entry.pack()

    login_button = Button(root, text="Login", command=verify_login)
    login_button.pack()

    result_label = Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    # Uncomment the following lines based on whether you want to use console or GUI
    # create_account_console()
    # login_user_console()

    # For GUI version, uncomment the following lines
     create_account_gui()
     login_user_gui()
