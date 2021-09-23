"""
Name: Subin Moon
Student Number: A01238145

books.py
"""
import json
import xlrd
from collections import OrderedDict
import doctest


# CONSTANTS
def ATTRIBUTE():
    """Return six attributes of each book."""
    return "author", "title", "publisher", "shelf", "category", "subject"


def USER_INPUT_SERVICE():
    """Return the user input for the main service."""
    return "search", "move", "exit"


# FUNCTIONS
def check_json_file(file_name: str, excel_file: str, sheet_name: str) -> list:
    """Check if there is a JSON file called somebooks.json in the same directory.

    This function opens the json file if it exists, otherwise, it convert the excel file to the json file and open the json file again.

    :param file_name: a string representing a file name
    :param excel_file: a string representing the name of excel file
    :param sheet_name: a string representing the name of specific sheet in the excel file
    :precondition: file_name, excel_file, and sheet_name must be strings
    :precondition: file_name and excel_file have the same name before each filename extension
    :postcondition: if json file exists, open the JSON file and return the data included
    :postcondition: otherwise create a new json file by converting the excel file content to the json file and return the content
    :return: a list which was converted from json file to python list
    """
    try:
        with open(file_name) as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        period_index = excel_file.index(".")
        json_file_name = excel_file[:period_index] + ".json"
        write_json_file(json_file_name, convert_excel_file(excel_file, sheet_name))
        return check_json_file(file_name, excel_file, sheet_name)


def convert_excel_file(excel_file: str, sheet_name: str) -> list:
    """Convert excel file to the regular list in python.

    :param excel_file: a string representing the name of excel file
    :param sheet_name: a string representing the name of specific sheet in the excel file
    :precondition: excel_file and sheet_name must be strings
    :postcondition: open the excel file, and convert the content to the list row by row
    :return: a converted list
    """
    workbook = xlrd.open_workbook(excel_file)
    sheet = workbook.sheet_by_name(sheet_name)

    book_list = []
    for row in range(1, sheet.nrows):
        books = OrderedDict()
        row_values = sheet.row_values(row)
        books["author"] = row_values[0]
        books["title"] = row_values[1]
        books["publisher"] = row_values[2]
        books["category"] = row_values[4]
        books["subject"] = row_values[5]
        book_list.append(books)

        if type(row_values[3]) != str:
            books["shelf"] = str(int(row_values[3]))
        else:
            books["shelf"] = str(row_values[3])

    return book_list


def write_json_file(file_name: str, content: list):
    """Write the content on the json file.

    :param file_name: a string
    :param content: a list
    :precondition: file_name must be a string
    :precondition: content must be a list
    :precondition: file_name must have '.json' as a filename extension
    :postcondition: open the json file and write the content on the file
    :return: no return
    """
    with open(file_name, 'w+') as file_object:
        json.dump(content, file_object)


def replace_empty_value(data: list) -> list:
    """Replace empty values of the attributes in the list with None.

    :param data: a list
    :precondition: data must be a list
    :precondition: data contains dictionaries representing each book
    :postcondition: replace the empty value of publishers with
    :return: a list which is modified

    >>> book_list = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "", "shelf": "1", "category": "Architecture", "subject": "Architectural History"},  {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}]
    >>> print(replace_empty_value(book_list))
    [{'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'None', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}, {'author': 'Herbert and Anderson', 'title': 'House Atreides', 'publisher': 'None', 'shelf': '33', 'category': 'Fiction', 'subject': 'SF'}]
    """
    for book in data:
        for attribute in book:
            if book[attribute] == "":
                book[attribute] = "None"
    return data


def get_user_input():
    """Get user input for the main service of books.py.

    :postcondition: if user inputs '1', return 'search'
    :postcondition: if user inputs '2', return 'move'
    :postcondition: if user inputs '3', return 'exit'
    :raises ValueError: if user inputs anything but a number
    :return: a string
    """
    while True:
        try:
            user_action = int(input("Enter (1) Search Books (2) Move Books (3) Exit\n"))
            for index, value in enumerate(USER_INPUT_SERVICE(), 1):
                if user_action == index:
                    return value
            if user_action > 3:
                raise IndexError("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter the number.")


