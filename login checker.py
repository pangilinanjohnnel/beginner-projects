while True:
    username=input("Enter your username: ")

    if len(username)>12:
        print("Your username is too long!!!")

    elif not username.find(" "):
        print("Your username can't have any spaces!!!")

    else:
        password = input("Enter your password: ")

        if len(password)>12:
            print("Your password is too long!!!")

        elif not password.find(" "):
            print("Your password can't have any spaces!!!")

        elif not any(ch.isupper() for ch in password):
            print("Password must contain at least one UPPERCASE letter!")

        elif not any(ch.islower() for ch in password):
            print("Password must contain at least one lowercase letter!")

        elif not any(ch.isdigit() for ch in password):
            print("Password must contain at least one number!")

        elif not any(not ch.isalnum() for ch in password):
            print("Password must contain at least one symbol!")

        else:
            break

print(f"Welcome {username} !!!")

