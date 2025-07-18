import json
import os

DATA_FILE = "journals.json"
# current_user = None


# def set_current_user(username):
#     global current_user
#     current_user = username


# def get_current_user():
#     return current_user


def init_jorunals():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"journals": []}, f)


def read_journal_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data


def write_Journal_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=5)


def appnd_journals_data(new_Journals):
    data = read_journal_data()
    data["journals"].append(new_Journals)
    write_Journal_data(data)
