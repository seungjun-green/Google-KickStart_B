def solution(N, D, C, M, S):
    for i in range(N):
        if (D == 0 and S[i] == 'D') or (C == 0 and S[i] == 'C' and 'D' in S[i+1:]):
            return "NO"
        else:
            if S[i] == 'D':
                D -= 1
                C += M
            else:
                C -= 1

    return "YES"


t = int(input())
for i in range(1, t + 1):
    temp = input().split()
    N, D, C, M = [int(j) for j in temp]
    temp = input().split()
    temp = temp[0]
    S = [c for c in temp]
    res = solution(N,D,C,M,S)
    print("Case #{}: {}".format(i, res))
