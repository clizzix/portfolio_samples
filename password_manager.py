from cryptography.fernet import Fernet

#ask user for master password

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter master password: ")
key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user + "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Enter name of account: ")
    pwd = input("Enter password: ")
    #create a text file to append pwd
    with open("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to create a new password or access an existing one? ( view, add) Press q to quit ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
