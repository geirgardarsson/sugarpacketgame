def mycopymatrix(mat):
    out = []
    for i in mat:
        out.append(i[:])

    return out

bs = ([[' ', 'a', 'b', 'c', ' '],
       ['1', ' ', ' ', ' ', ' '],
       ['2', ' ', ' ', ' ', ' '],
       ['3', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']])

column = []

for val,i in enumerate(bs):
    column.append(bs[val][1])

print(column)