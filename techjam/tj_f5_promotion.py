def min_cost(list,day,cost):
    mem = [[0 for x in range(len(list))] for y in range(len(list))]
    for i in range(len(list)):
        for j in range(len(day)):
            prev_index = find_prev(list,i,day,j)
            if prev_index >= 0:
                prev_cost = mem[prev_index][len(day)-1]
            else:
                prev_cost = 0
            current_cost = prev_cost+cost[j]
            if j-1 >= 0:
                current_cost = min(current_cost,mem[i][j-1])
            mem[i][j] = current_cost
    return mem[len(list)-1][len(day)-1]

def find_prev(list,i,day,j):
    cover_to = list[i] - day[j]
    if cover_to < 1:
        return -1
    for k in range (i-1,-1,-1):
        if list[k]<=cover_to:
            return k
    return -1

def main():
    day = [1, 7, 30]
    cost = [2, 7, 25]
    print(min_cost([1,2,3,5,7,21,30,31],day,cost))
    return

if __name__ == '__main__':
    main()
