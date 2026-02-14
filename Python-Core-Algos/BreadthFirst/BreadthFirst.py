from collections import deque

def shortest_distance(start, target, graph):
    ## Keep track of the visited nodes in the graph
    visited = [False] * len(graph)
    visited[start] = True
    ## Create a deque to have O(1) extraction
    nx = deque()
    pnt:int = start
    result = []
    nx.append(pnt)
    while nx:
        pnt1:int = nx.popleft()
        result.append(pnt1)
        if pnt1 == target:
            print(result)
            return len(result)
        ## Making sure we append all items on this level and making them left most
        for nbrs in graph[pnt1]:
            if visited[nbrs] == False:
                visited[nbrs] = True
                nx.append(nbrs)
    
    print(result)
    return -1

def main():
    graph = {
        0: [1, 2],
        1: [3],
        2: [3, 4],
        3: [5],
        4: [],
        5: []
    }

    start = 0
    target = 7

    result = shortest_distance(start, target, graph)
    print(result)


if __name__ == "__main__":
    main()