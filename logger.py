from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n\n"
    f"1 вариант: \n\n"
    f"{name}\n{surname}\n{phone}\n{address} \n\n"
    f"2 вариант: \n\n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберете вариант: \n\n"))

    while var != 1 and var != 2:
        print("Неправильный ввод. Введите 1 или 2.")
        var = int(input())
    
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address} \n\n")

    if var == 2:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n")
    print("Данные успешно внесены в справочник.")

def print_data():
    print ("Данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
        print(''.join(data_first_list))

    print ("Данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(data_second)
    
def read_data(filename, variant):
    records = []
    with open(filename, 'r', encoding='utf-8') as file:
        if variant == 1:
            content = file.read().strip()
            records_raw = content.split("\n\n") if content else []
            for record in records_raw:
                parts = record.split('\n')
                if len(parts) == 4:
                    records.append(parts)
        else:
            reader = reader(file, delimiter=';')
            for row in reader:
                if len(row) == 4:
                    records.append(row)
    return records

def write_data(filename, records, variant):
    with open(filename, 'w', encoding='utf-8') as file:
        if variant == 1:
            content = '\n\n'.join(['\n'.join(record) for record in records])
            file.write(content + '\n\n')
        else:
            writer = writer(file, delimiter=';')
            writer.writerows(records)

def select_record(records):
    for idx, record in enumerate(records, start=1):
        print(f"{idx}. Name: {record[0]}, Surname: {record[1]}, Phone: {record[2]}, Address: {record[3]}")
    selection = int(input("Выберите номер записи: ")) - 1
    return records[selection]

def update_delete_common_flow(variant, action):
    filename = 'data_first_variant.csv' if variant == 1 else 'data_second_variant.csv'
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    records = read_data(filename, variant)
    matches = [record for record in records if record[0] == name and record[1] == surname]

    if len(matches) == 0:
        print("Запись не найдена.")
        return
    elif len(matches) > 1:
        print("Найдено несколько записей:")
        selected_record = select_record(matches)
    else:
        selected_record = matches[0]

    if action == "update":
        new_name = input('Введите новое имя: ')
        new_surname = input('Введите новую фамилию: ')
        new_phone = input('Введите новый телефон: ')
        new_address = input('Введите новый адрес: ')
        records[records.index(selected_record)] = [new_name, new_surname, new_phone, new_address]
        print("Данные обновлены.")
    elif action == "delete":
        records.remove(selected_record)
        print("Данные удалены.")

    write_data(filename, records, variant)

def update_data():
    variant = int(input("В каком файле вы хотите изменить данные? 1 - Первый вариант, 2 - Второй вариант: "))
    update_delete_common_flow(variant, "update")

def delete_data():
    variant = int(input("В каком файле вы хотите удалить данные? 1 - Первый вариант, 2 - Второй вариант: "))
    update_delete_common_flow(variant, "delete")