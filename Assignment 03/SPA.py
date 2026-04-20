import random
import time
import sys

# Increase recursion limit
sys.setrecursionlimit(20000)

# ------------------ Sorting Algorithms ------------------

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merge Sort
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


# Quick Sort with RANDOM PIVOT
def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ------------------ Timing Function ------------------

def measure_time(sort_func, arr):
    temp = arr.copy()
    start = time.time()

    try:
        sort_func(temp)
    except TypeError:
        sort_func(temp, 0, len(temp) - 1)

    end = time.time()
    return (end - start) * 1000  # milliseconds


# ------------------ Dataset Generator ------------------

def generate_datasets(size):
    random.seed(42)

    random_list = [random.randint(1, 100000) for _ in range(size)]
    sorted_list = list(range(size))
    reverse_list = list(range(size, 0, -1))

    return random_list, sorted_list, reverse_list


# ------------------ Main Function ------------------

def main():
    sizes = [1000, 5000, 10000]

    print("Correctness Check:")
    test = [5, 2, 9, 1, 5, 6]

    temp = test.copy()
    insertion_sort(temp)
    print("Insertion Sort:", temp)

    temp = test.copy()
    merge_sort(temp)
    print("Merge Sort:", temp)

    temp = test.copy()
    quick_sort(temp, 0, len(temp) - 1)
    print("Quick Sort:", temp)

    print("\nPerformance Results (in ms):\n")

    for size in sizes:
        print(f"----- Size: {size} -----")
        random_list, sorted_list, reverse_list = generate_datasets(size)

        for name, dataset in [("Random", random_list),
                              ("Sorted", sorted_list),
                              ("Reverse", reverse_list)]:

            print(f"\n{name} Data:")

            t1 = measure_time(insertion_sort, dataset)
            t2 = measure_time(merge_sort, dataset)
            t3 = measure_time(quick_sort, dataset)

            print(f"Insertion Sort: {t1:.2f} ms")
            print(f"Merge Sort: {t2:.2f} ms")
            print(f"Quick Sort: {t3:.2f} ms")

        print()


if __name__ == "__main__":
    main()