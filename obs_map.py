#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 03:15:21 2019

@author: ishan
"""

import matplotlib.pyplot as plt
import numpy as np


show_animation = True


# Creating obstacle map 
ox,oy = [],[]
explore_x,explore_y = [],[]
backtrack = []
obstacle = np.zeros(shape=(250,150))
for x in range (0,250):    
    for y in range(0,150):

# Equations for rectangle        
        f1 = -y + 67.5
        f2 =  y - 112.5
        f3 =  -x + 50
        f4 =  x - 100
 
 #Equations for circle
        f5 = (x - 190)**2 + (y - 130)**2 - (15)**2   
        
 #Equation for ellipse
        f6 = (1/225) * ((x - 140)**2) + (1/36) * ((y - 120)**2) - 1
        
 #Equation for polygon-triangle 1
        f7 = 38*x + 23*y - 8530
        f8 = -y +52
        f9 = -38*x + 7*y +5830
        
#Equation for polygon-traingle 2
        f10 = 2*x + 19*y - 1314         
        f11 = -41*x -25*y + 6525
        f12 = 37*x -13*y -5355
        
#Equation for polygon-part 3
        f13 = y - 52
        f14 = 37*x - 20*y - 6101
        f15 = -y + 15
        f16 = -37*x + 13*y + 5355 
        if (f1<=0 and f2<=0 and f3<=0 and f4<=0 or f5<=0 or f6<=0 or (f7<=0 and f8<=0 and f9<=0) or (f10<=0 and f11<=0 and f12<=0) or (f13<=0 and f14<=0 and f15<=0 and f16<=0)): 
            obstacle[x][y] = 1
            ox.append(x)
            oy.append(y) 
            
for i in range(250):
        ox.append(i)
        oy.append(0)
        obstacle[i][0] = 1
for i in range(250):
        ox.append(i)
        oy.append(150)
        obstacle[i][149] = 1
for i in range(150):
        ox.append(0)
        oy.append(i)
        obstacle[0][i] = 1
for i in range(150):
        ox.append(250)
        oy.append(i)
        obstacle[249][i] = 1

#plotting the obstacle map
plt.plot(ox,oy,".k")
plt.ylim((0,150))
plt.xlim((0,250))