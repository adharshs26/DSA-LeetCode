class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        # Initialize the starting position and direction
        i, j = rStart, cStart
        res = []
        
        # Directions are right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        
        # Step length in the current direction
        steps = 1
        
        # Loop until the result list contains all cells
        while len(res) < rows * cols:
            for _ in range(steps):
                # Add the current position if it's within the matrix bounds
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                
                # Move in the current direction
                i += directions[dir_index][0]
                j += directions[dir_index][1]
            
            # Change direction (right -> down -> left -> up)
            dir_index = (dir_index + 1) % 4
            
            # After every two directions, increase the steps
            if dir_index % 2 == 0:
                steps += 1
        
        return res
    
rows = 1
cols = 4
rStart = 0
cStart = 0

print(Solution().spiralMatrixIII(rows,cols,rStart,cStart))