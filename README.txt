📓 Personal Journal Manager – CLI App

This is a Command-Line Journal Management System where users can:

    ✍️ Add personal journal entries

    🔍 Search journals by ID or title

    📖 View only their own entries

    🛠 Edit existing journals

    🗑 Delete their own journals

All journals are securely tagged with the logged-in user's identity and stored in a journals.json file

🔧 Features

    ✅ User authentication (login/register)

    📝 Add journal entries with title, content, category, and timestamp

    🔍 Search by journal ID or title

    📚 View your own journals only

    🛠 Edit title/content/date of existing journals

    🗑 Delete your journals

project/
│
├── main.py
├── auth.py
├── task_manager.py
├── journals_manager.py   <-- this project
├── utils/
│   ├── auth_utils.py
│   ├── journal_utils.py
│   └── ...
│
├── users.json
├── journals.json
└── README.md



🛠 Technologies Used

    Python 3.x

    File-based JSON storage

    CLI-based UX

    Modular architecture (auth + utils + managers)

