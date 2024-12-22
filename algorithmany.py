import time
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def fastest_sort(arr):
    start_total_time = time.perf_counter()  # 记录总耗时起点

    methods = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Python Built-in Sort": sorted
    }

    times = {}
    for method_name, method in methods.items():
        start_time = time.perf_counter()
        # 排序操作
        method(arr.copy())
        end_time = time.perf_counter()
        times[method_name] = end_time - start_time

    # 找到最快的方法
    fastest_method = min(times, key=times.get)
    print(f"Fastest method: {fastest_method}")

    # 使用最快的方法对原数组排序
    sorted_array = methods[fastest_method](arr)

    end_total_time = time.perf_counter()  # 记录总耗时终点
    print(f"Total time (judging + sorting): {end_total_time - start_total_time:.6f} seconds")

    return sorted_array


# 示例數據
nums =   # 生成30个随机数
print("Original array:", nums)
sorted_nums = fastest_sort(nums)
print("Sorted array:", sorted_nums)
