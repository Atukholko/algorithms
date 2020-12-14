import random
import time
import matplotlib.pyplot as plt


def find_quantity_of_even_and_odd_numbers(arr, n_):
    quantity_of_even, quantity_of_odd = 0, 0
    for num in arr:
        if num % 2 == 0:
            quantity_of_even += 1
    return quantity_of_even, n_ - quantity_of_even


number_of_repetitions = 5
number_of_executions = 10
input_data_size = list()
execution_time = list()
for i in range(number_of_repetitions):
    print("Enter n:")
    n = int(input())
    input_data_size.append(str(n))
    array = [random.randint(-10000, 10000) for i in range(n)]
    start_time = time.time()
    for _ in range(number_of_executions):
        find_quantity_of_even_and_odd_numbers(array, n)
    duration = time.time() - start_time
    execution_time.append(duration)
    print(i, ") Execution time =", duration)


fig, ax = plt.subplots()
ax.bar(input_data_size, execution_time)
ax.set_xlabel("input data size")
ax.set_ylabel("execution time")
fig.savefig("graph.png")
plt.show()
