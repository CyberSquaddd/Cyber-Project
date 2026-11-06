from random import random

def get_name():
    return input("Enter your full name: ")

def get_email():
    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter your email address: ")
    print("Email is valid")
    print()
    return email

def validate_email(email):
    if "@" in email:
        if "." in email[email.index("@"):]:
            return True
    return False

def validate_password(password, username):
    digit = False
    upper = False
    lower = False
    special = False
    user = True
    length8 = len(password)>7
    length12 = len(password)>11
    for c in password:
        if c.isupper(): upper = True
        if c.islower(): lower = True
        if c.isdigit(): digit = True
        if c in "!@#$%^&*": special = True
    if username in password:
        user = False
    sum = int(length8)+int(length12)+int(upper)+int(lower)+int(digit)+int(special)+int(user)
    if sum <=2: strength = "WEAK"
    elif sum <=4:strength = "FAIR"
    elif sum <=6: strength = "GOOD"
    else: strength = "STRONG"

    print("Password Strength:",strength)
    print("Criteria Check:")
    if length8: print("[✓]", end=" ")
    else: print("[✗]", end=" ")
    print("At least 8 characters")

    if length12: print("[✓]", end=" ")
    else: print("[✗]", end=" ")
    print("At least 12 characters")

    if upper: print("[✓]", end=" ")
    else: print("[✗]", end=" ")
    print("Contains uppercase letter")

    if lower:print("[✓]", end=" ")
    else:print("[✗]", end=" ")
    print("Contains lowercase letter")

    if digit: print("[✓]", end=" ")
    else: print("[✗]", end=" ")
    print("Contains digit")

    if special: print("[✓]", end=" ")
    else: print("[✗]", end=" ")
    print("Contains special character (!@#$%^&*)")

    if user: print("[✓]", end=" ")
    else: print("[✗]", end=" ")
    print("Does not contain username")

    print()

    if sum>=5:
        if strength=="STRONG":
            print(f"Congratulations! your password is {strength}! You can use this password.")
        else:
            print(f"Your password is {strength}. You can use this password.")
        return True
    return False
def get_password(username):
    pwd = input("Enter your password: ")
    while validate_password(pwd,username)==False:
        print("Password must have at least 8 characters\nPassword must have at least one uppercase letter\nPassword must have at least one lowercase letter\nPassword must have at least one digit")
        pwd = input("Enter your password: ")
    print("Password is valid!")
    return pwd

def get_password_confirmation(password):
    confirm = input("Confirm your password: ")
    while confirm!=password:
        print("Passwords do not match. Please try again.")
        confirm = input("Confirm your password: ")
    print("Password confirmed!")
    return confirm

def get_secret_word():
    sec = input("Enter your secret word (for account recovery): ")
    confirm = input("Confirm your secret word: ")
    while sec!=confirm:
        print("Secret words do not match. Please try again.")
        sec = input("Enter your secret word (for account recovery): ")
        confirm = input("Confirm your secret word: ")
    print("Secret word confirmed!")
    return sec

def generate_username(name):
    return name[0:3]+""+(name[len(name)-3:]).lower()+""+str(int((random()*899)+100))

def display_registration_summary(username,name,email):
    print("========== REGISTRATION SUCCESSFUL ==========")
    print("Username:",username)
    print("Name:",name)
    print("Email:",email)
    print("=============================================")

def main():
    print("=== USER REGISTRATION SYSTEM ===")
    print()
    name = get_name()
    email = get_email()
    print()
    username = generate_username(name)
    password = get_password(username)
    print()
    get_password_confirmation(password)
    print()
    secret = get_secret_word()
    print()
    display_registration_summary(username,name,email)


main()
yn = input("Register another user? (yes/no): ")
while yn!="no":
    print()
    main()
    yn = input("Register another user? (yes/no): ")
print("Thank you for using our registration system!")






