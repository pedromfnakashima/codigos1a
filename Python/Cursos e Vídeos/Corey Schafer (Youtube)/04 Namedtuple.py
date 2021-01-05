# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:41:37 2020

@author: pedro

Facilita a readability
"""

# https://www.youtube.com/watch?v=GfxJYp9_nJA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=39

globals().clear()

############################################
# Cores RGB

color = (55,155,255)

print(color[0])


############################################

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(blue=55,green=155,red=255)

print(color[0])

print(color.red)

white = Color(255,255,255)

print(white.red)


############################################




############################################




############################################

























