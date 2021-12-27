name = input('Введите имя: ')
print(name)
name1 = "Валера"

if name == name1:
    print('ТЫ МОЛОДЕЦ')
elif len(name) < 6:
    print ('Такое имя недопустимо')
elif name == 'Алеша Силкин':
    print("HELLO MOTO, Алеша Силкин")
else: 
    print('ТЫ РУКОЖОП')


print('КОНЕЦ')