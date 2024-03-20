Apple_Price = 30
Banana_Price = 25
Pineapple_Price = 35
Grape_Price = 75

User = input("User: ")
Pswd = input("Password: ")

if User == "warit" and Pswd == "1234":
    print("------------------------------------------")
    print("------------ WELCOME ", User, "---------------")
    print("------------------------------------------")
    print("                                          ")
    print("We have many products for you"aa)
    print("1. Apple", Apple_Price, "THB / pc")
    print("2. Banana", Banana_Price, "THB / pc")
    print("3. Pineapple", Pineapple_Price,"THB / pc")
    print("4. Grape", Grape_Price,"THB / pc")
    print("                                          ")
    print("Please input no.of piece for each product to buy")
    Apple_no = int(input("No. of Apple: "))
    Banana_no = int(input("No. of Banana: "))
    Pineapple_no = int(input("No. of Pineapple: "))
    Grape_no = int(input("No. of Grape: "))
    print("                                          ")
    print("Your buying list are as follow:")
    if Apple_no > 0:
        print("No. of Apple:",Apple_no, "pcs. : ", Apple_no*Apple_Price," THB")
    if Banana_no > 0:
        print("No. of Banana:",Banana_no, "pcs. : ", Banana_no *Banana_Price," THB")
    if Pineapple_no > 0:
        print("No. of Pineapple:", Pineapple_no, "pcs. : ", Pineapple_no * Pineapple_Price, " THB")
    if Grape_no > 0:
        print("No. of Grape:", Grape_no, "pcs. : ", Grape_no * Grape_Price, " THB")
    print("Total Price: ", Apple_no*Apple_Price + Banana_no*Banana_Price + Pineapple_no * Pineapple_Price +Grape_no * Grape_Price," THB")
else: print("Either username or password is error!")
