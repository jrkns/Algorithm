# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def bfs(level,graph, root):
    visited, queue = [], [root]
    k = 0
    last = root
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            level[w] = min(level[w],k)
            if w not in visited:
                visited.append(w)
                queue.append(w)
        if last not in queue:
            if len(queue) == 0:
                break
            last = queue[-1]
            k+=1
    return level

def solution(S, T):
    # write your code in Python 2.7
    S = S.lower()
    T = T.lower()
    pair = S.split('|')
    graph = {}
    level = {}
    for p in pair:
        a,b = p.split(',')
        if a not in graph.keys():
            graph[a] = set()
            level[a] = 99999999
        if b not in graph.keys():
            graph[b] = set()
            level[b] = 99999999
    level[T] = -1
    if len(graph) != len(level):
        return []
    for p in pair:
        a,b = p.split(',')
        graph[a].add(b)
    count = [0]*10000
    leveled = bfs(level,graph,T)
    for each in leveled:
        if leveled[each] >= 0 and leveled[each] != 99999999:
            count[leveled[each]] += 1
    ans = []
    for c in count:
        if c != 0:
            ans.append(c)
    return ans
    pass

print(solution('A,B|B,D|D,E|E,F|A,C|A,D|Q,A|K,D|Q,F|F,E|F,Y|E,Z|Z,X|X,K|D,K|Q,Y|Y,Q|Y,X|XX,X', 'D'))