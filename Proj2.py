import math
import random

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


def hill_climb(function_to_optimize,step_size, xmin, xmax, ymin, ymax):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-2.5, 2.5,0.1)
    Y = np.arange(-2.5, 2.5, 0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(X**2 + 3*Y**2)/ (0.1 + R**2) + (X**2+5*Y**2)*np.exp(1-R**2)/2
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.set_zlim(-5,5)
    flag = True
    #print(step_size)
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)
    best_intial = function_to_optimize(x,y)
    xPath = []
    yPath = []
    zPath = []
    xPath.append(x)
    yPath.append(y)
    zPath.append(function_to_optimize(x,y))

    #print(x)
    #print("1111")
    while flag == True:
        #print("333")
        temp = random.choice([True, False])
        if temp == True:
            x1 = x+step_size
        else:
            x1 = x - step_size
        if temp == True:
            y1 = y + step_size
        else:
            y1 = y - step_size
        bestNext = function_to_optimize(x1, y1)
        if bestNext < best_intial:
            best_intial = bestNext
            x = x1
            y = y1
            xPath.append(x)
            yPath.append(y)
            zPath.append(best_intial)
        else:
            flag = False

    print("x and y coordinate")
    print(x)
    print(y)
    print("hill climb best result")
    print(function_to_optimize(x,y))
    ax.plot(xPath, yPath, zPath, label = 'path')
    plt.show()

    return function_to_optimize

def function_to_optimize(x , y):
    r = math.sqrt(x*x+ y*y)

    part1 = math.sin(x*x+3*y*y)/(0.1+r*r)
    part3 = (math.exp(1-r**2))/2
    part2 = x**2+5*y**2
    z = part1+ part2*part3
    return z

def hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-2.5, 2.5,0.1)
    Y = np.arange(-2.5, 2.5,0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(X**2 + 3*Y**2)/ (0.1 + R**2) + (X**2+5*Y**2)*np.exp(1-R**2)/2
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.set_zlim(-5,5)
    #print(step_size)
    temp = 0
    list = []
    xPath = []
    yPath = []
    zPath = []
    flag = True
    while num_restarts> 0:
        x = random.uniform(xmin,xmax)
        y = random.uniform(ymin,ymax)
        best_inital = function_to_optimize(x,y)
        xPath.append(x)
        yPath.append(y)
        zPath.append(function_to_optimize(x,y))


        while flag == True :
            temp = random.choice([True, False])
            if temp == True:
                x1 = x+step_size
            else:
                x1 = x - step_size
            if temp == True:
                y1 = y + step_size
            else:
                y1 = y - step_size
            bestNext = function_to_optimize(x1, y1)
            if bestNext < best_inital:
                best_intial = bestNext
                x = x1
                y = y1
                xPath.append(x)
                yPath.append(y)
                zPath.append(best_intial)
            else:
                flag = False
        list.append(best_inital)
        #if smaller > best_inital:
            #smaller = best_inital
        num_restarts = num_restarts-1
    #print(list)
    #print(min(list))
    #print(smaller)
    print("hill climb random restart best: ")
    print(min(list))
    ax.plot(xPath, yPath, zPath, label = 'path')
    plt.show()

    return (min(list))

def simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-2.5, 2.5,0.1)
    Y = np.arange(-2.5, 2.5,0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(X**2 + 3*Y**2)/ (0.1 + R**2) + (X**2+5*Y**2)*np.exp(1-R**2)/2
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap= cm.coolwarm ,
                       linewidth=0, antialiased=False)
    ax.set_zlim(-5,5)

    x = random.uniform(xmin,xmax)
    y = random.uniform(ymin,ymax)
    #use delta to update temparture
    delta = 0.99
    inital_best = function_to_optimize(x,y)
    xPath = list()
    yPath = list()
    zPath = list()
    xPath.append(x)
    yPath.append(y)
    zPath.append(inital_best)
    result = inital_best
    while(max_temp > 2.5):
        #next move
        temp = random.choice([True, False])
        if temp == True:
            x1 = x+step_size
        else:
            x1 = x - step_size
        if temp == True:
            y1 = y + step_size
        else:
            y1 = y - step_size
        nextPoint = function_to_optimize(x1,y1)
        detF = (nextPoint - result)
        equation = math.exp(-detF/max_temp)
        #after move if you get smaller result, always move
        # nextPoint - result
        if(detF >=0 ):
            x = x1
            y = y1
            result = nextPoint
            xPath.append(x)
            yPath.append(y)
            zPath.append(nextPoint)
        else:
            if (equation > random.uniform(0 , 1)):
                result = nextPoint
                x = x1
                y = y1
                xPath.append(x)
                yPath.append(y)
                zPath.append(result)
        max_temp = max_temp*delta

    print("x and y as coordinate: ")
    print(x)
    print(y)
    print("simulated_annealing: ")
    print(result)
    ax.plot(xPath, yPath, zPath, label = 'path')
    plt.show()

    return x,y


xmin = -2.5
xmax = 2.5
ymin = -2.5
ymax = 2.5
step_size = 0.1
x = 1
y= 1
num_restarts = 5
max_temp = 25000000
function_to_optimize(x , y)
hill_climb(function_to_optimize,step_size,xmin, xmax,ymin,ymax)
hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax)
simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax)




