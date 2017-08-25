# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def to_sec(S):
    a = S.split(':')
    total = 0
    for i in range(len(a)):
        total += int(a[i]) * (60 ** (len(a) - 1 - i))
    return total


def to_sec_alt(S):
    a = S.split(':')
    if len(a) == 1:
        return int(a[0]) * 60
    elif len(a) == 2:
        return (int(a[0]) * 60) + int(a[1])
    return (int(a[0]) * 3600) + (int(a[1]) * 60) + int(a[2])


def solution(S):
    # write your code in Python 2.7
    calls = S.split('|')
    talks = []
    for call in calls:
        info = call.split(',')
        start = to_sec(info[0])
        talks.append((start, to_sec_alt(info[1])))
    talks = sorted(talks, key=lambda x: x[0])
    talker = [talks[0][0] + talks[0][1]]
    for talked in range(1, len(talks)):
        found = False
        start = talks[talked][0]
        length = talks[talked][1]
        for j in range(len(talker)):
            if talker[j] <= start + 60:
                talker[j] = talker[j] + length
                found = True
                break
        if not found:
            talker.append(start + length)
    return len(talker)
    pass
print(solution("00:00:00,24:00:00|00:00:00,1:01|00:00:01,23:58:59"))
print(solution("00:00:00,24:00:00|00:00:01,23:58:59|00:00:00,1:01"))
print(solution("00:00:01,23:58:59|00:00:00,1:01|00:00:00,24:00:00"))
print(solution("00:00:01,23:58:59|00:00:00,24:00:00|00:00:00,1:01"))
print(solution("23:55:58,1:01|23:56:59,1:01|23:55:57,1:01"))
print(solution("00:00:01,1:01|00:00:00,10:00|23:57:00,1:01|23:56:59,1:01|00:10:11,15:32|00:00:00,2:59|00:00:00,2:59|00:01:59,3:00|00:01:59,3:00|21:00:32,5:21"))
print(solution("8:30:0,02:0|8:30:0,02:0|8:31:0,10:0|8:31:0,10:0|8:40:0,10:0|8:40:0,10:0"))


