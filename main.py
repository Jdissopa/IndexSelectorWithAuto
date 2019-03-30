

svTable = [('cam', 5, 3), ('f', 4, 4), ('am', 3, 4), ('p', 1, 3), ('m', 2, 3), ('b', 1, 3)]


def index_select(i,j):
    S = [[0 if x == 0 or y == 0 else -1 for y in range(j)] for x in range(i)]
    if S[i][j] < 0:
        if j < svTable[i][1]:
            v = index_select(i - 1, j)
        else:
            v = max(index_select(i - 1, j), svTable[i][2] + index_select(i - 1, 0))
    return v

