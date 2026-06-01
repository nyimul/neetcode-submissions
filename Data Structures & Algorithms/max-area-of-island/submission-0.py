class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        if not grid:
            return maxArea
        
        # Is this not the same thing as just searching for islands and then keeping a running max count of 1s?

        #variables
        visited = set() # tuples of indices to keep track of locations
        directions = [[-1,0],[0,1],[1,0],[0,-1]] # up, right, down, left
        
        # bfs method:
        def getAreaBFS(rowIndex, colIndex):
            thisArea = 1
            # We can use a queue like deque to keep FIFO. And add to visited
            queue = collections.deque()
            queue.append((rowIndex, colIndex))
            print(queue)
            visited.add((rowIndex, colIndex))
            # We add to queue and visited when we explore something valid. Then we add everything around it, and THEN pop it
            while queue:
                # Really?! you forgot this^^^^
                #Pop a cell
                rowIndex, colIndex = queue.popleft()
                #Checking all 4 directions around this 1
                for directionRow, directionCol in directions:
                    checkRow = rowIndex + directionRow
                    checkCol = colIndex + directionCol
                    # BOUNDS CHECKS KILLE DYOU AGAIN!!!!!!
                    if (0 <= checkRow < len(grid) and 0 <= checkCol < len(grid[0]) and grid[checkRow][checkCol] == 1 and (checkRow, checkCol) not in visited):
                        thisArea += 1
                        queue.append((checkRow, checkCol))
                        visited.add((checkRow, checkCol))    
            return thisArea

        # iteration through the grid:
        for rowIndex, row in enumerate(grid):
            for colIndex, element in enumerate(row):
                #if it is a 1 and not been visited, we find that island's area and compare
                # didnt notice it is 1 and not "1"********
                if (element == 1 and (rowIndex, colIndex) not in visited):
                    # get the area of the island with dfs or bfs, then compare
                    thisArea = getAreaBFS(rowIndex, colIndex)
                    if (thisArea > maxArea):
                        maxArea = thisArea
        
        return maxArea