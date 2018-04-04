class Node():
    left = None
    right = None
    data = None

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder(root):
    if root == None:
        return

    print root.data
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return

    preorder(root.left)
    print root.data
    preorder(root.right)

def postorder(root):
    if root == None:
        return

    preorder(root.left)
    preorder(root.right)
    print root.data



root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print "preorder"
preorder(root)
print "inorder"
inorder(root)
print "postorder"
postorder(root)
