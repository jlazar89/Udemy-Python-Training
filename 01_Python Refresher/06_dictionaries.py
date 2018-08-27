#Dictionary with list in it
personDetails ={'name':'James','age':25,'grades':[20,45,60]}

# Dictionary with tuple in it
lotteryPlayer={
    'name':'Rolf',
    'number' :(9824429294,9696968585)
}

# dictionary in a dictionary
universities =[
    {
        'name': 'Oxford',
        'location' :'UK'
    },
    {
        'name' : 'MIT',
        'Location' :'US'
    }
]


# Exercise : create a dictionary variablecalled student
# Keys name, school, grades
student ={
    'name': 'James',
    'school': ' Computing',
    'grades': (66, 77, 88,)
}


def averageGrade(data):
    grades = data['grades']
    return sum(grades)/len(grades)

print(averageGrade(student))

def averageGradeofAllStudents(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total/count

print(averageGradeofAllStudents(student))
