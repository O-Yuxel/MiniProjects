def show_balance(balance):
    print(f"Bakiyeniz: {balance} TL")

def deposit(balance):
    money_deposit = int(input("Yatırılacak miktar: "))
    balance += money_deposit
    print(money_deposit, "TL başarıyla yatırıldı.")
    return balance

def withdraw(balance):
    money_withdraw = int(input("Çekilecek miktar: "))
    if money_withdraw <= balance:
        balance -= money_withdraw
        print(money_withdraw, "TL başarıyla çekildi.")
    else:
        print("Yetersiz bakiye.")
    return balance
    
def menu():
    balance = 3000

    while True:
        print("===== ATM =====\n\n1 - Bakiye Görüntüle\n2 - Para Yatır\n3 - Para Çek\n4 - Çıkış\n")
        answer = input("seçiminiz: ")
        if answer == "1":
            show_balance(balance)
        elif answer == "2":
            balance = deposit(balance)
        elif answer == "3":
            balance = withdraw(balance)
        elif answer == "4":
            print("İyi günler.")
            break
        else:
            print("Sadece menüdeki rakamları yazabilirsiniz!")

menu()