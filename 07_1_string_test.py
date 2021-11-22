







def solution(A):
    BRACKET = {'}': '{', ')': '(', ']': '['}
    BRACKET_L, BRACKET_R = BRACKET.values(), BRACKET.keys()
    arr = []
    for c in A:
        if c in BRACKET_L:
            # 左括号入栈
            arr.append(c)
        elif c in BRACKET_R:
            # 右括号，要么栈顶元素出栈，要么匹配失败
            if arr and arr[-1] == BRACKET[c]:
                arr.pop()
            else:
                # print(0)
                return 0
    # print(1)
    return 1


A = "(U)"
B = "[U]"
C = "\{U\}"
D = "((()))((()))"


solution(A)
solution(B)
solution(C)
solution(D)




# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".