def solution(S):
    ans = ""

    for i in range(len(S)):
        count = 1
        res = ''
        for j in range(i, -1, -1):
            if j == 0:
                break
            elif ord(S[j]) > ord(S[j-1]):
                count += 1
            else:
                break

        ans += str(count)
        ans += " "

    return ans


t = int(input())

for i in range(1, t + 1):
    temp = input().split()
    N = [int(j) for j in temp]
    temp = input().split()
    temp = temp[0]
    S = [c for c in temp]
    res = solution(S)
    print("Case #{}: {}".format(i, res))
