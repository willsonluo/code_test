
X = 10
Y = 71
D = 20
S = ''

gap = Y-X 

def solution(X,Y,D):
    gap = Y-X
    if gap == 0:
        return 0
    elif gap <= D:
        return 1
    elif gap%D ==0:
        print(int(gap/D))
        return int(gap/D)
    else:
        print(gap//D+1)
        return (gap//D+1)
    
solution(X,Y,D)

