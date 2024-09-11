#!/usr/bin/python3
"""
rotating a 2dimensional matrix in its place
"""
def rotate_2d_matrix(matrix):
  """
  rotates a 2d matrix in place
  """
  # [[4, 3, 1],
   # [2, 5, 7],
   # [6, 9, 8]]
  left, right = 0, len(matrix) - 1 # a left varibale to represent the left index values
  #and right for right index values
  top, bottom = left, right

  while left < right:
    for i in range(right - left): # n * n matrix, = n -1 circles
      # temporary store the top most left value
      top_left = matrix[top][left + i]

      # move the bottom left value to the top left
      matrix[top][left + i] = matrix[bottom][left + i]

      # move the bottom right value to the bottom left
      matrix[bottom][right - i] = matrix[bottom][left]

      # move the top right value to the bottom right
      matrix[top][right - i] = matrix[bottom][right - i]

      # move the value in the temp variable to the top right
      matrix[top][right - i] = top_left

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rotate_2d_matrix(matrix)
print(matrix)



