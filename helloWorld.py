import random

print('Hello, world!')
print('What is your name?') #ask for their name
myName = input()
print('It is nice to meet you, ' + myName + '.')
print ('The length of your name is: ' + str(len(myName)))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in one year.')
yourName = ''
while yourName != 'your name':
    print('Ok, let\'s try this again. \nWhat is your name?')
    yourName = input()
print('Thank you!')
while True:
    print('Final question: what is the name of your best friend?')
    yourName = input()
    if yourName == 'the name of your best friend':
        break
print('Thanks again!')

while True:
    print('Where are they!?!?!?!?')
    location = input()
    if location != '?':
        continue
    print ('Sorry to bother you. What is the password?')
    password = input()
    if password == 'big doinks':
        break
print('Access granted.')
for i in range(5):
    print('Welcome to the batcave for the ' + str(i+1) + 'th time!')

total = 0
for num in range(101):
    total += num
print('the sum of numbers from 0 to 100 is: ' + str(total))

print('here\'s some random numbers!)
for i in range(5):
    print(random.randint(1,10))