# 🔐 Personal Password Manager

A simple **Python-based Personal Password Manager** that allows users to save, view, generate, update, and delete passwords through a command-line interface.

This project is built using Python's built-in modules such as `random` and `string`, with password data stored locally in a `passwords.txt` file.

## ✨ Features

* 🔑 **Save Password** — Store a website and its password.
* 👀 **View Passwords** — Display all saved website credentials.
* 🎲 **Generate Password** — Generate an 8-character random password.
* 🔄 **Update Password** — Change the password saved for a website.
* 🗑️ **Delete Password** — Remove a website and its password.
* 💾 **File Storage** — Store password data locally in `passwords.txt`.
* 🚪 **Exit** — Safely close the password manager.

## 🛠️ Technologies Used

* **Python**
* `random` module
* `string` module
* File Handling
* Dictionary
* Functions
* Loops
* Conditional Statements
* Exception Handling

## 📂 Project Structure

```text
Personal-Password-Manager/
│
├── password_manager.py
├── passwords.txt
└── README.md
```

> `passwords.txt` is automatically created when you save your first password.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/personal-password-manager.git
```

### 2. Open the project folder

```bash
cd personal-password-manager
```

### 3. Run the Python program

```bash
python password_manager.py
```

## 📋 Menu

When you run the program, you will see:

```text
----- PERSONAL PASSWORD MANAGER -----

1. Save Password
2. View Password
3. Generate Password
4. Update Password
5. Delete Password
6. Exit
```

## 💻 Example

### Save Password

```text
Enter your Choice : 1
Enter Website : github.com
Enter Password : mypassword123
Password Saved!
```

### View Passwords

```text
----- SAVED PASSWORDS -----

github.com : mypassword123
gmail.com : example123
```

### Generate Password

```text
Enter your Choice : 3

Generated Password: aB7@xP2_
```

### Update Password

```text
Enter your Choice : 4
Enter Website to Update : github.com
Enter New Password : newpassword456
Password Updated!
```

### Delete Password

```text
Enter your Choice : 5
Enter Website to Delete : github.com
Password Deleted!
```

## 🧠 Concepts Practiced

This project helped practice several important Python concepts:

### Dictionary

Passwords are stored using a Python dictionary:

```python
passwords = {}
```

Example:

```python
passwords["github.com"] = "mypassword123"
```

### Functions

The project uses functions for reusable tasks:

```python
def generate_password():
    ...
```

and:

```python
def save_to_file():
    ...
```

### File Handling

Passwords are stored using Python file handling:

```python
with open("passwords.txt", "w") as file:
```

### Exception Handling

The program handles the case where the password file doesn't exist:

```python
try:
    ...
except FileNotFoundError:
    pass
```

### Random Password Generation

The program combines letters, numbers, and special characters:

```python
chars = string.ascii_letters + string.digits + "!@#.&_"
```

## 🔒 Security Note

**This project is for learning purposes.**

Passwords are stored as **plain text** inside `passwords.txt`. This means it is **not suitable for storing real or sensitive passwords**.

A production password manager should use proper encryption, secure key management, authentication, and other security protections.

## 🔮 Future Improvements

Possible improvements for this project:

* 🔐 Master password authentication
* 🔒 Encrypt stored passwords
* 🔎 Search passwords by website
* 📊 Password strength checker
* 📋 Copy password to clipboard
* 🎯 Custom password length
* 🔑 Generate stronger passwords
* 👤 Multiple user accounts
* 🖥️ GUI using Tkinter
* 🗄️ SQLite database storage
* 🌐 Web-based password manager

## 📚 Learning Outcome

By building this project, I practiced:

* Python fundamentals
* Dictionaries
* Functions
* Loops
* File handling
* Exception handling
* Random password generation
* CRUD operations
* Basic project structure

## 👨‍💻 Author

**Jishu Bhaskar**

Computer Science & Technology Student
Interested in Python, Web Development, Software Development, and AI/ML.

---

⭐ If you found this project useful, consider giving the repository a star!
