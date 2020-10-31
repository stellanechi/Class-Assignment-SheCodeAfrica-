# Examples on Class. A way of grouping functions and other statements

"""class Student_Record:
    pass
std_1 = Student_Record()
std_2 = Student_Record()

std_1.surname = 'Eneh'
std_1.firstname= 'Stella'
std_1.others= 'Nkechi'
std_1.program = 'SheCodeAfrica'
std_1.hort = 3
std_1.username = 'Nechi'
std_1.duration= 'Three'
std_1.mentor = 'Jerry'
std_1.email = 'stellanechi@gmail.com'

std_2.surname = 'Odo'
std_2.firstname= 'Mike'
std_2.others= 'John'
std_2.program = 'SheCodeAfrica'
std_2.hort = 3
std_2.username = 'mike'
std_2.duration= 'Three'
std_2.mentor = 'Jerry'
std_2.email = 'mike@gmail.com'

print(std_1.duration)
print(std_1.email)
print(std_2.program)
"""
class Personal_data:
    def __init__(self,name, sex, complexion, hieght, age, country):
        self.name = name
        self.sex = sex
        self.complexion = complexion
        self.hieght = hieght
        self.age = age
        self.country = country

call_1 = Personal_data('Stella', 'Female','Dark', 5.0, 20,'Nigeria')
call_2 = Personal_data('James', 'Male','Dark', 6.2, 40,'Canada')
call_3 = Personal_data('Angela', 'Female','Fair', 4.2, 12,'China')

print(call_1.name)
print(call_1.complexion)
print(call_2.name)
print(call_3.sex)
