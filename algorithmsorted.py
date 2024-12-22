import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def fastest_sort(arr):
    start_time = time.perf_counter()  # 計時開始
    sorted_array = sorted(arr)  # 用高度優化過的內建sorting
    end_time = time.perf_counter()  # 計時結束

    print(f"Sorting time: {end_time - start_time:.6f} seconds")
    return sorted_array


nums = ['777', '771', '117', '177', '111', '777', '717', '771', '117', '771']
print("Original array:", nums)
sorted_nums = fastest_sort(nums)
print("Sorted array:", sorted_nums)
