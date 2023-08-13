def searchMatrix(matrix, target):
    i = 0
    while target > matrix[i][-1]:
        i += 1
    return target in matrix[i]

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))