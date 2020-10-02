# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:24:53 2018

@author: SRM
"""

class area():
    def acircle(self,r):
        print(3.14*r*r)
    def asquare(self,r):
        print(r*r)
    def arectangle(self,l,b):
        print(l*b)
obj=area()
obj.acircle(10)
obj.asquare(25)
obj.arectangle(2,4)
