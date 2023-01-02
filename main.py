import json


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Sorry, try again"
        except ValueError:
            print("incorrect phone number")
        except KeyError:
            print("incorrect Name")
    return wrapper


def greetings(*args):
    print("How can I help you?")


@input_error
def add(*args):
    name = args[0][0]
    phone = args[0][1]
    int(phone)
    with open("contacts.json", "r") as file:
        dat = json.load(file)
    dat[name] = phone
    with open("contacts.json", "w") as file:
        json.dump(dat, file)
    print(f"contacts {name}, {phone} added")


@input_error
def change(*args):
    name = args[0][0]
    phone = args[0][1]
    int(phone)
    with open("contacts.json", "r") as file:
        dat = json.load(file)
    dat[name] = phone
    with open("contacts.json", "w") as file:
        json.dump(dat, file)
    print(f"contacts {name}, {phone} change")


@input_error
def output_phone(name):
    with open("contacts.json", "r") as file:
        dat = json.load(file)
    print(dat[name[0]])


def show_all(*args):
    with open("contacts.json", "r") as file:
        dat = json.load(file)
    print(dat)


COMMANDS = {
    greetings: "hello",
    add: "add",
    change: "b",
    output_phone: "phone",
    show_all: "show"
}


def command_parser(u_input: str):
    for comand, key_words in COMMANDS.items():
        if u_input.startswith(key_words):
            return comand, u_input.replace(key_words, "").strip().split(" ")
    return None, None


def main():
    while True:
        u_input = input(">>>")
        u_input = u_input.lower()
        if u_input in [".", "good bye", "close", "exit"]:
            print("Good bye!")
            break
        comand, data = command_parser(u_input)
        if not comand:
            print("Enter command")
        else:
            comand(data)


if __name__ == "__main__":
    main()
