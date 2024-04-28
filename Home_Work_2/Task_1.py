userList =[]
listCount = int(input("Сколько элементов будет в вашем списке:"))
poww = int(input("В какую степень мы будет возводить эти числа:"))
for i in range(listCount):
    userInput = (input("Введите элемент:"))
    if(userInput.isdigit()):  #Если число
        userList.append(pow(int(userInput),poww))
    else:  #Если строка
        userList.append(userInput*poww)
print(userList)
input()