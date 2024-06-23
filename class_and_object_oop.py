

#-------------------------Class--------------------------------------
# a python class is a group of attributess and mehtods
#  ATTRIBUTES?
#            attributes are represented by variable that contain data
#  METHODS ?
#           methods perform an action or task . it is similar to function.

# ------how to create class---------------------
#    SYNATX
class Classamte(object): # object is opitional
    def __init__(self):
        self.variable_value = 'value'
        self.variable_value = 'value2'
    def method_name(self):
        pass

# class : class keyword is used to create a class
# object : object represents the base class name from whaere all classes in python are derived .
#           the class is also derived from object class . this is opitionAL
# __init__() : this method is used to initized the varibles . this is a special method .
#                  we do not call this method explicitly
#  self : self is a variable which refers to current class instance / object

# example 

class Mobile:
    def __init__(self):
        self.model = 'IPHONE 14 PROMAX'
    def show_model(self):
        print("Model:", self.moddel)
# another 

class Mobile:
    def __init__(self,m): # m is a fomal argument
        self.model = m
    def show_model(self,p):
        price = p # local variable we also can use self here 
        print('Model:', self.model, 'price:', price)

# --------------------OBJECT ----------------------------------------
# object is class type variable or class instance . to use a class we should create an object to the class
# syntax 


#               object_name = class_name()
#               object_name = class_name(arg)    the argument which you can give

# -----------------how to create a object---------------------------
#example
#here example of phone class having arguments = model , price and colour

#1st approch

class Phone:
    def __init__(self, model,price,colour):  #with arguments
        self.model = model 
        self.price = price
        self.colour = colour
    
    def show_model(self):
        print('Model:',self.model)
    
    def show_price(self):
        print('Price:',self.price)

    def show_colour(self):
        print('Colour:',self.colour)

model = input('Enter phone model:')  #asking input from user
price = 120000
colour = input('enter phone colour')
phone_data = Phone(model,price,colour)

print('-'*33)  # for better look
phone_data.show_colour()
phone_data.show_model()
phone_data.show_price()

# BEST APPROCH with other example

class StudentsData:
    def __init__(self, name, father_name, age, section):
        self.name = name  
        self.father_name = father_name
        self.age = age
        self.section = section
    
    def get_name(self):
        return self.name
    
    def get_father_name(self):
        return self.father_name
    
    def get_age(self):
        return self.age
    
    def get_section(self):
        return self.section
    
    def display_info(self):
        print('-'*29)
        print("Student Name:", self.name)
        print("Father's Name:", self.father_name)
        print("Age:", self.age)
        print("Section:", self.section)


name = input("Enter your name: ")
father_name = input("Enter your father's Name: ")
age = input("Enter your age: ")
section = input("Enter your section: ")

students_data = StudentsData(name, father_name, age, section)
students_data.display_info()
# ---------------------------------------------------------------------