from unittest import main

class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []
    def __str__(self):
        title = self.name.center(30, "*")
        entryString = "\n"
        for entry in self.ledger:
            entryString += '{:<23.23} {:>6.7}'.format(entry['description'], "{:.2f}".format(entry['amount'])) + "\n"
        totalString = "Total: " + str(self.get_balance())
        return title + entryString + totalString

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount":abs(amount), "description":description})
    
    def withdraw(self, amount, description =""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-abs(amount), "description":description})
            return True
        else:
            return False
    
    def get_withdrawal(self):
        totalWithdrawal = 0
        for entry in self.ledger:
            if entry['amount'] < 0:
                totalWithdrawal += entry['amount']
        return totalWithdrawal

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def check_funds(self, amount):
        if self.get_balance() - abs(amount) >= 0:
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+str(category.name))
            category.deposit(amount, "Transfer from "+self.name)
            return True
        else:
            return False

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    chart = ""
    total_expenses = 0
    for entry in categories:
        total_expenses += entry.get_withdrawal()
    categoriesList = []
    normalizedCategory = []
    for entry in categories:
        categoriesList.append(entry.name)
    longestCategory = max(categoriesList, key=len)
    for i in range(4):
        normalizedCategory.append(" "*len(longestCategory))
    for entry in categoriesList:
        normalizedCategory.append(" "*len(longestCategory))
        normalizedCategory.append(entry + " "* (len(longestCategory) - len(entry)))
        normalizedCategory.append(" "*len(longestCategory))
    for tenthPercentage in range(10, -1, -1):
        chart += '{:>3}'.format(str(tenthPercentage*10)) + "|"
        for entry in categories:
            if within_Percentage(entry, tenthPercentage, total_expenses):
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    lines = " "*4 + (len(categories) * 3 + 1) * ("-") + "\n"
    verticalNames = vertical_set(normalizedCategory, len(longestCategory))

    return title + chart + lines + verticalNames

def within_Percentage(self, number, total):
    percentage = abs(self.get_withdrawal()/total)
    if number <= percentage *10:
        return True
    return False

def vertical_set(categories, size):
    nameString = ""
    for x in range(size):
        for y in categories:
            nameString += y[x]
        nameString += " "
        if x < 12:
            nameString += "\n"
    return nameString

food = Category("Food")
business = Category("Business")
entertainment = Category("Entertainment")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business,food, entertainment])