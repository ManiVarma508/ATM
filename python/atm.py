username='Lucky'
password='atm1234'

c_name=input("Enter your name:")
c_pass=str(input("Enter your password:"))

if c_name==username and c_pass==password:
    while True:
        print(''''
        1.Deposit
        2.withdraw
        3.mini_statement
        4.exit''')
        amount=50000
        option=int(input("select your option:"))
        if option==1:
            dep=int(input("Enter the amount:"))
            amount+=dep
            print("---------------------------")
            print("Total amount:",amount)
            print("---------------------------")
        elif option==2:
            withd=int(input("Enter the amount:"))
            amount-=withd
            print("---------------------------")
            print("Total amount",amount)
            print("---------------------------")
        elif option==3:
            print("=========OUR ATM==========")
            print("Username:",username)
            print("Total amount=",amount)
            print("Thanks for visiting")
            print("=========OUR ATM=========")      
        elif option==4:
            exit()
else:
    print("please enter correct login details")
