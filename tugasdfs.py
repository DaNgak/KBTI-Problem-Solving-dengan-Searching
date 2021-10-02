graph ={
    "A" : ["B"],
    "B" : ["A", "F", "G"],
    "C" : ["D", "G"],
    "D" : ["C", "H"],
    "E" : ["F"],
    "F" : ["B", "E"],
    "G" : ["B", "C"],
    "H" : ["D"]
}
visited = set()
def dfs(visited, graph, node, nodedicari):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        if node != nodedicari:
            for neighbour in graph[node]:
                if nodedicari not in visited :
                    dfs(visited, graph, neighbour, nodedicari)
        else :
            print("Finish")
print("Hasil penelusuran Node D menggunakan DFS")
dfs(visited, graph, "A", "D")