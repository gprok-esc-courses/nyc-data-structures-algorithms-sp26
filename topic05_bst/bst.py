
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.parent = None 
        self.left = None 
        self.right = None 


class BST:
    def __init__(self):
        self.root = None 

    def is_empty(self):
        return self.root is None
    
    def insert(self, value):
        new_node = TreeNode(value) 
        if self.is_empty():
            self.root = new_node
        else: 
            iter = self.root
            while True:
                if iter.value > value:   # go left
                    if iter.left is None:   # put the node here
                        iter.left = new_node
                        new_node.parent = iter 
                        break 
                    else:   # move left 
                        iter = iter.left 
                else:                    # go right 
                    if iter.right is None:  # put the node here
                        iter.right = new_node
                        new_node.parent = iter 
                        break 
                    else:   # move right
                        iter = iter.right 

    def display(self):
        self.inorder(self.root)

    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left) 
        print(node.value)
        if node.right is not None:
            self.inorder(node.right)


tree = BST()
tree.insert(100)
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(60)
tree.insert(80)
tree.insert(200)
tree.insert(150)
tree.insert(300)
tree.display()
