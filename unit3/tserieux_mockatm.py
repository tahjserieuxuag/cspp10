bank_account = 10000
print("1.Withdraw 2.Deposite 3.Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
while choice != "3" and bank_account > 0:
    if choice == "1":
        withdraw = int(input("How much money would you like to withdraw "))
        if withdraw > bank_account:
            print("Insufficient Funds")
        elif withdraw < bank_account:
            bank_account = bank_account - withdraw
            print(bank_account)
    elif choice == "2":
        deposit =int(input("How much money would you like to deposit "))
        bank_account = bank_account + deposit
        print(bank_account)
    elif choice == "3":
        print(bank_account)    
        break
    print("1.Withdraw 2.Deposite 3.Exit")
    choice = input("Welcome to ATM! Pick from above [1|2|3]: ")

    

print("Exit")

     