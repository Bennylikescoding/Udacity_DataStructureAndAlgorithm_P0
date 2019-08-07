"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Build a list to hold numbers that send texts,receive texts or receive incoming calls
list_negative = []
for telephone_number in texts:
	if telephone_number[0] not in list_negative:
		list_negative.append(telephone_number[0])
	if telephone_number[1] not in list_negative:
		list_negative.append(telephone_number[1])
for telephone_number2 in calls:
	if telephone_number2[1] not in list_negative:
		list_negative.append(telephone_number2[1])
	

out_going_calls = []
for outgoing_call in calls:
	if outgoing_call[0] not in out_going_calls:
		out_going_calls.append(outgoing_call[0])

#print (len(list_negative),len(out_going_calls))

#subtracting records:
list_telemarketers = []
for number in out_going_calls:
	if number not in list_negative:
		list_telemarketers.append(number)
print ("These numbers could be telemarketers: ")
for i in sorted(list_telemarketers):
	print (i)





