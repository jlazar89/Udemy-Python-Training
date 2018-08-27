lotteryPlayer ={
    'name' : 'jeffy',
    'numbers':(5,9,7,8,6)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,8,9,7)

    def total(self):
        return sum(self.numbers)

# Instance or creating an object of LotteryPlayer
# Object oriented programming
playerOne = LotteryPlayer("Jimmy")
playerTwo = LotteryPlayer("Jeffy")
print(playerOne.name)
print(playerTwo.name)


class Student:
    def __init__(self, name, school):
        self.name= name
        self.school = school
        self.marks =[]

    def average(self):
        return sum(self.marks)/len(self.marks)

    @staticmethod #staticmethod we don't need to pass 'self' as an argument
    def goToSchool():
        print("I'm going to school")

    @classmethod #classmethod it pass Class as an argument
    def printName(cls):
        print("Hello Hello ")



anna = Student("Anna","MIT")
anna.marks.append(56)
anna.marks.append(65)
anna.printName()
# Since it is a static method, dont need to creat an object/instance
Student.goToSchool()



# Exercise 1
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def addItem(self, name, price):
        item = {
            'name' : name,
            'price': price
        }
        self.items.append(item)

    def stockPrice(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")

    @staticmethod
    def storeDetails(cls):
        return '{}, Total stock Price : {}'.format(store.name, int(store.stockPrice))


storeProduct = Store("Biscuits")
storeProduct.addItem("Britannia",50)
print(storeProduct.stockPrice())
print(storeProduct.franchise("Amazon"))

# Exercise 2
