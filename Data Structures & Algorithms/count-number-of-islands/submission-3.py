class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Now let's do DFS. Usng recursion & stack.
        islands = 0

        if not grid:
            return islands
        
        # variables
        visited = set() # set bc checking for membership. We keep tuples of (rowIndex,colIndex) to keep track of locations
        directions = [[0, -1],[-1, 0],[0, 1],[1, 0]] # add to rowIndex, columnIndex to get l, u, r, d

        # dfs method
        def dfs(rowIndex, columnIndex):
            # Depth First Search - recursion with stack (LIFO)
            # First, let's add to visited
            visited.add((rowIndex, columnIndex))

            # dont need an actual deque or anything to represent the stack
            # we can just recursively call and it will act as the stack somehow?
            # "base case": when there is nothing left to explore in this island
            for directionRow, directionCol in directions:
                # we get each 4 directions
                checkRow = rowIndex + directionRow
                checkCol = columnIndex + directionCol
                # now we recurse iff this direction is valid
                if (0 <= checkRow < len(grid) and 0 <= checkCol < len(grid[0]) and grid[checkRow][checkCol] == "1" and (checkRow, checkCol) not in visited):
                    dfs(checkRow, checkCol)


        # iterating through grid
        for rowIndex, row in enumerate(grid):
            for columnIndex, element in enumerate(row):
                # We start depth first search if:
                # element is 1, it is not in visited
                if (element == "1" and (rowIndex, columnIndex) not in visited):
                    print((rowIndex, columnIndex))
                    print(visited)
                    dfs(rowIndex, columnIndex)
                    islands += 1
        
        return islands
