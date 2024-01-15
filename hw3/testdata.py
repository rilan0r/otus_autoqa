import json
import csv
from urllib.request import urlretrieve

users = 'https://raw.githubusercontent.com/konflic/examples/master/data/users.json'
books = 'https://raw.githubusercontent.com/konflic/examples/master/data/books.csv'
urlretrieve(users, 'users.json')
urlretrieve(books, 'books.csv')


with open("users.json", "r") as f:
    users_reader = json.loads(f.read())
    users_list = users_reader
    users_number = len(users_list)  # 28

with open("books.csv", "r") as f:
    books_reader = csv.DictReader(f)
    books_list = list(books_reader)
    books_number = len(books_list)  # 211


def convert_users_list(lst):
    converted_users_list = list()
    for user in lst:
        current_user = {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": []
            }
        converted_users_list.append(current_user)
    return converted_users_list

def convert_books_list(lst):
    converted_books_list = list()
    for book in lst:
        current_book = {
                "title": book['Title'],
                "author": book['Author'],
                "pages": book['Pages'],
                "genre": book['Genre']
            }
        converted_books_list.append(current_book)
    return converted_books_list


def books_generator(lst):
    for book in lst:
        yield book


users = convert_users_list(users_list)
books = convert_books_list(books_list)

books_per_user = books_number // users_number
users_with_extra_book = books_number % users_number

books_for_users = books_generator(books)

for index, user in enumerate(users):
    if index < users_with_extra_book:
        for i in range(books_per_user + 1):
            users[index]['books'].append(next(books_for_users))
    else:
        for i in range(books_per_user):
            users[index]['books'].append(next(books_for_users))


with open ("result.json", "w") as result:
    users = json.dumps(users, indent=4)
    result.write(users)
