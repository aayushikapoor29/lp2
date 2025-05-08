graph = {
    'A' : ['B','C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B'],
    'F' : ['C']
}

def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour, visited)


def bfs(start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

print('\nBFS: ')
bfs('A')
print('\n\nDFS: ')
dfs('A')