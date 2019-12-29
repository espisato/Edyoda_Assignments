"""
Write a program to convert Integer to Roman String. For example, if a given integer is 5 then your program should print "V".
Function Name : int_roman Input : int Output : str
"""      

def int_roman(number):
	denominations = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	roman_literals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

	result = ""
		
	"""
	In roman number system, numbers more than 4000 are denoted by a bar on the top of
	the roman conversion of the digit. For eg: 4000 will have a bar on digit '4'.
	For this program I have used the format "^roman^" instead of bar. So 45893 will be
	represented as ^XLV^DCCCXCIII.
	"""

	if number >= 4000:
		result += f"^{int_roman(number // 1000)}^{int_roman(number % 1000)}"
	else:
		for denom, roman in list(zip(denominations, roman_literals)):		
			multiplier = number // denom
			if multiplier:
				result += roman * multiplier
				number = number % denom		
	
	return result


#print("\n##### Integer to Roman Numbers #####")
#print(int_roman(int(input("Enter number: "))))

#print("\n########################################################################################################\n")



