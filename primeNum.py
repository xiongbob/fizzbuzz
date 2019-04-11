#Write a Program to decide the Prime Number or not
 
#Solution 1
num = int(input("Enter a number: "))
 
for i in range(1, num+1):
	if i == 1:
		print(i, " is not a prime number")
	elif i == 2:
		print(i, " is a prime number")
	else:
		found = 0
		for j in range(2, i):
			if i % j == 0:
				print(i, " is not a prime number")
				found = 1
				break
		if found == 0:
			print(i, " is a prime number")
 

"""
#Solution 2
num = int(input("Enter a number: "))
 
for i in range(2, num):
	if num % i  == 0:
		print("not prime number")
		break
else:
	print("prime numbe")

#Solution 3
# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
"""
