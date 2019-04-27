#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:20:37 2019

@author: ishan
"""

import matplotlib.pyplot as plt
import numpy as np


show_animation = True
# Creating obstacle map 
ox,oy = [],[]

obstacle = np.zeros(shape=(250,150))
#Mention the minkowski distance
m = 0

for x in range (0,250):    
    for y in range(0,150):
# Equations for rectangle        
        f1 = -y + (67.5 - m)
        f2 =  y - (112.5 +  m)
        f3 =  -x + (50 - m)
        f4 =  x - (100 + m)
 
 #Equations for circle
        f5 = (x - 190)**2 + (y - 130)**2 - (15+m)**2   
        
 #Equation for ellipse
        f6 = (1/(15+m)**2) * ((x - 140)**2) + (1/(6+m)**2) * ((y - 120)**2) - 1
        
 #Equation for polygon-triangle 1
        f7 = 38*x + 23*y - (m + 192.04)*44.42
        f8 = -y + 52 
        f9 = -38*x + 7*y + (-m + 150.88)*38.64
        
#Equation for polygon-traingle 2
        f10 = 2*x + 19*y - (m + 68.77)*19.10         
        f11 = -41*x -25*y  + (135.88 - m)*48.02
        f12 = 37*x -13*y  - (136.55 )*39.22
        
#Equation for polygon-part 3
        f13 = y - 52 
        f14 = 37*x - 20*y - (145.06 + m)*42.05
        f15 = -y + 15 - m
        f16 = -37*x + 13*y + (136.55)*39.22

#Equation for boundary 1:
        b1 = y - m
#Equation for boundary 2:
        b2 = x - m
#Equation for boundary 3:
        b3 = y - (150 - 1 - m)
#Equation for boundary 4:
        b4 = x - (250 - 1 - m)
        
        if (f1<=0 and f2<=0 and f3<=0 and f4<=0 or f5<=0 or f6<=0 or (f7<=0 and f8<=0 and f9<=0) or (f10<=0 and f11<=0 and f12<=0) or (f13<=0 and f14<=0 and f15<=0 and f16<=0) or b1<=0 or b2<=0 or b3>=0 or b4>=0):
            obstacle[x][y] = 1
            ox.append(x)
            oy.append(y)     

#plotting the obstacle map
plt.plot(ox,oy,".k")
plt.ylim((0,150))
plt.xlim((0,250))
# =============================================================================
c = 0
cx,cy = [],[]
m = m + c
for x in range (0,250):    
    for y in range(0,150):
# Equations for rectangle        
        f1 = -y + (67.5 - m)
        f2 =  y - (112.5 +  m)
        f3 =  -x + (50 - m)
        f4 =  x - (100 + m)
 
 #Equations for circle
        f5 = (x - 190)**2 + (y - 130)**2 - (15+m)**2   
        
 #Equation for ellipse
        f6 = (1/(15+m)**2) * ((x - 140)**2) + (1/(6+m)**2) * ((y - 120)**2) - 1
        
 #Equation for polygon-triangle 1
        f7 = 38*x + 23*y - (m + 192.04)*44.42
        f8 = -y + 52 
        f9 = -38*x + 7*y + (-m + 150.88)*38.64
        
#Equation for polygon-traingle 2
        f10 = 2*x + 19*y - (m + 68.77)*19.10         
        f11 = -41*x -25*y  + (135.88 - m)*48.02
        f12 = 37*x -13*y  - (136.55 )*39.22
        
#Equation for polygon-part 3
        f13 = y - 52 
        f14 = 37*x - 20*y - (145.06 + m)*42.05
        f15 = -y + 15 - m
        f16 = -37*x + 13*y + (136.55)*39.22

#Equation for boundary 1:
        b1 = y - m
#Equation for boundary 2:
        b2 = x - m
#Equation for boundary 3:
        b3 = y - (150 - m)
#Equation for boundary 4:
        b4 = x - (250 - m)
        
        if (f1<=0 and f2<=0 and f3<=0 and f4<=0 or f5<=0 or f6<=0 or (f7<=0 and f8<=0 and f9<=0) or (f10<=0 and f11<=0 and f12<=0) or (f13<=0 and f14<=0 and f15<=0 and f16<=0) or b1<0 or b2<0 or b3>0 or b4>0):
            obstacle[x][y] = 1
            cx.append(x)
            cy.append(y)
