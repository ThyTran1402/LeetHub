class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh_orange = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_orange += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while q and fresh_orange > 0:
            for i in range(len(q)):
               r, c = q.popleft()
               for dr, dc in directions:
                   row, col = dr + r, dc + c
                   
                   # check if bounds and fresh -> make rotten orange
                   if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                       continue
                   grid[row][col] = 2
                   q.append([row, col])
                   fresh_orange -= 1
            time += 1
        return time if fresh_orange == 0 else -1
    
    
# DFS  approach
#Time/Space complexity: O(M*N)