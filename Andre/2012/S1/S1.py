## 用排列组合
def sucker(lastNumber):
    if lastNumber < 4:
        return 0
    return (lastNumber - 1) * (lastNumber - 2) * (lastNumber - 3) // 6