class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8

customer1.addCart()

customer2 = Customer()
customer2.name = "James"
customer2.lastName = "Anthony"
customer2.age = 30
customer2.addCart()

customer3 = Customer()
customer3.name = "Namiki"
customer3.lastName = "Harumichi"
customer3.age = 25
customer3.addCart()

customer4 = Customer()
customer4.name = "Yae"
customer4.lastName = "Noguchi"
customer4.age = 19
customer4.addCart()
