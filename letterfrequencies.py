#Ask the user to enter some text. We're then going to display the distribution of letters from within the text.
#The program does the following:
#1. Convert all letters to lowercase
#2. Ignore characters that aren't lowercase letters
#3. Create a dictionary in which the keys are letters and the values are the counts.
#RM:  Instructor doesn't want us to use Counter.  I looked at solution.  Dumb.  I use counter to practice.

from collections import Counter
alphabet = "abcdefghijklmnopqrstuvwyxz"
letterinput = input("Enter some text: ").lower().strip()
finalletterinput = ""
for eachletterinput in letterinput:
	if eachletterinput in alphabet:
		finalletterinput += eachletterinput		
print(Counter(finalletterinput))
percentagefinalletterinput = Counter(finalletterinput)
for key, value in percentagefinalletterinput.items():
	# print(key, value, round((value/len(finalletterinput)),2))
	# print(key, value, format(value/len(finalletterinput),".2f"))
	# print(key, value, "{}%".format((value/len(finalletterinput))*100))
	print(key, value, "{0:.0%}".format((value/len(finalletterinput)))) #https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
'''
Enter some text: whothatgirl
Counter({'h': 2, 't': 2, 'w': 1, 'o': 1, 'a': 1, 'g': 1, 'i': 1, 'r': 1, 'l': 1})
w 1 9%
h 2 18%
o 1 9%
t 2 18%
a 1 9%
g 1 9%
i 1 9%
r 1 9%
l 1 9%
'''