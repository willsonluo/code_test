
def solution(A):
    if len(A) > 1:
        flag = 2
        max_flag = 2
        B = []
        B.append(A[0])
        B.append(A[1])
        for i in range(2,len(A)):
            if A[i] in B:
                flag+=1
                max_flag+=1
            else:
                B.pop(0)
                B.append(A[i])
                flag = 2
        # print(B)
        print(max(max_flag,flag))
        return max(max_flag,flag)
    else: 
        print(0)
        return 0
    
solution([4,2,2,4,2])
solution([1,2,3,2])
solution([0,5,4,4,5,12])
solution([4,4])
solution([0,0,0,9,8,0,0,0])
