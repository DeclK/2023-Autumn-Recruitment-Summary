---
title: Leetcode-diary 1
tags:
  - Leetcode
categories:
  - 编程
  - Leetcode
abbrlink: fc1adef0
date: 2022-03-01 15:39:27
---

# Leetcode-diary 1

diary 1 & diary 2 的目的是了解多种题型，没有深入

## String

### 14 Longest Common prefix

最短写法，妙用 zip 函数

我的写法，使用两个循环

### 58 Length Of Last Word

没有特别好注意的

### 387 First Unique Character in a String

[leetcode link](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

实际测试是可以使用 collections 库，Counter: Dict subclass for counting hashable items. 

### 383 Ransom Note 

[leetcode link](https://leetcode-cn.com/problems/ransom-note/)

### 415 Add Strings 

[leetcode link](https://leetcode-cn.com/problems/add-strings/)

### 205 Isomorphic Strings

[leetcode link](https://leetcode-cn.com/problems/isomorphic-strings/)

我的解法是先建立两个字典，然后逐对匹配，如果两者非空，则进行匹配；如果两者均以匹配，则看匹配是否一致；如果仅一个匹配则配对失败

另一种解法是单向匹配做两次，也能成

还有一种更简洁的写法是使用 map 函数，**一行解决** `return list(map(s.index, s)) == list(map(t.index, t))`

### 451 Sort Characters By Frequency

[leetcode link](https://leetcode-cn.com/problems/sort-characters-by-frequency/)

使用 `most_common()` 将其按照出现频率顺序排列，还可以指定参数能够输出 Top k 个词

### 294 Flip Game ii

这一题竟是会员题...那就只能看看题目，再看看其他解答了！有趣的是这一题需要一点点博弈论的知识，能更好的理解 [知乎](https://zhuanlan.zhihu.com/p/21300536)。代码参考 [CSDN](https://blog.csdn.net/qq_32424059/article/details/100765272)，既然每一种状态都有确定的输赢，那么使用递归去求解是再适合不过的了。定义递归问题：当前状态为必胜状态 

### 290 Word Pattern

[leetcode link](https://leetcode-cn.com/problems/word-pattern/)

这一题和之前的 205 同质字符串是一样的题，考察一个一一对应的问题，**最短写法：妙用 map 函数**

自己的写法。区别在于 205 有一个条件：两个字符出串的长度相等，这一题没有，在一开始判断即可，如果不满足直接判负

### 38 Count and Say

[leetcode link](https://leetcode-cn.com/problems/count-and-say/submissions/)

用迭代思维求解

用递归思维求解：

### 316 Remove Duplicate Letters

[leetcode link](https://leetcode-cn.com/problems/remove-duplicate-letters/)

一开始还是想使用动态规划来做这一题，但发现这题并不适合使用动态规划，因为其最优子结构之间并不存在关系，也就是无后效性。这题的本质在于：遍历时舍弃与保留数字的条件：

1. 为保证顺序性采用顺序遍历
2. 为保证不重复性，当当前数字已存在于已保留的数字中时舍弃当前数字，若不存在则保留当前数字
3. 当前数字小于前一个保留数字，并且之后仍会出前一个保留数字时，则舍弃前一个保留数字。这一步骤是整个题的核心，因为这保证了递减
4. 循环2，至到不舍弃前一个保留数字，此时保留当前数字，并遍历下一个数

这样的条件是否能够获我们想要的结果呢？很多算法题并没有给出各种算法的数学证明，只是一种直觉性的介绍，我认为需要证明在这样条件之下所保留的答案就是最终答案。使用反证法，该条件满足顺序性，也满足不重复性，只需要证明最小即可：

假设原序列为 $a=\{a_1, a_2,...,a_n\}$ 使用该方法获得的子序列为 $z=\{z_1,z_2,...,z_k\}$，若存在更小的序列 $z'=\{z_1,z_2,...,z_j,z_i,...\}$，具体来说就是将数字 $z_j$ 放到数字 $z_i$ 之前，显然有 $z_i>z_j\ (i<j)$，为保证这个序列 $z'$ 的任意性，$z_i$ 之后的数字可以时任意排列的。下面证明这样的序列是不存在的：

假设 $z_{i-1},z_i,z_j$ 在原序列中分别对应 $a_p,a_q,a_m\ (p<q<m)$。考虑使用算法获得的子序列得出：我们舍弃了 $p, q$ 之间的原序列 $\{a_p,a_{p+1},...,a_q\}$；再由假设序列得出：$a_m$ 存在于 $p,q$ 之间。**由两个推论得出：$a_m$ 存在于 $p,q$ 之间并被舍弃**，这个结论是不成立的！

 因为 $a_m$ 并不属于之前所保留的集合 $\{...,z_{i-1}\}$，当 $a_m$ 第一次出现时，一定会被作为保留数字留下来，所以要在之后舍弃 $a_m$ 则之后必须出现保留数字 $a_x$，该数字满足 $a_x < a_m$ 且 $a_x \notin \{...,z_i\}$，而 $a_x$ 也必须被舍弃，如此往复当遍历到 $a_q(=z_i)$ 时，最后一个 $a_x$ 将无法被舍弃，因为 $a_x < a_m = z_j < z_i=a_q$ 与推论矛盾，所以这样的序列 $z'$ 不存在

```python
# empty
```

### 539 Minimum Time Difference

[leetcode link](https://leetcode-cn.com/problems/minimum-time-difference/)

先进行升序排序即可

## Binary Search 

### 704 Binary Search 

[leetcode link](https://leetcode-cn.com/problems/binary-search/)

写了两种写法，一种是直接用列表自带的功能，另一种就是朴素的二分查找

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        # 终止条件
        while begin <= end:
            # 二分
            mid = (begin + end) // 2
            # 判定
            if nums[mid] == target:
                return mid
            # 更改搜索范围
            if nums[mid] > target:
            	end = mid - 1
			else:
            	begin = mid + 1
        return -1
```

总结：

1. 搜索范围一定要包含目标值，且要不断地缩小，这样才能够满足终止条件而不陷入死循环
2. 当目标超出了整个数组范围，二分搜索可能需要要特殊处理的
3. 当 begin & end 相邻的时候，情况会变得复杂一点，但是这个过程需要更清晰才能写好代码。以此题为例，此时 target 有两种情况：begin & end 的二者之一或者二者之间。下面具体分析一下最后的细节：
   1. 继续二分计算，mid 会因为整除操作而等于 begin
   2. 如果 begin 就是 target 则结束
   3. 如果 begin 不是 target 则说明 `nums[mid] < target` 即 `nums[begin] < target`，执行 `begin = mid + 1`
   4. 继续二分计算，mid 会因为整除操作而等于 end
   5. 如果 end 就是 target 则结束
   6. 如果 end 不是 target 则说明 `nums[mid] > target` 即 `nums[end] > target`，执行 `end = mid - 1`
   7. 此时 begin > end，循环结束
4. 判定条件一定要清晰

### 278 First Bad Version

[leetcode link](https://leetcode-cn.com/problems/first-bad-version/)

不知道 `isBadVersion()` 能不能判断 0 版本，所以先判断一下初始版本，好在之后统一写起来

### 35 Search Insert Position

[leetcode link](https://leetcode-cn.com/problems/search-insert-position/)

注意处理一下初始值问题（边界）就好

### 33 Search in Rotated Sorted Array

[leetcode link](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

我首先的想法是使用3次二分搜索解决问题，但我先偷个懒，写了第一种写法🤣效果也还不错，可能是因为 N 不够大，所以二叉搜索的优势显现不出来

题解使用了更简洁的代码，思想就是将范围转移讨论得更加清晰，根据 target & nums[mid] 和 nums[0] 的关系判断

### 153 Find Minimum in Rotated Sorted Array 

[leetcode link](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

调用上一题写的函数就可以了，当然最暴力的还是排序啦

### 154 Find Minimum in Rotated Sorted Array ii

[leetcode link](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

这里需要处理的是重复值，当有重复值存在时，则不能盲目缩小一般搜索范围，而是让仅往前走一步即可。我让 begin 向右走一步，但这可能会导致 begin 落入右侧范围，这时说明 begin 即为所求值 index

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_point(nums: List[int]):
            begin, end = 0, len(nums) - 1
            # 边界处理，否则目标超出搜索范围
            if nums[begin] < nums[-1]:
                return 0
            while begin <= end:
                mid = (begin + end) // 2
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    return mid + 1
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    return mid
                # 判断在哪一边
                if nums[mid] > nums[0]:
                    begin = mid + 1
                elif nums[mid] < nums[0]:
                    end = mid - 1
                else:
                # 如果 begin 仍然在左侧
                    if nums[begin] >= nums[0]:
                        begin += 1
                # 如果 begin 在右侧
                    else:
                        return begin
            # 只有一个数的情况
            return 0
        return nums[find_point(nums)]
```

## LinkedList

### 876 Middle of the Linked List 

[leetcode link](https://leetcode-cn.com/problems/middle-of-the-linked-list/)

### 21 Merge Two Sorted Lists

[leetcoke link](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

竟然没有马上想到递归，还是练习得不够啊

### 160 Intersection of Two Linked Lists

[leetcode link](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

从尾部开始遍历，比较好判断

### 24 Swap Nodes in Pairs

[leetcode link](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

依然是递归思想

### 2 Add Two Numbers

[leetcode link](https://leetcode-cn.com/problems/add-two-numbers/submissions/)

比较笨的方法就是按照一般思维，先得到数字再相加，再创建链表

更好的办法还是用递归的方法，这其实才是我看到这题的第一想法

## Array

### 27 Remove Element

[leetcode link](https://leetcode-cn.com/problems/remove-element/)

使用双指针的思想，“删除”不一定是真的删除。因为删除是很耗时的，但是实际使用来看，我用 remove 也能够达到同样的速度。leetcode 的服务器多次运行可能有不同的结果

### 26 Remove Duplicate from Sorted Array

[leetcode link](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

### 53 Maximum Subarray

[leetcode link](https://leetcode-cn.com/problems/maximum-subarray/)

这题一开始我想要使用递归的思想来解决，递归的数学模型其实就是数学归纳法：中止条件（推倒第一块积木） + 利用假设解决问题（多米诺效应）

但是似乎不能够通过归纳法简单地得出结论，我定义假设：已知序列 nums[:k] 的和及其开始位置，那么序列 nums[:k+1] 的连续最大和及其开始位置在哪里。**解析：使用动态规划**

动态规划其实是一个很大的研究领域，我认为之后有必要好好总结这个思想（recursive + momoization）。动态规划有几个关键概念：

1. 状态

2. 状态转移方程

3. 初始化

4. 无后效性：如果之前的阶段求解的子问题的结果包含了一些不确定的信息，导致了后面的阶段求解的子问题无法得到，或者很难得到，这叫「有后效性」

   解决「有后效性」的办法是固定住需要分类讨论的地方，通常有两个解决方法：

   1. 状态数组增加维度
   2. 把状态定义得更细致、准确

```python
# empty
```

## Matrix

### 74 Search a 2D Matrix

[leetcode link](https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix/)

这一题想使用 numpy 来做，但速度比较慢，可能因为 import 的原因

### 240 Search a 2D Matrix ii

[leetcode link](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/submissions/)

第一个直观的想法就是二分查找

但直觉感觉复杂度应该在 O(m + n) 所以还有更好的搜索方法，又想到一个方法：重视对角。因为对角是最小和最大值，先看 target 值在哪个区间，然后就去对应的区域搜索。但实现起来过于复杂，看题解是从右上角开始搜索，这的确更好

 ## Math

### 15 3Sum

[leetcode link](https://leetcode-cn.com/problems/power-of-three/)

算法时间复杂度为 O(1)，或者使用 log 逆运算

### 18 4Sum

[leetcode link](https://leetcode-cn.com/problems/power-of-four/)

类似于 3sum

### 560 Subarray Sum Equals K

[leetcode link](https://leetcode-cn.com/problems/subarray-sum-equals-k/submissions/)

前缀和 + 哈希表查找

## Tree

#### [95. 不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/) MARK 2

重新做了这一题，感觉还是挺难的。一开始卡在了使用深度搜索的方法上，如何去维护一个搜索的路径，这将会变得比较苦难。一段时间过后放弃，还是选择使用递归的方法，利用二叉搜索树的特性：知道了左侧子树和右侧子树的所有二叉搜索树，就能够通过两两组合获得最终的二叉搜索树。要注意的一个点是，需要在循环之内创建新的根节点，我两次都犯了这个错误，重复使用了根节点

#### [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) MARK 2

前序遍历：根节点，左，右

中序遍历：左，根节点，右

后序遍历：左，右，根节点
