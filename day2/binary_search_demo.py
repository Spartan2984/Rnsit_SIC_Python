import sys
import binary_search

print(f'The input numbers are \n {sys.argv[1:-1]}')
print('The search element is {sys.argv[-1]}')

search_element_index = binary_search.binary_search(sys.argv[1:-1], sys.argv[-1])
if search_element_index == -1:
    print()