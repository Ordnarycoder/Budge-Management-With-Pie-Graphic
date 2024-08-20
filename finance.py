import matplotlib.pyplot as plt
import numpy as np

class BudgetManagement:
    def __init__(self, income_amount, expense_amount):
        self.income_amount = income_amount
        self.expense_amount = expense_amount
        self.total_budget = self.income_amount - self.expense_amount

    def add_income(self):
        extra_income_type = input("What is income type: ")
        extra_income_value = float(input("Income amount: "))
        self.income_amount += extra_income_value
        print(f"Extra income type: {extra_income_type}\nExtra income value: {extra_income_value}\nTotal Income Value: {self.income_amount}")

    def add_expense(self):
        extra_expense_type = input("What is expense type: ")
        extra_expense_value = float(input("Expense amount: "))
        self.expense_amount += extra_expense_value
        print(f"Extra expense type: {extra_expense_type}\nExtra expense value: {extra_expense_value}\nTotal Expense Value: {self.expense_amount}")

    def profit_loss_analysis(self):
        self.total_budget = self.income_amount - self.expense_amount
        if self.total_budget > 0:
            print(f"Your profit amount: {self.total_budget}")
        elif self.total_budget < 0:
            print(f"Your loss amount: {abs(self.total_budget)}")
        else:
            print("You are breaking even.")

    def create_pie_graphics(self):
        plt.style.use('_mpl-gallery-nogrid')

        x = [self.income_amount, self.expense_amount]
        labels = ["Income", "Expense"]
        colors = ['green', 'red']

        plt.pie(x, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title("Income vs Expense Distribution")
        plt.show()

new = BudgetManagement(income_amount=1000, expense_amount=500)
new.create_pie_graphics()
