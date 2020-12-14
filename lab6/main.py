import time
import plotly.express as px
import random


def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        flag = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                flag = True
        if not flag:
            break
    return arr


def bose_nelson(data):
    m = 1
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(data, j, m, m)
            j = j + m + m
        m = m + m
    return data


def bose_nelson_merge(data, j, r, m):
    if j + r < len(data):
        if m == 1:
            if data[j] > data[j + r]:
                data[j], data[j + r] = data[j + r], data[j]
        else:
            m = m // 2
            bose_nelson_merge(data, j, r, m)
            if j + r + m < len(data):
                bose_nelson_merge(data, j + m, r, m)
            bose_nelson_merge(data, j + m, r - m, m)
    return data


def experimental_evaluation_data_bubble(repetitions: int):
    chart_data = []
    for i in range(repetitions):
        current_volume = 1000 + i * 1000
        current_array = [random.randint(0, current_volume) for _ in range(current_volume)]
        start_time = time.time()
        for _ in range(1000):
            bubble_sort(current_array)
        duration = time.time() - start_time
        chart_data.append(dict(size=current_volume, time=duration))
    return chart_data


def experimental_evaluation_data_bose_nelson(repetitions: int):
    chart_data = []
    for i in range(repetitions):
        current_volume = 1000 + i * 1000
        current_array = [random.randint(0, current_volume) for _ in range(current_volume)]
        start_time = time.time()
        for _ in range(1):
            bose_nelson(current_array)
        duration = time.time() - start_time
        chart_data.append(dict(size=current_volume, time=duration))
    return chart_data


def draw_chart(chart_data):
    chart_data.sort(key=lambda d: d['size'])
    print(chart_data)
    fig = px.line(chart_data, x="size", y="time")
    fig.show()


draw_chart(experimental_evaluation_data_bubble(10))
