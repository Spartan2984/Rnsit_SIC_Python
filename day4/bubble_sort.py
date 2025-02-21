def bubble_sort(array):
    for i in range (len(array)-1):
        for j in range (len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def optimized_bubble_sort(array):
    for i in range(len(array)-1):
        sorted=True
        for j in range (len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                sorted=False
        if sorted:
            return
        