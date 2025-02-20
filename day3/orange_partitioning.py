def partition_array(m,low ,high):
    k = low
    pivot = m[high]  # Choose the last element as pivot
    
    for i in range(low,high):  # Exclude the pivot from iteration
        if m[i] < pivot:
            m[i], m[k] = m[k], m[i]
            k += 1  # Move partition index forward
            
    # Swap pivot to its correct position
    m[k], m[high] = m[high], m[k]
    
    print(m)  # Print the final partitioned array
    return m  # Return the partitioned list
    return k

def quicksort(m,low,high):
    if low < high:
        pivot_index = partition_array(m,low,high)

# Take user input
print('Enter input numbers:')
m = list(map(int, input().split()))
partition_array(m,0,)

#Orange_partitioning