import cv2 
import numpy as np 
import time 

class TreeNode: 
    def __init__(self, data): 
        self.data = data 
        self.leftNode = None 
        self.rightNode = None 

def InorderTraversal(root): 
    if root == None: 
        return []

    return InorderTraversal(root.leftNode) + [root] + InorderTraversal(root.rightNode)

def PreorderTraversal(root): 
    if root == None: 
        return []

    return [root] + PreorderTraversal(root.leftNode) + PreorderTraversal(root.rightNode)

def PostorderTraversal(root): 
    if root == None: 
        return []

    return (
        PostorderTraversal(root.leftNode) + PostorderTraversal(root.rightNode) + [root]
    )

def DrawTree(root, positions, visited, current, sequence, title): 
    img = np.ones((650, 900, 3), dtype=np.uint8) * 245

    cv2.putText(img, title, (230, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2)

    # Draw connecting branches
    def draw_lines(node):

        if node == None: 
            return

        x1, y1 = positions[id(node)]

        if node.leftNode != None: 
            x2, y2 = positions[id(node.leftNode)]
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 3)
            draw_lines(node.leftNode)

        if node.rightNode != None: 
            x2, y2 = positions[id(node.rightNode)]
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 3)
            draw_lines(node.rightNode)

    draw_lines(root)

    def draw_nodes(node): 

        if node ==