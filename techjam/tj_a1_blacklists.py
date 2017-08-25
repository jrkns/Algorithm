def check_kad(black,s):
    for b in black:
        for i in range(len(b)):
            if b[:i] + b[i+1:] == s:
                return True
    return False

def check_gern(black,s):
    for b in black:
        for i in range(len(s)):
            if s[:i] + s[i+1:] == b:
                return True
    return False

def check_swap(black,s):
    for b in black:
        count = 0
        alpha = set()
        if len(s) != len(b):
            continue
        for i in range(len(s)):
            if s[i] == b[i]:
                count+=1
            else:
                alpha.add(s[i])
                alpha.add(b[i])
        if count == len(s)-2 and len(alpha) == 2:
            return True
    return False

def check_pid(black,s):
    for b in black:
        count = 0
        if len(s) != len(b):
            continue
        for i in range(len(s)):
            if s[i] == b[i]:
                count+=1
        if count == len(s)-1:
            return True
    return False

def solution(S):
    # write your code in Python 2.7
    S = S.lower()
    splited = S.split('#')
    black = splited[0].split('|')
    check = splited[1].split('|')
    ans = []
    for c in check:
        blacked = c in black or check_kad(black, c) or check_gern(black, c) or check_swap(black, c) or check_pid(black, c)
        if blacked:
            ans.append(1)
        else:
            ans.append(0)
    return ans
print(solution('FU|JohnDoe|Somchai|Tawatchai#Johdnoe|Somying|Thawatchai|Htawatcai|XX'))