虽然刷题一直饱受诟病，不过不可否认刷题确实能锻炼我们的编程能力，相信每个认真刷题的人都会有体会。LeetCode 是一个非常棒的 OJ（Online Judge）平台，收集了许多公司的面试题目。相对其他 OJ 平台而言，有着下面的几个优点：

* 题目全部来自业内大公司的真实面试
* 不用处理输入输出，精力全放在解决具体问题上
* 题目有丰富的讨论，可以参考别人的思路
* 精确了解自己代码在所有提交代码中运行效率的排名
* 支持多种主流语言：C/C++，Python, Java
* 可以在线进行测试，方便调试

在 LeetCode 刷题确实收获不少，锻炼逻辑思维，写代码能力，还有算法水平，[LeetCode 刷题指南（一）：为什么要刷题](http://selfboot.cn/2016/07/24/leetcode_guide_why/) 有详细的讨论。

# 不仅是代码

本仓库主要用来记录自己 LeetCode 上面 AC 的代码，其中很多代码都参考了 Discuss 中选票比较多的代码，效率不会差（时间排名基本都是在 Top 60% 左右）。

代码中还会有简明扼要的解题思路和关键点注释，有较好的可读性。此外，一些题目还提供了多种解决方法，供对比参考。还给出了一些比较有代表性的测试用例，方便快速地调试。比如 337 题，这里给出的代码为：

    class Solution(object):
        """ Dynamic programming,  memory DFS search.
        The problem exhibits the feature of optimal substructure and overlapping of subproblems.
            1. Optimal substructure:  If we want to "rob" maximum amount of money
            from current binary tree (rooted at "root"),
            we surely hope that we can do the same to its left and right subtrees.
            2. Overlapping of subproblems: Computed subproblems repeatedly,
            which resulted in bad time performance.
        More details can be found as bellows:
        https://leetcode.com/discuss/91899/step-by-step-tackling-of-the-problem
        """
        cache = {}
    
        def rob(self, root):
            if not root:
                return 0
    
            if root in self.cache:
                return self.cache[root]
    
            # Rob the root node.
            money = root.val
            if root.left:
                money += self.rob(root.left.right) + self.rob(root.left.left)
            if root.right:
                money += self.rob(root.right.left) + self.rob(root.right.right)
    
            # Do not rob the root node.
            self.cache[root] = max(money, self.rob(root.left) + self.rob(root.right))
            return self.cache[root]
    
    """
    []
    [3,4,5,1,3,null,1]
    [3,2,3,null,3,null,1]
    """

当然，这里也不止是代码。LeetCode 上面题目用到的解题思想和主要的算法其实就那么几种，我对题目进行了一个简单的分类，每类题目放在一个大的目录中，问题归类详情在 [List](List.md) 文件中。注意下面的几个目录：

* `Others`：一些暂时没有找到合适分类的题目；
* `ToBeOptimized`：一些解题方案需要优化的题目；
* `Combination`：一些同时用到多个解题思想的综合型题目。

对某一类下面的问题也会进行简单的总结（还没有完全完成），用来提炼问题的共同点和共同的解题思路，比如回溯法的总结：

> 如果把你放进迷宫，你该怎么走出来？一个比较稳妥地做法是试探法，简单来说就是试探某条路可否到达出口，不可以的话换另一条路。

> 具体来说就是每次遇到岔口，选择一个没有探索过的方向前进，当最终发现这个方向是条死路时，就回到这个岔口，选择另一个没有探索过的方向试探，如果这个路口所有方向都是死路，就回退到上一个路口继续尝试。最终会走出迷宫，或者回到入口（这时候迷宫本来就没有出口）。

> ......

# 一起来完善

你可以指出某个代码的冗余或者错误之处，也可以用更加清晰的解释来对某个代码进行注释。

你还可以完善某个分类下面问题的总结，说出你对某类问题的独到见解，总之可以做的很多。欢迎 Pull Request，让我们一起维护一个比较完善的 LeetCode 代码区。

