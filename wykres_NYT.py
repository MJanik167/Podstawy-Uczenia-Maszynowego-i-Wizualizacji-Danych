import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib as mpl

def sillyCurve(x):
    return(pow(1/4*x-8,2)/600) - 0.05

X = []
Y = range(1880,2018)

def generateData():
    for i in range(1,139):
        print()
        X.append(random.randrange(-200,200)/1000+sillyCurve(i))

generateData()

ax = plt.subplot()
ax.plot(Y,X,color="gray",marker=".")
ax.spines[["top","right","left","bottom"]].set_visible(False)
ax.tick_params(colors='gray',which="both")
plt.show()