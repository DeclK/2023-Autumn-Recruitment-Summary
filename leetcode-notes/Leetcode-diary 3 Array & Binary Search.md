---
title: Leetcode-diary 3 Array & Binary Search
tags:
  - Leetcode
categories:
  - 编程
  - Leetcode
abbrlink: 6921f8d1
date: 2022-03-21 15:39:28
---

# Leetcode-diary 3 Array & Binary Search

## Binary Search

#### [528. 按权重随机选择](https://leetcode-cn.com/problems/random-pick-with-weight/)

我先使用了 numpy 解决了这个问题，显然这一题需要使用二分查找。具体思路是将随机问题转化为一个在区间之内选择数字的问题

#### [162. 寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)

这一题的二分查找需要对逻辑非常清晰，也就是为什么当 mid 值小于任一邻值时，邻居方向必定有解。并且对于边界的情况需要好好思考，也就是左右不存在邻值。一个优雅的解法是定义一个辅助函数，来返回 -1 和 n 边界的值

#### [410. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/)

使用动态规划会超出时间限制，而且这一题的动态规划也挺绕的，主要是初始化如何进行：关键点为要关注有减号的地方，当这些地方超过了数组的范围，就需要进行初始化或者特殊处理，如果能在循环之外进行初始化就是最好不过的了，二维通常要多1个长度

这一题的最佳解法是二分搜索+贪心算法：假设一个值 x, 判断整个数组能不能分成 m 份, 每一份都小于等于 x，通过二分查找很快就能判定这个值的大小

#### [658. 找到 K 个最接近的元素](https://leetcode-cn.com/problems/find-k-closest-elements/)

先用二分查找到位置，然后使用双指针判断邻居

#### [1011. 在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/)

和410的题目是完全一样的

#### [315. 计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)

不理解...明明写的两种算法时间复杂度应该都是一样的，但写的第一种就是会超时，原因在于每次搜寻的都是最长的数组

## Array

现在重点突击 array & dp，感觉这两个才是大头的考点

#### [442. 数组中重复的数据](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/)

使用数组的下标做标记...第一次碰到，这就是原地哈希。充分利用了数组的范围在 [1, n] 之间这个信息。我的第一个想法还是位运算，在题解里找到一个位运算的解析，其实有一点点 bug，因为 python 的数值是可以无限大的，使用位来记录也有点作弊，但事实上由于计算机的限制，我们依然可以把这里看作 O(1) 空间

#### [581. 最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/)

很容易就想到方法，但是想要弄到 O(N) 需要另外的方法，我首先想到的依然是单调栈，一旦遇到降序的数字就需要维护单调栈，并记录 pop  掉的位置

#### [189. 轮转数组](https://leetcode-cn.com/problems/rotate-array/)

主要是对空间复杂度的要求，可以使用两次翻转数组完成。以后应该养成快速解题的习惯，而不应该拘泥于这些细节，如果感觉这些 trick 没什么帮助，就应赶紧跳过

#### [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

这一题又遇到了原地哈希的概念，在 442 中也是一样的。原地哈希算法主要应用在范围为 [0, len(nums)] 的数组解法中，将数组元素本身作为 `nums` 的下标，即 `nums[nums[i]]`，这将解决空间不足的问题。这一题虽然数字的范围很广，但稍加推测可以知道，答案的解必定在 1~n+1 之间，所以使用原地哈希也是比较自然的。常用的方法是对原始数组进行正负标定，来表征是否在集合中，于此同时在遍历数组的时候，需要使用 abs() 绝对值操作，来获取原始信息

我可以先把负数转换成一个很大的正数，这将不影响答案

#### [845. 数组中的最长山脉](https://leetcode-cn.com/problems/longest-mountain-in-array/)

先尝试了动态规划，但是超时了，用了 N 方复杂度，然后考虑使用栈，花费了比较长的时间，因为思路需要更细致。看了题解：使用两次动态规划，计算数字左侧可扩展的数字和右侧可扩展的数字！又是一题使用多个动态规划结果来解决的，这种题做的比较少

#### [274. H 指数](https://leetcode-cn.com/problems/h-index/)

很明显的就想到了二分查找的思想。但要实现 O(N) 复杂度就需要直接解题，这一题有一个特点，就是 H 指数一定不会超过 N，那么我们就可以使用一个 N + 1 数组进行存储，使用一个数组存储 store[i + 1] 代表值为 i 的次数，其中 store[N] 表示值 >=N 的次数

#### [275. H 指数 II](https://leetcode-cn.com/problems/h-index-ii/)

一个二分查找的题目，看第 k 个数字与其存储值 citations[k] 的大小

#### [220. 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/)

