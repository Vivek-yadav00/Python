# class Car:
   
        
    
#     def getWheel(self):
#         return "2"


# class Honda(Car):
#     def getCarName(self):
#         return "Honda"
    
#     def getWheel(self):
#         return "3"

# car = Honda()
# print(car.getCarName())

# def set_name(self,name):
#       self.name = name

#    def get_name(self):
#       return self.name
# student1 = Student()
# student1.set_name("Siddharth")

# student2 = Student()
# student2.set_name("Aman")
# print(student1.get_name())
# print(student2.name)

# class Rectangle:
#     def __init__(self,width,height):
#       self.a = width
#       self.b = height

#     def printWidth(self):
#         return self.a
    
# rectangle1 = Rectangle(width=2,height=4)

# print(rectangle1.printWidth())



# class Rectangle:
#     def _init_(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.height * self.width
#     def perimeter(self):
#         return 2*(self.height+self.width)
# rectangle1 = Rectangle(3,4)
# print(rectangle1.area())
# print(rectangle1.perimeter())
# # class Rectangle:
# #     def _init_(self,width,height):
# #         print(f"The rectangle is created with the height: {height} and width: {width} ")
# #         self.width = width
# #         self.height = height

# #     def area(self):
# #         return self.height * self.width

# #     def perimeter(self):
# #         return 2*(self.height+self.width)
# # rectangle1 = Rectangle(3,4)
# # rectangle2 = Rectangle(5,7)
# # rectangle3 = Rectangle(9,6)


# class Rectangle:
#     pass

# object1=Rectangle()
# object1.width = 42
# object1.heigt = 52

# print(object1.width)

# object2=Class_Name()
# object2.name="XYZ"
# object2.age=35

# print("object1 details:")
# print("Name:", object1.name)
# print("Office:", object1.age)


class test:
    def method1(self,name,age):
        self.name=name
        self.age=age
    def method2(self,name,age):
        print("my name is ",self.name.upper(),"and age is",self.age)
test1=test()
test1.method1("vivek",20)
test1.method2("my",9)



# class Test:
#      def __init__(self,name=None,age=None):
#          self.name=name
#          self.age=age
#      def method2(self,name):
#          print("my name is ",self.name,"and age is")

#      def test(self,age):
#          print(age)
# test1=Test(name="jio",age=78)
# test1.test(23)
# test1.method2("hello")


# # class parent:
# #     def set(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def get(self):
# #         print("my name is",self.name)
# # class child(parent):
# #   def get_age(self):
# #       print("age is",self.age)
# # test=child()
# # test.set("abcd",25)
# # test.get()
