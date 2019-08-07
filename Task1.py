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
all_telephone_numbers = []
for telephone_number in texts:
	all_telephone_numbers.append(telephone_number[0])
	all_telephone_numbers.append(telephone_number[1])
for telephone_number in calls:
	all_telephone_numbers.append(telephone_number[0])
	all_telephone_numbers.append(telephone_number[1])
#print (all_telephone_numbers[0:10])
#print ("numb of records is ", len(all_telephone_numbers), "correct num is ", 2 * (len(texts) + len(calls)))
# 2. deduplicate telephone numbers
# Ref: https://stackoverflow.com/questions/6764909/python-how-to-remove-all-duplicate-items-from-a-list
dedup_tele = list(set(all_telephone_numbers))
print ("There are", len(dedup_tele), "different telephone numbers in the records.")