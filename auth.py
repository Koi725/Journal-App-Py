from utils.auth_utils import *
from password import password_check


def login():
    email = input("Pls enter the email : ").strip()
    password = input("pls enter the password :")
    data = read_user_data()

    for user in data["users"]:
        if user["email"] == email and user["password"] == password:
            print(f"✅ Logged in Successfully, welcome {user['username']}!")
            set_current_user(user["username"])
            return 1

    print("Incorrect email or password....")
    return 0


def register():
    username = input("Pls enter the username : ").strip()
    email = input("Pls enter the email : ").strip()
    password = input("pls enter the password :").strip()

    data = read_user_data()

    if any(u["username"] == username for u in data["users"]):
        print(f"❌ Username '{username}' already exists. Try something else.")
        return False

    if password_check(password) < 8:
        print("❌ Very Weak Password, shame on u...!!")
        return False

    new_user = {
        "id": len(data["users"]) + 1,
        "username": username,
        "email": email,
        "password": password,
    }
    append_user_data(new_user)
    print("✅ Registration successful! You can now log in.")
    return True
