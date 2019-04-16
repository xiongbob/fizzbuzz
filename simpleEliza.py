
while True:
   chat = input("Good day. What is your problem? Enter your response here or Q to quit:  ")
   print(chat)

   if chat.upper().startswith("Q"):
      print("You exit to chat!")
      exit()