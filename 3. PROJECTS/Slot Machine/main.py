'''
create two mode one which accepts any money greater than 0.
and the other which accepts only 50, 100, 200, 500, 1000
'''

# deposit function


def deposit():

    while True:
        money = input("Enter the amount you want to deposit : ")

        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")

    return money


deposit()
