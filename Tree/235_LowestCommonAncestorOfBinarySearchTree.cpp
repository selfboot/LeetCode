/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-20 19:37:23
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // Easy to understand
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int min = p->val < q->val ? p->val : q->val;
        int max = p->val < q->val ? q->val : p->val;
        while(root){
            if(root->val < min){
                root = root->right;
            }
            else if(root->val > max){
                root = root->left;
            }
            else{
                return root;
            }
        }
        return nullptr;
    }
};
