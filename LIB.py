import datetime
import os


class LIB:
    """
    This class is used to keep record of books in the library
    It has total four modules:
        -> Display Books
        -> Issue Books
        -> Return Books
        -> Add Books
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "Books.txt"
        self.library_name = library_name
        self.books_dict = {}

        Id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            # print(line)
            self.books_dict.update(
                {
                    str(Id): {
                        "books_title": line.replace("\n", ""),
                        "lender_name": "",
                        "Issue_date": "",
                        "Status": "Available",
                    }
                }
            )
            Id = Id + 1

    def display_books(self):
        print("------------------ List of Books ------------------")
        print("Books ID", "\t", "Title")
        print("---------------------------------------------------")
        for key, value in self.books_dict.items():
            print(
                key, "\t\t", value.get("books_title"), "- [", value.get("Status"), "]"
            )

    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(
                    f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}"
                )

                return self.Issue_books()
            elif self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]["lender_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["Status"] = "Already Issued"
                print("Book Issued Successfully! \n")

        else:
            print("Book ID not found")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter book title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Book title too long!")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update(
                    {
                        str(int(max(self.books_dict)) + 1): {
                            "books_title": new_books,
                            "lender_name": "",
                            "Issue_date": "",
                            "Status": "Available",
                        }
                    }
                )
                print(f"This book {new_books} has been added succesfully!")

    def return_books(self):
        books_id = input("Enter books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print(
                    "This book is already available in library. Please check your book ID"
                )
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully Updated! \n")

        else:
            print("Book ID not found!")


try:
    myLIB = LIB("Books.txt", "Python's")
    press_key_dict = {
        "D": "Display Books",
        "I": "Issue Books",
        "A": "Add Books",
        "R": "Return Books",
        "Q": "Quit",
    }
    key_press = False
    while not (key_press == "q"):
        print(
            f"\n----------- Welcome to {myLIB.library_name} Library Management System -----------\n"
        )
        for key, value in press_key_dict.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\n Current Selection: Issue Book\n")
            myLIB.Issue_books()
        elif key_press == "a":
            print("\n Current Selection: Add Book\n")
            myLIB.add_books()
        elif key_press == "d":
            print("\n Current Selection: Display Book\n")
            myLIB.display_books()
        elif key_press == "r":
            print("\n Current Selection: Return Book\n")
            myLIB.return_books()
        elif key_press == "q":
            print("\n See you next time!\n")
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please try again :(")
