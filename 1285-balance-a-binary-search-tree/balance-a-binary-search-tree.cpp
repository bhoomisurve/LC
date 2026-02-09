
class Solution {
public:
    vector<int> sorted;

    void inorder(TreeNode* node){
    if (!node) return;
    inorder(node->left);
    sorted.push_back(node->val);
    inorder(node->right);
    }

    TreeNode* build(int left, int right){
    if (left > right) return nullptr;
    int mid = left + (right - left) / 2;
    TreeNode* root = new TreeNode(sorted[mid]);
    root->left = build(left, mid - 1);
    root->right = build(mid + 1, right);
    return root;
    }
    TreeNode* balanceBST(TreeNode* root) {
        inorder(root);
        return build(0, sorted.size() - 1);
    }
};