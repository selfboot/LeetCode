/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-05 08:14:38
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


// The leetcode way
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        queue<TreeNode*> nodes;
        nodes.push(root);
        string ans="";
        while(!nodes.empty()){
            TreeNode* head=nodes.front();
            nodes.pop();
            if(head!=NULL){
                ans+= to_string(head->val)+" ";
                nodes.push(head->left);
                nodes.push(head->right);
            }
            else{
                ans+="null ";
            }
        }
        return ans;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        vector<TreeNode *> nodes;
        string tmp;
        while(in>>tmp){
            if(tmp!="null"){
                nodes.push_back(new TreeNode(stoi(tmp)));
            }
            else{
                nodes.push_back(NULL);
            }
        }
        int pos=0, offset=1;
        while(offset < nodes.size()){
            if(nodes[pos]!=NULL){
                nodes[pos]->left=nodes[offset++];
                if(offset<nodes.size()) nodes[pos]->right=nodes[offset++];
            }
            pos+=1;
        }
        return nodes[0];
    }
};

// Refer to: Recursive preorder, Python and C++, O(n)
// https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n
class Codec_2 {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        serialize(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return deserialize(in);
    }

private:
    void serialize(TreeNode *root, ostringstream &out){
        if(root!=NULL){
            out << root->val << " ";
            serialize(root->left, out);
            serialize(root->right, out);
        }
        else{
            out << "# ";
        }
    }

    TreeNode* deserialize(istringstream &in){
        string val;
        in >> val;
        if(val=="#"){
            return NULL;
        }
        TreeNode *root = new TreeNode(stoi(val));
        root->left = deserialize(in);
        root->right = deserialize(in);
        return root;
    }
};

/*
Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(root))(codec.deserialize("1,null,3,4,5"))

[]
[1,2,null,3,4]
[1,2,3,null,4,null,5,null,6,7]
*/
