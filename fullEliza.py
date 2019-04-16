#solution - use dictionary and random lib
import random

#interact in a caring way
def get_response (chat):
# prededefined sets qulifiers and hedges for random lib 
	#and dictionary of substitute words
	dict = {"i": "you",
		"me": "you",
		"my": "your",
		"am": "are"}
	qualifier = ['Why do you say that',
                 'You seem to think that',
                 'So, you are concerned that']
	hedge = ['Please tell me more',
             'Many of my patients tell me the same thing',
             'It is getting late, maybe we had better quit']

#   random selection between hedge and qualifier with modification
	if random.randrange(2)==1:
		return(random.choice(hedge))
	else:
		response=[]      #if qualifier start with random qualifier
		response.append(random.choice(qualifier))

		chatSplit = chat.split()
		for item in chatSplit:
			if item == 'i':
				item = dict.get(item)
			elif item == 'me':
				item = dict.get(item)         
			elif item == 'my':
				item = dict.get(item)
			elif item == 'am':
				item = dict.get(item)
			response.append(item)
		return ' '.join(response)    # convert list to a concatenated string

# initialize
done = False     # flag to check
exit = ['q', 'i am feeling great']    # condition to exit our of program
while not(done):
	chat = input("Good day. What is your problem? Enter your response here or Q to quit: ")
	print("user: " + chat)
	
	if chat.lower() != 'q':        # check if user wants to quit
		print ('Eliza:', get_response(chat))
		
	if chat.lower() in exit:       # check if valid exit conditions update while loop condition
		done = True
		print ('Eliza: Thank you for stopping by. See you next time.')
		
	"""
	if chat.upper().startswith("Q"):
		print("You exit to chat!")
		exit()
	"""