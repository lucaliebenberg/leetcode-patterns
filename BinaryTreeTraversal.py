
# PreOrder: root -> left -> right
def preorder_traversal(self, node):
    if node:
        print(node.val, end='')
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

# InOrder: left -> root -> right
def inorder_traversal(self, node):
    if node:
        self.inorder_traversal(node.left)
        print(node.val, end='')
        self.inorder_traversal(node.right)

# PostOrder: left -> right -> root
def postorder_traversal(self, node):
    if node:
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.val, end='') 

# LevelOrder: level by level
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)

        result.append(current_level)

    return result


