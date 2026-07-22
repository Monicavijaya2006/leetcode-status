from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid, health):
        m = len(grid)
        n = len(grid[0])

        # Correct size: m rows and n columns
        dist = [[float('inf')] * n for _ in range(m)]

        dist[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cost, x, y = heappop(pq)

            if x == m-1 and y == n-1:
                return cost < health

            if cost > dist[x][y]:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heappush(pq, (new_cost, nx, ny))

        return False
        