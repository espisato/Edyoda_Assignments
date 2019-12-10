"""
How do you check if a given String contains valid brackets? Given a string containing just the characters '(', ')', '{', '}', '[' and ']', write a program in python to check if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Function Name : check_brackets Input : str Output : True/False
"""
##### Note: I changed the name "parentheses" to "brackets", because I think that is more suitable #####

def check_brackets(string):
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


print("\n##### Bracket pairing #####")

strings = ["({[]})", "{}])(", "{}[]()", "(][}{)", "[(([{}]{()}))]"]
for string in strings:
	print(f"Input: {string} \n Output:", check_brackets(string))


print("\n########################################################################################################\n")



