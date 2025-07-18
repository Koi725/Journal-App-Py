from auth import login, register
from journal_manager import *


def loginMenu():
    print(
        """
============================= LOGIN =============================   
1.login 
2.register
3.exit          
=================================================================       
  """
    )


def menu():
    print(
        """
=========================== MENU ===========================      
1.Add Journal 
2.View Journals
3.Search for Journal (By title or ID)
4.Edit Journal 
5.Delete Journal
6.exit           
=============================================================
  """
    )


def main():
    while True:
        loginMenu()
        try:
            choice = int(input("Pls Select an option : "))
        except ValueError:
            print("Invalid Option....")

        if choice == 1:
            if login():
                break
        elif choice == 2:
            if register():
                break
        elif choice == 3:
            print("Goodbye...Exiting the program..")
            break
        else:
            print("Invalid option...pls try again")
    while True:
        menu()
        try:
            op = int(input("Pls Select an option : "))
        except ValueError:
            print("Invalid input ")
        if op == 1:
            add_journals()
        elif op == 2:
            view_journal()
        elif op == 3:
            query = input("Enter the Journal ID or Title :")
            search_journals(query)
        elif op == 4:
            new_title = input("pls enter the new title : ")
            new_content = input("pls enter the new content :")
            new_date = datetime.now().isoformat()
            edit_journal(new_title, new_content, new_date)
        elif op == 5:
            try:
                id = int(input("pls enter the journal id u wanna delete :"))
            except ValueError:
                print("invalid input ")
            delete_journal(id)
        elif op == 6:
            print("Exiting the application....Goodbye")
            break
        else:
            print("Invalid option...")


if __name__ == "__main__":
    main()
