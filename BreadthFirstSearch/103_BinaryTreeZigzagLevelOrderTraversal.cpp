/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-24 11:19:42
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(root==NULL){
            return {};
        }
        vector<vector<int>> ans;
        deque<TreeNode*> levels{root};
        bool order=true;
        while(!levels.empty()){
            vector<int> cur_level;
            int l_size = levels.size();
            for(int i=0;i<l_size;i++){
                TreeNode* cur_node = levels.front();
                levels.pop_front();
                cur_level.push_back(cur_node->val);
                if(cur_node->left)  levels.push_back(cur_node->left);
                if(cur_node->right) levels.push_back(cur_node->right);
            }
            if(!order)  reverse(cur_level.begin(),cur_level.end());
            ans.push_back(cur_level);
            order = !order;
        }
        return ans;
    }
};

/*
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
*/
