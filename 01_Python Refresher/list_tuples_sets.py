# List are mutable, list are with square brackets
grades = [70,80,90]

#  Tuples are Immutable means size is fix,tuples are with round brackets
#  cannot change the elements in the tuple
tuples_grades = (70,80,90)

# set, collection  of unique values
set_grades= {77,80,90,100,100}

# prints the number of elements
print("List length " + str(len(grades)))

#Prints the average
print("Average : " +  str(sum(grades) / len(grades)))

print(set_grades)

grades.append(100) # appends to list
print(grades)

tuples_grades = tuples_grades + (100, 200,) # appends to a tuples_grades
print(tuples_grades)

my_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

# intersection of numbers
print("Intersection " + str(my_lottery_numbers.intersection(winning_numbers)))

# union of numbers
print("Union " + str(my_lottery_numbers.union(winning_numbers)))

# difference of numbers
print("Difference " + str(my_lottery_numbers.difference(winning_numbers)))

#########Exercise####
my_list = [60,30,10]
my_tuple =(2)

print("Sum of list items " + str(sum(my_list)))
print("Value of My tuple " + str(my_tuple))
