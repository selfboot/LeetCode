树（Tree）是n（n≥0）个有限数据元素的集合。当n＝0 时，称这棵树为空树。在一棵非空树T 中：

1. 有一个特殊的数据元素称为树的根结点，根结点没有前驱结点。
2. 除根结点之外的其余数据元素被分成m（m>0）个互不相交的集合T1，T2，…，Tm，其中每一个集合Ti（1≤i≤m）本身又是一棵树。树T1，T2，…，Tm 为这个根结点的子树（subtree）。

树具有以下特点：

1. 每个节点有零个或多个子节点。
2. 每个非根节点只有一个父节点。
3. 没有父节点的节点称为根节点。

相关术语（结点、孩子结点等术语忽略）：

* 祖先结点: 从根到该结点的所经分支上的所有结点子孙结点：以某结点为根的子树中任一结点都称为该结点的子孙；
* 结点层：规定树的根结点的层数为1，其余结点的层数等于它的双亲结点的层数加1；
* 结点的`度`：结点子树的个数。

# 二叉树

二叉树是`每个节点最多有两个子树`的树结构。二叉树的每个结点至多只有二棵子树，二叉树的子树有左右之分，次序不能颠倒。

图论中二叉树的定义如下：二叉树是一个连通无环图，并且每一个顶点的度不大于3。有根二叉树还要满足根结点的度不大于2。

二叉树的一些不是那么明显的性质：

1. 对任何一棵二叉树T，度为2的结点数为m，则叶子结点数为：m＋1。
2. 给定N个节点，能构成h(N)种不同的二叉树，其中h(N)为`卡特兰数`的第N项。h(n)=C(2*n，n)/(n+1)。

几种常用的二叉树：

* 满二叉树：一棵深度为k，且有2^k - 1个节点的二叉树；
* 完全二叉树：深度为k，有n个节点的二叉树，当且仅当其每一个节点都与深度为k的满二叉树中，序号为1至n的节点对应时。
* 二叉堆：它一棵完全的二叉树，二叉堆一般分为两种：最大堆和最小堆。

    * 最大（小）堆中的最大（小）元素值出现在根结点（堆顶）；
    * 堆中每个父节点的元素值都大（小）于等于其孩子结点（如果存在）。
* 二叉排序树：是一棵空树，或者是具有下列性质的二叉树：

     * 若左子树不空，则左子树上所有结点的值均小于它的根结点的值；
     * 若右子树不空，则右子树上所有结点的值均大于它的根结点的值；
     * 左、右子树也分别为二叉排序树；
     * 没有键值相等的节点。
* 平衡二叉树（AVL树）：它是一棵二叉排序树，且具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

## 二叉树的遍历


深度优先：

前根遍历  
中根遍历

后根遍历

124


广度优先搜索
116, 117

## 树与二叉树的转换

如果设定一定规则，就可用二叉树结构表示树，这样对树的操作实现就可以借助二叉树存储，利用二叉树上的操作来实现。

`树转换为二叉树`：将一棵树转换为二叉树的方法是：

* 树中所有相邻兄弟之间加一条连线。
* 对树中的每个结点，只保留它与第一个孩子结点之间的连线，删去它与其它孩子结点之间的连线。
* 以树的根结点为轴心，将整棵树顺时针转动一定的角度，使之结构层次分明。

![][1]

二叉树转换为树或森林的过程如下：

* 若某结点是其双亲的左孩子，则把该结点的右孩子、右孩子的右孩子……都与该结点的双亲结点用线连起来；
* 删去原二叉树中所有的双亲结点与右孩子结点的连线；
* 整理由（1）、（2）两步所得到的树或森林，使之结构层次分明。

![][2]

［[二叉树与森林的转换](http://www.nowcoder.com/questionTerminal/fe30dbe0dfb1498183e832dcba5ed908)］

# 二叉查找树

二叉查找树，也称排序二叉树，是指一棵空树或者具备下列性质的二叉树(每个结点都不能有多于两个儿子的树)：

1. 若任意结点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若任意结点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
3. 任意结点的左、右子树也分别为二叉查找树；
4. **没有键值相等的结点**。

从其性质可知，定义排序二叉树的一种自然的方式是递归的方法，其算法的核心为递归过程，由于它的平均深度为O(logN)，所以递归的操作树，一般不必担心栈空间被耗尽。

更多内容参考 [BS_Tree](https://github.com/xuelangZF/CS_Offer/blob/master/DataStructure/BS_Tree.md)

# 自平衡二叉搜索树

AVL树是最早提出的自平衡二叉树，它是一种特殊的二叉搜索树，任一节点的左子树深度和右子树深度相差不超过1，所以它也被称为高度平衡树。

AVL树的特性让二叉搜索树的节点实现平衡(balance)：节点相对均匀分布，而不是偏向某一侧。因此，AVL树种查找、插入和删除在平均和最坏情况下都是O（log n），增加和删除可能需要通过一次或多次树旋转来重新平衡这个树。


更多内容参考 [AVL_Tree](https://github.com/xuelangZF/CS_Offer/blob/master/DataStructure/AVL_Tree.md)

# 红黑树

红黑树是一种自平衡二叉查找树。它的统计性能要好于平衡二叉树（AVL树），因此，红黑树在很多地方都有应用。在C++ STL中，很多部分(目前包括set, multiset, map, multimap)应用了红黑树的变体。它是复杂的，但它的操作有着良好的最坏情况运行时间，并且在实践中是高效的: 它可以在O(log n)时间内做查找，插入和删除等操作。

详细内容参见 [RB_Tree](https://github.com/xuelangZF/CS_Offer/blob/master/DataStructure/RB_Tree.md)

# 题目

### [113 Path Sum II](https://leetcode.com/problems/path-sum-ii/)

### [108 Convert Sorted Array to Binary Search Tree](https://leetcode.com/problemset/algorithms/)


# 更多阅读

[Wiki: Tree (data structure)](https://en.wikipedia.org/wiki/Tree_(data_structure))   
[Wiki: Tree traversal](https://en.wikipedia.org/wiki/Tree_traversal)  
[csci 210: Data Structures Trees](http://www.bowdoin.edu/~ltoma/teaching/cs210/spring09/Slides/210-Trees.pdf)  
[The Tree Data Model](http://infolab.stanford.edu/~ullman/focs/ch05.pdf)  

[Lowest Common Ancestor of a Binary Tree Part I](http://articles.leetcode.com/lowest-common-ancestor-of-a-binary-tree-part-i/)  
[Lowest Common Ancestor of a Binary Tree Part II](http://articles.leetcode.com/lowest-common-ancestor-of-a-binary-tree-part-ii/)  

[1]: ../Images/Tree_1.jpg
[2]: ../Images/Tree_2.jpg

