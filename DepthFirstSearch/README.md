深度优先搜索


WikiPedia 里对 DFS 的说明如下：

> Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.  One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible  along each branch before backtracking.


# 一般化实现

递归实现


    def DFS(G, v):
        visited[v] = True
        for cur_node in v.adjacentNodes():
            if not visited[cur_node]:
                # Do something for the current node
                DFS(G, cur_node)
                
栈实现

    def DFS(G, v):
        nodes = stack()
        nodes.push(v)
        while not nodes.empty():
            cur_node = nodes.pop()
            # Do something for the current node
            visited[cur_node] = True
            for w in cur_node.adjacentNodes():
                if not visited[w]:
                    nodes.push(w)

[Clone Graph](https://leetcode.com/problems/clone-graph/) 是一个图的复制问题，可以用 DFS 来遍历图中所有的顶点。

# 例子，更好的理解

## 282. Expression Add Operators

# 更多阅读

[Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)

