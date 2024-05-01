class Wallet:
    balance:int
    valuta: list
    walletName:str
    def __init__(self, balance:int=0, walletName:str="",valuta:list=["руб","дол"]):
        self.balance = balance
        self.walletName = walletName
        self.valuta = valuta
    def deposit(self, moneyFrom:int):
        self.balance +=moneyFrom
        print(f"Вы внесли:{moneyFrom} {self.valuta[0]}")
        print(f"Сейчас на счету:{self.balance} {self.valuta[0]}")
    def payment(self, product:dict):
        finalSum:int = 0
        finalProd:dict =[]
        for k, v in product.items():
            finalSum = finalSum + v
            finalProd.append(k)
        print(f"Вы уверены, что хотите купить {finalProd}, за {finalSum} {self.valuta[0]}")
        paymentInput = (input("Y/N:")).lower()
        if(paymentInput == 'y'):
            if(self.balance>=finalSum):
                self.balance-=finalSum
                print(f"На счету осталось{self.balance} {self.valuta[0]}")
            else:
                print("У вас недостаточно денег!!!")
        else:
            pass
    def balance_check(self):
        print(f"Сейчас на счету {self.balance} {self.valuta[0]}")
    def wallet_name_check_change(self):

        print(f"Текущее имя кошелька:{self.walletName}")
        print("Хотите сменить имя кошелька?")
        ChangeNameInput = (input("Y/N:")).lower()
        if(ChangeNameInput == 'y'):
            otherNameInput = input("Введите новое имя кошелька:")
            self.walletName= otherNameInput
        else:
            pass
    def currency_exchange(self):
        pass
class Crypto_Wallet(Wallet):
    coin:int = 0
    BTC:int = 0
    ETH: int = 0
    valutaCoin:list =['BTC','ETH']
    def __init__(self, coin:int,BTC:int,ETH:int,balance:int ,walletName:str,valuta:list=["руб","дол"]):
        super().__init__(balance, walletName,valuta)
        self.coin = coin
        self.BTC = BTC
        self.ETH = ETH
    def deposit_for_coin(self, coinFrom:int):
        self.coin +=coinFrom
        print(f"Вы внесли:{coinFrom} коинов")
        print(f"Сейчас на счету:{self.coin} коинов")
    def transfer_coin_to_coin(self,coinFrom:int, valut:str):
        if(self.coin >= coinFrom):
            if(valut ==self.valutaCoin[0]):
                self.BTC+=coinFrom
                self.coin -=coinFrom
                print(f"Вы перевели {coinFrom} коинов в BTC")
            elif(valut ==self.valutaCoin[1]):
                self.ETH+=coinFrom
                self.coin -=coinFrom
                print(f"Вы перевели {coinFrom} коинов в ETH")
        else:
            print("У вас недостаточно коинов")
    def coin_check(self):
        print(f"Коины:{self.coin}\nBTC:{self.BTC}\nETH:{self.ETH}")
    def transfer_coin_to_valute():
        pass

    



while True:
    print("""1 - создать новый кошелёк
2 - выйти из программы""")
    userInput= input("Введите номер операции:")
    if(userInput=='1'):
        print("\n"*30)  #Я просто не умею чистить консоль
        cryptoWallet = Crypto_Wallet(0,0,0,0,"My_Crypto_Wallet")
        while True:
            print("Выберите операцию:")
            print("1 - пополнение баланса\n2 - пополние баланса коинами\n3 - оплата\n4 - узнать количество денег на балансе\n5 - узнать количество коинов на балансе\n6 - перевести коины\n7 - узнать имя кошелька\n8 - удалить кошелёк\n9 - выйти из меню\n10-перевод из валюты в валюту\n11-перевод из коинов в валюту\n12-перевод из валюты в коины")
            userInput = input("Введите номер операции:")
            if(userInput =='1'):
                try:
                    print()
                    depositInput=int(input("Введите сумму, которую хотите положить на кошелёк:"))
                    cryptoWallet.deposit(depositInput)
                except Exception as e:
                    print(e)
            elif(userInput =='2'):
                try:
                    print()
                    depositInput=int(input("Введите сумму, которую хотите положить на кошелёк:"))
                    cryptoWallet.deposit_for_coin(depositInput)
                except Exception as e:
                    print(e)
            elif(userInput =='3'):
                ourProducts:dict = {"Яблоки":60,"Бананы":120}
                cryptoWallet.payment(ourProducts)
            elif(userInput == '4'):
                cryptoWallet.balance_check()    
            elif(userInput == '5'):
                cryptoWallet.coin_check()
            elif(userInput == '6'):
                try:
                    valutaInput = int(input("Во что перевести коины:\n1-BTC\n2-ETH\n"))
                    depositInput=int(input("Введите количество коинов, которые хотите перевести:"))
                    cryptoWallet.transfer_coin_to_coin(depositInput,cryptoWallet.valutaCoin[valutaInput-1])
                except Exception as e:
                    print(e)        
            elif(userInput == '7'):
                cryptoWallet.wallet_name_check_change()
            elif(userInput == '8'):
                del(cryptoWallet)
                print("\n"*30)
                break
            elif(userInput == '9'):

                print("\n"*30)
                break
            elif(userInput == '10'):
                pass
            elif(userInput == '11'):
                pass
            elif(userInput == '12'):
                pass
            else:
                print("некорректный номер операции") 
    elif(userInput=='2'):
        break
    else:
        print("некорректный номер операции")