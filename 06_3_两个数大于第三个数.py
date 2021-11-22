

def solution(A):
    if len(A) > 2 and len(A)%2 == 0:
        A.sort()
        mid = len(A)//2
        # print("mid:",mid)
        if A[mid-1] + A[mid] > A[mid+1]:
            print(1)
            return 1 
        else:
            print(0)
            return 0
    elif len(A) == 3:
        A.sort()
        if A[0] + A[1] > A[2]:
            print(1)
            return 1
        else:
            print(0)
            return 0
    elif len(A) > 4 and len(A)%2 == 1:
        A.sort()
        mid1 = len(A)//2
        result1 = A[mid1-1] + A[mid1] > A[mid1+1]
        mid2 = mid1+1
        result2 = A[mid2-1] + A[mid2] > A[mid2+1]
        if result1 or result2:
            print(1)
            return 1
        else:
            print(0)
            return 0
    else:
        print(0)
        return 0
        

solution([])
solution([1, 1, 1, 1, 5, 5, 5])
solution([5, 3, 3])
solution([1,1,1,1,1,1])
solution([10,2,5,1,8,20])
solution([10,50,5,1])






# 对于一个长度为 N 的整型数组, 如果存在三个元素 i,j,k i ≠ j ≠ k, 0 ≤ i,j,k < N) 满足如下条件:

# A[i] + A[j] > A[k],
# A[j] + A[k] > A[i],
# A[k] + A[i] > A[j].
# 实现如下一个函数:

# class Solution { public int solution(int[] A); }

# 则返回1, 否则返回0.

# 对于数组:

# A[0] = 10    A[1] = 2    A[2] = 5
# A[3] = 1     A[4] = 8    A[5] = 20
# 函数应该返回 1, 因为坐标为i=0, j=2, k=4的元素满足所有的判定条件(例如: A[2] + A[4] > A[0]). 对于数组:

# A[0] = 10    A[1] = 50    A[2] = 5
# A[3] = 1
# 函数应该返回 0.

# 假定:

# N 是 [0..100,000] 内的 整数;
# 数组 A 每个元素是取值范围 [−2,147,483,648..2,147,483,647] 内的 整数 .