'''
Josh S
Savings Goal
Create a script that determines how many months it will take to save a
specific amount of money given a specific interest rate.

Input
Ask the user for their savings goal amount, the monthly deposit amount,
and the annual interest rate (as a whole number).

Output
Print out the user's balance for each month until they have met or exceeded their savings goal.
Finally, print out how many months it will take to reach the goal.

Hints
Each month, the accrued interest should be calculated before the monthly deposit is made.

Because the interest rate entered by the user is annual, not monthly,
and a whole number, it must be divided by 1200 (12 months * 100 percent).
'''

savingsGoal = float(input("Savings Goal: $"))
monthlyDeposit = float(input("Monthly Deposit: $"))
interestRate = float(input("Annual Interest Rate: ")) / 1200
intrest = 0
months = 1
total = monthlyDeposit
rate = interestRate
while total <= savingsGoal:
    print(f"Month {months}: You have saved ${round(total, 2)}")
    intrest = float(total * rate)
    total += intrest + monthlyDeposit
    months += 1
print(f"Month {months}: You have saved ${round(total, 2)}")
print(f"It will take {months} month(s) to save ${savingsGoal}")
