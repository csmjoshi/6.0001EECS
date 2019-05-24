#Mehul Vikas Joshi
#House Hunting


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annualRaise = float(input("Enter the semi-annual raise, as a decimal: "))
current_savings = 0.0
monthly_saved = (annual_salary/12) * portion_saved
down_payment = total_cost * 0.25
months = 0


while current_savings < down_payment:
	if months % 6 == 0 and months > 0:
		monthly_saved = monthly_saved + monthly_saved * semi_annualRaise

	current_savings += current_savings * 0.04/12.0 + monthly_saved
	months = months + 1
	
print("Number of months:", months) 
	
