from collections import Counter

convert = lambda x : ord(x) - ord('a')

def SearchingForStrings(target, sample):
    targetLen = len(target)
    sampleLen = len(sample)

    if (targetLen > sampleLen):
        return 0
    
    result = set()

    targetList = [0] * 26
    sampleList = [0] * 26
    

    for i in range(targetLen):
        targetList[convert(target[i])] += 1
        sampleList[convert(sample[i])] += 1
    
    if targetList == sampleList:
            result.add(sample[0:targetLen])
    
    for i in range(1, sampleLen-targetLen+1):
        sampleList[convert(sample[i-1])] -= 1
        sampleList[convert(sample[i+targetLen-1])] += 1

        ## if there's no difference, then it's a match
        if targetList == sampleList:
            result.add(sample[i: i+targetLen])

    return len(result)


target, sample = input(), input()

try:
    print(SearchingForStrings(target, sample))
except:
  print(target, sample)