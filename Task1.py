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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# 1. get all telephone numbers
all_telephone_numbers = set() # As the reviewer suggested, we use set() to automatically handle duplicates.

# The usage of python set(): https://www.programiz.com/python-programming/set
for telephone_number in texts:
	all_telephone_numbers.add(telephone_number[0])
	all_telephone_numbers.add(telephone_number[1])
for telephone_number in calls:
	all_telephone_numbers.add(telephone_number[0])
	all_telephone_numbers.add(telephone_number[1])
#print (all_telephone_numbers[0:10])
#print ("numb of records is ", len(all_telephone_numbers), "correct num is ", 2 * (len(texts) + len(calls)))

print ("There are", len(all_telephone_numbers), "different telephone numbers in the records.")
