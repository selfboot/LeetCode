/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-07 08:41:34
 */

#include "tree.h"
#include <queue>
#include <stack>
#include <sstream>
#include <string>
using namespace std;

string Tree::serialize(){
    string res = "";
    queue<shared_ptr<TreeNode>> que;
    que.push(root);
    while(!que.empty()){
        shared_ptr<TreeNode> head = que.front();
        que.pop();
        if(head){
            res+= to_string(head->value)+" ";
            que.push(head->left);
            que.push(head->right);
        }
        else{
            res+="null ";
        }
    }
    return res;
}

void Tree::deserialize(string data){
    istringstream in(data);
    vector<shared_ptr<TreeNode>> nodes;
    string tmp="";
    while (in>>tmp){
        if(tmp!="null") {
            nodes.push_back(make_shared<TreeNode> (stoi(tmp)));
        }
        else{
            nodes.push_back(nullptr);
        }
    }
    int pos = 0, offset = 1;
    while (offset < nodes.size()){
        if(nodes[pos]){
            if(nodes[offset]){
                nodes[pos]->left = nodes[offset];
            }
            offset++;
            if(offset < nodes.size()){
                if(nodes[offset]){
                    nodes[pos]->right = nodes[offset];
                }
                offset++;
            }
        }
        pos ++;
    }
    this->root = nodes[0];
}

// Recursively traversal.
string Tree::pre_order_r(shared_ptr<TreeNode> root){
    if(root == nullptr) return "";
    string res = to_string(root->value);
    res += pre_order_r(root->left);
    res += pre_order_r(root->right);
    return res;
}

string Tree::post_order_r(shared_ptr<TreeNode> root){
    if(root == nullptr) return "";
    string res = "";
    res += post_order_r(root->left);
    res += post_order_r(root->right);
    res += to_string(root->value);
    return res;
}

string Tree::in_order_r(shared_ptr<TreeNode> root){
    if(root == nullptr) return "";
    string res = "";
    res += in_order_r(root->left);
    res += to_string(root->value);
    res += in_order_r(root->right);
    return res;
}

string Tree::pre_order_i(shared_ptr<TreeNode> root){
    if(root== nullptr){
        return "";
    }
    string res = "";
    stack<shared_ptr<TreeNode>> s;
    s.push(root);
    while (!s.empty()){
        auto cur = s.top();
        s.pop();
        res += to_string(cur->value);
        if(cur->right) s.push(cur->right);
        if(cur->left) s.push(cur->left);
    }
    return res;
}

string Tree::post_order_i(shared_ptr<TreeNode> root){
    shared_ptr<TreeNode> p = root;
    stack<shared_ptr<TreeNode>> s;
    shared_ptr<TreeNode> last_visited = nullptr;
    string res = "";

    while (p!= nullptr || !s.empty()){
        if(p!= nullptr){
            s.push(p);
            p = p->left;
        }
        else{
            auto cur = s.top();
            if(cur->right != nullptr && cur->right != last_visited){
                // if right child exists and traversing node from left child, then move right.
                p = cur->right;
            }
            else{
                res += to_string(cur->value);
                last_visited = cur;
                s.pop();
            }
        }
    }
    return res;
}

string Tree::in_order_i(shared_ptr<TreeNode> root){
    shared_ptr<TreeNode> p = root;
    string res = "";
    stack<shared_ptr<TreeNode>> s;
    while (p!= nullptr || !s.empty()){
        if(p!= nullptr){
            s.push(p);
            p = p->left;
        }
        else{
            p = s.top();
            s.pop();
            res += to_string(p->value);
            p = p->right;
        }
    }
    return res;
}


