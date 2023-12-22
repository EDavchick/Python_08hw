"""
на Отлично в одного человека надо сделать консольное приложение Телефонный справочник 
с внешним хранилищем информации, и чтоб был реализован основной функционал - 
просмотр, сохранение, импорт, поиск, удаление, изменение данных.
"""

from random import *
import json

phonebook = {}
commands = ["all", "exit", "add", "save", "search", "del", "change"]


def all(book):
    for name, values in book.items():
        print(name, str(values))

def search(book):
    el = input('Put contact name: ')
    try:
        for k, v in book.items():
            if el in k:
                book.get(k, v)
                print(k, str(v))
    except:
        print("This name does not exist in your phonebook")

def add(book):
    key_up = {"Masha Alexeeva": 
             { "phones": [87649321, 74536129],
              "email": "mnbvc@gmail.com",
              "birthday": "25.09.1992"}
              }
    if key_up not in book.items():
        book.update(key_up)
        print(all(book))

# def change(book):
#     for name, values in book.items():
#         name = input('Put contact name: ')
#         

def delete(book):
    # contact = book.pop(input('Put contact name: '))
    contact = input('Put contact name: ')
    if contact in phonebook:
        del phonebook[contact]
    print(f"Contact {contact} was deleted")

def save():
    with open("phonebook.json", "w", encoding="utf-8") as book:
        book.write(json.dumps(phonebook, sort_keys=True))

def load():
    try:
        with open("phonebook.json", "r", encoding="utf-8") as book:
            phonebook = json.loads(book.read())
    except:
        phonebook = {"Alex Ivanov": 
             { "phones": [12345678, 87654321],
              "email": "qwer@gmail.com",
              "birthday": "05.05.1955"
              },
              "Borya Petrov": 
             { "phones": [22233447],
              "email": "poiuy@gmail.com",
              "birthday": "17.06.1985"
              },
              "Masha Alexeeva": 
             { "phones": [87649321, 74536129],
              "email": "mnbvc@gmail.com",
              "birthday": "25.09.1992"
              },
              }
    return phonebook

phonebook = load()
print("You have a commands: ", *commands, sep=", ")

while True:
    command = input("Put command: ")
    if command == "all":
        all(phonebook)
    elif command == "exit":
        save()
        print("Goodbye!")
        break
    elif command == "save":
        save()
        print("Your contacts were succssessfuly saved in file 'phonebook.json'")
    elif command == "add":
        add(phonebook)
        save()
    elif command == "load":
        load()
        print("Your contacts were succssessfuly loaded in file 'phonebook.json'")
    elif command == "search":
        search(phonebook)
    elif command == "del":
        delete(phonebook)
        save()
    elif command == "change":
        pass