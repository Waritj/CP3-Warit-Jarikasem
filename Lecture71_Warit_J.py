menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()

def calTotal():
    totalPrice = 0
    for number in range(len(priceList)):
        totalPrice = totalPrice + int(priceList[number])
    print('Total Price is', totalPrice, 'THB')

calTotal()
