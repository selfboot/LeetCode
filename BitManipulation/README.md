

# 常用位操作



其它常用位操作如下：

* 判断奇偶数：num&0x1  
* 丢弃最低位的1：num&(num-1)
* 对一个数变换符号：~num+1
* 对一个数取模(2^N )：num&0b11..1 （N个1）
* 返回 x，y中的最小值：y^((x^y) & -(x < y))


# 例子：更好的理解

## [260 Single Number III](https://leetcode.com/problems/single-number-iii/)

> 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

考虑如果数组里只有一个数字出现一次，其它数字均出现两次，那么可以直接将所有数字异或一遍，最后得到的数字即为只出现一次的数字。现在数组中有两个出现一次的，可以考虑通过`某种手段`将数组分为两部分，每部分中只有一个数字出现一次，其它均出现两次，这样对每部分进行异或就能找到一个数字。

假设 m 和 n 是两个不同的数字，拆分时要将 m, n 放在不同的部分去，同时保证其它数字两次出现在同一个部分中。m, n不同，所以至少有一位是不同的，例如m为0的话n就为1。为了方便，可以找出m, n发生差异所在的最低位k，那么：

    2^k = (m^n) & (-m^n)

求m, n 的异或只需要将数组中所有数字异或一遍即可。划分数组可以根据num&2^k 是否为1的结果。

[具体实现](https://github.com/xuelangZF/LeetCode/blob/master/BitManipulation/260_SingleNumberIII.py)

## [338 Counting Bits](https://leetcode.com/problems/counting-bits/)

> 给定整数 n，返回长度为 n+1 的数组arr，其中arr[i]为 整数i 的二进制表示中 1 的个数。

我们知道计算一个整数二进制表示中 1 的个数可以这样来做，

    while(x){
        count += 1;
        x = x&(x-1); // 将最低位的1置为0
    }

因此，很容易想到利用动态规划的思想来解决这个问题，动态转移方程为：

    ans[i] = ans[i >> 1] + (i&0x1)
    # ans[i] = ans[i & (i - 1)] + 1

[具体实现](https://github.com/xuelangZF/LeetCode/blob/master/BitManipulation/338_CountingBits.py)
        
此外统计一个整数的二进制表示中0的个数可以这样实现：

    while((x+1))
    {
      count++;
      x=x|(x+1);
    }


# 参考  
[你不知道的按位运算](http://selfboot.cn/2015/09/23/something_about_bit_operation/)  
[Leetcode Discuss](https://leetcode.com/discuss/52351/accepted-java-space-easy-solution-with-detail-explanations)  
[位运算简介及实用技巧（一）：基础篇](http://www.matrix67.com/blog/archives/263)  
[位运算简介及实用技巧（二）：进阶篇(1)](http://www.matrix67.com/blog/archives/264)  
[位运算简介及实用技巧（三）：进阶篇(2)](http://www.matrix67.com/blog/archives/266)  
[位运算简介及实用技巧（四）：实战篇](http://www.matrix67.com/blog/archives/268)

