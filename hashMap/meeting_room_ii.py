"""
meeting schedule: [4,10],[3,5],[14,25],[5,8]
return the min meeting room number which can hold all of them

--     4,           ,10
--   3    5
          5      8
              6     9        14   25

"""

import collections

pairs = [[4, 10], [3, 5], [14, 25], [5, 8], [6, 9]]

def meeting_room(meetings: []) -> int:
    m = collections.defaultdict(int)
    for each in meetings:
        m[each[0]] += 1
        m[each[1]] -= 1
    li = sorted(m.items(), key=lambda item: item[0])
    res = cur = 0
    for e in li:
        cur += e[1]
        res = max(cur, res)
    return res


print(meeting_room(pairs))


def merge_schedule(schedules: []) -> [int]:
    res = []
    if len(schedules) < 1 or len(schedules[0]) <= 1:
        return res

    sl = sorted(schedules, key=lambda item: item[0])
    start = sl[0][0]
    end = sl[0][1]

    for i, n in enumerate(sl[1:]):
        if start < n[0] < end:
            if end < n[1]:
                end = n[1]
            if i == len(sl) - 2:
                res.append([start, end])
        else:
            res.append([start, end])
            start, end = n[0], n[1]
            if i == len(sl) - 2:
                res.append([start, end])
    return res


print(merge_schedule(pairs))

def merge_schedule_stack(schedules: []) -> [int]:
    res = []
    if len(schedules) < 1 or len(schedules[0]) <= 1:
        return res

    sorted_schedule = sorted(schedules, key=lambda item: item[0])
    res.append(sorted_schedule[0])

    for _, n in enumerate(sorted_schedule):
        if res[-1][1] < n[0]:
            res.append(n)
        else:
            res[-1][1] = max(res[-1][1], n[1])

    return res


print(merge_schedule_stack(pairs))
