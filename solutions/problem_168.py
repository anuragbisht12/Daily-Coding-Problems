def rotate_matrix(m):
    num_layers = len(m) // 2
    max_ind = len(m) - 1

    for layer in range(num_layers):
        # rotate all numbers
        for ind in range(layer, max_ind - layer):
            # rotate 4 numbers
            temp = m[layer][ind]
            m[layer][ind] = m[max_ind - ind][layer]
            m[max_ind - ind][layer] = m[max_ind - layer][max_ind - ind]
            m[max_ind - layer][max_ind - ind] = m[ind][max_ind - layer]
            m[ind][max_ind - layer] = temp


# Tests
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
rotate_matrix(matrix_1)
assert matrix_1 == [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]

matrix_2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
rotate_matrix(matrix_2)
assert matrix_2 == [[13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4]]



"""
Best way
"""

# clockwise 90 degree

def rotate90clockwise(array):

  N=len(array)

# transpose
  for i in range(N):
    for j in range(i):
      array[i][j],array[j][i]=array[j][i],array[i][j]

# swap columns

  for i in range(N):
    for j in range(N//2):
      array[i][j],array[i][N-j-1]=array[i][N-j-1],array[i][j]

  return array



def rotate90anticlockwise(array):

  N=len(array)

  for i in range(N):
    for j in range(i):
      array[i][j],array[j][i]=array[j][i],array[i][j]

# swap rows
  for i in range(N//2):
    for j in range(N):
      array[i][j],array[N-i-1][j]=array[N-i-1][j],array[i][j]

  return array

arr=[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
print(rotate90clockwise(arr))

print(rotate90anticlockwise(arr))
