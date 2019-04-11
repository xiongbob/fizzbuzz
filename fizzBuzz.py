#Write a program that prints the numbers from 1 to 100.
#For multiples of 3 print “Fizz” instead of the number.
#For the multiples of five print “Buzz”.
#For numbers which are multiples of both 3 and 5 print “FizzBuzz”.

#Solution 1
a = 0
while a <= 99:
	a += 1 # Same as a = a + 1 
	if a%3 == 0 and a%5 == 0: print('FizzBuzz')
	elif a%3 == 0: print('Fizz')
	elif a%5 == 0: print('Buzz')
	else: print (a)
	
