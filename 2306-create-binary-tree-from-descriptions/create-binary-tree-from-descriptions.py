
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for pv, cv, isleft in descriptions:
            if pv not in nodes:
                nodes[pv] = TreeNode(pv)
            if cv not in nodes:
                nodes[cv] = TreeNode(cv)

            p = nodes[pv]
            c = nodes[cv]

            if isleft:
                p.left = c
            else:
                p.right= c
            children.add(cv)
        for val in nodes:
            if val not in children:
                return nodes[val]
