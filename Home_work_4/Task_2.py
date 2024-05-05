def fibonacci(num:int, dct:dict):
    for i in range(num):
        dct[i+3] = dct.get(i+1,0)+dct.get(i+2,0)  
        yield dct.get(i+1,0)  

step_num = 9
step_dict = {1:1, 2:1}
gen = fibonacci(step_num,step_dict)
for i in range(step_num):  #Я не нашёл лучшего метода передать в итератор кол-во итераций
    print(next(gen))