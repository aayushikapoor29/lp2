import heapq

def astar(grid, start, goal):
    def h(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open = [(0 + h(start, goal), 0, start, [])]
    seen = set()
    
    while open:
        _, cost, node, path = heapq.heappop(open)
        if node in seen: continue
        seen.add(node)
        path = path + [node]
        if node == goal: return path
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            x, y = node[0]+dx, node[1]+dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                heapq.heappush(open, (cost+1+h((x,y), goal), cost+1, (x,y), path))


    return None

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)
print("Path:" if path else "No path")
if path:
    for p in path:
        print(p)
