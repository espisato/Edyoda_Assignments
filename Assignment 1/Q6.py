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


