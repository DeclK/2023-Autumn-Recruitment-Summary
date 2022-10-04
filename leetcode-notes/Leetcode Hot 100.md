---
title: Leetcode-diary Hot 100
tags:
  - Leetcode
categories:
  - 编程
  - Leetcode
abbrlink: e1eb0c73
---
# Leetcode Hot 100

[Leeetcod Hot 100](https://leetcode.cn/problem-list/2cktkvj/)

#### [10. 正则表达式匹配](https://leetcode.cn/problems/regular-expression-matching/)

这一题卡了我挺久的，很早就把状态方程给写出来了，但是在循环的时候不能很清晰地得到循环的方式...

现在理清思路过后总结一下，如何比较顺利找到正确的状态转移方程，并且获得遍历状态的方式得到最终结果：

1. 动态规划有时候像是一种抽象/复杂的分类讨论。得益于递归的性质，我们大多数情况不需要对所有之前的状态进行分析，只需要讨论一些比较近的过去状态就可以了，也即我们知道了这些过去状态就能够解决当前状态。如何去寻找这些过去状态，是一个比较麻烦的问题

   ```mermaid
   graph LR
   	x1((x1))
   	x2((x2))
   	x3((x3))
   	x4((x4))
   	x5((x5))
   	x6((...))
   	x1 --> x3
   	x2 --> x3
   	x3 --> x5
   	x4 --> x5
   	x2 --> x4
   	x3 --> x4
   	x4 --> x6
   	x5 --> x6
   ```

   在此简单写一个启发思路：先找到距离当前状态最优解最近的子最优解，这些子最优解对应的过去状态应该就是我们要重点关注的。因为这些子最优解距离最优解已经很近了，其中的可提升空间已经很少，讨论这些子最优解在对应状态下转移到当前最优解的情况，往往就能解决当前状态的最优解

2. 另一个难点在于状态循环，如果得到我们最终需要的答案。上一步是宏观上的递归思维，那么这一步我们就要回到微观的递归思维，也就是要彻底的递归，直到找到迭代的起点

   得到了状态转移方程后，我们就知道了当前的状态需要获得哪些过去状态完成转移，而我们只需要找到最少需要的过去状态，并且以此递归回去，就能够清晰的找到迭代路径了。说的太玄了，就拿这一题来距离吧

   ```python
   class Solution:
       def isMatch(self, s: str, p: str) -> bool:
           n = len(s)
           m = len(p)
           dp = [[False] * (m + 1) for _ in range(n + 1)]
           dp[0][0] = True
   
           def match(index_j, index_i):
               if p[index_j] == s[index_i]: return True
               if p[index_j] == '.': return True
   
           for i in range(n + 1):
               for j in range(1, m + 1):
                   index_i = i - 1
                   index_j = j - 1
                   if p[index_j] == '*':
                       if match(index_j - 1, index_i):
                           dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or dp[i - 1][j]
                       else:
                           dp[i][j] = dp[i][j - 2]
                   else:
                       if match(index_j, index_i):
                           dp[i][j] = dp[i - 1][j - 1]
                       else:
                           dp[i][j] = False
           return dp[n][m]
   ```

   状态转移方程在代码中显示的很清楚，有多个子状态需要考虑。如果要得到 `dp[i][j]` 我们必然需要知道 `dp[i][j - 1], dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]` 这些状态的值。实际上我们只需要知道 `dp[i][j - 1]` 或者 `dp[i - 1][j]` 的值就可以了，为什么？以 `dp[i][j - 1]` 为例，当我们知道了它的状态后，根据递归的假设，我们也就知道了所有 `dp[0~i][0~j-1]` 的所有状态，其他的子状态也就不攻自破了。也就是说有一条迭代路径是从 0 开始一直迭代到 j 的。同理我们也可以得到另一条循环路径是从 0 迭代到 i 的。为了得到所有的状态，两条循环路径必须相互嵌套，这就能得到上面的代码了

#### [15. 三数之和](https://leetcode.cn/problems/3sum/)

用两重循环+字典查询解决

#### [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

本应该用队列来做的，但是没有显示地使用

#### [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)

基础栈

#### [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)

准备使用暴力求解

#### [31. 下一个排列](https://leetcode.cn/problems/next-permutation/)

这一题有几个细节要注意：1. 逆向开始，找到最先减小的数字；2. 找到比这个数字最大的最小数字；3. 交换这两个数字，然后顺序排列

#### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

偷懒，用 bisect 写好了

#### [39. 组合总和](https://leetcode.cn/problems/combination-sum/)

一开始想着用动态规划的思路，但是这一题要把路径给返回，所以考虑了深度搜索

#### [46. 全排列](https://leetcode.cn/problems/permutations/)

使用深度搜索，中间嵌套一个循环

#### [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/)

本来想用动态规划，结果超时。还是要根据题目的性质来判断：看看当前位置是不是最远的

#### [62. 不同路径](https://leetcode.cn/problems/unique-paths/)

本来想用深度搜索，结果超时。慢慢静下心来分析动态规划的循环特点，从对角开始循环

#### [72. 编辑距离](https://leetcode.cn/problems/edit-distance/)

一道困难的动态规划问题。一开始思考的时候就发现与最大匹配字串有点关系，但是实际上关系没有那么大，所以想着以最后一个字符串相同作为增加的状态来判断 `dp[i][j]` 的解。

#### [75. 颜色分类](https://leetcode.cn/problems/sort-colors/)

多亏了快速排序里的 partition，能够很快地掌握交换代码

#### [78. 子集](https://leetcode.cn/problems/subsets/)

深度搜索

#### [79. 单词搜索](https://leetcode.cn/problems/word-search/)

其实是比较困难的一道题。使用遍历+深度搜索解决

#### [96. 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/)

使用递归的方法，左侧数量乘以右侧数量，然后再求和。这也是不同二叉树形态的数量。如果是求不同二叉树的数量，则再乘以 n 的阶乘

#### [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)

使用递归，检查左右子树是否相等，递归的时候注意左右侧要反着来

#### [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

使用 `collections.deque` 方便遍历

#### [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

递归构造，不断地获得左右子树的前序与中序

#### [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

比较直接的方法就是用 O(n) 复杂度。也可以使用后序遍历，然后记录每一个节点的后续节点，在后序遍历时就把后续节点接到右边，并删除左侧

#### [136. 只出现一次的数字](https://leetcode.cn/problems/single-number/)

比较明显的异或运算

#### [139. 单词拆分](https://leetcode.cn/problems/word-break/)

使用动态规划解决，一开始想要用二维，后来发现不需要用二维。直接去讨论什么情况下 s[:i] 的结果会为 true，就是在去掉某个单词过后仍能能匹配

#### [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

使用两次相遇解决。快慢指针第一次相遇 slow 走了 nb 次，而 fast 走了 2nb 次，因为 `f = s + nb & f = 2s`

而从 head 开始走 `a + nb` 次就一定到达环形入口。而快慢指针在第一次相遇时已经走了 nb 次，所以只要再放一个指针在 head，二者同时开始走，并且速度相同，二者一定会在环形入口相遇

#### [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

这一题要使用双端链表，这里使用双端队列勉强替代一下

#### [148. 排序链表](https://leetcode.cn/problems/sort-list/)

用暴力法完成了

#### [155. 最小栈](https://leetcode.cn/problems/min-stack/)

要以常数时间获得最小值，就需要维护每个状态时的最小值列表即可

#### [169. 多数元素](https://leetcode.cn/problems/majority-element/)

摩尔投票法。有一种对波的感觉，对波为零过后重新开始

#### [198. 打家劫舍](https://leetcode.cn/problems/house-robber/)

简单的动态规划

#### [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

使用深度搜索去标记标记岛屿，然后遍历每个位置获得岛屿数量

#### [207. 课程表](https://leetcode.cn/problems/course-schedule/)

一道经典的拓扑排序问题。我先找到图中的无父节点的节点，然后消除这些父节点以及与子节点的连接。如果到最后找不到无父节点的节点，并且还有节点剩余那么就不符合要求

可以使用队列广度搜索来优化，使用一个字典记录节点关系，使用一个数组记录出入度（方便获得无入度节点），使用一个数组记录是否访问过

#### [208. 实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/)

TODO

#### [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

使用快搜复习了一次

#### [221. 最大正方形](https://leetcode.cn/problems/maximal-square/)

使用比较暴力的动态规划，直接找以该位置为最大正方形的右下角的可能。该边长有3个制约条件，一个是左上一格的最大正方形，一个是其最长左侧，一个是最长上侧

实际上直接考虑 `dp[i][j-1] & dp[i-1][j]` 就能够考虑最长左侧和最长上侧了

这一题也让我联想到了最大矩形，但二者的解题思路是完全不一样的。最大矩形使用的使用的时单调栈，当然也可以用（类似接雨水）动态规划解决

#### [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

简单递归

#### [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/)

动态规划，减去某个平方数需要最少多少个平方数

#### [283. 移动零](https://leetcode.cn/problems/move-zeroes/)

双指针，类似于快排

#### [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)

想到了二分查找的方法，符合时间复杂度和空间复杂度。但是可以用双指针变为 O(N) 时间复杂度

#### [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

很快就得出了 O(N^2) 的动态规划答案。最优还可以用二分查找进行优化，有点双重动态规划的感觉🤣维护一个列表：长度为 i 的最长子序列的末尾最小值，这个列表一定是单增的，可以使用二分查找

#### [309. 最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

和其他的股票题是一样的，只要讨论清楚了前一天的股票状态就能够轻松动态规划

#### [297. 二叉树的序列化与反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)

一道考验层序遍历的题，只要注意考虑负数就好。不太熟悉的是反序列化，依然是把握住入队出队的时机就好。序列信息和二叉树的出入队不在同一个节奏，序列信息会先出队一个，其出队主要是用于构建子树

#### [312. 戳气球](https://leetcode.cn/problems/burst-balloons/)

这一题要用 O(N^3) 的复杂度去处理，没有其他的捷径。动态规划的状态确定的比较巧妙，我们要让某个气球最后爆，这个球最后爆的时候需要确定两侧的状态，这个时候使用空区间去定义状态会很方便，也是比较自然的推理。这样在球子区间的最优解时也不会遇到两侧状态未知的状态。为了更好地适应空区间，还可以直接在数组两侧 pad，这样就不用讨论边界情况

#### [322. 零钱兑换](https://leetcode.cn/problems/coin-change/)

这一题我的状态定义太过于复杂了，搜索的时间老是搜爆了。一开始定义使用 i 个硬币和为 j 所使用的最少硬币数，现在反过头来看，这个定义就很有问题！！正确的定义方式就是和为 j 所使用的最少硬币数量，然后再使用动态规划

#### [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/)

二叉树版本，直接递归解决

#### [338. 比特位计数](https://leetcode.cn/problems/counting-bits/)

先用暴力法快速解决。可以使用动态规划来解决，基本的关系为 `dp[j] = dp[i] + 1` 其中 j 比 i 多正好一个1，从数值来看就是多 $2^n$ 个数。给定 j，找到 i 就可以了。这个也很好找 `i = j & (j - 1)`

#### [394. 字符串解码](https://leetcode.cn/problems/decode-string/)

不是括号匹配的解法，但思路差不多。遇到反括号过后往前找，找到前括号过后获得子串，重复子串，然后继续往前走

#### [399. 除法求值](https://leetcode.cn/problems/evaluate-division/)

先建立一个双向连接的图，两个节点是能够互相到达的。从一个节点出发，能够到达另一个节点，就有解。这就需要深度搜索来完成

#### [406. 根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/)

先想到了 O(N^2) 的解法，从大到小依次处理，因为把小的往前移动，不会影响前面大数的判断。这里有一个小技巧，不需要写自定义的函数，元组是可以比较大小的！

#### [416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

这个和很容易找到，一开始想用深度搜素去做，应该马上反应过来会超时。于是思路就集中到动态规划上面，状态为 `dp[i][j]` 表示使用前 i 个数，和为 j 的可能性

#### [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

首先是判断两个字符串是不是异位词，这个是常数时间复杂度，知道这个了过后就可以滑动窗口顺序遍历了

#### [448. 找到所有数组中消失的数字](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/)

常规做法很简单，要使用 O(1) 空间复杂度无非就几个选择：1. 双指针；2. 原地运算；3. 把数组当作字典来用

这一题就恰好可以使用 3 这个方法。不断地去把数字放到它该去的地方

#### [461. 汉明距离](https://leetcode.cn/problems/hamming-distance/)

标准的位运算题目，`&1` 就可以得到尾数，然后不断平移 `>>` 即可

#### [494. 目标和](https://leetcode.cn/problems/target-sum/)

动态规划其实思路很简单，但是要做一些坐标系转换。明明使用深度搜索不会超时的...

#### [538. 把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

使用的比较粗糙的方法

#### [617. 合并二叉树](https://leetcode.cn/problems/merge-two-binary-trees/)

递归合并

#### [621. 任务调度器](https://leetcode.cn/problems/task-scheduler/)

我觉得这一题应该是个困难题，比较考察对于问题本质分析，不能使用递归完成。这一题要用一种“桶”的模拟思想会比较好理解。这个桶能够保证我们的任务在规则之内比较好放置任务，如果遇到矛盾也有统一的方法能够方便解决

#### [739. 每日温度](https://leetcode.cn/problems/daily-temperatures/)

单调栈解决
