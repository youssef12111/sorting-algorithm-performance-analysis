# Full Name: Youssef Hegazi Elseisi
# Student ID: G21152698


# Using with open() to open the file
# https://www.quora.com/Is-there-a-good-reason-to-not-open-files-in-a-with-statement-in-Python


import random
import time
import psutil
import sys



# Generate unique random data as lists
def generate_unique_random_data(size, lower_bound, upper_bound):
    if upper_bound - lower_bound + 1 < size:
        raise ValueError("Range is too small to generate unique values.")
    return random.sample(range(lower_bound, upper_bound + 1), size)



# Dataset 1: Unique random data
random_data_10_000 = generate_unique_random_data(10_000, 100_000, 1_000_000)
random_data_100_000 = generate_unique_random_data(100_000, 100_000, 1_000_000)

# Dataset 2: Reversed unique data
reversed_data_10_000  =  sorted(random_data_10_000, reverse = True)
reversed_data_100_000 = sorted(random_data_100_000, reverse = True)



# Merge sort: returns sorted array and swap count.
def merge_sort(arr):
    n = len(arr)
    temp_arr = [0] * n
    swaps = count_swaps_in_merge_sort(arr, temp_arr, 0, n - 1)
    return arr, swaps




# Merges two sorted subarrays and counts swaps needed to sort them.
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    
    j = mid + 1
    k = left    
    swaps = 0

    # Merge the two subarrays into temp_arr
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            swaps += (mid - i + 1)  # Count swaps
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return swaps



# Counts swaps needed to sort the array using merge sort.
def count_swaps_in_merge_sort(arr, temp_arr, left, right):
    swaps = 0
    if left < right:
        mid = (left + right) // 2

        swaps += count_swaps_in_merge_sort(arr, temp_arr, left, mid)
        swaps += count_swaps_in_merge_sort(arr, temp_arr, mid + 1, right)
        swaps += merge_and_count(arr, temp_arr, left, mid, right)

    return swaps




# Performs quick sort and returns the sorted array with the swap count.
def quick_sort(arr):
    global swap_count  
    swap_count = 0
    arr_copy = arr.copy()
    quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy, swap_count




# Seperate the array into partitions 
def partition(array, low, high):
    global swap_count # Global Variable
    pivot_index = random.randint(low, high)  # Random pivot selection
    array[pivot_index], array[high] = array[high], array[pivot_index]  # Swap pivot to end
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            swap_count += 1

    array[i + 1], array[high] = array[high], array[i + 1]
    swap_count += 1
    return i + 1




# Recursively sorts the array using quick sort with tail call optimization.
def quick_sort_recursive(array, low, high):
    while low < high:
        pi = partition(array, low, high)

        # Tail call optimization
        if pi - low < high - pi:
            quick_sort_recursive(array, low, pi - 1)
            low = pi + 1
        else:
            quick_sort_recursive(array, pi + 1, high)
            high = pi - 1



# Adjust recursion limit for large datasets
sys.setrecursionlimit(2000)




# Appends a title and data string to a specified file.
def write_on_file(file_name, data, title):
    with open(file_name, 'a') as file:
        file.write(title + '\n')
        if isinstance(data, list):
            file.write(" ".join(map(str, data)) + '\n')
        else:
            file.write(f"{data}\n")




# Returns the current memory usage of the process in kilobytes (KB).
def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024  # in KB




# Tracks and logs the performance (execution time, memory usage, and swaps) of a sorting algorithm.
def track_sorting_performance(dataset, algorithm, title):
    try:
        start_time = time.time()
        memory_before = memory_usage()
        array, total_swaps = algorithm(dataset)
        end_time = time.time()
        memory_after = memory_usage()

        execution_time = (end_time - start_time) * 1000
        memory_used = memory_after - memory_before

        write_on_file("sorting_algorithim_number_of_comparisons.txt", total_swaps, f"{title}_number_of_comparisons")
        write_on_file("sorting_algorithim_execution_time.txt", execution_time, f"{title}_execution_time")
        write_on_file("sorting_algorithim_memory_usage.txt", f"{memory_used:.2f} KB", f"{title}_memory_usage")
        write_on_file(f"{title}.txt", array, title)
    except Exception as e:
        write_on_file("error_log.txt", str(e), f"Error in {title}")



# Track performance for all datasets
track_sorting_performance(random_data_10_000, merge_sort, "random_merge_sort_array_10k")
track_sorting_performance(random_data_100_000, merge_sort, "random_merge_sort_array_100k")
track_sorting_performance(reversed_data_10_000, merge_sort, "reversed_merge_sort_array_10k")
track_sorting_performance(reversed_data_100_000, merge_sort, "reversed_merge_sort_array_100k")
track_sorting_performance(random_data_10_000, quick_sort, "random_quick_sort_array_10k")
track_sorting_performance(random_data_100_000, quick_sort, "random_quick_sort_array_100k")
track_sorting_performance(reversed_data_10_000, quick_sort, "reversed_quick_sort_array_10k")
track_sorting_performance(reversed_data_100_000, quick_sort, "reversed_quick_sort_array_100k")





















