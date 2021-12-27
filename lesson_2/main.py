HELP = """
help - вывести на экран справочные материлы
add - добавить команду
show - вывести на экран созданные задачи
exit - выход из программы"""

today = []
tomorrow = []
other = []


run = True

while run:
    print("Ожидание команды....")
    command = input('Введите команду')
    
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Задачи на сегодня", today)
        print("Задачи на завтра", tomorrow)
        print("Остальные задачи", other)

    elif command == "add":
        date = input("Введите дату для добавления задач")
        task = input ("Введите название задачи")
        if date == "сегодня":
            #task = input ("Введите название задачи")
            today.append(task)
            print('Задача добавлена!')
        elif date == "завтра":
            #task = input ("Введите название задачи")
            tomorrow.append(task)
            print('Задача добавлена!')
        else:
            #task = input ("Введите название задачи")
            other.append(task)
            print('Задача добавлена!')

    elif command == "exit":
        print('Получена команда на выход')
        print("Спасибо за пользование! До свидания!")
        break
    else:
        print ("Неизвестная команда. Программа завершает работу")
        break
