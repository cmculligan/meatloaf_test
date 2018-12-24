

# PROGRAM TO DETRRMINE IF YOU ARE MEATLOAF OR HALL AND OATS
#	FLOWCHART BELOW

''' Would you do anything for love?
		Almost Anything  (Hall And Oats)
		I would (Meatloaf)
	But what about 'that'?
		I can't go for that (Hall and Oats)
			No can do (Hall and Oats)
		I won't (Meatloaf)
	Result >  You are Meatloaf or You are Hall and Oats
'''

question1 = 'Would you do anything for love? >> '
question2 = 'But what about \"that\"? >> '

print ('\n\nWelcome to the \"Are you Meatloaf Test\" \n\nChoose wisely\n')
		
# Set selection1 variable to the input received for question1 "PRINT THE QUESTION"

selection1 = input(question1)

# Evaluate the input, is it either "yes" or "y", if so they are Meatloaf.  If input is neither than they are Hall and Oats

if (selection1 == 'yes' or selection1 == 'y'):
	print ('\n \n So far you are Meatloaf!')
else:
	print ('\n \n So far you are Hall and Oats')

print ('\n \n')

# Ask the second question and print options for user to choose, set variable selection2 to user input

print ('1) I can\'t go for that, no can do \n2) I won\'t \n \n')

selection2 = input(question2)

# Line 44 could also could be expressed as:
# while (selection2) != '1' and (selection2) != '2':
# while (selection2 not in ('1', '2')):
# Run while loop until user inputs a valid option, in this case '1' or '2' 

while not (selection2 == '1' or selection2 == '2'):
	print ('Seriously tho you do have to actually enter a 1 or a 2 \n')
	selection2 = input(question2)
if (selection2) == '1':
		print ('\n \n\n You are Hall and Oats!')
elif (selection2) == '2':
		print ('\n \n \n You are Meatloaf!')
	
print ('\n\n')

# Is exit() even necessary?
exit()
