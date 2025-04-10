from text_utils import clean_text


clients = []




#function append clients in dict for check unique in email
def add_client(name, email):
    name = clean_text(name)
    email = email.strip().lower()
    unique_client = {"name":name, "email":email}
    
    for client in clients:
        if client["email"] == unique_client["email"]:
            return False
    clients.append(unique_client)
    
    return True


def find_client(email):
    normalized_email = email.strip().lower()
    
    for client in clients:
        if client["email"] == normalized_email:
            return client
    
    return None 


def delete_client(email):
    normalized_email = email.strip().lower()
    
    for i, client in enumerate(clients):
        if client["email"] == normalized_email:
            del clients[i]
            return True
    
    
    return False


def find_by_name(name):
    normalized_name = name.strip().lower()
    results = []

    for client in clients:
        if normalized_name in client["name"].lower():
            results.append(client)

    return results


def show_menu():
    print("\nМЕНЮ:")
    print("1 - Добавить клиента")
    print("2 - Удалить клиента")
    print("3 - Найти клиента по email")
    print("4 - Найти клиента по имени")
    print("5 - Показать всех клиентов")
    print("6 - Выйти из программы\n")

    
    while True:
        user_input = input("Введите число: ")
        if user_input == "1":
            name = input("Введите имя: ")
            email = input("Введите email: ")
            result = add_client(name, email)
            if result:
                print("Клиент добавлен.")
            else:
                print("Такой клиент уже есть.")

            
        elif user_input == "2":
            email = input("Введите email: ")
            result = delete_client(email)
            if result:
                print("Клиент удален.")
            else:
                print("Клиент не найден.")   
                
        elif user_input == "3":
            email = input("Введите email: ")
            result = find_client(email)
            if result:
                print(f"Имя: {result['name']}, Email: {result['email']}")
            else:
                print("Клиент не найден.")
                          
        elif user_input == "4":
            name = input("Введите имя: ")
            result = find_by_name(name)
            if result:
                for client in result:
                    print(f"Имя: {client['name']}, Email: {client['email']}")
            else:
                print("Клиенты не найдены.")
  
                
        elif user_input == "5":
            for client in clients:
                print(f"Имя: {client['name']}, Email: {client['email']}")
        elif user_input == "6":
            break
        else:
            print("Ошибка!Введено неверное значение!")
        

             
    
        

    


if __name__ == "__main__":
    show_menu()
        