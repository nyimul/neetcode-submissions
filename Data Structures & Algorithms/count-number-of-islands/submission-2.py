class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Redo BFS from scratch, after studying it.
        islands = 0
        if not grid:
            return islands
        
        # set for checking if a specific element has been visited
        # we will check using tuples of indices
        visited = set()

        #directions thing
        # left, up, right, down
        directions = [[0,-1], [-1,0], [0,1], [1,0]]

        def bfs(indexRow, indexCol):
            # Use a queue, with deque
            queue = collections.deque()
            queue.append((indexRow,indexCol))
            visited.add((indexRow,indexCol))
            #print(visited)
            
            while queue:
                indexRow, indexCol = queue.pop()

                # Use directions
                for directionRow, directionCol in directions:
                    r = indexRow + directionRow
                    c = indexCol + directionCol
                    # This line killed u btw
                    if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1" and (r, c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))

        for indexRow, row in enumerate(grid):
            for indexCol, element in enumerate(row):
                print((indexRow, indexCol))
                if (element == "1" and (indexRow, indexCol) not in visited):
                    # Call search algorithm:
                    bfs(indexRow, indexCol)
                    islands += 1
        
        return islands
