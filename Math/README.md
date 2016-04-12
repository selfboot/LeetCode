


# 题目

### [223 Rectangle Area](https://leetcode.com/problems/rectangle-area/)  

> 计算平面坐标系中两个矩形覆盖的面积。注意两个矩形有可能相交，相交部分面积只能算一次，其中给出了每个矩形的左下角和右上角的坐标。

下图为矩形的可能情况：

![][1]

解决问题关键在于假设矩形相交，然后找出重合的小矩形的左下角坐标和右上角坐标，判断这两个坐标是否能够构成矩形。
    
    // 假设两个矩形相交，重合矩形的坐标如下
    int left = max(A, E);
    int bottom = max(B, F);
    int right = min(C, G);
    int top = min(D, H);

矩形相交的条件为 `left < right && bottom < top`。






[1]: ../Images/223_rectangle_area.png

