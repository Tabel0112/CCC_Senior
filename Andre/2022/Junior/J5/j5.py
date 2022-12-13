def maxSquare(n, trees):
    matrix = [[1] * n for _ in range(n)]
    for tree in trees:
        matrix[int(tree[0])-1][int(tree[1])-1] = 0
    
    for i in range(1, n):
        for j in range(1, n):
            if matrix[i][j] != 0:
                matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
    
    return matrix

n = int(input())
m = int(input())

trees = []
for _ in range(m):
    trees.append(input().split())

result = maxSquare(n, trees)
for row in result:
    print(row)
