from logger import input_data, print_data, update_data, delete_data

def interface():
    print("Добрый день! Вы попали на специальный бот справочник! \n 1 - Записать данные \n 2 - Вывести данные \n 3 - Изменить данные \n 4 - Удалить данные")
    choice = input("Выберите действие (1-4): ")
    while choice not in ['1', '2', '3', '4']:
        print("Неправильный ввод. Введите 1, 2, 3 или 4.")
        choice = input("Выберите действие (1-4): ")
    
    if choice == '1':
        input_data()
    elif choice == '2':
        print_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        delete_data()