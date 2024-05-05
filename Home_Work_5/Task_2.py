import calendar as cal  #Отсылка на убунту
import re
from faker import Faker
#
def cal_func(year,month):
    shablon = r"\d{4}-\d{2}"  #Родной Хабр спасает
    ourDate = f"{year}-{month}"
    print(ourDate)
    if(re.match(shablon,ourDate) and (month>0 and month<=12)):
        print(cal.month(year,month))
    else:
        print("Вы неправильно ввели данные")
#
ourYear = int(input("Введите год в формате ГГГГ:"))
ourMonth = int(input("Введите месяц в формате ММ:"))
cal_func(ourYear,ourMonth)
fake = Faker("ru_RU")
ourNumber = fake.phone_number()
#Это для тестов номера. Чтобы из головы не выдумывать
# ourNumber = "+79112544315"
# ourNumber = "79112544315"
# ourNumber = "89112544315"
print(ourNumber)  #Смотрим какой номер сгенерировал Faker
numberShablon = r"[-+]?7\d{10}|7\d{10}|8\d{10}"  #Снова Хабр
#Тут проблемка в том, что Faker разные форматы номеров выдаёт. Если иметь единый шаблон(или знать все), то всё будет гладко
#Но фейкера по условию тут нет. Поэтому без него всё хорошо работает
if(re.match(numberShablon,ourNumber)):
    print (ourNumber)  #Если номер подходит под шаблон, то он выведется второй раз
