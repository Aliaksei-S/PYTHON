#x = 1
#while x <=10:
#    print(x)
#    x = x+1
#print(x)

HELP = """
help - напечатать справку по программе
add - добавить задачу в список
show - показать список всех задач
"""
tasks = []

run = True

while run:
    command = input('Введите команду:')
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input('Введите название задачи: ')
        tasks.append(task)
        print("Задача добавлена")
    else:
        print("ТЫ РУКОЖОП")
        break 
print("Неизвестная команда. Работа программы завершена!")