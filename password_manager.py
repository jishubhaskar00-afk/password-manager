import random
import string


passwords = {}

#load exiting password file
try:
    with open("passwords.txt","r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#.&_"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

# Save all passwords to file 
def save_to_file(): 
    with open("passwords.txt", "w") as file: 
        for site, pwd in passwords.items(): 
            file.write(f"{site}:{pwd}\n")

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----")
    print("1. Save Password")
    print("2. View Password")    
    print("3. Generate Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Exit")

    choice = input("Enter your Choice : ")

    if choice == "1":
        site = input("Enter Website : ")
        pwd = input("Enter Password : ")

        passwords[site] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{site} : {pwd}\n")

        print("Saved!")

    elif choice == "2":
        if not passwords:
            print("No Data!!")
        else:
            for site, pwd in passwords.items():
                print(site,":", pwd)

    elif choice == "3":
        print("Generated Password", generate_password())


    elif choice == "4": 
        site = input("Enter Website to Update : ") 
        if site in passwords: 
            new_pwd = input("Enter New Password : ") 
            passwords[site] = new_pwd 
            save_to_file() 
            print("Password Updated!") 
        else: 
            print("Website Not Found!")

    elif choice == "5":
        site = input("Enter Website to Delete : ") 
        if site in passwords: 
            del passwords[site] 
            save_to_file() 
            print("Password Deleted!") 
        else: 
            print("Website Not Found!")

    elif choice == "6":
        print("Thanks for using Password Manager...")
        break

    else:
        print("Invalid Input")