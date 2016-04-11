/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-11 14:30:46
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
    bool isSymmetric(TreeNode* root) {
        return root==NULL || helper(root->left, root->right);
    }

    bool helper(TreeNode* lNode, TreeNode* rNode){
        if(lNode == NULL || rNode == NULL){
            return lNode == rNode;
        }
        if(lNode->val != rNode->val){
            return false;
        }
        return helper(lNode->left, rNode->right) && helper(lNode->right, rNode->left);
    }
};

/*
[]
[1]
[1,2,3]
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
*/
