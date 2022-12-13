import math

def goodSamples(N, M, K):
    ### check if K is not feasible by M & N
    combinationCap = (1 + M) * M / 2 + (N - M) * M
    if (K > combinationCap or K < N):
        return -1

    pitchCap = 1

    for i in range(M):
        x =  (1 + pitchCap) * pitchCap / 2
        y = (N - pitchCap)
        maxComb =  x + y * pitchCap
        minComb =   x + y
        if maxComb >= K and minComb <= K:
            break
        pitchCap += 1
    
    default = []
    for i in range(pitchCap):
        default.append(pitchCap - i)

    if N == pitchCap:
        return " ".join([str(x) for x in default])

    x = math.floor((1 + pitchCap) * pitchCap / 2)
    rem = math.floor((K - x) % (N - pitchCap))
    restNum = math.floor((K - x -  rem) / (N - pitchCap))
    maxAddOn = pitchCap - restNum

    result = []
    for i in range(N - pitchCap):
        addNum = restNum
        if (rem > maxAddOn):
            rem -= maxAddOn
            addNum = pitchCap
        elif (rem > 0):
            addNum += rem
            rem = 0
        
        if (default and addNum <= default[0]):
            result.append(default[0])
            default.pop(0)
        
        result.append(addNum)

    
    for num in default:
        result.append(num)

    return " ".join(convert(result, pitchCap))

def convert(list, m):
    result = [0] * len(list)
    result[0] = 0
    curr = 0

    for i, n in enumerate(list):
        if result[i] == 0:
            curr += 1
            curr = (curr - 1) % m + 1
            result[i] = str(curr)
        else:
            curr = result[i]
        
        if n + i < len(list):
            result[n+i] = str(curr)
    
    return result

[N, M, K] = map(lambda x: int(x), input().split())

print(goodSamples(N, M, K))

# try:
#     print(" ".join(goodSamples(N, M, K)))
# except:
#     print(N, M, K)

