
from os import path, makedirs, listdir
from datetime import date

name = input("Please, enter your name: ")
surname = input("Please, enter your surname: ")
personal_id_number = int(input("Please, enter you personal ID number: "))

file_created = ""
today_date = date.today().strftime("%Y-%m-%d")


def create_folder():
    if not path.exists(today_date):
        makedirs(today_date)

def create_file():
    global file_created
    file_created = path.join(today_date, f"{personal_id_number}.txt")


def write_file_info():
    with open(file_created, "w") as f:
        f.write(f"Name: {name}\nSurname: {surname}\nPersonal ID number: {personal_id_number}\n")


def output_to_screen():
    for file in listdir(today_date):
        with open(path.join(today_date, file), "r") as f:
            print(f.read())


create_folder()
create_file()
write_file_info()
output_to_screen()
