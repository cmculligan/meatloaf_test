

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
question2 = 'But what about \"that\"? >>'

print ('\n \n')
print ('Welcome to the \"Are you Meatloaf Test\"')
print ('Choose wisely')
		
selection1 = input(question1)

if (selection1 == 'yes'):
	print ('\n \n So far you are Meatloaf!')
	print (question2)
else:
	print ('\n \n So far you are Hall and Oats')
	print (question2)

print ('\n \n')
print ('1) I can\'t go for that, no can do')
print ('2) I won\'t')

selection2 = input(question2)

if (selection2) == '1':
	print ('\n \n\n You are Hall and Oats!')
else:
	print ('\n \n \n You are Meatloaf!')
	
print ('\n')
exit()