def fibonacci(num:int):
    l =[1,1]
    for i in range(num):
        l.append(l[i+1]+l[i])
        yield l[i]
step_num = 9
gen = fibonacci(step_num)
for i in range(step_num):  #Я не нашёл лучшего метода передать в итератор кол-во итераций
    print(next(gen))