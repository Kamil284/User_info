import json
class User:
    def __init__(self, name: str, surname: str, date_birth: str):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth



def user_add():
    print('Add new user ')
    name = input('Name: ')
    surname = input('Surname: ')
    date_birth = input('Date of birth: ')
    user = {
        "name": name,
        "surname": surname,
        "date of birth": date_birth
    }
    try:
        with open("users.json", "r") as file:
            info = json.load(file)
    except FileNotFoundError:
        info = []

    info.append(user)

    with open("users.json", "w") as file:
        json.dump(info, file, indent=4)

    print('User add completled.')


def view_users():
    try:
        with open("users.json", "r") as file:
            info = json.load(file)
            for idx, user in enumerate(info, start=1):
                print(f"User {idx}:")
                print(f"Name: {user['name']}")
                print(f"Surname: {user['surname']}")
                print(f"Date of birth: {user['date of birth']}")
                print("------------------------")
    except FileNotFoundError:
        print("The file 'user.json' does not exist or is empty.")
while True:
    print("Choice number: ")
    print("1. User add")
    print("2. View users")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        user_add()
    elif choice == "2":
        view_users()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Your choice is wrong")

