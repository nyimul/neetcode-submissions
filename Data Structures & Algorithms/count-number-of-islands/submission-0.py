class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS and DFS examples below.

        # Edge case: empty grid:
        if not grid:
            return islands
        # grid rows & columns counts
        numRows = len(grid)
        numCols = len(grid[0])
        # number of islands:
        islands = 0
        #              left    up   right  down
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        # visited set, NOT like dict {} which is for hashmaps. We store TUPLES of indices
        visited = set()

        def bfs(rowIndex, columnIndex):
            print("Begin BFS")
            # First In, First Out queue with deque:
            queue = deque([(rowIndex, columnIndex)])
            visited.add((rowIndex, columnIndex))

            # always checking if our queue has anything:
            while queue:
                # We pop from the queue
                rowIndex, columnIndex = queue.popleft()

                #For each of the directions, we check if it is in bounds and if is 1.
                for directionRow, directionCol in directions:
                    if (rowIndex + directionRow in range(numRows) and columnIndex + directionCol in range(numCols)):
                        # In range! Is it 1 and has it not been visited before?
                        if (grid[rowIndex + directionRow][columnIndex + directionCol] == "1" and (rowIndex + directionRow,columnIndex + directionCol) not in visited):
                            # Add to queue, mark as visited
                            queue.append((rowIndex + directionRow,columnIndex + directionCol))
                            visited.add((rowIndex + directionRow,columnIndex + directionCol))
                            # And we have to run BFS on this cell too.
                    

                

        # Will implement dfs later:
        def dfs():
            print("dfs")

        # Iterate through the entire grid:
        for rowIndex, row in enumerate(grid):
            # We have indexed through by row, now need to do it for EACH row:
            for columnIndex, element in enumerate(row):
                if (element == "1" and (rowIndex, columnIndex) not in visited):
                    # Explore the island, either with bfs or dfs
                    bfs(rowIndex, columnIndex)
                    #dfs()
                    islands += 1
        
        return islands
                    

        

