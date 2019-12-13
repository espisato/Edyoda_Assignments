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

def numbers_to_chars(number_sequence):
	subsets = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

	output = ""
	temp_list = [['', 0]]
	digits = list(str(number_sequence))
	for digit in digits:
		# to prevent the use of 0s and 1s
		if digit == '0' or digit == '1':
			return "0s and 1s not allowed"
		if digit == temp_list[-1][0]:	# if already exists in temp_list, add a count
			frequency += 1
			temp_list[-1][1] = frequency
		else:				# if doesn't exist in temp_list, add the character and count 1
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


#print("\n##### Pre-Smartphone keys #####") 
#print("Output generated:", numbers_to_chars(int(input("Enter your number sequence: "))))


#print("\n########################################################################################################\n")


"""
Given a dict of tickets("to":"from")
{"Chennai":"Bangalore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"} find out the sequence of travel.
Expected Output : Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Bangalore
Function Name : travel_sequence Input : dict Output : dict
"""

def travel_sequence(d):
	sequence = {}	

	# searching for starting city
	for key, value in d.items():
		if key not in d.values():
			sequence[key] = value
			temp = value

	# getting items and arranging in sequence
	while temp:
		if d.get(temp):      # check for a None value
			sequence.setdefault(temp, d.get(temp))
		temp = d.get(temp)

	return(sequence)


#print("\n##### Travel Sequence #####")
#tickets = {"Chennai":"Bangalore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}
#print("Tickets: {} \n Travel sequence: {}".format(tickets, travel_sequence(tickets)))


#print("\n########################################################################################################\n")
"""
Given a dictionary that associates the names of states with a list of the names of cities that appear in it,write a program that creates a new dictionary that associates the name of a city with the list of states that it appears in.
As an example, if the first dictionary is
Input : states = {'New Hampshire': ['Concord', 'Hanover'],
'Massachusetts': ['Boston', 'Concord', 'Springfield'],
'Illinois': ['Chicago', 'Springfield', 'Peoria'] }
Output:
cities = {'Hanover': ['New Hampshire'],
'Chicago': ['Illinois'],'Boston': ['Massachusetts'],
'Peoria': ['Illinois'],'Concord': ['New Hampshire','Massachusetts'],
'Springfield': ['Massachusetts', 'Illinois']}
Function Name : city_with_states Input : dict Output : dict
"""

#states = {'New Hampshire': ['Concord', 'Hanover'],'Massachusetts': ['Boston', 'Concord', 'Springfield'],'Illinois': ['Chicago', 'Springfield', 'Peoria']}

def city_with_states(d):
	cities = {}
	for key in d:
		val = d[key]
		# traversing through the list values referenced by a single state
		for city in val:
			# if city does not exist in cities, add to it (city: state)
			if city not in cities:
				cities[city] = [key]
			# if city already exists in cities, append the value (state) 
			else:
				cities[city].append(key)
	return cities

#print("\n##### Cities associated with states #####")
#print(city_with_states(states))


#print("\n########################################################################################################\n")


"""
How do you check if a given String contains valid brackets? Given a string containing just the characters '(', ')', '{', '}', '[' and ']', write a program in python to check if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Function Name : check_parentheses Input : str Output : True/False
"""

def check_parentheses(string):
    opening_brackets = '({['
    closing_brackets = ')}]'
    mapping = dict(zip(opening_brackets, closing_brackets))
    temp = []

    for char in string:
        if char in opening_brackets:
            temp.append(mapping[char])
        elif char in closing_brackets:
            if not temp or char != temp.pop():
                return False
    return not temp


#print("\n##### Bracket pairing #####")

#strings = ["({[]})", "{}])(", "{}[]()", "(][}{)", "[(([{}]{()}))]"]
#for string in strings:
#	print(f"Input: {string} \n Output:", check_parentheses(string))


#print("\n########################################################################################################\n")



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



"""
Write a program utility that counts the number of lines of actual python code in a. For the purpose of this exercise, a line is counted if it contains something other than whitespace or text in a comment.
remember that comment start sequences that appear inside python strings should be ignored.
Function Name : count_code_lines Input : str Output : int
"""

#input_code = """
#Linear search implementation
#Takes list and a key as input and returns True or False as answer
#def linear_saerch(l,key):
#    for value in l:
#        if key == value:
#            return True #Return True is key exist
#    else:
#        return False #Return False if key does not exist
#
#l = [100,200,300,400,500,600]
#key = 500
#result = linear_search(l,key)
#print(result)
#"""

def count_code_lines(string):
	count = 0
	for line in string.splitlines():
		chars = [char for char in line]
		# to check if a line is commented or is empty
		if chars and chars[0] != '#' and chars != []:
			count += 1
	return count

#print("\n##### Counting code lines #####")
#print("No of lines of code:", count_code_lines(input_code))
#
#
#print("\n########################################################################################################\n")


"""
Write a program to check the strength of a supplied password
The length of the password must be at least 8 characters in length The password must contain at least 1 capital letter The password must contain at least 1 digit The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)
We need to provide feedback to the user about the strength of their password
Provide the user with a list of reasons why their password is 'weak'
Function Name : check_password_strength Input : str Output : tuple (str,list) eg ("Weak",["The password must contain at least 1 capital letter"])
"""

