/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-02 16:21:11
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
    int rob(TreeNode* root) {
        map<TreeNode*, int> cache;
        return rob_dp(root, cache);
    }

    int rob_dp(TreeNode* root, map<TreeNode*, int> &cache){
        if(root==NULL){
            return 0;
        }
        if(cache.find(root)!=cache.end()){
            return cache[root];
        }
        int money = root->val;
        if(root->left!=NULL){
            money += rob_dp(root->left->left, cache) + rob_dp(root->left->right, cache);
        }
        if(root->right!=NULL){
            money += rob_dp(root->right->left, cache) + rob_dp(root->right->right, cache);
        }
        cache[root] = max(money, rob_dp(root->left, cache) + rob_dp(root->right, cache));
        return cache[root];
    }
};

/*
[]
[3,4,5,1,3,null,1]
[3,2,3,null,3,null,1]
*/
