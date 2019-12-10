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

states = {'New Hampshire': ['Concord', 'Hanover'],
'Massachusetts': ['Boston', 'Concord', 'Springfield'],
'Illinois': ['Chicago', 'Springfield', 'Peoria'] }

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

print("\n##### Cities associated with states #####")
print(city_with_states(states))


print("\n########################################################################################################\n")


