class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS :D
        maxArea = 0
        if not grid:
            return maxArea
        
        # variables
        visited = set() # membership of visited tuple indices
        directions = [[-1,0],[0,1],[1,0],[0,-1]] # up right down left

        #dfs algorithm
        def dfs(rowIndex, colIndex):
            # VERY IMPORTANT TO COUNT ITSELF HERE:::::
            visited.add((rowIndex, colIndex))
            area = 1
            # Recursive stack
            for directionRow, directionCol in directions:
                checkRow = rowIndex + directionRow
                checkCol = colIndex + directionCol
                if (0 <= checkRow < len(grid) and 0 <= checkCol < len(grid[0]) and grid[checkRow][checkCol] == 1 and (checkRow, checkCol) not in visited):
                    # Recurse
                    visited.add((checkRow, checkCol))
                    area += dfs(checkRow, checkCol)
            return area

        
        # Iterate through the grid:
        for rowIndex, row in enumerate(grid):
            for colIndex, element in enumerate(row):
                # Check if it is a 1 and has not been visited before
                if (element == 1 and (rowIndex, colIndex) not in visited):
                    thisArea = dfs(rowIndex, colIndex)
                    if (thisArea > maxArea):
                        maxArea = thisArea
        
        return maxArea