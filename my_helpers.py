# -*- coding: utf-8 -*-
"""
@author: Nayden Dochev
"""

from nltk import Tree

def list_to_string(tree):
    l = tree.leaves()
    s = ""
    b = 0

    for i in l:
        if b:
            s += " "
        s += i[0]
        b = 1
    return s
