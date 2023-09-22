import json


class User:
    def __init__(self, name: str, surname: str, date_birth: str):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "date_birth": self.date_birth
        }

def file_exists(file_name):
    try:
        with open(file_name, "r"):
            return True
    except FileNotFoundError:
        return False


def create_empty_file(file_name):
    with open(file_name, "w") as file:
        json.dump([], file)

def user_add():
    print('Add new user ')
    name = input('Name: ')
    surname = input('Surname: ')
    date_birth = input('Date of birth: ')

    new_user = User(name, surname, date_birth)

    # Sprawdzanie istnienia pliku
    if not file_exists("users.json"):
        create_empty_file("users.json")

    with open("users.json", "r") as file:
        info = json.load(file)

    info.append(new_user.to_dict())

    with open("users.json", "w") as file:
        json.dump(info, file, indent=4)

    print('User add completed.')


def view_users():
    if not file_exists("users.json"):
        print("The file 'user.json' does not exist or is empty.")
        return

    with open("users.json", "r") as file:
        info = json.load(file)
        for idx, user_data in enumerate(info, start=1):
            user = User(user_data['name'], user_data['surname'], user_data['date_birth'])
            print(f"User {idx}:")
            print(f"Name: {user.name}")
            print(f"Surname: {user.surname}")
            print(f"Date of birth: {user.date_birth}")
            print("------------------------")


def select_user():
    user_id = input("Enter the user ID you want to select: ")
    try:
        user_id = int(user_id)
    except ValueError:
        print("Invalid user ID. Please enter a valid number.")
        return

    if not file_exists("users.json"):
        print("The file 'user.json' does not exist or is empty.")
        return

    with open("users.json", "r") as file:
        info = json.load(file)
        if user_id >= 1 and user_id <= len(info):
            selected_user_data = info[user_id - 1]
            selected_user = User(selected_user_data['name'], selected_user_data['surname'],
                                 selected_user_data['date_birth'])
            print("  ")
            print(f"Selected User {user_id}:")
            print(f"Name: {selected_user.name}")
            print(f"Surname: {selected_user.surname}")
            print(f"Date of birth: {selected_user.date_birth}")
            print("__________________________")
        else:
            print("Invalid user ID. Please enter a valid number.")


def management():
    while True:
        print("Choice number: ")
        print("1. User add")
        print("2. View users")
        print("3. Select user by ID")
        print("4. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            user_add()
        elif choice == "2":
            view_users()
        elif choice == "3":
            select_user()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Your choice is wrong")


if __name__ == "__main__":
    management()