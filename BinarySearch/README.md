`二分查找算法`（binary search）是一种在有序数组中查找某一特定元素的算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半，因此时间复杂度为 logn。

![][1]

算法看起来十分简单，但要注意相关的几个问题：

* 递归还是迭代？
* 递归实现时，检查参数的有效性（low/high参数）；
* 计算二分查找中的中值时防止溢出；
* 如何查找第一个/最后一个等值？
 
# 简单实现

下面来看下简单二分查找（数组中不包含重复数字）的两种实现方案。

递归实现如下：

    // 在 nums[begin, end) 中查找 target
    int binary_search(const vector<int> &nums, int begin, int end, int target){
        if(begin<0 || begin>=end || end>nums.size()){
            return -1;
        }
        int mid = begin + (end-1 - begin)/2;
        if(nums[mid] > target){
            return binary_search(nums, begin, mid, target);
        }
        else if(nums[mid] < target){
            return binary_search(nums, mid+1, end, target);
        }
        else{
            return mid;
        }
    }

循环实现如下：

    int binary_search(const vector<int> &nums, int target){
        int left = 0;
        int right = nums.size() - 1;
        while(left <= right){
            int mid = left + (right-left) / 2; // 防止溢出
            // int mid = (left+right)/2  
            if(nums[mid] > target){
                right = mid - 1;
            }
            else if(nums[mid] < target){
                left = mid + 1;
            }
            else{
                return mid;
            }
        }
        return -1; // 没有找到target
    }

# 题目

### [74 Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

> 在一个二维数组中，每一行都按照从左到右递增的顺序排序，且每一列第一个数字都比上一列最后一个数字大，判断该二维数组中是否存在给定的数字。如下例子   

>   [1,   3,  5,  7],  
>   [10, 11, 16, 20],  
>   [23, 30, 34, 50]    

将二维数组看做是排好序的一维数组，然后按照一般的二分查找即可。注意left,right 开始值分别为 0, rows*cols-1，mid 的坐标为 (mid/cols, mid%cols)。

[具体实现]()

### [240 Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

> 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列也是按照从上到下的顺序递增，判断该二维数组中是否存在给定的数字。如下例子：

> [1,   4,  7, 11, 15],  
> [2,   5,  8, 12, 19],  
> [3,   6,  9, 16, 22],  


