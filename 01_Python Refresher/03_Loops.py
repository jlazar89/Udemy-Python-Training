name = "Jeffy Lazar"

# Simple Iterating in a Loop and printing all string characters
# For loop
for character in name:
    print(character)

# List of number and iterating through the number and
# printing the square of each number
numberList =[1,4,5,6,7,8,9,22]
for number in numberList:
    print(number**2)

printNumber = True
while printNumber == True:
    print(10)

    # Taking user input in the console
    user_input = input("Should we print again? (y/n)")
    # If condition
    if user_input =='n':
        printNumber = False
