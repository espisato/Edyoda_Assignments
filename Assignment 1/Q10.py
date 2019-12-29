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
		return len(even_list), even_list
	else:
		return len(odd_list), odd_list


#print("\n##### Even Sum Adjacent elements #####")
#
#number_list = [1, 3, 5, 6, 4, 7, 6, 8, 9, 5, 0, 6, 4, 8, 0]
#result = adj_sum_even(number_list)
#print("Input list: {} \n {} elements removed: {}".format(number_list, *result))
#
#
#print("\n########################################################################################################\n")


