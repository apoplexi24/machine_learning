# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 01:16:46 2021

@author: shiva
"""

import numpy as np
def levenshtein(s, t):
   
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                z = 0 
            else:
                z = 1
            distance[row][col] = min(distance[row-1][col] + 1,      
                                 distance[row][col-1] + 1,          
                                 distance[row-1][col-1] + z)     
   
        return "The strings have {} genomic polymorphisms.".format(distance[row][col])
    
"gcctatcggtgaccaactcgatgggtctatcggcaagccacgcgatgtg"
"atatcttggcaaccaactcgatgggtctatcggcaagccacgcgatatg"
Distance = levenshtein(a,b)
print(Distance)
print(len(a))