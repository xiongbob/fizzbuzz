#Write a Program: Collatz Sequence
""" What is Collatz Sequence?
The Collatz conjecture is a conjecture that a particular sequence always reaches 1.
The sequence is defined as: start with a number n. 
The next number in the sequence is n/2 if n is even and 3n + 1 if n is odd.
"""

"""Pseudocode and Algorithms
1. Create a function collatz that takes an integer n as argument.
2. Create a loop that runs as long as n is greater than 1.
3. In each iteration of the loop, update the value of n.
4. If n is even, set n to n/2 and if n is odd, set it to 3n + 1.
5. Print the value of n in each iteration.
"""

"""Solution 1
def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    print(1, end='')
 
 
n = int(input('Please enter your number n: '))
print('Sequence: ', end='')
collatz(n)
"""

"""
#Solution 2
print("Please enter your number: ")
try:
    number = (int(input()))
except ValueError:
          print("Please enter a valid INTEGER.")


def collatz(number):
    while number != 1:

        if number % 2==0:
            number = (number//2)
            #print(number)
            print(int(number))

        elif number % 2==1:
            number = (3*number+1) 
            #print(number)
            print(int(number))

collatz(number)
"""

#Solution 3
seq = [ ]
x = (int(input("Please enter your number: ")))
if (x == 1):
   print ("Number can't be 1")
seq.append (x)
while x > 1:
    if x % 2 == 0:
        x=int(x/2)
    else:
        x = 3 * x + 1
    seq.append (x)
print (seq)

"""

while True:
 x=int(input('ENTER NO.:'))
 print ('----------------')
 while x>0:
  if x%2==0:
   x = x/2
  elif x>1:
   x = 3*x + 1
  else:
   break
   print (x)
"""