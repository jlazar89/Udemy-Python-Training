class Student:
    def __init__(self,name,school):
        self.name= name
        self.school= school
        self.marks= []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls,origin, friend_name, *args):
        return cls(friend_name, origin.school,*args )

class WorkingStudent(Student):
    def __init__(self ,name, school, salary, job_title):
        super().__init__(name,school)
        self.salary = salary
        self.job_title = job_title

jeffy = WorkingStudent("Jeffy", "Oxford", 20.200 ,"Software Developer")
print(jeffy.salary)

friend = WorkingStudent.friend(jeffy,"Aamir",85, "Software Developer")
print("Name is {}".format(friend.name))
print("His school is {}".format(friend.school))
print("and finally his salary {}".format(friend.salary))
