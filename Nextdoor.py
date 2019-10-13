matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]
]

k = 2 

def rotate_matrix(matrix, k):
    length = len(matrix[0])
    row = 0
    col = 0 
    endrow = len(matrix) - 1 
    endcol = len(matrix[0]) - 1 
    for rotate in range(k):
        mid = length // 2 
        while row < endrow and mid < endcol: 
            cache = matrix[row][mid]
            matrix[row][mid] = matrix[mid][row]
            matrix[mid][row] = matrix[endrow][mid]
            matrix[endrow][mid] = matrix[mid][endcol]
            matrix[mid][endcol] = cache 
            
            row += 1 
            endrow -= 1 
            endcol -= 1 
        endrow = len(matrix) - 1 
        endcol = length - 1
        row = 0 
        
    return matrix
                
print(rotate_matrix(matrix,k))