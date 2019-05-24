#Mehul Vikas Joshi
#House Hunting
#given the total cost of a new house
#portion_down_payment
#current_savings
#annual return r
#annual salary
#portion_saved
#find the total months it will take to save up enough money for a down payment


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
current_savings = 0.0
monthly_saved = (annual_salary/12) * portion_saved
down_payment = total_cost * 0.25
months = 0


while current_savings < down_payment:
	increase = current_savings * 0.04/12.0
	current_savings += current_savings * 0.04/12.0 + monthly_saved
	months = months + 1
	
print("Number of months:",months) 
	
