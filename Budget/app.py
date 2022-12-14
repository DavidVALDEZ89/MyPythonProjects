class Category:
    
    def __init__(self,name):
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}\n"  #[0:23] returns up to 23 characters, :23 fills up with spaces if there are no characters
            total += item['amount']
        
        receipt = title + items + "Total: " + str(total) + "\n"
        return receipt
    
    def deposit (self,amount,description=""):
        """A deposit method that accepts an amount and description. 
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list in the form of 
        {"amount": amount, "description": description}.
        
        """
        self.ledger.append({"amount": amount, "description": description})  #Sends the information into the list
        
    
    def withdraw (self, amount, description=""):
        """A withdraw method that is similar to the deposit method, 
        but the amount passed in should be stored in the ledger as a negative number. 
        If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise.
        """
        if self.check_funds(amount):  #This part checks if we have enough founds in the budget
            self.ledger.append({"amount": -amount, "description": description})  # Sends the information into the list
            return True
        return False
    
    def get_balance (self):
        """A get_balance method that returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred.
        """
        balance = 0
        for i in self.ledger:
            balance += i["amount"]  #sums up the items
        return balance
    
    def transfer(self,amount,category):
        """A transfer method that accepts an amount and another budget category as arguments. 
        The method should add a withdrawal with the amount and the description "Transfer to 
        [Destination Budget Category]". The method should then add a deposit to the other 
        budget category with the amount and the description "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. 
        This method should return True if the transfer took place, and False otherwise.
        """
        if self.check_funds(amount):  #This part checks if we have enough founds in the budget
            self.withdraw(amount,"Transfers to "+ category.name)  #takes foney from the given category
            category.deposit(amount,"Transfers from"+self.name)
            return True
        return False
    
    def check_funds(self, amount):
        """A check_funds method that accepts an amount as an argument. 
        It returns False if the amount is greater than the balance of the budget category 
        and returns True otherwise. This method should be used by both the withdraw method 
        and transfer method.
        """
        if self.get_balance() >= amount:
            return True
        return False
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
