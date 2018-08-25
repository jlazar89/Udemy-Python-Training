contacts = ["John","Anna","James"]
person =input("Enter the person you know :")

# If else  conditions
# use {} with format to subsitute things in strings
if person in contacts:
    print("{} already in Contacts List ".format(person))
else:
    print("{} Not In Contacts List".format(person))


# exercise to return only even numbers from the list below
numbers = [1,2,3,4,5,6,7,8,9,10,20,32,33]

def evenNumbersFromList():
    evenNumbers =[]
    oddNUmbers =[]
    for no in numbers:
        if(no % 2==0):
            evenNumbers.append(no)
        else:
            oddNUmbers.append(no)

    return oddNUmbers

print(evenNumbersFromList())

# To print even numbers till 500
def evenNumbers():
    evenNumbersList =[]
    for no in range(0,100):
        if(no % 2==0):
            evenNumbersList.append(no)

    return evenNumbersList

print(evenNumbers())


# Return quit if 'q' is input and add if 'a' is input
def user_menu(choice):
    if choice =='a':
        return "Add"
    elif choice == 'q':
        return "Quit"

print(user_menu(input("Input value")))


def partyListMembers():
    # Ask the user for a list of pesople they know
    # Split the string into a List
    # Return that list
    people = input("Enter the Members list separeted by commas :")
    list = people.split(",")
    memberlist =[]
    for person in list:
        memberlist.append(person.strip()) #strip removes white spaces from back and front
    return memberlist

def askUser():
    # ask user for name
    # See if the user is in the list of people they know
    # print out that they are invited to the party
    person = input("Enter Your Name :")
    memberlist = partyListMembers()
    if person in memberlist:
        print("{} is invited".format(person))
    else:
        print("{} is not invited".format(person))

askUser()
