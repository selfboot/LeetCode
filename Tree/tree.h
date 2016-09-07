#ifndef TREE_H
#define TREE_H
#include <iostream>

// Definition for a binary tree node.
struct TreeNode
{
    int value;
    std::shared_ptr<TreeNode> left;
    std::shared_ptr<TreeNode> right;
    TreeNode(int v): value(v), left(nullptr), right(nullptr){
    }
};

/*
A binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, if a tree looks like the following:
    1
   / \
  2   3
     / \
    4   5

Then it can be serialize to string: 1 2 3 null null 4 5.
*/
class Tree
{
public:
    Tree(){
        root = nullptr;
    }

    std::string serialize();
    void deserialize(std::string data);
    std::shared_ptr<TreeNode> get_root(){
        return root;
    }

    // Recursively traversal.
    std::string pre_order_r(std::shared_ptr<TreeNode>);
    std::string post_order_r(std::shared_ptr<TreeNode>);
    std::string in_order_r(std::shared_ptr<TreeNode>);

    // Iteratively traversal.
    std::string pre_order_i(std::shared_ptr<TreeNode>);
    std::string post_order_i(std::shared_ptr<TreeNode>);
    std::string in_order_i(std::shared_ptr<TreeNode>);

private:
    std::shared_ptr<TreeNode> root;
};

#endif

