def file_writer(text:str,fileName:str):  #Я не знаю, как проверить наличие файла в директории. Это ни на что не влияет, но обидно. Такую фичу можно только с библиотеками накрутить
        file = open(f"Home_work_4\\{fileName}.txt",'a+',encoding="utf-8")  #Если передать имя файла, которого не существует, то он сам создастся
        file.write(f"{text}\n")
        file.close()

Name = "Text"
add_str = input("Введите строку:")
file_writer(add_str,Name)
with open(f"Home_work_4\\{Name}.txt",'r',encoding="utf-8") as file:
    l = file.readlines()
    for index,element in enumerate(l):
          if((index+1) % 2 == 0):
                print(element)
          