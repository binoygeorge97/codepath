'''
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
'''

# UMPIRE
# Understand the problem: FUNCTION transpose() -> Flip the rows and columns of the given 'matrix'
# Match: for loop to iterate through the rows and columns of the matrix
''''
Plan:
FOR i in matrix:
    FOR j in i:
        store j in a new list at the index of j's position in i
RETURN the new list
'''



def transpose(matrix):
    transpose_matrix=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            transpose_matrix[j][i]=matrix[i][j]   
    return transpose_matrix



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))