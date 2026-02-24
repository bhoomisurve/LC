/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }

    int dfs(TreeNode* node, int currentsum){
        if (!node) return 0;
        currentsum = (currentsum << 1) | node -> val;
        if (node->left == nullptr && node-> right == nullptr){
            return currentsum;
        }

        return dfs(node->left, currentsum) + dfs(node->right, currentsum);
    }
};