def check_password_strength(string):
	reasons = []

	# check length of string
	if len(string) < 8:
		reasons.append("The password must be of at least 8 characters.")

	# check if all the characters are digits
	if string.isdigit():
		reasons.append("The password must contain at least 1 alphabet.")

	#check if the first character is iin upper case
	if string.islower():
		reasons.append("The password must contain at least 1 uppercase character.") 
	
	# check if string contains at least one digit
	def check_digit():
		for char in string:
			if char.isdigit():
				return True
	if not check_digit():
		reasons.append("The password must contain at least 1 digit.")
			
	
	# check for special characters
	def check_special_characters():
		for char in string:
			if char in "!@#$&":
				return True
	if string.isalnum():
		reasons.append("The password must contain at least 1 special character.")
	elif not check_special_characters():
		reasons.append("Only special characters allowed are '!', '@', '#', '$' and '&'.")

	if reasons:
		return ("Weak", reasons)
	else:
		return ("Strong", ["You have successfully created a strong password!."]) 



#print("\n##### Password Validation #####")

#results = check_password_strength(input("Enter your password: "))
#print(results[0])
#for result in results[1]:
#	print(result)


#print("\n########################################################################################################\n")


"""
Check if given sentence is syntactically correct or not
A simple sentence if syntactically correct if it fulfills given rules. The following are given rules.

Sentence must start with an Uppercase character (e.g. Noun/ I/ We/ He etc.)
There must be spaces between words.
Then the sentence must end with a full stop(.).
Two continuous spaces are not allowed.
Two continuous uppercase characters are not allowed.
However the sentence can end after an uppercase character.
Function Name : check_sentence Input : str Output : tuple (True/False,list) eg (False,["There must be spaces between words."])
"""

def check_sentence(string):
	reasons = []
	words = string.split(' ')

	# check first chaacter is in Capital
	if not [char for char in string][0].isupper():
		reasons.append("Sentence must start with an Uppercase character.")

	# check for spaces in the sentence
	if ' ' not in string:
		reasons.append("Spaces must be present between words in a sentence.")
	
	# check full-stop at the end of the sentence
	if '.' != string[-1]:
		reasons.append("Sentence must end with a full-stop.")
	
	# check for continuous spaces
	if '' in string.split(' ')[1:-1]:
		reasons.append("Continuous spaces are not allowed.")
	
	# check for continuous uppercase characters allowing an uppercase character at end
	for i in range(len(string) - 3):
		if string[i].isupper() and string[i+1].isupper():
			reasons.append("Continuous uppercase characters are not allowed.")
			break
	
	if reasons:
		return (False, reasons)
	else:
		return (True, ["Your sentence is syntactically correct!"])

#print("\n##### Sentence Validation #####")
#
#results = check_sentence(input("Type your sentence: ")) 
#if results[0]:
#	print(results[1][0])
#else:
#	for result in results[1]:
#		print(result)


#print("\n########################################################################################################\n")


"""
Given an array arr[] of integers and an integer K, the task is to find the greatest contiguous sub-array of size K.
Sub-array X is said to be greater than sub-array Y if the first non-matching element in both the sub-arrays has a greater value in X than in Y.
For example : Input: arr[] = {1, 4, 3, 2, 5}, K = 4 Output: 4 3 2 5 Two subarrays are {1, 4, 3, 2} and {4, 3, 2, 5}. First non-matching element from array1 and array 2 : 1 and 4 as 4 is greater Hence, the greater one is {4, 3, 2, 5}
Function Name : greatest_sub_array() Input : list Output : list
"""


def greatest_sub_array(array):
	k = int(input("Enter the size of sub-array: "))
	subarrays = []	

	# sub-dividing array into sub-arrays of length k 
	for i in range(len(array)):
		if len(array) - i >= k:
			subarrays.append(array[i : i + k])

	temp = [0]
	for subarray in subarrays:
		index = 0
		# if first index value is equal in both subarrays, increment index to 1
		if temp[index] == subarray[index]:
			index += 1
		if subarray[index] > temp[index]:
			temp = subarray

	return temp

#print("\n##### Greatest Sub Array #####")
#
#array1 = [1, 4, 3, 5, 2, 6, 6]
#print("Array1: ", array1, "\nGSA: ", greatest_sub_array(array1))
#array2 = [1, 5, 3, 3, 4, 5, 3, 6, 5, 7]
#print("Array1: ", array2, "\nGSA: ", greatest_sub_array(array2))
	

#print("\n########################################################################################################\n")


"""
Given a list of N integers. The task is to eliminate the minimum number of elements such that in the resulting list the sum of any two adjacent values is even.
Numbers = [1, 3, 5, 4, 2] Output = [1, 3, 5] Total elements removed 2 Elements to be removed [4,2]
Function Name : adj_sum_even() Input : list Output : tuple(int,list)
"""

def adj_sum_even(number_list):
	"""
	To get a list of adjacent values having the sum even, it can either consist totally 
	odd numbers or totally even numbers. In other words, odd numbers and even numbers can 
	never be together in the list in this scenario.
	So, by default, the list (either odd_list or even_list), 
	having greater number of elements will be the expected output.
	"""

	odd_list = [number for number in number_list if number % 2 != 0]
	even_list = [number for number in number_list if number % 2 == 0]

	if len(odd_list) > len(even_list):
		return len(even_list), odd_list
	else:
		return len(odd_list), even_list


#print("\n##### Even Sum Adjacent elements #####")
#
#number_list = [1, 3, 5, 6, 4, 7, 6, 8, 9, 5, 0, 6, 4, 8, 0]
#result = adj_sum_even(number_list)
#print("Input list: {} \n {} elements removed resulting {} as output.".format(number_list, *result))
#
#
#print("\n########################################################################################################\n")


