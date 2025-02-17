from math import sqrt

N = int(input())
root = int(sqrt(N)) 

if root * root == N:
    print('N is a perfect square')
else:
    print('N is not a perfect square')
