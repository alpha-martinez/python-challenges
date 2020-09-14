print("Welcome to Chase bank.")

balance = "7000"

def banking(balance):
    print('Your current balance is')
    print('$' + balance)
    first = input("What would you like to do? (deposit, withdraw, check_balance)")

    if first == "deposit":
        deposit = input('How much would you like to deposit? ')
        print('Deposited $' + int(deposit))
        balance = int(deposit) + int(balance)
    elif first == "withdraw":
        withdraw = input('How much would you like to withdraw from your account? ')
        print ('Withdrew $' + withdraw)
        balance = int(balance) - int(withdraw)    
    elif action == "check_balance":
        balance == balance
    else:     
        print('Sorry')

    done = input('Are you done? (yes or no)')
    if done == "yes":
        print('Have a nice day!')
    else: 
        print('What would you like to do next? (deposit, withdraw, check_balance)') 
        
banking(balance)

print("Have a nice day!")   