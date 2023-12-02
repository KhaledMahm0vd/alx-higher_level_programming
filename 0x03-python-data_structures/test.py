#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
i = 0
j = 0
list_j = []
while i < len(matrix) + 1:
        while j < len(matrix[i]) + 1:
            j += 1
            list_j.append(j)
            print(j)
        i += 1
