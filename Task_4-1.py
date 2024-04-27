userName = input("Введите ваше имя:")
userSurname = input("Введите вашу фамилию:")
userAge = input("Введите ваш возраст:")
#Вывод с использованием форматной строки
print("""
Ваше имя:{0}
Ваша фамилия:{1}
Ваш возраст:{age}
""".format(userName,userSurname,age = userAge))
#Вывод с использованием f-string
print(f"""
Ваше имя:{userName}
Ваша фамилия:{userSurname}
Ваш возраст:{userAge}
""")
#Чтобы не закрывалась
input()