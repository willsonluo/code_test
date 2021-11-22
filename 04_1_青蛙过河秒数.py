import profile
# X = 5
# A = [1,3,1,4,5,3,2,1]
def solution(X, A):
    temp_max = 0
    dictA = {}
    dict_key = []
    if len(A) > 0 and X > 0:
        if X ==1 and 1 in A:
            # print(0)
            return 0
        else:
            for key in A:
                dictA[key] =dictA.get(key,0)+1
                # dict_key = list(dictA.keys())
            for a1 in range(X):
                if a1+1 in dictA.keys():
                    if temp_max < A.index(a1+1):
                        temp_max = A.index(a1+1)
                    # temp_list1.append(temp_index)
                else:
                    # print(-1)
                    return -1
            if temp_max > X:
                # print(temp_max)
                return temp_max
            

profile.run('solution(5, [1, 3, 1, 4, 2, 3, 4,3,5,4])')
# solution(2,[2, 2, 2, 2, 2])
# solution(1,[1])
# solution(3, [1, 3, 1, 3, 2, 1, 3])
# For example, for the input (1, [1]) the solution returned a wrong answer (got -1 expected 0).