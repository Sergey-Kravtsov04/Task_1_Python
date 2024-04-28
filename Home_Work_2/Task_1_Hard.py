dictionary = {"Имя": ["Андрей", "Кирилл", "Анна", "Евгений", "Евгений", "Александр", "Татьяна", "Аркадий", "Игорь", "Кирилл"],
              "Фамилия": ["Иванов", "Лазарев", "Петрова", "Надобников", "Никитин", "Иванов", "Никитина", "Лихачев", "Никитин", "Левашев"],
              "Город проживания": ["Москва", "Омск", "Псков", "Псков", "Москва", "Псков", "Москва", "Омск", "Псков", "Москва"],
              "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
              "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
              "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
              "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия", "Работает", "Студент"]
              }
i=0 #Вспомогательная переменная для получения индекса value относительно списка
fullList=[]
nameList=[]
surNameList=[]
fullNameList = []
yearList = []
monthList = []
dayList =[]
birthdayList = []
countryList=[]
statusList = []
for key,value in dictionary.items():
    fullList.append(value)

for value in fullList[0]:  #Перемещаем имена в отдельный список
    if (value == "Кирилл"):  #Издеваемся над Кирилллом
        value+="л"
    if(value =="Александр"):
        fullList[6][i]="Работает"
    nameList.append(value)
    i+=1
i=0 #Обнуляем i
for value in fullList[1]:  #Перемещаем фамилии в отдельный список
    if(value =="Никитина" or value =="Никитин"):  #Никитины по условию переехали
        fullList[2][i] = "Махачкала"
    if (value == "Лихачев"):
        fullList[6][i] = "Мертв"  #Я не смог удалить Лихачева полностью на данном этапе. Просто поменял статус
    surNameList.append(value)
    i+=1  
for i in range(len(nameList)):  #Соединяем имена с фамилиями.
    tmpStr=f"{nameList[i]} {surNameList[i]}"
    fullNameList.append(tmpStr)
for value in fullList[3]:  #Перемещаем года рождения в отдельный список
    yearList.append(value)
for value in fullList[4]:  #Перемещаем месяцы рождения в отдельный список
    if value<10:
        value = "0"+str(value)  #Для форматы ГГГГ-ММ-ДД
    monthList.append(value)
for value in fullList[5]:  #Перемещаем дни рождения в отдельный список
    if value<10:
        value = "0"+str(value)  #Для форматы ГГГГ-ММ-ДД
    dayList.append(value)
for i in range(len(nameList)):  #Объединяем прошлые 3 листа в один, который содержит полную дату рождения
    tmpStr=f"{yearList[i]}-{monthList[i]}-{dayList[i]}"
    birthdayList.append(tmpStr)
for value in fullList[2]:  #Перемещаем города в отдельный список
    countryList.append(value)
for value in fullList[6]:  #Перемещаем статусы в отдельный список
    statusList.append(value)
#Объединяем получившиеся листы в один
newDataList = list(zip(fullNameList,birthdayList,countryList,statusList))  
for value in newDataList:  
    print(newDataList.index(value)+1,value)
print()  
#Это вообще не нужно было делать. Но зато здеcь можно удобно удалить Лихачева
#Проблема в том, что эти данные будет проблематично занести в словарь
# for value in newDataList:
    # if(value[0]=="Аркадий Лихачев"):  #Лихачев погиб, поэтому удаляем
    #     newDataList.remove(value)
    #     continue
    # print(newDataList.index(value)+1,value)
newDict = {}  #Создаём новый словарь  
newDict["Имя Фамилия:"]=fullNameList
newDict["Дата рождения:"]=birthdayList
newDict["Город проживания:"]=countryList
newDict["Статус:"]=statusList
for key,value in newDict.items():
    print(key,value)
input()