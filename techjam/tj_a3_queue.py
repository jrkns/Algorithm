# Greedy Algorithm giving wrong answer!!!!
# This solution is wrong!!!

def solution(A):
    A = sorted(A,reverse=1)
    q_A = []
    c_A = 0
    q_B = []
    c_B = 0
    for customer in A:
        if c_A < c_B:
            q_A.append(customer)
            c_A += int(customer)
        else:
            q_B.append(customer)
            c_B += int(customer)

    return max(c_A,c_B)


print(solution([3,3,1,2]))