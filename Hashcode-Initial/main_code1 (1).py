# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:38:58 2021

@author: anisumitaya
"""
import filehandle

streets,cars,stime=filehandle.ret()
#print(streets)
#print(cars)
route_to_inter=[]
for i in cars:
    stop=[]
    '''for t in streets:
        if i[1]==t[2]:
            stop.append(t[0])'''
    for j in i[1:]:
        for k in streets:
            if j==k[2]:
                stop.append(k[1])
    route_to_inter.append(stop)
#print(route_to_inter,"route") 

import inout
begs,ends=inout.di()


#print(inter_freq,"Inter freq")




       
priority=[]
for key in ends:
    maxi=len(begs[key])+len(ends[key]) 
    if maxi==0:
        pass
    else:
        priority.append([maxi,key])
priority.sort(reverse=True)
print(priority)



inter_freq=[]
for ele in priority:
    count=0
    for i in route_to_inter:
        if ele[1] in i:
            count+=1
    inter_freq.append([ele[1],count])
    
Op = [str(len(begs.keys()))+'\n']
#print(ends)
for i in priority:
    Op.append(i[1]+'\n')
    Op.append(str(len(ends[i[1]]))+'\n')
    
    for k in inter_freq:
        if i[1]==k[0]:
            time=k[1]//len(ends[i[1]])
            if time>stime:
                time=stime
            elif time==0:
                time=1
            else:
               pass 
                
               
            
            
            
            
    for j in ends[i[1]]:
        Op.append(j+' '+str(time)+'\n')
#print(Op) 

f=open("SubD.txt",'w')
f.writelines(Op)
f.close()


