class Node:
    def __init__(self,val=None):
        self.val = val
        self.childs = []

def dfs(node,cache):
    if not node:
        return 0

    for c in node.childs:
        cache[node.val].extend(dfs(c,cache))
    cache[node.val].extend([node.val])

    return cache[node.val]

def solution(node):
    import collections
    cache = collections.defaultdict(list)
    dfs(n,cache)

    maxx = float('-inf')
    result = None
    
    for item in cache:
        if len(cache[item])>1:
            val = sum(cache[item])/len(cache[item])
        
            if val>maxx:
                result = item
                maxx = val
    return result
    

# Testcase
n = Node(20)
n12 = Node(12)
n12.childs = [Node(11), Node(2), Node(3)]
n18 = Node(18)
n18.childs = [Node(15), Node(8)]

n.childs = [n12,n18]


solution(n)



'''
Question 1 :
Imagine that an employment tree represents the formal employee hierarchy at Amazon. Manager nodes have
chid nodes for each employee that reports to them; each of these employees can, in turn, have child nodes
representing their respective reportees. Each node in the tree contains an integer representing the number of
months the employee has spent at the company. Team tenure is computed as the average tenure of the manager
and all the company employees working below the manager. The oldest team has the highest team tenure.

Write an algorithm to find the manager of the team with the highest tenure. An employee must have child nodes
to be a manager.

Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

Example 1:

Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.'''