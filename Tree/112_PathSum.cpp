/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-19 09:57:21
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
    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL){
            return false;
        }
        if(root->left==NULL && root->right == NULL){
            return root->val == sum;
        }
        if(root->left && hasPathSum(root->left, sum-root->val)){
            return true;
        }
        if(root->right && hasPathSum(root->right, sum-root->val)){
            return true;
        }
    }
};

/*
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,null,null,3,4,null,null,4]
9
*/
