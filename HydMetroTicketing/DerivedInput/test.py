function findInOrderAncestor(n):
    if (n.right != null):
        return findMinKeyWithinTree(n.right)
    ancestor = n.parent
    child = n
    while (ancestor != null AND child == ancestor.right):
        child = ancestor
        ancestor = child.parent
        return ancestor

function findMinKeyWithinTree(root):
    while (root.left != null):
        root = root.left
    return root