# simple list declaration
simpleListDeclaration = [44,55,66,77,88]

# [0,1,2,3,4]
list2 = [x for x in range(5) ]

# [0,3,6,9,12]
list3 = [x * 3 for x in range(5)]

# [0,2,4,6,8]
list4 = [n for n in range(10) if n % 2 ==0]
print(list4)

namesList = ["James", "Peter", "Aamir", "Nishad", "Abdul"]
contactsList =[person.strip().lower() for person in namesList]
print(contactsList)
