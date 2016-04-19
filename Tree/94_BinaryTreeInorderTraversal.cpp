/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-19 11:32:27
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
    // iteratively implement
    vector<int> inorderTraversal(TreeNode* root) {
        vector<TreeNode*> node_stack;
        vector<int> inorder_val;
        while(root!=NULL || !node_stack.empty()){
            if(root!=NULL){
                node_stack.push_back(root);
                root = root->left;
            }
            else{
                TreeNode *node = node_stack.back();
                inorder_val.push_back(node->val);
                node_stack.pop_back();
                root = node->right;
            }
        }
        return inorder_val;
    }
};

/*
[]
[1]
[1,2,3,null,null,4,null,null,5]
*/
