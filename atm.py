class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin 

    def balanceinquiry(self):
        print("Your balance is : $90")

    def cashwithdrawal(self,amount):
        new_amount=90-amount
        print("You withdrawed: " +str(amount) + "Your remaining balance is " + str(new_amount))

def main ():
    name=input("Hello Enter your name: ")
    print("Hello,"+name)
    cardnumber=input("Insert your cardnumber: ")
    pin=input("Enter your pin: ")
    new_user=Atm(cardnumber,pin)

    print("choose you activity: ")
    print("1.Balance Inquiry")
    print("2.Cash Withdrawal")
    activity=int(input("Enter activity choice: "))

    if (activity ==1):
        new_user.balanceinquiry()
    elif(activity==2):
        amount=int (input("Enter the amount: "))
        new_user.cashwithdrawal(amount)
    else:
        print("Enter a valid number: ")

if __name__ == "__main__":
    main()


