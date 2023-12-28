import csv

def display_contacts(contacts):
    for contact in contacts:
        print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}")

def load_contacts(file_path):
    contacts = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    return contacts

def save_contacts(file_path, contacts):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    new_contact = {
        'Фамилия': input("Введите фамилию: "),
        'Имя': input("Введите имя: "),
        'Отчество': input("Введите отчество: "),
        'Номер телефона': input("Введите номер телефона: ")
    }
    contacts.append(new_contact)
    print("Контакт добавлен.")

def edit_contact(contacts, search_key, search_value):
    for contact in contacts:
        if contact[search_key] == search_value:
            contact['Фамилия'] = input("Введите новую фамилию: ")
            contact['Имя'] = input("Введите новое имя: ")
            contact['Отчество'] = input("Введите новое отчество: ")
            contact['Номер телефона'] = input("Введите новый номер телефона: ")
            print("Контакт изменен.")
            return
    print(f"Контакт с {search_key} '{search_value}' не найден.")

def delete_contact(contacts, search_key, search_value):
    for i, contact in enumerate(contacts):
        if contact[search_key] == search_value:
            del contacts[i]
            print("Контакт удален.")
            return
    print(f"Контакт с {search_key} '{search_value}' не найден.")

def main():
    contacts_file_path = 'contacts.csv'
    contacts = load_contacts(contacts_file_path)

    while True:
        print("\n1. Вывести контакты")
        print("2. Сохранить контакты")
        print("3. Добавить контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            save_contacts(contacts_file_path, contacts)
            print("Контакты сохранены.")
        elif choice == '3':
            add_contact(contacts)
        elif choice == '4':
            search_key = input("Введите ключ для поиска (Фамилия, Имя, Отчество, Номер телефона): ").capitalize()
            search_value = input("Введите значение для поиска: ")
            edit_contact(contacts, search_key, search_value)
        elif choice == '5':
            search_key = input("Введите ключ для поиска (Фамилия, Имя, Отчество, Номер телефона): ").capitalize()
            search_value = input("Введите значение для поиска: ")
            delete_contact(contacts, search_key, search_value)
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 6.")

if __name__ == "__main__":
    main()