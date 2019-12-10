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



print("\n##### Password Validation #####")

results = check_password_strength(input("Enter your password: "))
print(results[0])
for result in results[1]:
	print(result)


print("\n########################################################################################################\n")


