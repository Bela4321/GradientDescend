from random import uniform
import matplotlib.pyplot as plt


def f(x,y):
    return (6*x*y**2+5*x**2+9*x*y-5*y**3)/(x**4+y**4+1)

def dfdx(x,y):
    return (10*x+6*y**2+9*y)/(x**4+y**4+1)-(4*x**3*(5*x**2+6*y**2*x+9*y*x-5*y**3))/(x**4+y**4+1)**2

def dfdy(x,y):
    return (-15*y**2+12*x*y+9*x)/(y**4+x**4+1)-(4*y**3*(-5*y**3+6*x*y**2+9*x*y+5*x**2))/(y**4+x**4+1)**2


domain = [[-2,2],[-2,2]]
iterations=1000
save=[]
alpha=0.01
for i in range(iterations):
    point= [uniform(domain[0][0],domain[0][1]),uniform(domain[1][0],domain[1][1])]
    gradient=(dfdx(point[0],point[1]),dfdy(point[0],point[1]))
    difference= 10
    for j in range(1000):
        newPoint = [point[0]+gradient[0]*alpha,point[1]+gradient[1]*alpha]
        gradient=(dfdx(point[0],point[1]),dfdy(point[0],point[1]))
        point = newPoint
    #test divergence
    current= point
    for j in range(100):
        newPoint = [newPoint[0] + gradient[0] * alpha, newPoint[1] + gradient[1] * alpha]
        gradient = (dfdx(newPoint[0], newPoint[1]), dfdy(newPoint[0], newPoint[1]))

    if (abs(current[0]-newPoint[0])+abs(current[1]-newPoint[1])<0.1):
        save.append(newPoint)


#show
plt.scatter([ele[0] for ele in save],[ele[1] for ele in save])
plt.show()

#condense save
result=[]
while(len(save)!=0):
    result.append(save[0])
    for i in range(len(save)-1,-1,-1):
        if (abs(save[i][0]-result[-1][0])+abs(save[i][1]-result[-1][1])<0.0001):
            del save[i]

print (result)