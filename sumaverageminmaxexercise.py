#Write a program that asks the user, again and again, to enter a number. (We will assume that the user will only enter integers. The real world is a complex place, but we'll pretend that our users are well behaved for the purposes of this exercise.)
#When the user enters an empty string, then stop asking for additional inputs. Along the way, as the user is entering numbers, I want you to store those numbers in a list. I also want you to keep track of the minimum and maximum values that you've seen so far. 
#When the user has finished entering numbers, your program should print out: The sum of these numbers, The average (mean) of these numbers, The largest and smallest numbers you received from the user.

userintegerslist = []
while True:
	userinput = input("Enter an integer ").strip()
	#a string is considered True except if it's empty.  If it's empty, then it's considered False.
	if not userinput:
		break
	else:
		userinput = int(userinput)
		userintegerslist.append(userinput)
		print("The minimum number is {}".format(min(userintegerslist)))
		print("The maximum number is {}".format(max(userintegerslist)))
print("The sum of the numbers inputted is {}".format(sum(userintegerslist)))
print("The average of the numbers inputted is {}".format((sum(userintegerslist))/len(userintegerslist)))
print("The minimum number is {}".format(min(userintegerslist)))
print("The maximum number is {}".format(max(userintegerslist)))
'''
Enter an integer 4
The minimum number is 4
The maximum number is 4
Enter an integer 5
The minimum number is 4
The maximum number is 5
Enter an integer 88
The minimum number is 4
The maximum number is 88
Enter an integer 6
The minimum number is 4
The maximum number is 88
Enter an integer -2
The minimum number is -2
The maximum number is 88
Enter an integer 
The sum of the numbers inputted is 101
The average of the numbers inputted is 20.2
The minimum number is -2
The maximum number is 88
'''