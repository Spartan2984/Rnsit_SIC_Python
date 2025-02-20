def merge_sort(numbers, low, high):
    if low < high:
        mid = (low + high) // 2  # Corrected midpoint calculation
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid + 1, high)
        merge(numbers, low, mid, high)

def merge(numbers, low, mid, high):
    array1 = numbers[low:mid+1]  # Left half includes mid
    array2 = numbers[mid+1:high+1]  # Right half starts from mid+1
    
    i, j, k = 0, 0, low  # Use k to track the index in numbers[]
    
    # Merge two subarrays into the original array
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            numbers[k] = array1[i]
            i += 1
        else:
            numbers[k] = array2[j]
            j += 1
        k += 1

    # Copy any remaining elements
    while i < len(array1):
        numbers[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        numbers[k] = array2[j]
        j += 1
        k += 1

# Test the function
arr = [2, 3, 4, 5, 6, 7, 8]
merge_sort(arr, 0, len(arr) - 1)
print(arr)  # Should print sorted array
