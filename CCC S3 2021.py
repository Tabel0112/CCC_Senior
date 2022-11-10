def findPMax(N, P, W, D):
    PMax = 0
    for i in range(N):
        if P[i] > PMax:
            PMax = P[i]
    return PMax

def findPMin(N, P, W, D):
    PMin = 2 ** 31 - 1
    for i in range(N):
        if P[i] < PMin:
            PMin = P[i]
    return PMin

def calTotalTime(N, P, W , D, p):
    # 算出所有人移动到pos p 的时间
    totalTime = 0
    for i in range(N):
        totalTime += max(abs(P[i] - p) - D[i], 0) * W[i]
    
    return totalTime


def ternarySearch(N, P, W, D):
    left = findPMin(N, P, W, D)
    right = findPMax(N, P, W, D)


    while right - left > 2:
        leftPoint = (right - left) // 3 + left
        rightPoint = 2 * (right - left) // 3 + left
        leftTime = calTotalTime(N, P, W , D, leftPoint)
        rightTime = calTotalTime(N, P, W , D, rightPoint)

        
        if leftTime < rightTime:
            right = rightPoint
        else:
            left = leftPoint
    
    return min(calTotalTime(N, P, W , D, left), calTotalTime(N, P, W , D, right), calTotalTime(N, P, W , D, (left + right) // 2))

P = []
W = []
D = []

N = int(input())
for i in range(N):
    inputs = input().split()
    P.append(int(inputs[0]))
    W.append(int(inputs[1]))
    D.append(int(inputs[2]))

print(ternarySearch(N, P, W, D))
