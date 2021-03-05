# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:17:39 2021

@author: Sristi
"""
import filehandle

begs={}
ends={}
lb=[]
le=[]
streets,cars,stime=filehandle.ret()
for i in streets:
    lb=[]
    le=[]
    key1=i[0]
    key2=i[1]
    for j in streets:
        if j[0]==key1:
            lb.append(j[2])
           
        if j[1]==key2:
            le.append(j[2])
    begs[i[0]]=lb
    ends[i[1]]=le

       
priority=[]
for key in begs:
    maxi=len(begs[key])+len(ends[key])  
    priority.append([maxi,key])
priority.sort(reverse=True)
print(priority)


time={}
for i in streets:
    time[i[2]]=i[-1]
#print(time)
tim=[]

for i in cars:
    t=0
    for j in i[2:]:
        t+=int(time[j])
    tim.append(t)
print(tim,"time")
    
check=[]
for key in ends:
    check.append([len(ends[key]),key])
check.sort()



index=[]
for item in range(len(check)):
    for j in range(len(check)):
        if check[item][1]==priority[j][1]:
            index.append([j,check[item][1]])
            
index.sort()
print(check)
print("INDEX",index)
def di():
    return begs,ends
'''
2--->1
1--->3
3--->3
0--->4

'''
    
#print(tim)    
            
#print(cars)
'''            
0 1 2 3
 1+3+2 = 6s

-----> 
 
-----> 

1 2 0 = 4s
 
    '''  
#print(begs,ends)