import random
import timeit
import matplotlib.pyplot as plt
from solution import brute_force, calculate_prefix, calculate_kadane

hundred_list, thousand_list, ten_list, fifty_list = [], [], [], []
numberOf = [100, 1000, 5000, 10000]
functions = [brute_force, calculate_prefix, calculate_kadane]
host = list()
func = ""
result = ""
host.append(hundred_list)
host.append(thousand_list)
host.append(ten_list)
host.append(fifty_list)


def populate(range_val, a_list):
    for k in range(0, range_val):
        n = random.randint(-100, 100)
        a_list.append(n)


for i in range(0, len(numberOf)):
    populate(numberOf[i], host[i])
for j, f in enumerate(functions):
    time_passed = list()
    if j == 0:
        func = 'Brute Force Approach'
    elif j == 1:
        func = 'Prefix Approach'
    elif j == 2:
        func = 'Kadane Algorithm Approach'
    for i in range(0, len(host)):
        result = ""
        start = timeit.default_timer()
        result += func + " --> " + str(f(host[i]))
        stop = timeit.default_timer()
        res = round(stop - start, 6)
        result += " for time: " + str(res)
        print(result + '\n')
        time_passed.append(stop - start)
    plt.plot(numberOf, time_passed, label=func)

plt.xscale("log")
plt.yscale("log")

# label axis
plt.xlabel("n")
plt.ylabel("time")
plt.legend()
plt.show()
