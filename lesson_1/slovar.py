# cat: кошка
# bat: летучая мышь

# ключ: значение

dictionary = {
    "cat": "кошка",
    "bat": "летучая мышь"
}
print(dictionary)
cat=dictionary["cat"]
print(cat)

counrties = {
    "Африка" : ["Египет", "Конго", "ЮАР"],
    "Азия" : ["Китай", "Таиланд", "Индонезия"] 
}
africa = counrties["Африка"]
print(africa)

africa_key = "Африка"
print(counrties[africa_key])

counrties["Европа"] = ["Австрия", "Испания", "Италия"]
print(counrties)
print(counrties["Европа"])

africa.append("Эфиопия")
print(africa)
print(counrties)
print(counrties["Африка"])

name = input("Введите имя: ")
#print(name)
print("Привет", name)