# trees are a type of graph, which are connected without cycles.

# 2 common ways to represent a graph
    # Adjacency list - most common way
        # can represent the graph as a list or hash table of lists (arrays, arraylists, linked lists etc...)

        # better to use node classes unless there is a good reason not to, rather than just make a list of lists etc..
    # Adjacency Matrix
        # can also set the graph as a matrix


# Searching a graph
    # 2 most common ways to search a graph = depth-first search and breadth-first search

# depth-first --> first start at root or another arbibtrary node, and explore each branch completely before moving onto next branch.
    # first go deep, then go wide.
    # DFS is preferred if we want to visit every node in the graph - simpler

# breadth-first search --> start at root or any node, and explore neighbours first, before going onto any of the children.
    # go wide first, then go deep
    # breadth-first search is used for finding shortest path (or just any path between 2 nodes)
    # breadth-first search is generally better than DFS