import math

def solution(S,T):
    data = []
    answer = 0
    global_min = math.inf
    curr_min = 0

    for i in range(len(T)):
        data.append(ord(T[i]))

    for i in range(len(S)):
        for k in range(len(T)):
            curr_min = min(abs(data[k]-ord(S[i])), 26-abs(data[k]-ord(S[i])))

            if curr_min < global_min:
                global_min = curr_min

        answer += global_min
        global_min = math.inf

    return answer

  
t = int(input())
for i in range(1,t+1):
    temp = input().split()
    S = temp[0]
    temp = input().split()
    T = temp[0]
    res = solution(S,T)
    print("Case #{}: {}".format(i, res))


