import numpy as np
import time
start_time = time.perf_counter()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def is_nearly_sorted(arr):
    inversions = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            inversions += 1
    return inversions <= len(arr) // 4


def get_best_sorting_algorithm(arr):
    n = len(arr)
    max_val = max(arr)
    unique_ratio = len(set(arr)) / len(arr)

    if n <= 10:
        return "Bubble Sort", bubble_sort

    if is_nearly_sorted(arr):
        return "Bubble Sort", bubble_sort

    if max_val < 100 and n > 10:
        return "Counting Sort", counting_sort

    if unique_ratio < 0.5:  # 很多重複元素
        return "Counting Sort", counting_sort

    return "Quick Sort", quick_sort


# 使用示例
if __name__ == "__main__":
    # 測試數列
    test_array = [3747, 4195, 1321, 7881, 1954, 3406, 90, 7456, 6807, 3527, 3478, 3123, 5850, 1002, 73, 416, 9239, 48, 5619, 3728, 9754, 8156, 2301, 216, 8412, 94, 13, 59, 5839, 5427]
    algo_name, sort_func = get_best_sorting_algorithm(test_array)
    sorted_array = sort_func(test_array.copy())
    print(f"Original array: {test_array}")
    print(f"Best algorithm: {algo_name}")
    print(f"Sorted array: {sorted_array}")
time_sorted = time.perf_counter() - start_time
print(f"Execution time: {time_sorted:.6f}seconds")
