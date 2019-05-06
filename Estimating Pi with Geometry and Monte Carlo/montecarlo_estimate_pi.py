import random
import time
import math
import pandas as pd
import matplotlib.pyplot as plt

## This function estimates the value of pi using a circle inscribed
## in a square (A=1 sq. unit).  
def montecarlo2d(num_simulations):
    num_cir = 0
    for i in range(num_simulations):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            num_cir += 1
    return 4 * (num_cir / num_simulations)

## This function estimates the value of pi using a sphere inscribed
## in a cube (A=1 cubed unit)
def montecarlo3d(num_simulations):
    num_sph = 0
    for i in range(num_simulations):
        x = random.random()
        y = random.random()
        z = random.random()
        if x**2 + y**2 + z**2 <= 1:
            num_sph += 1
    return 6 * (num_sph / num_simulations)

## This function estimates the value of pi using a n-sphere in 4D
## inscribed in a 4D hypercube (or tesseract). (A=1 unit^4)
def montecarlo4d(num_simulations):
    num_nsphere = 0
    for i in range(num_simulations):
        x1 = random.random()
        x2 = random.random()
        x3 = random.random()
        x4 = random.random()
        if (x1)**2 + (x2)**2 + (x3)**2 + (x4)**2 <= 1:
            num_nsphere += 1
    return math.sqrt(32 * (num_nsphere/num_simulations))

##Set test values to measure run-time
num_sim_list = [1000000,5000000,10000000]
df = pd.DataFrame()
df['num_sims'] = num_sim_list

##Measure the run-times of each function over various num_simulations
def measure_runtime(function_name):
    times = []
    for elem in num_sim_list:
        start = time.time()
        function_name(elem)
        end = time.time()
        times.append(end-start)
    return times

## Run measure_runtime() for each function and store data in a dataframe
## this function is called in plot_data()
functions = [montecarlo2d,montecarlo3d,montecarlo4d]
def collect_data():
    counter = 2
    for elem in functions:
        df[str(counter) + 'D'] = measure_runtime(elem)
        counter += 1
    return df

## Plot data from dataframe to compare runtimes
def plot_data():
    collect_data()
    plt.plot(df['num_sims'], df['2D'], label = '2D')
    plt.plot(df['num_sims'], df['3D'], label = '3D')
    plt.plot(df['num_sims'], df['4D'], label = '4D')
    plt.xlabel('# of simulations')
    plt.ylabel('run time (sec)')
    plt.legend(loc='upper left')
    plt.show()
