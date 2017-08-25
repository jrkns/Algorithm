# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def check_kad(black, s):
    for b in black:
        for i in range(len(b)):
            if b[:i] + b[i + 1:] == s:
                return True
    return False

def check_gern(black, s):
    for b in black:
        for i in range(len(s)):
            if s[:i] + s[i + 1:] == b:
                return True
    return False

def check_swap(black, s):
    for b in black:
        count = 0
        alpha = set()
        if len(s) != len(b):
            continue
        for i in range(len(s)):
            if s[i] == b[i]:
                count += 1
            else:
                alpha.add(s[i])
                alpha.add(b[i])
        if count == len(s) - 2 and len(alpha) == 2:
            return True
    return False

def check_pid(black, s):
    for b in black:
        count = 0
        if len(s) != len(b):
            continue
        for i in range(len(s)):
            if s[i] == b[i]:
                count += 1
        if count == len(s) - 1:
            return True
    return False

def gen_gern(s):
    gern = set()
    for i in range(len(s)):
        gern.add(s[:i] + s[i + 1:])
    return gern

def solution(S):
    # write your code in Python 2.7
    c = S.lower().strip()

    missing = ['aaaaa', 'aaaab', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhhh', 'iiiii', 'jjjjj',
                   'kkkkk', 'lllll', 'mmmmm', 'nnnnn', 'ooooo', 'ppppp', 'qqqqq', 'rrrrr', 'sssss', 'ttttt', 'uuuuu',
                   'vvvvv',
                   'wwwww', 'xxxxw', 'yyyyy', 'zzzzz', 'zzzzy']
    if len(c) == 5:
        return 1
    if len(c) == 4:
        return 1
    if len(c) == 6:
        gern = gen_gern(c)
        if len(gern) == 1 and gern in missing:
            return 0
        return 1
    black = ['johndoe', 'techjam', 'kbtgtech', 'ilovecoding', 'thisiseasy', 'letsgototravel', 'afterfinish', 'majhcet']
    blacked = check_kad(black, c) or check_gern(black, c) or check_swap(black, c) or check_pid(black, c)
    if blacked:
        return 1
    return 0

    pass