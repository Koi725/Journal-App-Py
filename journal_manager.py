from utils.auth_utils import *
from utils.journals_utils import *
from datetime import datetime


def add_journals():
    title = input("Enter the title of Journals : ").strip()
    content = input("Enter the Content of journal : ").strip()
    category = input("Enter the category of Journal : ").strip()
    date = datetime.now().isoformat()

    journals = read_journal_data()

    duplicate = any(
        j["content"] == content or j["title"] == title for j in journals["journals"]
    )

    if duplicate:
        print("❌ Content or title already exists. Use another one.")
        return False

    new_journal = {
        "id": len(journals["journals"]) + 1,
        "title": title,
        "content": content,
        "category": category,
        "date": date,
        "created_by": get_current_user(),  # optional if you're using auth
    }

    appnd_journals_data(new_journal)
    print("✅ Journal added successfully!")
    return True


def view_journal():
    data = read_journal_data()
    for journal in data["journals"]:
        if journal["created_by"] == get_current_user():
            print(
                f"🆔 {journal['id']} | 📌 {journal['title']} | 📄 {journal['content']} | 📊 {journal['category']} | 🕒 {journal['date']} | {journal['created_by']}"
            )
        else:
            print("U have no Journals..!")


def search_journals(query):
    data = read_journal_data()
    journals = [j for j in data["journals"] if j["created_by"] == get_current_user()]

    results = [
        j
        for j in journals
        if query.lower() in j["title"].lower() or str(j["id"]) == query
    ]

    if results:
        for j in results:
            print(
                f"🔍 Found → 🆔 {j['id']} | 📌 {j['title']} | 📄 {j['content']} | 📊 {j['category']} | 🕒 {j['date']}"
            )
    else:
        print("❌ No matching journal found.")


def edit_journal(new_title, new_content, new_date):
    try:
        id = int(input("Pls enter the Journal ID u want to change : "))
    except ValueError:
        print("Invalid input")

    data = read_journal_data()

    for jornal in data["journals"]:
        if jornal["id"] == id and jornal["created_by"] == get_current_user():
            jornal["title"] = new_title
            jornal["content"] = new_content
            jornal["date"] = new_date
            write_Journal_data(data)
            print("✅ Task updated.")
            return
    print("❌ Task not found or permission denied.")


def delete_journal(id):
    data = read_journal_data()
    for journal in data["journals"]:
        if journal["id"] == id and journal["created_by"] == get_current_user():
            data["journals"].remove(journal)
            write_Journal_data(data)
            print("🗑️ Journal deleted.")
            return
    print("❌ Task not found or permission denied.")
