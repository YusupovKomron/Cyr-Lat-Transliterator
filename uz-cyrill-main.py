# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:42:26 2022

@author: asliddinxanov
"""

from transliterate import to_cyrillic, to_latin

a = input("Enter word:")
if a.isascii():
    print(to_cyrillic(a))
else:
    print(to_latin(a))
    