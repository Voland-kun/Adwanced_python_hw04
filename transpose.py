def transpose(init_matrix: []) -> []:
    result_matrix = [[None for i in range(len(init_matrix))] for j in range(len(init_matrix[0]))]
    for i in range(len(init_matrix)):
        for j in range(len(init_matrix[0])):
            result_matrix[j][i] = init_matrix[i][j]
    return result_matrix


def zip_transpose(init_matrix: []) -> []:
    result_matrix = []
    for i in zip(*init_matrix):
        result_matrix.append(list(i))
    return result_matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix1 = [[1,2,3],[4,5,6]]

for o in matrix:
    print(o)
print()

result = transpose(matrix)
for n in result:
    print(n)
print()

res = zip_transpose(matrix)
for i in res:
    print(i)
