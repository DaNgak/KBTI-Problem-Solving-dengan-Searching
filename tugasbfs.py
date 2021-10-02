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
visited = []
queue = []
def bfs(visited, graph, node, nodedicari):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        if(s != nodedicari):
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        else :
            print("Finish")
            break
print("Hasil penelusuran Node D menggunakan BFS")
bfs(visited, graph, "A", "D")
