"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
###### use previous variables in Task1:#########
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
####################################

# 1. get time spent of the sending and receiving telephone number.
dict_of_telephone_time = {}
time_spent_of_this_telephone_number = 0
total_time_spent_of_this_telephone_number = 0
for telephone_number in dedup_tele:
	for item in calls:
		if item[0] == telephone_number or item[1] == telephone_number:
			total_time_spent_of_this_telephone_number += int(item[3])
			dict_of_telephone_time[telephone_number] = total_time_spent_of_this_telephone_number		
	total_time_spent_of_this_telephone_number = 0
# Simply print out 
#for key, val in dict_of_telephone_time.items():
#    print("phone call of ", key, "spent: ", val, "seconds")

# 2. get the longest time spent
longest_time_spent = max(dict_of_telephone_time.values())
#print (longest_time_spent)
for key, value in dict_of_telephone_time.items():
	if value == longest_time_spent:
		print (key," spent the longest time", longest_time_spent, "seconds, on the phone during September 2016.")
















