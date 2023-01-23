import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import random

def piSim():
    #n is number of simulations
    #the imaginary area range is 20 units wide and 10 units tall
    #the square is 2x2 units and its center is at (5, 5)
    #the circle has a radius of 2 unit and its center is at (15,5)
    cPlot = []
    n = 1000
    squareCount = 0
    circleCount = 0
    history = []
    #current ratio is y and x in number of sims
    t = 0
    ratio = []

    #these are the radnomly generated plots
    while n != t:
        cPlot = [random.random() * 20, random.random() * 10]
        history.append(cPlot)

        #check if random plot is in sqaure
        if (7 > cPlot[0] > 3) and (7 > cPlot[1] > 3):
            squareCount += 1

        #check if random plot is in circle
        elif ( pow(cPlot[0] - 15,2) + pow(cPlot[1] - 5,2) < 16):
            circleCount += 1

        t += 1

        if squareCount != 0:
            ratio.append(circleCount/squareCount)


    return [history,ratio, circleCount, squareCount]

run = piSim()

plots1 = run[0]
plots2 = run[1]
circleCount = run[2]
squareCount = run[3]

plt.subplot(2, 1, 1)
plt.scatter(*zip(*plots1), .25, 'black')
plt.xlabel("X Units")
plt.ylabel("Y Units")
plt.title("Monte Carlo Pi Plots")
circle = Circle((15,5),4, fill=False)
plt.gca().add_patch(circle)
rect = Rectangle((3,3), 4, 4, fill=False)
plt.gca().add_patch(rect)
width = 700
height = 700
plt.axis('equal')
plt.axis([0, 20, 0, 10])


plt.subplot(2, 1, 2)
plt.plot(plots2, 'black')
plt.xlabel("Simulations")
plt.ylabel("Circle to Square Ratio")
plt.title("Monte Carlo Pi Ratio")

plt.show()