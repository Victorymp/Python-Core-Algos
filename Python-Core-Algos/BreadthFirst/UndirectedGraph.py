# Return the number of connected components in the graph.

# The graph may contain cycles.

# The graph may not be fully connected.

# You must traverse the graph using either DFS or BFS.

# Do not modify the input graph.

from collections import deque


def count_components(graph):
    # Implement traversal logic here

    ## Start from the node 0
    ## We will have to keep track of known connections 
    ## We will have to traverse all items in the graph
    ## Can not count connections we visited

    visited = [False] * len(graph)
    ## Known connections
    kc = {}
    nx = deque()
    nx.append(0)
    while nx:
        pntC:int = nx.popleft()

        if not kc.get(pntC) :
          for nbr in graph[pntC]:
              if not visited[nbr]:
                  ## If it has a child add a tuple of that connection
                  kc[pntC] = nbr
                  nx.append(nbr)
                  visited[nbr] = True
                           

    return len(kc)

def main():
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
        4: []
    }

    result = count_components(graph)
    print(result)


if __name__ == "__main__":
    main()
