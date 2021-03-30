# Google-Hashcode
Score
A – An example
2,002 points

B – By the ocean
4,554,473 points

C – Checkmate
1,011,194 points

D – Daily commute
1,521,076 points

E – Etoile
636,114 points

F – Forever jammed
252,870 points

Total score
7,977,729 points

#The above score was machieved in the extended round.


The code for the larger traffic datasets like D and F required alloting 1 second to each incoming road at each intersection for green light.

DISCLAMER:
The code used high levels of brute-force and greedy approach.


MAJOR PROBLEMS WE RAN INTO:
->Keeping real time track of cars on each road and the time elapsed from the beginning. Need for use of threading concept suspected.
->Reducing Time Complexity of the solution. The time taken to generate the output file was alarmingly a lot. (The fact that we used brute force couldn't have been more evident.)
->Dealing with huge traffic especially at D and F datasets.


Pending Issues:
-> Cleaning the code.
->Dealing with the above mentioned problems.
