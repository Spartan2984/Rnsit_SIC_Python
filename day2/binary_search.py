def binarysearch(array,search_element):
    high=len(array)-1
    low=0
    while low<=high:
        mid=(high+low)//2
        if array[mid]==search_element:
            return mid
        elif array[mid]>search_element:
            high=mid-1
        else:
            low=mid+1

