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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
list_of_receiver_called_by_080 = []
for call in calls:
	if call[0][:5] == '(080)':
		if call[1] not in list_of_receiver_called_by_080:
			list_of_receiver_called_by_080.append(call[1])

list_of_areacodes_prefix = []
for record in list_of_receiver_called_by_080:
	if record.startswith('('):
		list_of_areacodes_prefix.append(record[2:record.index(')')])
	else:
		list_of_areacodes_prefix.append(record[0:4])

list_of_areacodes_prefix_deduplicate = []
for i in list_of_areacodes_prefix:
	if i not in list_of_areacodes_prefix_deduplicate:
		list_of_areacodes_prefix_deduplicate.append(i)

print ("The numbers called by people in Bangalore have codes:")
for item in sorted(list_of_areacodes_prefix_deduplicate):
	print (item)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

list_of_sender_080 = []
list_of_receiver_also_080 = []
for item1 in calls:
	if item1[0][:5] == '(080)':
		list_of_sender_080.append(item1)

for item2 in list_of_sender_080:
	if item2[1][:5] == '(080)':
		list_of_receiver_also_080.append(item2)

#print ("percentage 2 is ", len(list_of_receiver_also_080))
#print ("percentage 1 is ", len(list_of_sender_080))

# Format percentage, ref: https://stackoverflow.com/questions/5306756/how-to-show-percentage-in-python
percentage = "{0:.2%}".format(len(list_of_receiver_also_080) / len(list_of_sender_080))
print (percentage, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")









