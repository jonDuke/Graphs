
def find_deepest(graph, starting_node, depth=0):
    """
    recursive depth search, returns the deepest node found

    works with any number of parents, even though the problem only has 0-2

    returns a tuple: (ancestor_id, depth)
    """
    # base case, no parents (would not have been added to the graph structure)
    if starting_node not in graph:
        return starting_node, depth
    
    # call dfs again on each parent
    deepest = -1
    for parent in graph[starting_node]:
        result = find_deepest(graph, parent, depth+1)
        if result[1] > deepest:
            # save the deepest ancestor result found
            deepest = result[1]
            found = result[0]
        elif result[1] == deepest and found > result[0]:
            # same depth, but make sure we get lower parent id
            found = result[0]

    return found, deepest


def earliest_ancestor(ancestors, starting_node):
    # build the graph, keys are node id's and values are lists of parents
    graph = {}
    for link in ancestors:
        # link is a (parent, child) tuple
        if link[1] in graph:
            graph[link[1]].append(link[0])
        else:
            graph[link[1]] = [link[0]]
    
    if starting_node not in graph:
        # starting_node has no ancestors
        return -1
    
    # use the recursive search to find the earliest ancestor
    return find_deepest(graph, starting_node)[0]
