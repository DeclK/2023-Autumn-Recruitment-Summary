---
title: Leetcode-diary 4 String
tags:
  - Leetcode
categories:
  - 编程
  - Leetcode
abbrlink: 984b9f00
date: 2022-03-01 15:39:28
---

# String

对 string 类的题目进行深度学习，重点总结方法，过多的代码就不放出来了

### 556 Next Greater Element |||

[leetcode link](https://leetcode-cn.com/problems/next-greater-element-iii/)

这一题的代码写的也是相当丑，题目中其实有两个要求，相当于是求最大中的最小，我在解题的时候没有考虑全，所以修改了较长的时间。这种最大中的最小基本上都有一个单调栈的感觉在里面：数列必须是单增的，遇到第一个减少的数字则是关键点！

学习点：简易的将字符串列表转为数字的方法

```python
int(''.join(list_of_str))
```

### 395 Longest Substring with At Least K Repeating Characters

[leetcode link](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/)

又是一个与子序列相关的问题，一般有几种思路：递归，动态规划，通过条件不断地扩充解或者剔除不满足的成员（这几种思路也可能相互重叠）。一开始选择了不断扩充的方法，但是会遗漏部分的解。在此基础之上很快就延申出了递归的思路迅速求解了：递归地剔除不满足的数字

### 419 Battleships in a Board

[leetcode link](https://leetcode-cn.com/problems/battleships-in-a-board/)

这一题我使用了连通的想法，既然不相邻，那么连通的 X 就是一个战舰。另一个进阶的想法是统计左上角 X 的个数

### 151 Reverse Words in a String

[leetcode link](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

两行代码写完：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        print(s.split())
        return ' '.join(s.split()[::-1])
```

注意这里使用的是 `split()` 而不是 `split(' ')`，二者有着细微的差别，如果有多个空格存在的话，后者分隔后会多出一些空字符串成员 `''`，而前者不会

### 5 Longest Palindromic Substring

[leetcode link](https://leetcode-cn.com/problems/longest-palindromic-substring/)

这一题给了我一个教训，如果长时间想不到好的方法，如果有一个平方时间复杂度的想法也应该尽快实现！这一题采用中心扩展法

### 516 Longest Palindromic Subsequence

[leetcode link](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)

动态规划又给我上了一课：

1. 什么是状态：在确定条件下的问题的解（即子问题的解），并且状态需要是唯一的（或者说最优的）
2. 状态转移：不同条件下的子问题之间的关联，这就是这一题的难点。状态转移的方向我习惯性地认为是两个状态之间的转移，实际上，一个复杂状态是由多个可能的子状态转移而来
3. 状态转移的着力点在于：从简单到复杂的推演过程，或者从复杂到简单的退化过程

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        # 不能用 [[0] * n] * n 因为这样列表中的成员指向的是同一个

        # 注意遍历顺序，需要从短到长的遍历，并且有一个倒序
        for j in range(0, n):
            dp[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
```

### 647 Palindromic Substrings 

[leetcode link](https://leetcode-cn.com/problems/palindromic-substrings/)

这一题就是求出字符串中所有的回文字符串，这一题相当于第5题。我顺便使用动态规划把这一题给完成了，即判断某个字串是否是回文字符串

### 336 Palindrome Pairs 

[leetcode link](https://leetcode-cn.com/problems/palindrome-pairs/)

显然不可能使用平方时间去做，这样的话大概率需要做 N 次，也就是说对每一个成员进行分析，根据分析结果将其分配到其属于的地方，而这个分配过程是一个 O(1) 的时间，这显然就需要用到字典，因为只有字典的查询时间才是最快的

这一题的虽然大体思路很快就拿出来了，但是其中的细节太多了，比如：如何找到需要的字串，使用前缀后缀的思想最快；遇到相同长度的会重复计算...

### 115 Distinct Subsequences

[leetcode link](https://leetcode-cn.com/problems/distinct-subsequences/)

使用了两种方法，第一种是递归的思路，很快就实现出来了，但是复杂度没有经过仔细考虑，答案超时。马上开始动态规划的思路，很快就联想到了增加状态的思路，也很快实现出来了，不过还是有一些边界条件需要进行考虑，没有考虑清楚。这里依然使用了与之前相同的策略：使得表格中的最左侧初始化为1

### 334 Increasing Triplet Subsequence 

[leetcode link](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)

这一题并不是特别常规，一开始想用单调栈，但后面发现单调栈并不好维护。之后直接通过三元组的特性解决了

### 32 Longest Valid Parenthese

[leetcode link](https://leetcode-cn.com/problems/longest-valid-parentheses/)

这一题首先想到的就是用动态规划来做，但是转移方程的讨论比较别扭，最终使用栈的方法来匹配括号，留下未匹配的括号，最后求得最长间隔即可

### 301 Remove Invalid Parentheses

[leetcode link](https://leetcode-cn.com/problems/remove-invalid-parentheses/)

这一题竟然是直接用的搜索算法！大失误大失误，因为题目给的字符串长度是比较小的，几乎只能穷举，最终使用深度搜索完成

深度搜索又有了新的解题框架：在计算各种路径的时候，一个直观考虑是某个数字是否被选进路径当中，这样就省下一些循环，只需要记录搜索位置和路径即可

### 443 String Compression

[leetcode link](https://leetcode-cn.com/problems/string-compression/)

这一题好像服务器的判定方法有点不一样，需要点击右下角的执行代码能够看到结果。好像也需要原地修改数组

### 820 Short Encoding of Words 

[leetcode link](https://leetcode-cn.com/problems/short-encoding-of-words/)

这一题的题目描述真的很糟糕，理解了好几次才发现与顺序无关，如果发现理解错误过后应当从头来过，看有没有更简单的解法

最后通过总结其融合的规律，看一个字符串是否能否被融合

### 49 Group Anagrams

[leetcode link](https://leetcode-cn.com/problems/group-anagrams/)

这一题差一点又被这个异位词的概念给误导了。学习点：

1. 字符串是可以被 `sorted` 的，返回一个排好序的列表
2. 字典和列表等可变类型是不可以作为关键字的
3. `collection.defualtdict` 可以解决由于不存在关键字产生的报错，当关键字不存在时直接创建定义好的数据类型

### 3 Longest Substring Without Repeating Characters 

[leetcode link](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

双指针滑动窗口，没啥好说的

### 76 Minimum Window Substring

[leetcode link](76 Minimum Window Substring)

这也是典型的思路简单，但是写起来有比较多的细节的困难题。很容易就想到了双指针滑动窗口的写法，但是依然犯了很多错

### 1004 Max Consecutive Ones |||

[leetcode link](https://leetcode-cn.com/problems/max-consecutive-ones-iii/)

依然是双指针滑动窗口，滑动滑动！似乎双指针的特点：左右两端能够以清晰的条件进行移动，在过程中能够遍历出所有值，并求得最优

一路整下来还是挺伤的...之后不太能把每个板块都刷了...还是重点突击一下剑指offer吧！之后的秋招有时间再继续弄弄