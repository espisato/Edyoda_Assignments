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

print("\n##### Sentence Validation #####")

results = check_sentence(input("Type your sentence: ")) 
if results[0]:
	print(results[1][0])
else:
	for result in results[1]:
		print(result)


print("\n########################################################################################################\n")


