class Solution:

    def checkSubSequence(self, I,P):
        ptr_i=ptr_p=0

        while ptr_i < len(I) and ptr_p < len(P):
            if I[ptr_i] == P[ptr_p]:
                ptr_i+=1
                ptr_p+=1
            else:
                ptr_p+=1

        if ptr_i==len(I):
            return True
        else:
            return False

    def lettersToDelete(self, I, P):
        if self.checkSubSequence(I,P) == False:
            return "IMPOSSIBLE"
        else:
            return len(P)-len(I)


t = int(input())
for i in range(t):
    I = input()
    P = input()
    res = Solution().lettersToDelete(I, P)
    print(f"Case #{i + 1}: {res}")

