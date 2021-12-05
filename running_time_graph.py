import matplotlib.pyplot as plt
import math
import timeit
from scipy.special import comb

#constant in file
EXECUTION_NUM = 10
LOOP_NUM = 1
STEP = 1

def func1():
    #describe arbitrary processing
    for _ in range(10**3):
        print("func1")

def func2():
    #describe arbitrary processing
    for _ in range(10**2):
        print("func2")

def func3():
    #describe arbitrary processing
    for _ in range(10**1):
        print("func3")

time_func1 = []
time_func2 = []
time_func3 = []

arithmeticProgression_list = [x for x in range(0, LOOP_NUM, STEP)]
for r in arithmeticProgression_list:
    #function1
    result = timeit.timeit("func1()", number = EXECUTION_NUM, globals=globals())
    time_func1.append(result/EXECUTION_NUM)

    #function2
    result = timeit.timeit("func2()", number = EXECUTION_NUM, globals=globals())
    time_func2.append(result/EXECUTION_NUM)

    #function3
    result = timeit.timeit("func3()", number = EXECUTION_NUM, globals=globals())
    time_func3.append(result/EXECUTION_NUM)

plt.plot(arithmeticProgression_list, time_func1, marker="o", color="r", linestyle="-", label="func1")
plt.plot(arithmeticProgression_list, time_func2, marker="o", color="g", linestyle="-", label="func2")
plt.plot(arithmeticProgression_list, time_func3, marker="o", color="b", linestyle="-", label="func3")

plt.xlabel("r", fontsize=18)
plt.ylabel("time(sec)[log]", fontsize=18)
plt.legend(loc="upper left")
plt.yscale("log")
plt.show()