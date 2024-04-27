set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

tmpSet= set1|set2
finalSet = tmpSet|set3
ourList =[]

for numb in set1:
    for numb1 in set2:
        if(numb == numb1):
            ourList.append(numb1)
for numb in tmpSet:
    for numb1 in set3:
        if(numb == numb1):
            ourList.append(numb1)
print(finalSet) 
print(ourList)  #Тут разницу проверяем, наверное. Я не до конца понял формулировку


