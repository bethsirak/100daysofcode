Bill_amount = float(input("What was the total bill amount? "))

tip_percentage= float(input("What percentage tip would you like to give? 10, 12 or 15? "))

number_of_people= float(input("How many people to split the bill? "))

total_bill_amount = (Bill_amount*(tip_percentage/100)) + Bill_amount

total_bill_amount_pp = total_bill_amount/number_of_people

final_amount = round(total_bill_amount_pp, 2)

final_amount = "{:.2f}".format(total_bill_amount_pp)

print(f"Each person should pay: ${final_amount}")