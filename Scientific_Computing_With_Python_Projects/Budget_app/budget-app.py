class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    # returns balance of category based on deposits and withdrawals
    def get_balance(self):
        prices = []
        for i in self.ledger:
            prices.append(i["amount"])
        balance_total = sum(prices)
        return balance_total
    
    # This must be used by withdraw and transfer.
    # Accepts an amount as an argument
    # Returns False if amount less than balance of budget and True otherwise
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False
    
    # Add an amount and description to the category:
    def deposit(self, amount, description = ""):
        deposit_dict = {"amount": amount, "description": description}
        self.ledger.append(deposit_dict)
    
    # have to add a dictionary ONLY if there are enough funds
    # if no funds, return False. If funds, do the operation and return True:
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            withdraw_dict = {"amount": -amount, "description": description}
            self.ledger.append(withdraw_dict)
            return True
        else:
            return False

    # put an amount and name of another budget.
    # add a withdrawal with amount and the description "Transfer to [Destination Budget Category]"
    # add a deposit with amount and description "Transfer from [Source Budget Category]"
    # IF no funds, cancel previous 2 steps. return True if transfer Ok, if not, returns False
    # 5
    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, description = "Transfer to " + destination.name)
            destination.deposit(amount, description = "Transfer from " + self.name)
            return True
        else:
            return False
    
    # To be printed:
    def __str__(self):
        # title with 30 characters and name centered, filled with "*":
        table = self.name.center(30,"*") + "\n"
        for i in self.ledger:
            table += f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
        table += f"Total: {format(self.get_balance(),'.2f')}"
        return table

def create_spend_chart(categories):
    names = []
    spent = []
    percent_spent = []
    sum_spent = 0
    
    for i in categories:
        # Get names from each category in a list:
        names.append(i.name)
        # Get total withdraw values from each category in a list:
        spent_parcial = 0
        for j in i.ledger:
            if j["amount"] < 0:
                spent_parcial -= j["amount"]
        spent.append(round(spent_parcial,2))
        
    # Get spent in total:
    sum_spent = sum(spent)
        
    # Get percentages spent in a list, by categories:
    for i in spent:
        # Rounded to 2 decimals in percent:
        percent_spent.append(round(i / sum_spent, 2) * 100)
        
    
    # Now we can go to create the bar chart:
    bar_chart = "Percentage spent by category\n"
    # Create a counter to have from 100 to 0:
    counter = 100
    # With this we have the layout of the bar:
    while counter >= 0:
        # Added align to right with width 4 to adjust the percentages:
        bar_chart += str(counter).rjust(3) + "| "
        
        # If the percentage is greater or equal than the counter, add a bar:
        for i in percent_spent:
            if i >= counter:
                bar_chart += "o  "
            # If the percentage is lesser than the counter, add only spaces:
            else:
                bar_chart += "   "    
        # Substract then 10 to the counter to keep writing the bar:
        counter -= 10
        # And start the next iteration of the loop in a new line:
        bar_chart += "\n"
            
    # Add necessary spaces in the horizontal line, and depending on the number of
    # categories, enlarge the line. Also we add a newline and the respective spaces
    # to align correctly the posterior names:
    bar_chart += "    ----" + ("---" * (len(percent_spent) - 1)) + "\n" + "     "
    
    # Check the number of letters of the longest category name:
    longest_name = 0
    for i in names:
        if len(i) > longest_name:
            longest_name = len(i)
            
    # Loop through each letter of each category in one line:
    for i in range(longest_name):
        for j in names:
            if len(j) > i:
                bar_chart += j[i] + "  "
            else:
                bar_chart += "   "
        if i < longest_name - 1:
            bar_chart += "\n     "
    # Return the string containing the bar chart
    return bar_chart
