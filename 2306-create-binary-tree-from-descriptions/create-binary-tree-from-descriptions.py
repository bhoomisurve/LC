class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parentVal, childVal, isLeft in descriptions:

            if parentVal not in nodes:
                nodes[parentVal] = TreeNode(parentVal)

            if childVal not in nodes:
                nodes[childVal] = TreeNode(childVal)

            parent = nodes[parentVal]
            child = nodes[childVal]

            if isLeft:
                parent.left = child
            else:
                parent.right = child

            children.add(childVal)

        for val in nodes:
            if val not in children:
                return nodes[val]