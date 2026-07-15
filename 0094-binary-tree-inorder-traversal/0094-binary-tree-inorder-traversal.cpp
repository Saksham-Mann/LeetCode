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
    void inorder (TreeNode* T, vector<int>* v){
        if(T==nullptr){
            return;
        }
        inorder(T->left, v);
        v->push_back(T->val);
        inorder(T->right,v);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> sol;
        vector<int>* ptr =&sol;
        inorder(root,ptr);
        return sol;
    }
};