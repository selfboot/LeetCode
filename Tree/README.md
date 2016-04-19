树是一种基本的、应用十分广泛的数据结构。

# 树的起源


# 树的实现


# 树的操作

树的操作基本上都有递归和非递归两个版本。


## 遍历

深度优先：

前根遍历
中根遍历


    def inorderTraversal(self, root):
        tree_stack = []
        inorder_tra = []
        while root or tree_stack:
            # Go along the left child
            if root:
                tree_stack.append(root)
                root = root.left
            # Meet a left, go back to the parent node
            else:
                node = tree_stack.pop()
                inorder_tra.append(node.val)
                root = node.right

        return inorder_tra

后根遍历

124


广度优先搜索
116, 117

## 构建


# 二叉树

## 完美二叉树

## 二叉搜索树

## 平衡二叉搜索树

构建二叉树：递归构建，找到当前根，然后递归求出左子树的根和右子树的根，并建立父子关系。如下面题目：

108

恢复二叉树


# 题目

### [113 Path Sum II](https://leetcode.com/problems/path-sum-ii/)

### [108 Convert Sorted Array to Binary Search Tree](https://leetcode.com/problemset/algorithms/)


# 更多阅读

[Tree (data structure)](https://en.wikipedia.org/wiki/Tree_(data_structure))  
[csci 210: Data Structures Trees](http://www.bowdoin.edu/~ltoma/teaching/cs210/spring09/Slides/210-Trees.pdf)  
[The Tree Data Model](http://infolab.stanford.edu/~ullman/focs/ch05.pdf)  


