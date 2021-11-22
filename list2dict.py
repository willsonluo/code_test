# A = ['a','f','c']
# dictA = {}

# for key in A:
#     dictA[key] =dictA.get(key,0)+1
    
# print('a' in dictA.keys())



def counting(m,A):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    print(count)
    return count

counting(5, [1, 3, 1, 4, 2, 3, 4,3,5,4])