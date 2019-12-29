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