def user_input_book_search(data: list) -> list:
    """Get user input to search books.

    :param data: a list
    :precondition: data must be a list
    :precondition: data contains dictionaries representing each book
    :postcondition: search books by the search_point according to the user input
    :postcondition: search books with the provided information
    :postcondition: after getting the search point and the information, book_search function will be executed
    :raises ValueError: if the user inputs anything but a number
    :return: a list which is resulted from book_search function
    """
    while True:
        try:
            search_point = input(
                "Search by - \n Enter (1) Author (2) Title (3) Publisher (4) Shelf (5) Category (6) Subject:\n")
            info = input("Search string: ").lower()
            for index, value in enumerate(ATTRIBUTE(), 1):
                if int(search_point) == index:
                    return book_search(value, info, data)
            if int(search_point) > 6:
                raise IndexError("Please enter the number from 1 to 6.")
        except ValueError:
            print("Please enter the number.")


def book_search(search_point: str, info: str, data: list) -> list:
    """Search for books by author, or title, or publisher, or shelf, or category, or subject.

    :param search_point: a string
    :param info: a string
    :param data: a list
    :precondition: search_point must be a string by which search the books
    :precondition: info must be a string with which search the books
    :precondition: data contains dictionaries representing each book
    :precondition: search for a the book with the given info
    :precondition: search within the attribute which user choose as search_point
    :precondition: search within the data
    :postcondition: if info is included in any value of attributes, append the book to the result list
    :postcondition: return a list containing applicable books which are in dictionary types
    :return: a list

    >>> book_list = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
    >>> print(book_search("category", "archi", book_list))
    [{'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}, {'author': 'Alphin', 'title': 'The Lego Architect', 'publisher': 'No Starch Press', 'shelf': '3', 'category': 'Architecture', 'subject': 'Models'}]
    """
    result = []
    for i in range(len(data)):
        if search_point == "shelf":
            try:
                if int(info) == int(data[i][search_point]):
                    result.append(data[i])
            except ValueError:
                if info in data[i][search_point].lower():
                    result.append(data[i])
        else:
            if info in data[i][search_point].lower():
                result.append(data[i])
    return result


def print_book_search(result: list):
    """Print the length of the result list as well as the elements.

    :param result: a list
    :precondition: result must be a list
    :postcondition: print two things - the number of results and a numbered list of results
    :postcondition: for the result printed, all the attributes of each book should be printed
    :return: no return

    >>> data = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}]
    >>> print_book_search(data)
    The result has 2 book(s).
    1. {'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '1', 'category': 'Architecture', 'subject': 'Architectural History'}
    2. {'author': 'Gustafson', 'title': 'Craft Perception and Practice 1', 'publisher': 'Ronsdale Press', 'shelf': '1', 'category': 'Art', 'subject': 'Craft'}
    """
    print(f"The result has {len(result)} book(s).")
    for counter in range(len(result)):
        print(f"{counter + 1}. {result[counter]}")


def print_shelf(data: list) -> list:
    """Print the existed shelves in the data.

    :param data: a list
    :precondition: data must be a list
    :precondition: data contains dictionaries representing each book
    :postcondition: append the shelves from the data to the shelf_list
    :postcondition: no duplicates allowed in the shelf_list
    :postcondition: print the shelves out with numbered list
    :postcondition: return a list of the shelves
    :return: a list

    >>> book_list = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Gustafson", "title": "Craft Perception and Practice 1", "publisher": "Ronsdale Press", "shelf": "1", "category": "Art", "subject": "Craft"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "None", "shelf": "33", "category": "Fiction", "subject": "SF"}, {"author": "Liu", "title": "The Wandering Earth", "publisher": "Head of Zeus", "shelf": "Gaby", "category": "Fiction", "subject": "SF (Chinese)"}, {"author": "Bagnall", "title": "Maximum Lego EV3", "publisher": "Variant Press", "shelf": "Students", "category": "Programming", "subject": "Java"}]
    >>> print_shelf(book_list)
    1. 1
    2. 3
    3. 33
    4. Gaby
    5. Students
    ['1', '3', '33', 'Gaby', 'Students']
    """
    shelf_list = []
    for book in data:
        if book["shelf"] not in shelf_list:
            shelf_list.append(book["shelf"])
    for index in range(len(shelf_list)):
        print(f"{index + 1}. {shelf_list[index]}")
    return shelf_list


