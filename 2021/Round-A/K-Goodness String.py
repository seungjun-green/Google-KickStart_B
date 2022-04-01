class Solution:
    def kGoodnessString(self, N, K, S):
        curr = 0
        for i in range(0, N//2):
            if (S[i] != S[N-i-1]):
                curr+=1

        return abs(K-curr)

t = int(input())
for i in range(1,t+1):
    N, K = input().split()
    S = input()
    res = Solution().kGoodnessString(int(N), int(K), S)
    print(f"Case #{i}: {res}")
