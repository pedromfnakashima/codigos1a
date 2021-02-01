# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:28:24 2020

@author: pedro
"""
globals().clear()

from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Logging In ...')

