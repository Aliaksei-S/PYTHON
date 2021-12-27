HELP = """
help - напечатать справку по программе
add - добавить задачу в список
show - показать список всех задач
"""
tasks = []

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
