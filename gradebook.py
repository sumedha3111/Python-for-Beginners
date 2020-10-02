# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:31:24 2018

@author: SRM
"""

class student():
    def __init__(self,name,rn,dob):
        self.name=name
        rn=int(input("Enter the roll number"))
        self.rn=rn
        self.dob=dob
    def display(self):
        print("name of the student is",self.name)
        print("roll number of the student is",self.rn)
        print("DOB of the student is",self.dob)
        return
s1=student("ABC",416,"12-01-18")
s1.display()
print('\n')
s2=student("XYZ",417,"2-04-19")
s2.display()
print('\n')
s3=student("ABC",418,"5-06-22")
s3.display()
print('\n')
