"""
#solution 1 - hard code
while True:
	chat = input("Good day. What is your problem? Enter your response here or Q to quit: ")
	chatSplit = chat.split()
	newStr = ""
	for item in chatSplit:
		if item == 'i':
			item = 'you'
		elif item == 'me':
			item = 'you'
		elif item == 'my':
			item = 'your'
		elif item == 'am':
			item = 'are'
		newStr = newStr + item + " "
	print(newStr)

	if chat.upper().startswith("Q"):
		print("You exit to chat!")
		exit()
	
	
"""

#solution 2 - use dictionary
dict = {"i": "you",
		"me": "you",
		"my": "your",
		"am": "are"}

while True:
	chat = input("Good day. What is your problem? Enter your response here or Q to quit: ")
	
	print("user: " + chat)
	if chat.upper().startswith("Q"):
		print("You exit to chat!")
		exit()
	chatSplit = chat.split()
	newStr = ""
	for item in chatSplit:
		if item == 'i':
			newItem = dict.get(item)
		elif item == 'me':
			newItem = dict.get(item)  
		elif item == 'my':
			newItem = dict.get(item)
		elif item == 'am':
			newItem = dict.get(item)
		else:
			newItem = item
		newStr = newStr + newItem + " "
	print("Eliza " + newStr)
		
	
			
"""
#solution 3 - Try to use replace(), but having issue and need to do more researches on...
		   chatCont = input("Enter your response here or Q to quit: ")
		   chatContSplit = chatCont.split()
		   for item in chatContSplit:
			   if item == 'i':
				   chat.replace(item, dict["i"])
			   elif item == 'me':
				   chat.replace(item, dict["me"])   
			   elif item == 'my':
				   chat.replace(item, dict["my"])
			   elif item == 'am':
				   chat.replace(item, dict["am"])
		   print(chatCont)
		"""