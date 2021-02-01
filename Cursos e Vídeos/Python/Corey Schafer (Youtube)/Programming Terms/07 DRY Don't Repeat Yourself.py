# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:39:21 2020

@author: pedro
"""
##############################################
# não é DRY ##################################
##############################################

def homePage():
    print('<div class="header">')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')
    
    print('<p>Welcome to our Home Page!</p>')
    
    print('<div class="footer">')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')

def aboutPage():
    print('<div class="header">')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')
    
    print('<p>Welcome to our About Page!</p>')

    print('<div class="footer">')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')


def contactPage():
    print('<div class="header">')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')
    
    print('<p>Welcome to our Contact Page!</p>')

    print('<div class="footer">')
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')
    print('</div>')

homePage()
aboutPage()
contactPage()

##############################################
# é DRY ######################################
##############################################

def nav_menu():
    print('<a href="#">Home</a>')
    print('<a href="#">About</a>')
    print('<a href="#">Contact</a>')

def header():
    print('<div class="header">')
    nav_menu()
    print('</div>')

def footer():
    print('<div class="footer">')
    nav_menu()
    print('</div>')

def homePage():
    header()
    print('<p>Welcome to our Home Page!</p>')
    footer()

def aboutPage():
    header()
    print('<p>Welcome to our About Page!</p>')
    footer()


def contactPage():
    header()
    print('<p>Welcome to our Contact Page!</p>')
    footer()

homePage()
aboutPage()
contactPage()

##############################################
# não é DRY ##################################
##############################################

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

import unittest

class CalcTestCase(unittest.TestCase):
    """ """
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_add(self):
        num1 = 10
        num2 = 5
        self.assertTrue(add(num1,num2), num1 + num2)
        
    def test_subtract(self):
        num1 = 10
        num2 = 5
        self.assertTrue(subtract(num1,num2), num1 - num2)

    def test_multiply(self):
        num1 = 10
        num2 = 5
        self.assertTrue(multiply(num1,num2), num1 * num2)

    def test_divide(self):
        num1 = 10
        num2 = 5
        self.assertTrue(divide(num1,num2), num1 / num2)

if __name__ == '__main__':
    unittest.main()

print(unittest.main())

##############################################
# é DRY ######################################
##############################################


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

import unittest

class CalcTestCase(unittest.TestCase):
    """ """
    def setUp(self):
        self.num1 = 10
        self.num2 = 5
    
    def tearDown(self):
        pass
    
    def test_add(self):
        self.assertTrue(add(self.num1,self.num2), self.num1 + self.num2)
        
    def test_subtract(self):
        self.assertTrue(subtract(self.num1,self.num2), self.num1 - self.num2)

    def test_multiply(self):
        self.assertTrue(multiply(self.num1,self.num2), self.num1 * self.num2)

    def test_divide(self):
        self.assertTrue(divide(self.num1,self.num2), self.num1 / self.num2)

if __name__ == '__main__':
    unittest.main()

print(unittest.main())
























