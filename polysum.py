import math #Math module contains mathematical functions
def polysum(n,s):
	'''
	Input: 'n' is the number of sides of a polygon with side length 's'
	Returns the  sum the area and square of the perimeter of the regular polygon rounded to 4 decimal places
	'''
    area=(0.25*n*s*s)/(math.tan(math.pi/n))
    perimeter=n*s
    res=area+(perimeter*perimeter)
    res=round(res,4)
    return res
print(polysum(5,3))