import random


# set up random variables
y0=random.randint(0,99)
x0=random.randint(0,99)
print(y0,x0)


#walk one random step
if random.random() < 0.5:
    y0=y0+1
else:
    y0=y0-1
 #print value of variable   
#print(y0)

#walk one random step
if random.random() < 0.5:
    x0=x0+1
else:
    x0=x0-1
 #print value of variable   
#print(x0)
print(y0,x0)
#walk one random step
if random.random() < 0.5:
    y0=y0+1
else:
    y0=y0-1
 #print value of variable   
#print(y0)

#walk one random step
if random.random() < 0.5:
    x0=x0+1
else:
    x0=x0-1
 #print value of variable   
#print(x0)
print(y0,x0)


# set up variables
y1=random.randint(0,99)
x1=random.randint(0,99)
print(y1,x1)

#walk one random step
if random.random() < 0.5:
    y1=y1+1
else:
    y1=y1-1
 #print value of variable   
#print(y0)

#walk one random step
if random.random() < 0.5:
    x1=x1+1
else:
    x1=x1-1
 #print value of variable   
#print(x0)
print(y1,x1)
#walk one random step
if random.random() < 0.5:
    y1=y1+1
else:
    y1=y1-1
 #print value of variable   
#print(y0)

#walk one random step
if random.random() < 0.5:
    x1=x1+1
else:
    x1=x1-1
 #print value of variable   
#print(x0)
print(y1,x1)
 
#Euclidian distance
dy=(y0-y1)**2
dx=(x0-x1)**2
eud=(dy+dx)**0.5
print(eud)
