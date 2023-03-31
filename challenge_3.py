"""Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
https://pythonprinciples.com/challenges/Online-status/
"""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(dict_statuses):
	counter_online = 0
	for i in dict_statuses:
		if dict_statuses[i] == "online":
			counter_online += 1
	return counter_online

	# return len([i for i in dict_statuses if dict_statuses[i] == "online"])



online_count(statuses)