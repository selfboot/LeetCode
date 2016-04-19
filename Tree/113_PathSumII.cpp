/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-19 10:25:40
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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> pathList;
        vector<int> path;
        findPath(root, sum, path, pathList);
        return pathList;
    }

    void findPath(TreeNode* root, int sum, vector<int> path, vector<vector<int>> &pathList){
        if(root==NULL)  return;
        path.push_back(root->val);
        if(root->left == NULL && root->right==NULL && root->val==sum){
            pathList.push_back(path);
        }
        findPath(root->left, sum-root->val, path, pathList);
        findPath(root->right, sum-root->val, path, pathList);
        path.pop_back();
    }
};

/*
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,3,3,3]
6
*/
