def zero_matrix(matrix):
     col=[]
     row=[]
     for i in range(len(matrix)):
          for j in range(len(matrix[0])):
               if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
     for r in row:
          for i in range(len(matrix[0])):
               matrix[r][i]=0
     for c in col:
          for j in range(len(matrix)):
               matrix[j][c]=0
     for a in matrix:
          print(a)

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
zero_matrix(matrix)
