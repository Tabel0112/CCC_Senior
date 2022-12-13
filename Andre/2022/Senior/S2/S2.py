def goodGroups(together: dict, separate: dict, groups: list):
    violation = 0
    for group in groups:
        for student in group:
            if student in together:
                for pair in together[student]:
                    if pair not in group:
                        # print(group)
                        violation += 1
                

            if student in separate:
                for pair in separate[student]:
                    if pair in group:
                        # print(group)
                        violation += 1
    return violation

together = {}
T = int(input())
for i in range(T):
    pair = input().split()
    if pair[0] not in together:
        together[pair[0]] = [pair[1]]
    else:
        together[pair[0]].append(pair[1])

separate = {}
S = int(input())
for i in range(S):
    pair = input().split()
    if pair[0] not in separate:
        separate[pair[0]] = [pair[1]]
    else:
        separate[pair[0]].append(pair[1])

# print(together, separate)
groups = []
G = int(input())
for i in range(G):
    group = input().split()
    groups.append(group)

print(goodGroups(together, separate, groups))