def user_input_move_shelf(data: list) -> list:
    """Get user input to move a book to another shelf.

    :param data: a list
    :precondition: data must be a list
    :precondition: data contains dictionaries representing each book
    :postcondition: execute book_search related functions to identify the book the user wants to move
    :postcondition: once the book is selected, execute move_book_shelf function
    :raises ValueError: if the user inputs anything but a number
    :raises IndexError: if the book input is not found in the list
    :return: a list which is resulted from move_book_shelf function
    """
    while True:
        try:
            print("Which book do you want to move?")
            result = user_input_book_search(data)
            print_book_search(result)
            user_input = int(input("Enter the number of the book you want to move: "))
            book = result[user_input - 1]

            shelf_list = print_shelf(data)
            shelf_move_to = input("Enter the shelf you want to move to: ")
            shelf = shelf_list[int(shelf_move_to) - 1]

            return move_book_shelf(book, shelf, data)

        except ValueError:
            print("Please enter the number.")
        except IndexError:
            print("Sorry, we don't have such books.")


def move_book_shelf(book: dict, shelf_move_to: str, data: list) -> list:
    """Modify the value of "shelf" attribute of the given book in the data list.

    :param book: a dictionary
    :param shelf_move_to: a string
    :param data: a list
    :precondition: book must be a dictionary
    :precondition: move_to_shelf must be a string
    :precondition: data must be a list
    :precondition: data contains dictionaries representing each book
    :postcondition: find the index of the given book in the data list
    :postcondition: update the shelf value of the book to the given shelf value
    :postcondition: print the statement to let the user know that the shelf is successfully moved
    :postcondition: return a data list with modified book information
    :return: a list

    >>> book_list = [{"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}, {"author": "Alphin", "title": "The Lego Architect", "publisher": "No Starch Press", "shelf": "3", "category": "Architecture", "subject": "Models"}, {"author": "Herbert and Anderson", "title": "House Atreides", "publisher": "", "shelf": "33", "category": "Fiction", "subject": "SF"}]
    >>> book_info = {"author": "Ambroziak", "title": "Michael Graves Images of a Grand Tour", "publisher": "Princeton Architectural Press", "shelf": "1", "category": "Architecture", "subject": "Architectural History"}
    >>> print(move_book_shelf(book_info, "3.0", book_list))
    Michael Graves Images of a Grand Tour is now on 3.0 shelf.
    [{'author': 'Ambroziak', 'title': 'Michael Graves Images of a Grand Tour', 'publisher': 'Princeton Architectural Press', 'shelf': '3.0', 'category': 'Architecture', 'subject': 'Architectural History'}, {'author': 'Alphin', 'title': 'The Lego Architect', 'publisher': 'No Starch Press', 'shelf': '3', 'category': 'Architecture', 'subject': 'Models'}, {'author': 'Herbert and Anderson', 'title': 'House Atreides', 'publisher': '', 'shelf': '33', 'category': 'Fiction', 'subject': 'SF'}]
    """
    book_index = data.index(book)
    data[book_index]["shelf"] = shelf_move_to.title()
    print("{title} is now on {shelf} shelf.".format(title=book["title"], shelf=data[book_index]["shelf"]))
    return data


def save_json(file_name: str, content: list):
    """Dump the content to the json file to modify

    :param file_name: a string
    :param content: a list
    :precondition: file_name must be a string
    :precondition: content must be a list
    :postcondition: open the file and overwrite the content
    :return: no return
    """
    with open(file_name, "w+") as file_object:
        json.dump(content, file_object)


def library():
    """Run the program containing functions to search books and move the books to the other shelf and modify the json file as needed.

    :postcondition: if user inputs 'exit', the program ends
    :postcondition: if user inputs 'search', book_search related function will be executed
    :postcondition: if user inputs 'move', move_book_shelf related function will be executed
    :return: no return
    """
    data = check_json_file("somebooks.json", "somebooks.xls", "Books")
    data = replace_empty_value(data)
    while True:
        user_action = get_user_input()
        if user_action == "exit":  # Exit
            print("Thanks for your visit. Have a nice day!")
            exit(0)

        elif user_action == "search":  # Search
            print_book_search(user_input_book_search(data))

        else:  # Move
            save_json("somebooks.json", user_input_move_shelf(data))


def main():
    """Drive the program."""
    doctest.testmod(verbose=True)
    library()


if __name__ == "__main__":
    main()