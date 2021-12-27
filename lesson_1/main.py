date = input('Введите дату')
task = input('Введите задачу')
print(date, task)

data1 = input ('Введите дату')
task1 = input ('Введите задачу')
data2 = input ('Введите дату')
task2 = input ('Введите задачу')
data3 = input ('Введите дату')
task3 = input ('Введите задачу')
print(data1,task1)
print(data2,task2)
print(data3,task3)

task_dict = {}
task_dict[data1] = [task1]
task_dict[data2] = [task2]
task_dict[data3] = [task3]
print(task_dict)