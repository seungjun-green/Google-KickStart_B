def countAR(R1,R2,R3, val):
    # remaking the R2
    temp = R2[1]
    R2[1] = val
    R2.append(temp)


    # Generating rows to be checked
    R4 = [R1[0], R2[0], R3[0]]
    R5 = [R1[1], R2[1], R3[1]]
    R6 = [R1[2], R2[2], R3[2]]

    R7 = [R1[0], R2[1], R3[2]]
    R8 = [R1[2], R2[1], R3[0]]

    count = 0

    dataSet = [R1,R2,R3,R4,R5,R6,R7,R8]
    
    # check all possible 8 rows
    for row in dataSet:
        if check(row):
            count += 1

    return count


def check(dataSet):
    if (dataSet[1] - dataSet[0]) == (dataSet[2] - dataSet[1]):
        return True
    else:
        return False



def solution(R1,R2,R3):

    current_count = 0
    global_max = 0

    possible = [(R1[0]+R3[2])//2,(R1[2]+R3[0])//2,(R2[0]+R2[1])//2,(R1[1]+R3[1])//2]


    # Iterating all possible mat[1][1], check number of Arithmetic rows,
    # keep updating global_max, and after iteration ended, return the global_max
    for i in possible:
        current_count = countAR(R1,R2.copy(),R3,i)

        if current_count > global_max:
            global_max = current_count


    return global_max


t = int(input())
for i in range(1, t+1):
    temp = input().split()
    R1 = [int (j) for j in temp]
    temp = input().split()
    R2 = [int(j) for j in temp]
    temp = input().split()
    R3 = [int(j) for j in temp]
    res = solution(R1,R2,R3)
    print("Case #{}: {}" .format(i, res))
