#!/usr/bin/python



# def frange(start,stop, step=1,0):
#     while start < stop:
#         yield start
#         start +=step

#data = [ [i/100,0 for i in range(0, 100, 1)],  ],

# def f(size):
#  	for index in range(size):
#  		yield range(index, index + size)


# data = [f(100)],


# w, h = 100, 100;
# Matrix = [[0 for x in range(w)], for y in range(h)], 


#print(Matrix)
"""data =[
"""
#print(m) for m in ([print(n) for n in data], )

data = [[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,],
 [  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,],
 [  2,   3,   4,   5,   6,   7,   8,   9,  10,  11,],
 [  3,   4,   5,   6,   7,   8,   9,  10,  11,  12,],
 [  4,   5,   6,   7,   8,   9,  10,  11,  12,  13,],
 [  5,   6,   7,   8,   9,  10,  11,  12,  13,  14,],
 [  6,   7,   8,   9,  10,  11,  12,  13,  14,  15,],
 [  7,   8,   9,  10,  11,  12,  13,  14,  15,  16,],
 [  8,   9,  10,  11,  12,  13,  14,  15,  16,  17,],
 [  9,  10,  11,  12,  13,  14,  15,  16,  17,  18,],]

n = 100
data = [ [  x + y for x in range(n) ] for y in range(n) ]
#
for i in range(n):
	for j in range(n):
		#if i > n /2 - n/10 and i < (n / 2 + n / 10): #if i + j > n*2 - n / 8:   
		if i > n /2 - n/10 and i < (n / 2 + n / 10) and \
		j > n /2 - n/10 and j < (n / 2 + n / 10):   
			data[i][j] += 100
#
from pylab import *
imshow(data)
xlabel('X (m)')
ylabel('Y (m)')
#title('Matplotlib example')
show()	