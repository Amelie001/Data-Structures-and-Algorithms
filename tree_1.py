class TreeNode: 
    def __init__(self, data): 
        self.data = data 
        self.leftNode = None
        self.rightNode = None

def InorderTraversal(root): 
    if root.leftNode != None: 
        InorderTraversal(root.leftNode)
    print(root.data)
    if root.rightNode != None:
        InorderTraversal(root.rightNode)

def PreorderTraversal(root): 
    print(root.data)
    if root.leftNode != None: 
        PreorderTraversal(root.leftNode)
    if root.rightNode != None: 
        PreorderTraversal(root.rightNode)

def PostorderTraversal(root): 
    if root.leftNode != None:
        PostorderTraversal(root.leftNode)
    if root.rightNode != None: 
        PostorderTraversal(root.rightNode)
    print(root.data)

root = TreeNode(5)
root.leftNode = TreeNode(7)
root.leftNode.leftNode = TreeNode(2)

root.rightNode = TreeNode(8)
root.rightNode.leftNode = TreeNode(7)
root.rightNode.rightNode = TreeNode(9)

InorderTraversal(root)
PreorderTraversal(root)
PostorderTraversal(root)