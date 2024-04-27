userList =[]
listCount = int(input("Сколько элементов будет в вашем списке:"))
poww = int(input("В какую степень мы будет возводить эти числа:"))
for i in range(listCount):
    numberCheck = True
    userInput = (input("Введите элемент:"))
    for character in userInput:
        if character not in['1','2','3','4','5','6','7','8','9','0']:
            numberCheck=False
            break
    if(numberCheck):  #Если число
        userList.append(pow(int(userInput),poww))
    else:  #Если строка
        userList.append(userInput*poww)
print(userList)
input()