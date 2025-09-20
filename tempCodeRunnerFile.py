class Test :

#     def __init__(self):
#         self.a = 10
#     def m1(self):
#         self.b = 20

# t=Test()
# t.m1()
# print(t.__dict__)


# #How to access instance variable
# class Test:

#     def __init__(self):
#         self.a = 10
#         print(self.a)

#     def m1(self):
#         print(self.a)

# t = Test()
# t.m1()
# print(t.a)

# # static variable :
# class Test:
#     a = 10
#     def __init__(self):
#         Test.b = 20
#     def m1(self):
#         Test.c = 30

#     def m2(self):
#         print("Static variable values")
#         print(Test.a)
#         print(Test.b)
#         print(Test.c)

# t=Test()
# t.m1()
# print(Test.__dict__)
# t.m2()