import json
import os

DATA_FILE = "users.json"
current_user = None


def get_current_user():
    return current_user


def set_current_user(username):
    global current_user
    current_user = username


def init():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"users": []}, f, indent=4)


def read_user_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data


def write_user_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def append_user_data(new_data):
    data = read_user_data()
    data["users"].append(new_data)
    write_user_data(data)
