def solution(N, K, S):
    target = K
    currentPoint = 0

    for i in range(0, N//2):
        if S[i] != S[N-1-i]:
            currentPoint += 1
        else:
            pass


    if currentPoint == K:
        return 0
    else:
        return abs(currentPoint-target)

      
t = int(input())
for i in range(1, t+1):
    temp = input().split()
    N, K = [int(j) for j in temp]
    temp = input().split()
    temp = temp[0]
    S = [c for c in temp]
    res = solution(N, K, S)
    print("Case #{}: {}".format(i, res))

