# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:38:58 2021

@author: anisumitaya
"""
#import filehandle
import dailycomm 
# streets,cars,stime=filehandle.ret()
# #print(streets)
# #print(cars)
# route_to_inter=[]
# for i in cars:
#     stop=[]
#     for j in i[1:]:
#         for k in streets:
#             if j==k[2]:
#                 stop.append(k[1])
#     route_to_inter.append(stop)
#print(route_to_inter,"route") 

import inout
begs,ends=inout.di()
#print(inter_freq) 
# priority=[]
# for key in ends:
#     maxi=len(begs[key])+len(ends[key]) 
#     if maxi==0:
#         pass
#     else:
#         priority.append([maxi,key])
# priority.sort(reverse=True)
# #print(priority)

# inter_freq=[]
# for ele in priority:
#     count=0
#     for i in route_to_inter:
#         if ele[1] in i:
#             count+=1
#     inter_freq.append([ele[1],count])
    
#Op = [str(len(begs.keys()))+'\n']
#print(ends)
mapp2,accmap=dailycomm.retlist()
# #print(mapp2)
# traffic=[]
# for key in ends:
#     #print(key)
#     minil=[]
#     for road in ends[key]: 
#         #print(road)
#         for j in range (len(mapp2)):
#             if road == mapp2[j][1]:
#                 minil.append(mapp2[j][0])
#     traffic.append([key,minil])
  
#Quick question : minil is a list containing the cars lined up for that road
# traffic is a list of lists containing intersection and cars in that intersection in the order of most frequent roads
# Now the most frequented road cannot have less number of cars than the latter roads so it is safe to assume that the minilist for each intersection would be sorted in the reverse order.
# Another interesting thing is sum(minil)<=simulation time? || sum(minil)<=total cars   
    
# print(traffic) 


OP=[str(len(begs.keys()))+'\n']
def greenlight(OP):
    for mkey in ends:
        OP.append(mkey+'\n')
        OP.append(str(len(ends[mkey]))+'\n')
        outl=[]
        #count=0
        for key in mapp2:
           
            # print("key",key)
            if key in accmap:
                if key in ends[mkey]:
                    if accmap[key]!=0:
                        outl+=[key +' '+str(accmap[key]) +'\n']
               #     count+=1
        # if count>0:
        #     OP.append(str(count)+'\n')
        #     count=0
        # print("OP",OP)
        # print('outl',outl)
        OP=OP+outl
                    
    return OP
       #OP gives roads and the time for green light cycle for each intersection
        
    
    # for key1 in ends:
    #     for key2 in accmap:
    #         if key2 in ends[key1]:
    #         print("yes")
    #             for i in len(ends[key1]):
    #                 print(accmap[key1][i])
    #             if accmap[key1][i]!=0:
    #                 out=ends[key1][i]+' '+accmap[key1][i]+'\n'
    #                 print("out",out)
    #             else:
    #                 pass
    #             OP.append(out)
    # return OP

stuff=greenlight(OP)
f=open("SubbF.txt",'w')
f.writelines(stuff)
f.close()
            
                
                
        
            


# for i in priority:
#     Op.append(i[1]+'\n')
#     Op.append(str(len(ends[i[1]]))+'\n')
    
#     for k in inter_freq:
#         if i[1]==k[0]:
#             time=k[1]//len(ends[i[1]])  #proportianal to roads--freq
#             if time>stime:
#                 time=stime
#             elif time==0:
#                 time=1
#             else:
#                pass
            
            
#     for j in ends[i[1]]:
#         Op.append(j+' '+str(time)+'\n')
# #print(Op) 

'''f=open("SubbD.txt",'w')
f.writelines(Op)
f.close()'''

'''
mapps=[[freq,road_name]...]
#The road with max frequency of cars comes first.

adding the incoming cars from mapps to minil for each intersection
minil=[cars_in_2,cars_in_1,cars_in_3]
# Hence the car frequency would be in decreasing order given that 
#we traversed mapps to compute this 

traffic=[[key1,[cars_in_2,cars_in_3,cars_in_1..]],[key2,..]]
 # Here cars_in_1,2,3 is sorted--reverse order 
 
ends={key1:[road_1,road_2,road_3..]..}
#Here road_1,2,3 is not in the same order as the cars_in_1,2,3!



'''
