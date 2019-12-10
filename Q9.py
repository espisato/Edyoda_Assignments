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

print("\n##### Greatest Sub Array #####")

array1 = [1, 4, 3, 5, 2, 6, 6]
print("Array1: ", array1, "\nGSA: ", greatest_sub_array(array1))
array2 = [1, 5, 3, 3, 4, 5, 3, 6, 5, 7]
print("Array1: ", array2, "\nGSA: ", greatest_sub_array(array2))
	

print("\n########################################################################################################\n")


