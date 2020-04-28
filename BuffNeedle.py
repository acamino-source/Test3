
# Monte Carlo simulation of Buffons needle to estimate the probability when any part of a disc of diameter d=3/4 crosses a parallel line of distance w=1 after 1, 984, 444, 444 tosses

import random
import math

def checkCrosses(y,d,delta):
    if (y+d*math.sin(delta))>= math.sin(2*delta):
        # Checking if "needle" crosses the polar coordinate 
        return True
    else:
        return False

N = int(input('Enter the total number of times that the needle is randomly dropped: N = '))
d = float(input('Enter the length of the needle: d = '))
w = 1 # only taking first quadrant for simplicity
N_c = 0 # total number of times the "needle" crosses one of the parallel lines

# Simulating N times
for i in range(0,N):
    theta = random.random()*90 # Angle in degrees which is measured with respect to rightmost parallel line
    x = random.random()*w # x-coordinate of midpoint of "needle"
    y = random.random()*w

    theta_r = math.radians(theta) # Angle in radians which is measured with respect to rightmost parallel line
    delta = 0.5*d*math.sin(theta_r) # Delta value used to find enpoints of "needle"
    x_left = x + delta #leftmost endpoint of "needle"
    x_right = x - delta #rightmost endpoint of "needle"

    if checkCrosses(y,d,theta_r):
        N_c+=1

print('Total number of times that the needle is randomly dropped: ',str(N))
print('Total number of times the disc crossed polar equation: ',str(N_c))
print('Probability when any part of the disc crosses a parallel line for a total of N tosses: ',str((N_c/N)))


    

