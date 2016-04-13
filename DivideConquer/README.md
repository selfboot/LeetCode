





# 题目

### [240 Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

> 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列也是按照从上到下的顺序递增，判断该二维数组中是否存在给定的数字。如下例子：

> [1,   4,  7, 11, 15],  
> [2,   5,  8, 12, 19],  
> [3,   6,  9, 16, 22],  

首先选取数组中右上角的数字，如果该数字等于要查找的数字，查找过程结束；如果该数字大于要查找的数字，剔除这个数字所在的列；如果该数字小于要查找的数字，剔除这个数字所在的行。也就是说每次都在数组的查找范围内剔除一行或者一列。

[具体实现](https://github.com/xuelangZF/LeetCode/blob/master/DivideConquer/240_Search2DMatrixII.py)


