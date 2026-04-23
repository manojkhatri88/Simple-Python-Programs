import random
import string

passwords = {}

#load exisiting password file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pswd = line.strip().split(":")
            passwords[website] = pswd

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----")
    print("1. Save password")
    print("2. View passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("enter website: ")
        pswd = input("enter password: ")

        passwords[site] = pswd

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pswd}\n")
        print("Saved!")

    elif choice == "2":
        if not passwords:
            print("No data")
        else:
            for site, pswd in passwords.items():
                print(site, ":", pswd)
    
    elif choice == "3":
        print("Generated password", generate_password())

    elif choice == "4":
        print("ok bye!")
        break

    else:
        print("In-valid input")