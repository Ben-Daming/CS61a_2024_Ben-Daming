#an example of non-local function
def makewithdraw(balance):
    'return a function that return balance-amount'
    def withdraw(amount):
        nonlocal balance
        if balance-amount<0:
            return 'no enough money'
        balance-=amount
        return balance
    return withdraw
