def square_generator(lst:list) ->list:
    return [x**2 for x in lst]
def dict_generator(day:list) ->dict:
    return {day[value]:value+1 for value in range(0,7)}
def list_to_lower(library:list) ->set:
    return {str.lower(x) for x in library}
#
ourLst = []
for i in range(1,11):  
    ourLst.append(i)
print(square_generator(ourLst))
#
daysLst =["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
print(dict_generator(daysLst))
#
librarisLst =["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
print(list_to_lower(librarisLst))


