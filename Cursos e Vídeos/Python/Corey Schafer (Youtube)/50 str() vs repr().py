# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:42:00 2020

@author: pedro

O objetivo de __repr__ é ser não ambíguo.

O objetivo de __str__ é ser legível.
"""

# https://www.youtube.com/watch?v=5cvM-crlDvg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=50

##################################################

globals().clear()

a = [1,2,3,4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

##################################################

globals().clear()

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))

print()

print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))

print()



