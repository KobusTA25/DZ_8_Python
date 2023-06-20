def input_dataset():
    surname = input("Введите фимилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите телефон: ")
    return {"surname": surname, "name": name, "patronymic": patronymic, "phone": phone}

def controller():
    mode = int(input("Сделайте выбор: введите 1 для поиска ФИО, введите 2 для добавления ФИО: "))
    if mode == 1:
        surname = inp_surname()
        find_person(surname)
    elif mode == 2:
        dataset = input_dataset()
        write_person(dataset)
    else:
        print("Вы ввели неверные данные.")
        controller()

def inp_surname():
    surname = input("Введите фамилию поиска: ")
    return surname

def write_person(dataset: dict):
    with open('spravochnic.txt', 'a', encoding='utf-8') as file:
        file.write('\n\n')
        file.write(' '.join(dataset.values()))

def find_person(surname: str):
    with open('spravochnic.txt', 'r', encoding='utf-8') as file:
        entries = file.readlines()
        for entry in entries:
            data = entry.strip().split(' ')
            if data[0] == surname:
                print("Фамилия:", data[0])
                print("Имя:", data[1])
                print("Отчество:", data[2])
                print("Телефон:", data[3])
                print()

controller() 