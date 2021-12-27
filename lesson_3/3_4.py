import random
HELP = """
help - вывести на экран справочные материлы
add - добавить команду
show - вывести на экран созданные задачи
exit - выход из программы
random - добавляет случайную команду на дату сегодня """
RANDON_TASK = "Слуйчайная команда"
RANDOM_TASKS = ['записаться на курс в Нетологию','написать письмо Гвидо (создателю языка PYTHON)','помыть машину','покормить кошку']
tasks = {}
def add_todo (date, task):
    if date in tasks:
            tasks [date].append(task)
            print("Задача", task, " добавлена на дату", date)
    else:
        tasks [date]  = [task]
        print("Задача", task, " добавлена на дату", date)


run = True

while run:
    print("Ожидание команды....")
    print("Все доступные действия доступны по команде help")
    command = input('Введите команду: ')
    if command == "help":
        print(HELP)

    elif command == "show":
      date = input("Введите дату для отображения списка задач: ")
      if date in tasks:
          for task in tasks[date]:
              print ('Дата ', date, 'задача: ',task)
      else:
        print('На  дату', date, 'задачи отсутствуют')    
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")    
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo('Сегодня', task)
    elif command == "exit":
        print('Получена команда на выход')
        print("Спасибо за пользование! До свидания!")
        break
    else:
        print ("Неизвестная команда. Программа завершает работу")
        break
