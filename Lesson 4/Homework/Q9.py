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

class Lunch:
    def order(self, food_name):
        return Customer().order_food(food_name)

    def receipt(self):
        return Employee().food_receipt()


class Customer:

    @classmethod
    def order_food(cls, food_name):
        cls.food_name = Employee().take_order(food_name)


class Employee:
    def take_order(self, food_name):
        return Food(food_name).name

    def food_receipt(self):
        return Customer().food_name


class Food:
    def __init__(self, name):
        self.name = name


Lunch().order("Penis")
print(Lunch().receipt())