def function():
    b = input()
    a = input()
    la,lb = len(a),len(b)
    # aaaaa a
    if la < lb :
        print(0)
        return
    b = "".join(sorted(b))
    visited = set()
    for i in range(0,la - lb + 1):
        cmpa = "".join(sorted(a[i : (i + lb)]))
        if cmpa == b:
            visited.add(a[i : (i + lb)])

    print(len(visited))

function()