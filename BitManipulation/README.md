

## 常用位操作




其它常用位操作如下：

* 判断奇偶数：num&0x1  
* 丢弃最低位的1：num&(num-1)
* 对一个数变换符号：~num+1
* 对一个数取模(2^N )：num&0b11..1 （N个1）

## 题目

### [260 Single Number III](https://leetcode.com/problems/single-number-iii/)

> 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

考虑如果数组里只有一个数字出现一次，其它数字均出现两次，那么可以直接将所有数字异或一遍，最后得到的数字即为只出现一次的数字。现在数组中有两个出现一次的，可以考虑通过`某种手段`将数组分为两部分，每部分中只有一个数字出现一次，其它均出现两次，这样对每部分进行异或就能找到一个数字。

假设 m 和 n 是两个不同的数字，拆分时要将 m, n 放在不同的部分去，同时保证其它数字两次出现在同一个部分中。m, n不同，所以至少有一位是不同的，例如m为0的话n就为1。为了方便，可以找出m, n发生差异所在的最低位k，那么：

    2^k = (m^n) & (-m^n)

求m, n 的异或只需要将数组中所有数字异或一遍即可。划分数组可以根据num&2^k 是否为1的结果。

具体代码在 

### [338 Counting Bits](https://leetcode.com/problems/counting-bits/)

> 整数的二进制表示中0（或者1）的个数
 
实现如下：

    int count_0(int x)
    {
        int n=0;
        while((x+1))
        {
            n++;
            x=x|(x+1);
        }
        return n;
    }
    
    int count_1(int x)
    {
        int n=0;
        while(x)
        {
            n++;
            x=x&(x-1);
        }
        return n;
    }


# 参考  
[你不知道的按位运算](http://selfboot.cn/2015/09/23/something_about_bit_operation/)  
[Leetcode Discuss](https://leetcode.com/discuss/52351/accepted-java-space-easy-solution-with-detail-explanations)

