class Solution:
    def findSmllestOne(self,N):


        # getting the new_number
        curr_sum = 0
        for n in N:
            curr_sum+=int(n)

        new_number = 0
        for i in range(0,10):
            curr = i+curr_sum
            if curr%9==0:
                new_digit = i
                break

        # inserting new number at right place

        # if new_number is 0, insert 0 right before the most significant digit.
        if new_number == 0:
            return (N[:1] + '0' + N[1:])

        # iterating the N from the most significant digit, found the first digit that is bigger than new_numebr
        # then insert the new_number right before it.
        for i in range(len(N)):
            if new_number < int(N[i]):
                return (N[:i] + str(new_number) + N[i:])
            else:
                pass

        # if all digits in N is smaller than new_number, then insert the new number right before most significant digit.
        return (N+str(new_number))


t = int(input())
for i in range(t):
    N = input()
    res = Solution().findSmllestOne(N)
    print(f"Case #{i+1}: {res}")
