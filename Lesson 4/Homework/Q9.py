# class Lunch:
#     def __init__(self):
#         self.customer= Customer()
#         self.employee= Employee()
# class Customer:
#     def __init__(self):
#         None
#     def place_order(self,foodname):
#
#     def
# class Employee:
#
# class Food:
#     def __init__(self):

# class Lunch:
#     def order(self, food_name):
#         return Customer().order_food(food_name)
#
#     def receipt(self):
#         return Employee().food_receipt()
#
#
# class Customer:
#
#     @classmethod
#     def order_food(cls, food_name):
#         cls.food_name = Employee().take_order(food_name)
#
#
# class Employee:
#     def take_order(self, food_name):
#         return Food(food_name).name
#
#     def food_receipt(self):
#         return Customer().food_name
#
#
# class Food:
#     def __init__(self, name):
#         self.name = name
#
#
# Lunch().order("Pizza")
# print(Lunch().receipt())




class Lunch:
    def __init__(self): # make/embed Customer and Employee
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):  # start a Customer order simulation
        self.customer.placeOrder(foodName, self.employee)
    def result(self):  # ask the Customer what kind of Food it has
        self.customer.printFood()

class Customer:
    def __init__(self):  # initialize my food to None
        self.food = None
    def placeOrder(self, foodName, employee):  # place order with an Employee
        self.food = employee.takeOrder(foodName)
    def printFood(self):  # print the name of my food
        print(self.food.name)

class Employee:
    def takeOrder(self, foodName):  # return a Food, with requested name
        return Food(foodName)

class Food:
    def __init__(self, name):  # store food name
        self.name = name
lunch= Lunch()
lunch.order("burritos")
lunch.result()







