class Solution:
    def findSmllestOne(self,N):
        given_sum = 0

        for n in N:
            given_sum+=int(n)


        new_digit = 0

        for i in range(0,10):
            curr = i+given_sum
            if curr%9==0:
                new_digit = i
                break


        if new_digit == 0:
            return (N[:1] + '0' + N[1:])

        for i in range(len(N)):
            if new_digit < int(N[i]):
                print(N[i])
                return (N[:i] + str(new_digit) + N[i:])
            else:
                pass



        return (N+str(new_digit))


t = int(input())
for i in range(t):
    N = input()
    res = Solution().findSmllestOne(N)
    print(f"Case #{i+1}: {res}")
