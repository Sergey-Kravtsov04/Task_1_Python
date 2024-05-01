class Wallet:
    balance:int = 0
    valuta: str ="руб"
    walletName:str=""
    def __init__(self, balance, walletName):
        self.balance = balance
        self.walletName = walletName
    def deposit(self, moneyFrom:int):
        self.balance +=moneyFrom
        print(f"Вы внесли:{moneyFrom} {self.valuta}")
        print(f"Сейчас на счету:{self.balance} {self.valuta}")
    def payment(self, product:dict):
        finalSum:int = 0
        finalProd:dict =[]
        for k, v in product.items():
            finalSum = finalSum + v
            finalProd.append(k)
        print(f"Вы уверены, что хотите купить {finalProd}, за {finalSum} {self.valuta}")
        paymentInput = (input("Y/N:")).lower()
        if(paymentInput == 'y'):
            if(self.balance>=finalSum):
                self.balance-=finalSum
                print(f"На счету осталось{self.balance} {self.valuta}")
            else:
                print("У вас недостаточно денег!!!")
        else:
            pass
    def balance_check(self):
        print(f"Сейчас на счету {self.balance} {self.valuta}")
    def wallet_name_check_change(self):
        print(f"Текущее имя кошелька:{self.walletName}")
        print("Хотите сменить имя кошелька?")
        ChangeNameInput = (input("Y/N:")).lower()
        if(ChangeNameInput == 'y'):
            otherNameInput = input("Введите новое имя кошелька:")
            self.walletName= otherNameInput
        else:
            pass


while True:
    print("""1 - создать новый кошелёк
2 - выйти из программы""")
    userInput= input("Введите номер операции:")
    if(userInput=='1'):
        print("\n"*30)  #Я просто не умею чистить консоль
        userWallet = Wallet(0,"MyWallet")
        while True:
            print("Выберите операцию:")
            print("""    1 - пополнение баланса
    2 - оплата
    3 - узнать количество денег на балансе
    4 - удалить кошелёк
    5 - узнать имя кошелька
    6 - выйти из меню""")
            userInput = input("Введите номер операции:")
            if(userInput =='1'):
                try:
                    depositInput=int(input("Введите сумму, которую хотите положить на кошелёк:"))
                    userWallet.deposit(depositInput)
                except Exception as e:
                    print(e)
            elif(userInput =='2'):
                ourProducts:dict = {"Яблоки":60,"Бананы":120}
                userWallet.payment(ourProducts)
            elif(userInput == '3'):
                userWallet.balance_check()                
            elif(userInput == '4'):
                del(userWallet)
                print("\n"*30)
                break
            elif(userInput == '5'):
                userWallet.wallet_name_check_change()
            elif(userInput == '6'):
                print("\n"*30)
                break
            else:
                print("некорректный номер операции") 
    elif(userInput=='2'):
        break
    else:
        print("некорректный номер операции")
             
