def find_factors(number):
	factor = []
	for i in range(1, number, 1):
		if (number % i )== 0:
			factor.append(i)
	return factor


def perfect_number(number):
	a = sum(find_factors(number))
	if a== number:
		print("This is a perfect number")
	else:
		print("This is not a perfect number")

a = int(input("Enter the number you want to check"))
perfect_number(a)