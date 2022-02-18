# Username Generator Program

#1 Display title and instructions
#2 Ask for user input, first and last name
#3 Slice four letters of last name
#4 Slice first letter of first name
#5 Combine sliced letters to create username

print('Welcome to the Username Generator Program.')

first = str(input('Enter first name: '))
last = str(input('Enter last name: '))

last = last[0:4] # Slice first letter up to but not including 4
first = first[0] # Slice first letter, starting at 0

print('Your username is: ' + str.lower(last) + str.lower(first)) # Change to lower case for username format