这一题也不太常规，虽然我使用了暴力解法。第一种思路是使用红黑树维护有序数组，但是原生 Python 里没有这样的数据结构，需要使用 [sortedcontainiers](https://grantjenks.com/docs/sortedcontainers/) 这个库...这个库其实用于维护有序数组非常有用，但考虑到笔试面试的时候可能用不上这个库，所以了解一下第二种思路：桶排序。最多使用 k 个桶，每个桶的编号为 m，这个编号代表了数值在 $m \times (t + 1) \sim (m + 1)\times (t + 1) - 1$ 之间的数，使用字典 `bucket` 创建桶，具体思路如下：

1. 从第一个元素开始遍历，假设当前元素为 `num[i]`，计算其所属桶的编号 `m = num[i] // (t + 1)`
2. 查询当前是否存在有桶的编号，如果存在则返回 true，如果不存在则查找相邻编号 `m + 1 or m - 1` 的桶是否存在，如果存在查看桶中元素是否符合 `abs(bucket[m + 1 or m - 1] - num[i]) <= t`，如果存在也返回 true，如果依然不存在则建立新的桶。此时如果桶的个数超过了 k 个，则删除最早建立的桶 `bucker(num[i - k] // (t + 1))`。通过字典能够快速实现新建桶和删除桶

#### [307. 区域和检索 - 数组可修改](https://leetcode-cn.com/problems/range-sum-query-mutable/)

线段树...直接放弃，如果真的需要徒手实现这样的数据结构还是算了吧

#### [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

这一题是一个系列，一起干掉！这一题真正展示了动态规划的本质：一个问题使用动态规划的终极标准就是该问题能否由**一些**子问题（状态）方便解决，而这些子问题又能够通过**递归**方便解决，子问题可以是与原问题不同的问题。通过递归解决子问题（状态）可以有两种方式：1. 状态自身的简单递归；2. 不同状态之间的递归

这一题直接记录最多交易 k 次的情况。我起始思路其实是从思考 k -1 次的情况开始：如果知道到截止到第 j 天的 k - 1 次的情况，通过 n 次循环就能很快得出此问题的答案。然而事实是解决这两个子问题会变得比较复杂，也就是说我们要解决两个问题：

1. `dp_1[i][j]` 代表到第 i 天最多交易 j 次的情况
2. `dp_2[i][j]` 代表第 i 天到第 j 天最多交易1次的情况

这似乎不是一个好的状态定义，尤其是第二个子问题直接需要 n 方的时间复杂度。题解的思路为，如果知道每个时间点的所有买卖状态，就能够知道下一个时间点的所有买卖状态。每个时间点买卖状态有 2 * k + 1个：

0. 第 i 天，最多0次交易，并不持有股票的最大收益
1. 第 i 天，最多0次交易，并持有1支股票的最大收益
2. 第 i 天，最多1次交易，并不持有股票的最大收益
3. 第 i 天，最多1次交易，并持有1支股票的最大收益
4. 第 i 天，最多2次交易，并不持有股票的最大收益
5. ...

该题的难点在于找到合适的状态。由于需要知道前一天是否持有股票才能进行买入卖出，所以需要定义此时买入卖出的状态，这样在更新第 i + 1 天的时候，能够根据昨日的状态更新所有 2 * k + 1 个状态

#### [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

太经典的贪心算法了，使用双指针不断地进行贪心搜索，返回搜索过程中的最大值

#### [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

这一题有多种解法：1. 动态规划；2. 单调栈（维护单调属性）；3. 双指针（动态规划的升级）

重点提一下双指针：因为我们是不断地移动较小指针，所以即使指针中间出现更大/更小的值，也不会对当前较小指针接的水有所影响

#### [128. 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)

虽然需要时间复杂度为 O(N)，但我还是要先实现一个暴力解法，迅速解题，并且暴力解法的时间复杂度并不是很高。接着我就想到了连通的思想，使用一个集合，然后不断地寻找其连通的数字

#### [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

这一题在剑指里面刷过，我再自己写一次，关键是在于维护一个有序数组。首先实现了堆的写法，思路还是比较清晰。但是维护单调性质的数据结构应该首先考虑单调栈，这一题更特殊一点，要维护一个定长的数组，所以需要从栈底删除元素，所以更加自然的就得出了单调队列的方法

#### [295. 数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream/)

一开始题目就理解错了...需要的是有序列表的中位数！之前还在剑指 offer 做过这一题的！使用最大堆维护左边，最小堆维护右边

#### [209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

思路非常的清晰，一个是使用双指针进行滑动窗口，另一个是进行二分查找。二分查找效率更差，不过也是一种暴力解，在调试不出来的时候可以进一步尝试

#### [238. 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self/)

上下三角形存储所需要的乘积。如果需要使用常数存储空间，那么使用一个流转循环的方式即可

#### [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

动态规划，使用两个状态：最大整数，最小负数分析即可

#### [713. 乘积小于K的子数组](https://leetcode-cn.com/problems/subarray-product-less-than-k/)

这里总结了一下双指针的套路：双指针常常与连续/顺序有关, 并且能够通过指针移动方便地更新区间的性质。通常，双指针可以使用两个循环甚至一个循环完成，**先将某个指针移动**，然后进行条件判断(并移动指针)，直到满足/不满足某个条件，进入下一次循环

大多数的循环都应该是如此：需要收尾相接，也就是循环结束的末尾需要和开头对应，初始情况需要特殊处理。换句话说循环的开头需要能够处理初始状况和满足条件的状况！

本题的双指针不太一样，右指针需要按照顺序移动, 左指针将灵活移动

#### [974. 和可被 K 整除的子数组](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/)

直接求前缀和，统计其余数相同的位置，只要余数相等那么他们的差必定是 k 的倍数，并且特殊处理前缀和为0的情况

#### [945. 使数组唯一的最小增量](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/)

我想用 empty 记录一个空缺位置。更好理解的是：直接先排序，然后遇到与前一个数字相等就将其变为前一个数字加一

#### [321. 拼接最大数](https://leetcode-cn.com/problems/create-maximum-number/)

这一题很明显是两道中等题目拼接而来，需要对中等题目有比较高的熟练程度！我很快就解出了一个子问题，但是第二个子问题将两个数字进行拼接这一步解决得不太顺畅。首先让我想到了 offer 45，但实际上二者并没有特别类似，虽然有朦朦胧胧的想法，但是并不精确，题解中直接比较两个字符串的字典序大小，非常好用

#### [402. 移掉 K 位数字](https://leetcode-cn.com/problems/remove-k-digits/)

这是解决上一题的子问题。学习点：**可以使用 strip/lstrip/rstrip 来对字符串前后进行裁切**

#### [403. 青蛙过河](https://leetcode-cn.com/problems/frog-jump/)

动态规划，这一题就是纯粹地从简单推广到复杂，记录到达当前石头的步长，尝试从当前石头向前出发，更新其他石头的状态和步长。再一次清晰了动态规划的核心：建立当前所得状态与未知状态之间的转移方程

#### [1029. 两地调度](https://leetcode-cn.com/problems/two-city-scheduling/)

假设他们都去了同一个地方，看如果他们去另一个地方需要花费多少

#### [986. 区间列表的交集](https://leetcode-cn.com/problems/interval-list-intersections/)

纯纯的递归写法，仅需要不断地判断第一个区间是否相交即可，然后 pop 出尾端较小的首部，继续递归

#### [939. 最小面积矩形](https://leetcode-cn.com/problems/minimum-area-rectangle/)

使用哈希表进行查询，需要使用暴力解法

#### [957. N 天后的牢房](https://leetcode-cn.com/problems/prison-cells-after-n-days/)

这一题比较有意思。因为牢房的数量是恒定的，所以状态是可以穷举的。我只需要知道到哪一个状态过后又回到初始状态，就可以进入循环求解了。这里还运用了字典是按照顺序创建的特性

#### [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

这一题的二分查找挺奇诡哎的...不太好理解，并不是一般的每次排除掉一半的搜索范围，感觉是每次排除 1/4 的搜索范围，不过这样也能够达成指数级的下降。同时还需要处理边界条件 k = 1 or 0 的情况，**代码我没有尝试写过，之后要写一下**

#### [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

和之前的重叠区间是类似的，把握好了重叠条件即可

#### [376. 摆动序列](https://leetcode-cn.com/problems/wiggle-subsequence/)



## Hard

#### [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

首先复习了一下反转链表，都是典型的递归处理，这一题是建立在反转链表之上的。不过此题在解决递归时的基础情况需要进行更进一步的判断：链表的长度是否小于 k。判断过后再进行接下来的反转

#### [85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

这一题是 84 题的升级版本，需要 84 题的结果...关键点在于构建 array。这里是使用一个数组进行更新的形式

#### [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

这一题使用单调栈，可以说是单调栈的本质：寻找左侧/右侧第一个小于/大于某个数的数字。这一题还需要使用”哨兵“变量，增强原数组，这样就能够统一处理，而不用特殊处理开头和结尾

#### [376. 摆动序列](https://leetcode-cn.com/problems/wiggle-subsequence/)

先使用了动态规划，是 N 方复杂度。接着考虑将多次单调的数值去除，使用 O(N) 复杂度

#### [324. 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/)

一个小一个大的进行排序，但是要倒着来排。这里要求时间复杂度 O(N) 可以使用桶排序，因为数值的范围比较小

## 其他

#### [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

并查集常常可以使用深度搜索进行替代，今后遇到并查集，可以先创建一个连通的结构，然后使用深度搜索解决
