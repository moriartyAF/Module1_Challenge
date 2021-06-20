import csv
from pathlib import Path, WindowsPath

# Part 1: Automate the Calculations.
print()
print("Part 1: Automate the Calculations")
loan_costs = [500, 600, 200, 1000, 450]

loan_count = len(loan_costs)
print("The number of loans in the portfolio = ",loan_count)

total_loan_amount = sum(loan_costs)
print("The total loan amount of the portfolio = $ ",total_loan_amount)

avg_loan_amount = float(total_loan_amount) / float(loan_count)
avg_loan_amount_rounded = round(avg_loan_amount,2)
print("The average loan amount within the portfolio = $ ",avg_loan_amount_rounded)
print()

# Part 2: Analyze Loan Data.
print("Part 2: Analyze Loan Data")
loan = {"loan_price": 500,"remaining_months": 9,"repayment_interval": "bullet","future_value": 1000}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print("The future value of this loan = $ ",future_value)
print("The number of months remaining on this loan = ",remaining_months)

discount_rate = .2
present_value = float(future_value) / (1 + float(discount_rate)/12)**float(remaining_months)
present_value_rounded = round(present_value,2)
print("The discount rate applied to the loan valuation = ",discount_rate)
print("The present value of this loan = $ ",present_value_rounded," (rounded to two decimal places)")

loan_price = loan.get("loan_price")
net_loan_value = present_value_rounded - loan_price
if present_value > loan_price:
    print("This loan is worth buying. The present value of the loan exceeds the price of the loan by $ ",net_loan_value)
elif present_value < loan_price:
    print("This loan is not worth buying. The price of the loan exceeds the present value of the loan by $ ",net_loan_value)
else:
    print("The purchase of this loan is a judgment call, as the present value of the loan and the price of the loan are equal.")    
print()

# Part 3: Perform Financial Calculations.
print("Part 3: Perform Financial Calculations")
new_loan = {"loan_price": 800,"remaining_months": 12,"repayment_interval": "bullet","future_value": 1000}

def PV_Calculator(future_value,remaining_months,annual_discount_rate):
    present_value_raw = float(future_value) / (1 + float(annual_discount_rate)/12)**float(remaining_months)
    present_value = round(present_value_raw,2)
    return present_value

discount_rate = .2
new_loan_present_value = PV_Calculator(new_loan["future_value"],new_loan["remaining_months"],discount_rate)
print("The present value for this new loan is $ ",new_loan_present_value," (rounded to two decimal places)")
print()

# Part 4: Conditionally filter lists of loans.
print("Part 4: Conditionally filter lists of loans")
loans = [   {"loan_price": 700,"remaining_months": 9,"repayment_interval": "monthly","future_value": 1000},
            {"loan_price": 500,"remaining_months": 13,"repayment_interval": "bullet","future_value": 1000},
            {"loan_price": 200,"remaining_months": 16,"repayment_interval": "bullet","future_value": 1000},
            {"loan_price": 900,"remaining_months": 16,"repayment_interval": "bullet","future_value": 1000}  ]

loanheader = ["loan_price","remaining_months","repayment_interval","future_value"]

inexpensive_loans = []

for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)
print()

# Part 5: Save the results.
print("Part 5: Save the results")
csvpath = Path("inexpensive_loans.csv")

with open(csvpath,'w') as csvfile:
    csvwrite = csv.writer(csvfile,delimiter=',')

    csvwrite.writerow(loanheader)

    for row in inexpensive_loans:
        csvwrite.writerow(row.values())
print("New CSV file name = ",csvpath)
print("New CSV file absolute path = ",csvpath.absolute())



