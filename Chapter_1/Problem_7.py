def rotate_matrix(matrix):
     for i in range(len(matrix)):
          for j in range(i,len(matrix[0])):
               matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]

     for a in matrix:
          a.reverse()
     for a in matrix:
          print(a)

#Time complexity O(N*N)
#Space complexity O(1)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate_matrix(matrix)
