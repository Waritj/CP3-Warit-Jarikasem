def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator():
    vat = 7
    totalPrice = int(input("Price: "))
    return totalPrice + (totalPrice * vat / 100)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return price1 + price2

logResult = login()
if logResult == True:
    showMenu()
    no = menuSelect()
    if no == 1:
        print(vatCalculator())
    elif no == 2:
        print(priceCalculator())
else:
    print("Login Error!")
