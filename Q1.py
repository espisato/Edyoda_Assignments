"""
In the pre-smartphone era,each number key is assigned a subset of the alphabet {a,b,…,z}.
#- 2 is assigned {a,b,c}
#- 3 is assigned {d,e,f}
#- 4 is assigned {g,h,i}
#- 5 is assigned {j,k,l}
#- 6 is assigned {m,n,o}
#- 7 is assigned {p,q,r,s}
#- 8 is assigned {t,u,v}
#- 9 is assigned {w,x,y,z}

Write a function numbers_to_chars() to find the characters generated using key 9999335533. Output should be "zeke"
Function Name : numbers_to_chars() Input : Integer number sequence Output : Str
"""

subsets = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

def numbers_to_chars(number_sequence):
	output = ""
	temp_list = [['', 0]]
	digits = list(str(number_sequence))
	for digit in digits:
		# to prevent the use of 0s and 1s
		if digit == '0' or digit == '1':
			return "0s and 1s not allowed"
		if digit == temp_list[-1][0]:	# if already exists in temp_list add a count
			frequency += 1
			temp_list[-1][1] = frequency
		else:				# if doesn't exist in temp_list add the character and count 1
			frequency = 1
			temp_list.append([digit, frequency])
	
	# function to check simultaneous repitition of characters more than the key index limits
	def repetitions(digit, frequency):
		temp_var = ""
		if digit in "79":
			limit = 4
		else:
			limit = 3
		while frequency > limit:
			temp_var += subsets[digit][limit - 1] 
			frequency = frequency - limit
			repetitions(digit, frequency)
		else:
			temp_var += subsets[digit][frequency - 1]
		return temp_var

	for temp in temp_list[1:]:
		output += repetitions(*temp)	
	
	return output


print("\n##### Pre-Smartphone keys #####") 
print("Output generated:", numbers_to_chars(int(input("Enter your number sequence: "))))


print("\n########################################################################################################\n")


