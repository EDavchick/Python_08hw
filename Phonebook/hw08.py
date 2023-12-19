"""
на Отлично в одного человека надо сделать консольное приложение Телефонный справочник 
с внешним хранилищем информации, и чтоб был реализован основной функционал - 
просмотр, сохранение, импорт, поиск, удаление, изменение данных.
"""

from random import *
import json

phonebook = {}
commands = ["all", "exit", "add", "save", "search", "del", "change"]

new_contact = {"Katya Borisova": 
             { "phones": [64591236],
              "email": "frty@gmail.com",
              "birthday": "07.12.1977"
              }
              }

def all_phonebook(book):
    for name, values in book.items():
        print(name, values)
        print()

def search(book):
    for name in book.items():
        name = input('Put contact name: ')
        if name == name:
            print(f"{name}: ", book.get(name))
        else:
            print(f"{name} does not exist in your phonebook")
        return

def add(new_contact):
    for key,value in new_contact.items():
        phonebook[key] = value

# def change(book):
#     for name, values in book.items():
#         name = input('Put contact name: ')
#         

def delete(book):
    contact = book.pop(input('Put contact name: '))
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
        all_phonebook(phonebook)
    elif command == "exit":
        save()
        print("Goodbye!")
        break
    elif command == "save":
        save()
        print("Your contacts were succssessfuly saved in file 'phonebook.json'")
    elif command == "add":
        add(new_contact)
        save()
        print(phonebook)
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