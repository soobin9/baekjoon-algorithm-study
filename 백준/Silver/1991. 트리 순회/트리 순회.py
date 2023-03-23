class Node:
    def __init__(node, data, left_node, right_node):
        node.data = data
        node.left_node = left_node
        node.right_node = right_node
        

n = int(input())
tree = {}

def preOrder(node):
    print(node.data, end = '')
    if (node.left_node != '.'):
        preOrder(tree[node.left_node])
    if (node.right_node != '.'):
        preOrder(tree[node.right_node])
        
def inOrder(node):
    if (node.left_node != '.'):
        inOrder(tree[node.left_node])
    print(node.data, end = '')
    if (node.right_node != '.'):
        inOrder(tree[node.right_node])

def postOrder(node):
    if (node.left_node != '.'):
        postOrder(tree[node.left_node])
    if (node.right_node != '.'):
        postOrder(tree[node.right_node])
    print(node.data, end = '')

# tree set 
for _ in range(n):
    data, left_node, right_node = input().split(' ')
    tree[data] = Node(data, left_node, right_node)
    
preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])
print()