/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-16 12:35:32
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
    /*
    Recursive method: DFS.
    If the current (sub)tree contains both p and q, then the function result is their LCA.
    If only one of them is in that subtree, then the result is that one of them.
    If neither are in that subtree, the result is null/None/nil.

    More version can be found here:
    https://discuss.leetcode.com/topic/18561/4-lines-c-java-python-ruby
    */
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL || root==p || root==q){
            return root;
        }
        TreeNode* l = lowestCommonAncestor(root->left, p, q);
        TreeNode* r = lowestCommonAncestor(root->right, p, q);
        if(l && r){
            return root;
        }
        else{
            return l ? l : r;
        }
    }
};

class Solution_2 {
public:
    /*
    Iteratice method.
    */
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        map<TreeNode*, TreeNode*> parent;
        parent.insert({root, NULL});
        queue<TreeNode*> que;
        que.push(root);
        // Build the relationship from child to parent
        while(parent.find(p) == parent.end() || parent.find(q) == parent.end()){
            TreeNode *cur = que.front();
            que.pop();
            if(cur->left){
                que.push(cur->left);
                parent.insert({cur->left, cur});
            }
            if(cur->right){
                que.push(cur->right);
                parent.insert({cur->right, cur});
            }
        }
        // Trace brack from one node, record the path. Then trace from the other.
        set<TreeNode*> ancestor;
        while(p){
            ancestor.insert(p);
            p = parent[p];
        }
        while(ancestor.find(q) == ancestor.end()){
            q = parent[q];
        }
        return q;
    }
};

