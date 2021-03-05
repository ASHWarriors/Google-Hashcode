# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:51:48 2021

@author: Sristi
"""
import filehandle
streets,cars,stime=filehandle.ret()
roads=[]
mapp=[]
accessmap={}
for i in cars:
    roads=roads+i[1:]
for i in streets:
    freq=roads.count(i[2])
    mapp.append([freq,i[2]])
    accessmap[i[2]]=freq

mapp.sort(reverse=True)
maps=[]
for i in range(len(mapp)):
    maps.append(mapp[i][1])
#print(mapp)
'''f2= open(r"new.txt","w")
f2.writelines(["yo","hy"])
f2.close()'''

def retlist():
    return maps,accessmap