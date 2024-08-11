class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        
        ans = 0
        def check(m): #To check if 3x3 matrix is magic cube
            
            #Checking if duplicates are present
            if not(m[0][0] != m[0][1] != m[0][2] != m[1][0] != m[1][1] != m[1][2] != m[2][0] != m[2][1] != m[2][2]): 
                return 0

                
            #checking if any number is not in between 1 and 15
            if not(0<m[0][0]<16 and 0<m[0][1]<16 and 0<m[0][2]<16 and 0<m[1][0]<16 and 0<m[1][1]<16 and 0<m[1][2]<16 and 0<m[2][0]<16 and 0<m[2][1]<16 and 0<m[2][2]<16): 
                return 0

            #checking if sum of rows and columns are 15
            for i in range(3):
                if m[i][0]+m[i][1]+m[i][2] != 15:
                    return 0
                if m[0][i]+m[1][i]+m[2][i] != 15:
                    return 0


            if m[0][0]+m[1][1]+m[2][2] != 15:                #checking diagonal 1
                return 0
            if m[2][0]+m[1][1]+m[0][2] != 15:                #checking diagonal 2
                return 0
            return 1
		
		#checking for each 3x3 matrix starting from index [i,j] 
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2): 
                ans += check([[grid[i][j],grid[i][j+1],grid[i][j+2]],
                              [grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]],
                              [grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]])
        return ans
                

grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(Solution().numMagicSquaresInside(grid))