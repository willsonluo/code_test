
from typing import final


A = [1,2,3,4,5]

def solution(A):
    if 1 not in A:
        # print(1)
        return 1
    elif 1 in A:
        A.sort()    
        runtime = 0    
        for i in range(len(A)-1):
            if A[i]+1 != A[i+1]:
                return A[i]+1
                runtime+=1
        if runtime == 0:
            return A[-1]+1
                

print(A)
solution([])
solution([1])
solution([2])
solution([3,2])
solution([1,2,3,5])
solution([1,2,3,4,5])