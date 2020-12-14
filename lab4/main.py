import random
import time
import pandas
import plotly.express as px


n = 5
initial_data = [random.randint(0, 100) for i in range(n)]
initial_data.sort()


def interpolation_search(arr, search_argument):

    low = 0
    high = len(arr) - 1

    while arr[low] <= search_argument <= arr[high]:
        mid = int(low + (search_argument - arr[low]) / (arr[high] - arr[low]) * (high - low))
        if arr[mid] == search_argument:
            return mid
        elif arr[mid] > search_argument:
            high = mid - 1
        elif arr[mid] < search_argument:
            low = mid + 1
        else:
            return -1
    return -1


input_data_size = []
execution_time = []
chart_data = []


def interpolation_search_processing():
    search_argument = 23
    n = 0
    for i in range(5):
        n = n + 1000000
        initial_data = [random.randint(0, 100) for i in range(n)]
        initial_data.sort()

        if search_argument >= 0:

            start_time = time.time()
            for i in range(100):
                interpolation_search(initial_data, random.randint(0, 99))
            duration = time.time() - start_time
            #num = interpolation_search(initial_data, random.randint(0, 99))
            chart_data.append(dict(size=n, time=duration))
            # if num >= 0:
            #     print(initial_data[num])
            # else:
            #     print("No such element")


interpolation_search_processing()

fig = px.line(chart_data, x="size", y="time")
fig.show()
# fig, ax = plt.subplots()
# ax.line(input_data_size, execution_time)
# ax.set_xlabel("input data size")
# ax.set_ylabel("execution time")
# fig.savefig("chart.png")
# plt.show()
