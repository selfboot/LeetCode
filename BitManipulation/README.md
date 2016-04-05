

## 常用位操作

常用位操作如下：

* 判断奇偶数：num&0x1  
* 丢弃最低位的1：num&(num-1)
* 对一个数变换符号：~num+1
* 对一个数取模(2^N )：num&0b11..1 （N个1）

## 题目

**[338 Counting Bits](https://leetcode.com/problems/counting-bits/)**

正整数中二进制表示中1的个数为count[i]，那么：

    count[i] = count[i>>1] + (i&0x1) // or
    count[i] = count[i&(i-1)] + 1


参考  
[你不知道的按位运算](http://selfboot.cn/2015/09/23/something_about_bit_operation/)  


