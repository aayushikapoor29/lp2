def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume the current index is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # Greedy choice: pick smaller element
                min_idx = j
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:  ", sorted_arr)
