#!/usr/bin/python3
"""
Rotating a 2-dimensional matrix in its place
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # Save the top left value
            top_left = matrix[top][left + i]

            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move top left (saved) to top right
            matrix[top + i][right] = top_left

        left += 1
        right -= 1
