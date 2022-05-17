import re
import random

class chatbot:
    
    def Quantity(self, qlist):
        self.q = qlist
        print("Select quantity: ")
        for i in self.q:
            print(i, end=" ")
        choice = input("\nHow much would you like to order\n")
        r = re.compile(choice)
        finalflavour = list(filter(r.match, self.q))
        if finalflavour == []:
            print("Please select a proper quantity\n")
            return self.Quantity()
        return finalflavour[0]
    
    def cakeflavour(self, flavlist):
        self.flavour = flavlist
        print("Today's available flavours are: ")
        for i in self.flavour:
            print(i, end=", ")
        choice = input("Which flavour would you like?\n")
        r = re.compile(choice)
        finalflavour = list(filter(r.match, self.flavour))
        if finalflavour == []:
            print("We are sorry that flavour is unavailable today\n")
            return self.cakeflavour()
        return finalflavour[0]
        
    
    def question(self):
        name = input("Hi, I am Cakebot. What is your name?\n")
        print("\tWe have been in the premier spot for custom cakes, cookies, cupcakes and many more\n")
        product = int(input("That said what would you like to do?\n1.Check existing order\n2.Place a new order\n"))
        if (product == 1):
            orderid = int(input("Enter order Id: "))
            if (orderid%2 == 0 and orderid<500):
                print("Your order no: " , orderid, "has been dispatched")
            else:
                print("Your order no: " , orderid, "is being prepared")
        else:
            prod = input("\nWhat would you like to order?\n")
            cake = re.search(".*cake*", prod)
            cookie = re.search(".*cookie*", prod)
            cupcake = re.search(".*cupcake*", prod)
            pie = re.search(".*pie*", prod)
            if (cake):
                fla = self.cakeflavour(["Strawberry and cream", "Dark Chocolate Champagne", "Red Devil", "Bubble Gum", "Tiramisu"])
                qua = self.Quantity(["0.5kg", "1kg", "2kg", "3kg"])
                print("\nYour order of ", qua, fla , " cake is confirmed\n")
                print("Please pay $", random.randint(250, 800))
            if (cupcake):
                fla = self.cakeflavour(["Strawberry and cream", "Dark Chocolate Champagne", "Red Devil", "Bubble Gum", "Tiramisu"])
                qua = self.Quantity(["1nos", "2nos", "6nos", "12nos"])
                print("\nYour order of ", qua, fla , " cupcake is confirmed")
                print("Please pay $", random.randint(80, 800))
            if (cookie):
                fla = self.cakeflavour(["Chocolate Chip", "Oatmeal Raisin", "Gingersnap", "Biscotti", "Peanutbutter"])
                qua = self.Quantity(["1nos", "2nos", "6nos", "12nos"])
                print("\nYour order of ", qua, fla , " cookie is confirmed")
                print("Please pay $", random.randint(80, 400))
            if (pie):
                fla = self.cakeflavour(["Apple Pie", "Pecan Pie", "Cherry Pie", "Pumpkin Pie", "Lemon Meringue Pie", "Shepherd's Pie"])
                qua = self.Quantity(["1piece", "2pieces", "3pieces", "Full pie"])
                print("\nYour order of ", qua, fla , " pie is confirmed")
                print("Please pay $", random.randint(300, 2000))
            print("\nThank you for ordering.\nYour order Id is: OI -", random.randint(488148,848418))
            
c = chatbot()
c.question()
                
