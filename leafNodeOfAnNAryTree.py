t = [[] for i in range(1005)]


# Function to perform DFS on the tree
def dfs(node, parent):
    flag = 1

    # Iterating the children of current node
    for ir in t[node]:

        # There is at least a child
        # of the current node
        if (ir != parent):
            flag = 0
            dfs(ir, node)

            # Current node is connected to only
    # its parent i.e. it is a leaf node
    if (flag == 1):
        print(node)

    # Driver code
# List of all edges
edges = [[1, 2],
         [1, 3],
         [2, 4],
         [3, 5],
         [3, 6],
         [3, 7],
         [6, 8]]

# Count of edges
count = len(edges)

# Number of nodes
node_Size = count + 1

# Create the tree
for i in range(count):
    t[edges[i][0]].append(edges[i][1])
    t[edges[i][1]].append(edges[i][0])

# Function call
dfs(1, 0)