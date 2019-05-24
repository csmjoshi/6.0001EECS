#Finding the right amount to save away
#Mehul Vikas Joshi
#Write a program to find the best savings rate to achieve a down payment on a $1M house
#in 36 months

#This is an optimization problem and I think that it will be best solved with binary search
#For the sake of simplicity assume the following as always true


sar = 0.07
ar = 0.04
dp = 250000.00
ss = float(input("Enter the starting salary: "))
ms = ss/12.0
steps = 0

high=10000
low=0
percent=(high+low)/200
elipson = 0.01
#print(ms)
def findN(ms):
	n=0
	for m in range(0, 37):
		if m % 6==0 and m > 0:
			ms=ms+ms*0.07
		n+=n*0.04/12.0 + ms
	#print(n)
	return n
					
val = findN(ms)
if val == dp:
	print("Best savings rate:", 1.000)
elif val > dp:
	#run the bisection search
	#print(percent)
	while abs(val - dp) >= 0.0001:
		#print(high, low, percent)
		steps+=1
		if val < dp:
			low = percent*100
		else:
			high = percent*100
		percent= (low+high)/200
		val = findN(ms*percent)

	print("Best savings rate:", round(percent, 4))
	print("Steps in bisection search:", steps)
else:
	print("It is not possible to pay the down payment in three years")
