from store import Store
from time import sleep


    def main():
        store()


    def store():
        print("Hello Customer! Welcome to the Online Coffee Store.")
        sleep(1)
        print("One moment please while we load the store for you.")
        sleep(2)
        print('******************************************************************************************************')
        print()
        userName = input("What is your name? ")
        print()
        print("Thank You, one moment please.")
        sleep(1)
        print("*******************************************************************************************************")
        print()
        print(" 1. Columbian Roast, coffee, 8.45")
        print(" 2. Pumpkin Spice, coffee, 10.35")
        print(" 3. Jedi Java, coffee, 13.25")
        print(" 4.Tastea, tea, 6.75")
        print(" 5. Earl Grey (hot), tea, 4.50")
        print(" 6. Westminster Queen's Choice, tea, 1.95")
        print()
        print("DISCLAMER: Name, Type, Cost Per Pound")
        print()
        print("*******************************************************************************************************")
        print()
        order = input("What would you like? ")
        if order == 1:
            productPrice = 8.45
        elif order == 2:
            productPrice = 10.35
        elif order == 3:
            productPrice = 13.25
        elif order == 4:
            productPrice = 6.75
        elif order == 5:
            productPrice = 4.50
        elif order == 6:
            productPrice = 1.95
        else:
            TypeError("Invalid Input, Please put in a number.")
            order()
        howMuch = input(float("How much would you like? (Number of Pounds): "))
        orderCost = productPrice * howMuch
        while not float:
            TypeError("Invalid Input, Please put in a number.")
            howMuch()
        return userName, howMuch, orderCost

    def get_shipping():
        print()
        print("*******************************************************************************************************")
        print()
        print("1. Standard Shipping, Normal shipping method, 4.50, 1.86")
        print("2. FedEx, Faster; but more expensive, 0.00, 4.65")
        print("3. UPS, Less expensive for very large orders, 12.00, 0.95")
        print()
        print("DISCLAMER: Name of Shipping, Description, Up Front Cost, Cost Per Pound")
        shippingType = input(float("Which shipping method would you like? "))
        while not float:
            TypeError("Invalid Input. Please enter an option that is printed above.")
            shippingType
        print("*******************************************************************************************************")
        return shippingType

    def cost(howMuch, shippingType):
        if shippingType == 1:
            shippingTotal = 4.50 + (howMuch * 1.86)
        elif shippingType == 2:
            shippingTotal = 0.00 + (howMuch * 4.65)
        elif shippingType == 3:
            shippingTotal = 12.00 + (howMuch * 0.95)
        else:
            print("If you see this.. it's too late.")
        return shippingTotal

    def total_cost(orderCost, shippingTotal):
        totalCost = (orderCost + shippingTotal)
        return totalCost

    def get_receipt(userName, howMuch, orderCost, shippingType, shippingTotal, totalCost):
        print()
        print("*******************************************************************************************************")
        print(f' Order Name: {userName}')
        print("*******************************************************************************************************")
        print()
        print(f' Number of Pounds Ordered:     {howMuch}')
        print(f' Order Cost Before Shipping:   {orderCost}')
        print(f' Shipping Type Selected:       {shippingType}')
        print(f' Cost Of Shipping:             {shippingTotal}')
        print("*******************************************************************************************************")
        print()
        print(f' Total Cost:                   {totalCost}')
        print()
        print("*******************************************************************************************************")









main()