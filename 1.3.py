graph = {
'0': set(['1','2']),
'1': set(['0','3','4']),
'2': set(['0']),
'3': set(['1']), 
'4': set(['2','3'])
}

def dfs(graph, start, visited= None):

    if visited is None:
        visited = set()
    visited.add(start)
    for v in graph[start] - visited:
        dfs(graph, v, visited)
    return visited

print(dfs(graph, '1'))