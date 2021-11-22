
A = [9,3,9,7,9,7,3]
def solution(A):
    if len(A)>0:
        dictA = {}
        for key in A:
            dictA[key] =dictA.get(key,0)+1
        print(dictA)
        for key,value in dictA.items():
            if value%2 == 1:
                print(int(key))
                return int(key)
            

# def solution(A):
#     if len(A) > 0:
#         A1 = list(set(A))
#         for i in range(len(A1)):
#             if A.count(A1[i]) == 1:
#                 print(A1[i])
#                 return(A1[i])

solution(A)
    
    





# 给定一个非空数组 A，包含有 N 个整数，起始下标为 0。数组包含有奇数个元素，其中除了唯一一个元素之外，其他每个元素都可以与数组中另一个有相同值的元素配对。

# 比如，在下面这个数组中：

# A[0] = 9  A[1] = 3  A[2] = 9
# A[3] = 3  A[4] = 9  A[5] = 7
# A[6] = 9 
# 下标为 0 和 2 的元素的值是 9
# 下标为 1 和 3 的元素的值是 3
# 下标为 4 和 6 的元素的值是 9
# 下标为 5 的元素的值是 7，无法配对
# 写一个函数：

# def solution(A)

# 对满足上述条件的数组 A，返回数组中无法配对的元素的值。

# 比如，给定以下数组：

# A[0] = 9  A[1] = 3  A[2] = 9
# A[3] = 3  A[4] = 9  A[5] = 7
# A[6] = 9 
# 函数应该返回 7，如上述解释。

# 假定:

# N is an odd integer within the range [1..1,000,000];
# 数组 A 每个元素是取值范围 [1..1,000,000,000] 内的 整数 ;
# all but one of the values in A occur an even number of times.