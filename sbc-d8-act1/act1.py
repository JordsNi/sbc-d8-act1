file1 = open("user.txt", "r")
file2 = open("pass.txt", "r")
logins = {}

def register():
    user = input("Register\nEnter your username: ")
    passs = input("Enter your username: ")
    with open("user.txt", "r+") as f1, open("pass.txt", "r+") as f2:
        read1 = f1.read()
        read2 = f2.read()
        if user in read1 and passs in read2:
            print("User already exists!")
        else:
            f1.write(f"{user}\n")
            f2.write(f"{passs}\n")
            print("Account successfully created!")


def login():
    log = True
    while log:
        user_log = input("Login\nEnter your username: ")
        pass_log = input("Enter your password: ")
        with open("user.txt", "r") as f1, open("pass.txt", "r") as f2:
            read1 = f1.readlines()
            read2 = f2.readlines()
            u = [line.strip() for line in read1]
            p = [line.strip() for line in read2]
        if (user_log in u and pass_log in p) and (u.index(user_log) == p.index(pass_log)):
            logins[user_log] = pass_log
            print(logins)
            print("Successfully Login!")
            log = False
        else:
            print("Invalid username and/or password!")


def password():
    new_pass = input("Enter your new password: ")
    with open(r"pass.txt", "r+") as f1:
        read1 = f1.read()
        for key, value in logins.items():
            if value in f1:
                print(f"Username: {key} Password: {value}")
                logins.update({key:new_pass})
        rep = read1.replace(value, new_pass)
    with open(r"pass.txt", "w") as f2:
        f2.write(rep)
    print("Password changed successfully!")

while True:
    logs = input("Account Register[A]\nLogin[B]\nChange Password[C]\nChoose your action:").upper()
    if logs == "A":
        register()
    if logs == "B":
        login()
    if logs == "C":
        password()
    else:
        ...