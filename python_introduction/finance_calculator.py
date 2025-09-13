# This program calculates monthly savings and projects annual savings with interest
#Input monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
#monthly savings calculation
monthly_savings = monthly_income - total_monthly_expenses
# Projected annual savings with 5% interest
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
#Display the results
print("Your monthly savings are:", monthly_savings)
print("Your projected  savings after one year , with interest, is:", projected_annual_savings)