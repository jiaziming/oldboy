#!/usr/bin/env python
#-*-conding:utf-8-*-

class SchoolMember(object):
    member = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()


    def enroll(self):
        self.member += 1
        print("\033[32;1m the  [%s] school member[%s] is enrolled!\033[0m "  %(self.name,self.member))
    def tell(self):
        print("Hello my name is %s" %self.name)


class Teacher(SchoolMember):
    def __init__(self,name,age,sex,course,salary):
        super(Teacher,self).__init__(name,age,sex)  #新式类集成方法
        #schoolmember.__init__(self,name,age,sex)   #经典类继承方法
        self.course = course
        self.salary = salary
    def teaching(self):
        print("Teacher [%s] is teaching [%s]" %(self.name,self.course))


class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        super(Student,self).__init__(name,age,sex)
        self.course = course
        self.tuition = tuition
    def pay_tution(self):
        print("cao , student paying tution [%s]"  %self.name,self.tuition)



t1 = Teacher("Alex",22,"F",'py',1000)
t2 = Teacher("tanglan",25,"N/A","PY",900)

s1 = Student("sanjiang",25,"Felme","python",13333)
s2 = Student("baona",22,"F","python",25555)

t1.tell()
t2.tell()

s1.tell()
s1.pay_tution()
s2.pay_tution()
