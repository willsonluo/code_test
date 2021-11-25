
def solution(A):
    if len(A) > 1:
        B = list(set(A))
        # print(A)
        # print(B)
        result = []
        for i in range(len(B)-1):
            if B[i] + 2 == B[i+1]:
                # print("item:",B[i],B[i+1])
                idx_a = A.index(B[i])
                idx_b = A.index(B[i+1])
                # print("index:",idx_a,idx_b)
                result.append(abs(idx_b-idx_a))                
        if len(result) != 0:      
            print(max(result))
            return max(result)     
        else:
            print(-1)
            return -1 
    else:
        print(-1)
        return -1

solution([0,0,0,0,0,0,0,0,1,2])
solution([0,0,0,0,0,0,0,0])
solution([0,3,3,7,5,3,11,1])
solution([1,4,7,3,3,5])