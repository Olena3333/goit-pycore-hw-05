def error_handler(func): #Декоратор для обробки помилок вводу
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"Unexpected error: {e}"
    return wrapper

def parse_input(user_input): #Розбиває введений рядок користувача на команду та аргументи.
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


@error_handler
def add_contact(args, contacts): #Додає новий контакт
    if len(args) < 2:
        raise ValueError  # викликає обробку декоратором
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@error_handler
def change_contact(args, contacts): #Змінює номер телефону існуючого контакту
    if len(args) < 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@error_handler
def show_phone(args, contacts): #Показує номер телефону за іменем
    if len(args) < 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@error_handler
def show_all(contacts): #Показує всі контакти
    if not contacts:
        return "No contacts."
    return "\n".join(f"{n}: {p}" for n, p in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Try: add, change, phone, all, hello, exit")

main()
