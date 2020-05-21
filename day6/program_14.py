#to solve this question i used geeksforgeeks{in anticlockwise} as a reference 
#  https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
#
N = 4
def rotateMatrix(mat): 
	
	for x in range(0, int(N / 2)): 
		
		for y in range(x, N-x-1): 
			
			temp = mat[N-1-y][x]
			mat[N-1-y][x]=mat[N-1-x][N-1-y]
			mat[N-1-x][N-1-y]=mat[y][N-1-x]
			mat[y][N-1-x]=mat[x][y]
			mat[x][y]=temp			


# Function to print the matrix 
def displayMatrix( mat ): 
	
	for i in range(0, N): 
		
		for j in range(0, N): 
			
			print (mat[i][j], end = ' ') 
		print ("") 
	

mat = [ [1, 2, 3, 4 ], 
		[5, 6, 7, 8 ], 
		[9, 10, 11, 12 ], 
		[13, 14, 15, 16 ] ] 
		

rotateMatrix(mat) 

displayMatrix(mat) 