print("Welcome to Chase bank.")


def banking():
    balance = 7000
    print("Your current balance is $" + str(balance))
    first_prompt = input("Would you like to deposit, withdraw or check_balance?")
    
    if first_prompt == "deposit":
        deposit = input("How much would you like to deposit?")
        balance = int(balance) + int(deposit)
        print("Your new balance is $" + str(balance))
        final_prompt()
        
    elif first_prompt == "withdraw":
        withdraw = input("How much would you like to withdraw?")
        balance = balance - int(withdraw)
        print("Withdrew $" + str(withdraw) + ". Your new balance is $" + str(balance))
        final_prompt()
    
    elif first_prompt == "check_balance":
        print(balance)
    else:
        print('move it then')

def final_prompt():
    done = input("Would you like to do anything else? Y/N")
    done = done.upper()
    if done == "Y":
        banking()
    else:
        print("Have a nice day!")
        
banking()