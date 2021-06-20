# MODULE 1 CHALLENGE, created by Tim Moriarty 6/20/2021

# import CSV library, and Path function from pathlib library
import csv
from pathlib import Path


# print blank row and title row
print()
print("Part 1: Automate the Calculations")

# define loan cost list
loan_costs = [500, 600, 200, 1000, 450]

# count number of loans
loan_count = len(loan_costs)
print("The number of loans in the portfolio = ",loan_count)

# get loan total
total_loan_amount = sum(loan_costs)
print("The total loan amount of the portfolio = $ ",total_loan_amount)

# calculate average loan amount, and then round to two decimal places
avg_loan_amount = float(total_loan_amount) / float(loan_count)
avg_loan_amount_rounded = round(avg_loan_amount,2)
print("The average loan amount within the portfolio = $ ",avg_loan_amount_rounded)


# print blank row and title row
print()
print("Part 2: Analyze Loan Data")

# define loan dictionary
loan = {"loan_price": 500,"remaining_months": 9,"repayment_interval": "bullet","future_value": 1000}

# extract future value and remaining months values
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print("The future value of this loan = $ ",future_value)
print("The number of months remaining on this loan = ",remaining_months)

# set discount rate
discount_rate = .2

# calculate present value, and then round to two decimal places
present_value = float(future_value) / (1 + float(discount_rate)/12)**float(remaining_months)
present_value_rounded = round(present_value,2)
print("The discount rate applied to the loan valuation = ",discount_rate)
print("The present value of this loan = $ ",present_value_rounded," (rounded to two decimal places)")

# extract loan price
loan_price = loan.get("loan_price")

# calculate net loan value
net_loan_value = present_value_rounded - loan_price

# assess present value vs. price of loan to determine buy/no buy decision
if present_value > loan_price:
    print("This loan is worth buying. The present value of the loan exceeds the price of the loan by $ ",net_loan_value)
elif present_value < loan_price:
    print("This loan is not worth buying. The price of the loan exceeds the present value of the loan by $ ",net_loan_value)
else:
    print("The purchase of this loan is a judgment call, as the present value of the loan and the price of the loan are equal.")    


# print blank row and title row
print()
print("Part 3: Perform Financial Calculations")

# define loan dictionary
new_loan = {"loan_price": 800,"remaining_months": 12,"repayment_interval": "bullet","future_value": 1000}

# define a function "PV_Calculator", which takes in the future value of loan, remaining months of loan, and 
# an annual discount rate, and produces a present value based upon the monthly version of the present value formula, and 
# rounds the present value to two decimal places
def PV_Calculator(future_value,remaining_months,annual_discount_rate):
    present_value_raw = float(future_value) / (1 + float(annual_discount_rate)/12)**float(remaining_months)
    present_value = round(present_value_raw,2)
    return present_value

# establish the annual discount rate
discount_rate = .2

# call the "PV_Calculator" function, providing the function inputs "future_value" (from the loan dictionary),
# "remaining_months" (from the loan dictionary), and the "discount_rate" variable created immediately above
new_loan_present_value = PV_Calculator(new_loan["future_value"],new_loan["remaining_months"],discount_rate)
print("The present value for this new loan is $ ",new_loan_present_value," (rounded to two decimal places)")


# print blank row and title row
print()
print("Part 4: Conditionally filter lists of loans")

# define loan dictionary
loans = [   {"loan_price": 700,"remaining_months": 9,"repayment_interval": "monthly","future_value": 1000},
            {"loan_price": 500,"remaining_months": 13,"repayment_interval": "bullet","future_value": 1000},
            {"loan_price": 200,"remaining_months": 16,"repayment_interval": "bullet","future_value": 1000},
            {"loan_price": 900,"remaining_months": 16,"repayment_interval": "bullet","future_value": 1000}  ]

# establish the CSV header
loanheader = ["loan_price","remaining_months","repayment_interval","future_value"]

# create an empty new list to hold filtered list of loans from loan dictionary
inexpensive_loans = []

# conditionally filter each loan in loan dictionary to find loans with a "loan_price" less than or equal to $500,
# and copy entire row of information for these eligible loans from loan dictionary into the "inexpensive_loans" list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
print(inexpensive_loans)


# print blank row and title row
print()
print("Part 5: Save the results")

# set variable for CSV file location using Path function
csvpath = Path("inexpensive_loans.csv")

# use open function in conjunction with path variable, indicating that we're writing to a CSV file
with open(csvpath,'w') as csvfile:
    
    # create object to hold Python list of data converted to CSV file data, in comma-delimited format
    csvwrite = csv.writer(csvfile,delimiter=',')

    # write CSV file headers ("loanheader") as first row of file
    csvwrite.writerow(loanheader)

    # for each row in the "inexpensive loans" list, write the row values into the CSV file
    for row in inexpensive_loans:
        csvwrite.writerow(row.values())
        
# show file name and entire absolute path of new CSV file        
print("New CSV file name = ",csvpath)
print("New CSV file absolute path = ",csvpath.absolute())
