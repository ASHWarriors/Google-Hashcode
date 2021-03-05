# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:58:56 2021

@author: anisumitaya
"""
f= open("a.txt")
raw_list= f.readlines()
f.close()
#print(raw_list)
first_line= raw_list[0].rstrip("\n").split(" ")
print(first_line)
stime=int(first_line[0])
range1= int(first_line[2])
range2=int(first_line[3])
raw_streets= raw_list[1:1+range1]
raw_cars= raw_list[1+range1:]
#print(raw_streets)
#print(raw_cars)
streets=[]
cars=[]
for i in raw_streets:
    streets.append(i.rstrip("\n").split(" "))
for i in raw_cars:
    cars.append(i.rstrip("\n").split(" "))
print(streets)
print(cars,'cars') 

def ret():
    return streets,cars,stime

'''
f= open("Sub1.txt",'w')
f.writelines()'''