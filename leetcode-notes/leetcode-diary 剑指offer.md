---
title: Leetcode-diary 剑指offer
tags:
  - Leetcode
categories:
  - 编程
  - Leetcode
abbrlink: ff9614a6
date: 2022-03-01 15:39:29
---

# leetcode-diary 剑指offer

因为这个题库是大家强推的，所以先刷比较重要的才是更有效率的策略，之后再深入各个板块，[leetcode 剑指offer](https://leetcode-cn.com/problem-list/xb9nqhhg/)

现在开始每天复习 offer，旨在能够遇到原题时快速写出最优的答案。会在题目之后 mark 做了几次

#### [Offer 07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/) MARK 2

前序/后序 + 中序能构建二叉树，但前序 + 后续不能够构建二叉树，仅能明确父子关系。这一题使用递归的方法进行：由前序确定根节点，左子树前序，右子树前序；由中序确定根节点，左子树中序，右子树中序，由此就能够构建递归算法。基础情况就是仅有一个节点的情况（如果使用 index 就直接考虑 index 不满足时的情况）

#### [Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

使用两个栈，一个用于进，一个用于出

在 `append` 的时候操作和栈是一模一样的，在 `pop` 的时候要分两种情况讨论：1. 当出栈不为空，则 `pop` 出栈；2. 当出栈为空，则把进栈的数字放入出栈，再 `pop`；3. 当两个栈都为空，则返回 -1

#### [Offer 10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)

有多种解法：1. 递归；2. 公式法；3. 迭代/动态规划；4. 矩阵快速幂

简单说一下所谓快速幂的思想：求一个数 a 的 N 次方，相当于用两个 a 的 N/2 次方相乘。使用递归的方法求解即可，当遇到 N 为奇数的时候，拆分为 a 乘以 a 的 N - 1 次方即可

#### [Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

这是之前做的一个困难题，这里又巩固了一下。又重新理解了一下二分查找，mid 值并不是用于搜索目标的，而是一个确定范围的“探针”，能够迅速让搜索范围缩小一半，需要注意下面三点：

1. 一般判定搜索结束的条件：
   1. 找到解
   2. left == right

2. 要保证左侧往前走 `left = mid + 1`，不要使用 `left = mid` 这样的缩小范围的方式，因为由于整除的下取整性质，一旦发生 `mid == left`，这将会陷入死循环

3. 保持最优解（如果存在）在左右指针的范围之内。即：在二分搜索的时候 `right = mid - 1` 要考虑是否会跳过最优解

#### [Offer 12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

一开始想使用动态规划，简单算了一下其复杂度，应该会比较离谱，所以改为深度搜索，即对每个位置进行深度搜索，这样的复杂度会更加合理。这里也要使用回溯的技巧，显然我已经掌握了

#### [Offer 14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)

这一题直接套用数学上的直觉，当分得越均匀越好。更直接的答案是，拆分成尽量多的长度3，如果余数为1则要拆分成两个2  

#### [Offer 15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

这一题有两个方法，比较好理解的是对每一位进行检查。另一个是 n & (n - 1) 直到 n 为0

对于2的运算可以转化为位运算：

1. 向下整除2等价于右移一位 n >> 1。同样的乘以2等价于向左移动一位，这样还可以更方便地计算2的 N 次方

2. 取2的余数等价于判断二进制最右一位值 n & 1

#### [Offer 18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

使用双指针比较合理一些，必须要记录前一个指针所指的对象。这样的话还需要对 head 情况进行特殊处理

#### [Offer 20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

这一题的自动机还是第一次见到，具体情况请直接看题解

#### [Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

使用双指针进行原地修改

#### [Offer 24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

用了两种方法，一个是原地修改（迭代），另一个是取出来再创建，再有一个就是递归，最好尝试一下写一个新的递归函数返回头尾	

#### [Offer 25. 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)

首先想到的当然就是递归。另一个方法就是使用一个空节点作为开头，使用迭代的方法将两个链表穿起来，这样就能够避免一些边界情况处理，比如 head 节点。另一个学习点是 None 可以用作 False 进行判断

#### [Offer 26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)

显然需要递归进行判断是否是子结构，并递归进行遍历每一个子节点

#### [Offer 27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)

方法一使用递归，这是最明显的，也可以使用队列来进行层序遍历

#### [Offer 28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)

方法一使用递归，判断左右两个子树是否对称；方法二使用判断每一层是否是中心对称（这个感觉比较麻烦）

#### [Offer 29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

这一题太迷了...很明显不应该是简单题，因为不能使用简单的代码进行迭代，而需要对每一次运动进行细节判定，所以代码就难看了

#### [Offer 30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

跟随栈的 pop and push 维护一个最小栈即可

#### [Offer 31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

这里采用模拟出入栈的方式进行：创建一个模拟栈，然后先入栈，然后看能不能出栈，直到不能出栈；接着进入下一次入栈的循环。要注意的是在判断能不能出栈时有两种情况：

1. 栈不为空，且栈最后一位正好是我们要出栈的元素
2. 栈为空 or 最后一位不是我们要出栈的元素

#### [Offer 32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

层序遍历，使用队列。由于循环终止的条件是队列为空，所以需要先加入一个根节点，然后再开始循环

#### [Offer 33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

判断后续遍历输出是否是某**二叉搜索树**的输出。一般后序遍历是不能确定一棵树的，但如果是二叉搜索树那就可以！同理，前序遍历也能够确定一个二叉搜索树，但中序遍历似乎不行...因为中序遍历无法确定根节点的位置

这一题的数据变化正好有单调的感觉，所以可以考虑使用单调栈，建议看一下题解，逻辑还是比较复杂，需要倒序来看。比较当前节点和栈顶节点的大小：

1. 如果当前节点大于栈顶节点，则当前节点为栈顶节点的右节点
2. 如果当前节点小于栈顶节点，则当前节点为栈中**某一节点**的左节点，该节点是距离当前节点最近的点

这是两个基本性质，通过这两个基本性质单调栈的使用方法就出来了。现在我们需要判定二叉搜索树，这主要看第一条性质。因为当前节点的大小可以很大，有可能大出了根节点的大小，例如某倒序为 `[5, 2, 3, 6 ,1]`，这样就不是二叉搜索树了，所以整个过程中我们还需要知道当前栈的根节点是谁

#### [Offer 34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

深度搜索预定，一开始读题的时候又审错了。是要找从**根节点到叶节点**的情况！这样对于剪枝的情况只能是到达根节点后再进行判断，同时进行搜索时也要判断一下左右节点是否为空

#### [Offer 35. 复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

这一题有两种解法，一种是使用旧表节点作为 key，其 value 为复制的新节点，然后对旧表进行循环，通过对哈希表的查询把新表连接起来。另一种是拼接和拆分，感觉比较晦涩

#### [Offer 36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)

**中序遍历能够顺序输出二叉搜索树**中的值，所以这一题应当优先考虑中序遍历（然而我一开始并不知道这一点，直接莽了递归，调试太痛苦了，指针的变化很难弄清楚，最好使用 tempt 变量存储节点，然后再进行指针连接）

一些关键的技巧为：使用一个变量 `pre, head` 来记录每一个节点前节点和最终输出的头节点，在每次中序遍历的时候将该节点与前节点进行连接，然后更新前节点。在遍历结束后再将头节点和尾节点连接

#### [Offer 37. 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

层序遍历的流程：1. 需要先在队列中放入一个元素；2. 循环中，先 pop 再 pop 出的节点的子节点，然后 appen 其子节点

需要注意的是 deque 的 popleft 速度比列表的 pop(0) 要快得多

#### [Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

一开始想到的是直接解决，找出所有的可能排列，还想了一下逐渐增加字符的递归方法。然而这些思路不够简洁，对于排列最好还是使用深度搜索的方法，但是为了解决重复性的问题，需要进行剪枝，即某个位置的字符不会重复搜索

如果日常中需要偷懒的话就直接使用 Python 库 `itertools.permutations()`

#### [Offer 39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

这一题虽然简单，但是有多种不同的方法：1. 使用 Counter or hash table 找到最多的数字并进行判断；2. 将数组进行排序，只要第一位和中位数是一样的即可；3. 投票法：假设票数为零则当前数作为众数，并与接下来的数进行比较，遇到与该数相等的则票数加一，遇到不相等的票数减一，如此进行循环。其原理是：当票数为零时，之后的计算得到的众数就是全局的众数，最后还可以判断一下，如果 count 大于一般则为真众数，否则众数不存在

#### [Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

三个思路：1. 排序；2. 堆；3. 快排思想：寻找第 k 小 or 第 k + 1 小的数，找到过后把其左边的数一同输出即为答案，期望时间为 O(N)

又学习到了一个新方法：python 的交换值语法可以用一行写完，不需要 tempt 值。同时这一题让我对快排的代码完全了解了，实现了原地修改和非原地修改两种版本

#### [Offer 41. 数据流中的中位数](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/)

这里介绍 python 有关堆的库 heapq 堆队列，需要了解的有几点：

1. 建堆是 O(N) 时间复杂度；
2. 堆是一个完全二叉树，但是完全可以使用一个数组来实现，因为完全二叉树的根节点和子节点之间的 index 关系是确定的：`left = root * 2 + 1` & `right = root * 2 + 2`
3. insert & pop 的时间复杂度都是 O(logN)

python 里面只实现了最小堆，最大堆可以通过把值取负数实现。建堆可以使用 `heapify(list)` or 直接向一个列表插入即可自动建堆 `heappush(list, num)`，删除堆顶操作为 `heappop`，获得堆顶直接取切片 `list[0]`

这一题通过建立两个堆，一个最大堆和一个最小堆。其中最大堆 B 保留较小的数，最小堆 A 保留较大的数，这将使得 A >= B 以两个堆的数量是否相等为判断：

1. 当两个堆数量相等时，把数字插入最大堆 B，然后 pop 出 B 堆中的最大值，将其插入 A 中
2. 当两个堆数量不等时（准确来说当 A 堆比 B 堆多一个数时），把数字插入最小堆 B，然后 pop 出 A 堆中的最小值，将其插入 B 中

以上的两个方法将维护这两个堆，保持输入的数组均匀分成两份

#### [Offer 42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

很明显的动态规划题目，以第 i 个数为结尾的连续子数组的最大和为状态进行构建

#### [Offer 43. 1～n 整数中 1 出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)

这是一个困难题，这一题没有什么套路可言。完全是通过逻辑的推演得出的解题思路，其主思路是计算每一位上出现1的次数，而每一位出现1的次数要分三种情况讨论：

1. 该位是0，则出现次数仅与高位相关：`high * 10 ** i`
2. 该位是1，则出现次数与高位和地位相关：`high * 10 ** i + low + 1`
3. 该位是除0，1之外的其他数字，则出现次数仅与高位相关：`(high + 1) * 10 ** i`

#### [Offer 44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

这一题和上一题一样，也是需要通过题目本身的逻辑推演出迭代思路，不能够通过递归的方法进行。也是根据数的位数作为突破口，先寻找这是几位数，然后再看数字是几，最后再得出答案

#### [Offer 45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

这一题本质是一个排序问题，如何比较两个数 x, y 的大小定义为前后两种不同拼接的字符串大小：若 xy < yx 则 x < y 反之 x > y

python 中自定义排序需要使用 `functools.cmp_to_key(cmp_func)`，该函数作为参数传入  `sorted(,key=)`，更多原理参考 [知乎](https://zhuanlan.zhihu.com/p/26546486)，其核心是通过重载算符返回一个可比较的类

#### [Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

比较明显一道深度搜索的题目，很快就解出来了，这题学到的是答案一般在完成一条搜索路径后再添加，在中途是不添加的

#### [Offer 47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)

先尝试了深度搜索，但超时了，再做了动态规划

#### [Offer 48. 最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)

这一题之前做过，使用双指针 + 一个哈希表存储，也可以尝试使用动态规划解决但思路就比较复杂一点

对于双指针的题目需要注意的几个点：

1. 两个指针的意义，一定要定义清楚，并且当前状态的其他变量也要定义清楚。比如：左指针定义为字串的起始点；右指针定义为字串即将包含的数字
2. 出现两个指针重合时的情况，通常比较特殊，也就是初始情况，如果不能和普通情况融合，就单独讨论
3. **循环：**对当前状态进行讨论，然后更新状态，回到循环开始

#### [Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)

这一题比较好理解的是堆方法，动态规划方法不太好理解，如果推导出下一个丑数的过程（三指针逐渐往前滚动），下面引用题解中的评论

>设置3个索引a, b, c，分别记录前几个数已经被乘2， 乘3， 乘5了，比如a表示前(a-1)个数都已经乘过一次2了，下次应该乘2的是第a个数；b表示前(b-1)个数都已经乘过一次3了，下次应该乘3的是第b个数；c表示前(c-1)个数都已经乘过一次5了，下次应该乘5的是第c个数

#### [Offer 50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)

直接调用 counter 杀死比赛。这里还有一种解法是使用有序字典 OrderedDict，实际上 python 在 3.6 之后其字典就是有序的，所以可以不必使用 collections 库

#### [Offer 51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)

使用归并排序+递归完成

#### [Offer 52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

首先想到的是哈希表解决，比较优雅的方法是两个指针都向前走 (a + b - c) 步一定能够得到其交点 or None，其中 a, b 分别为链表的长度，c 为公共链表的长度，具体操作为当二者的指针不相等时则一直循环，若二者的指针为 None 则将其指向对方的头节点

#### [Offer 53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

显然使用二分查找，这里再重新自己写一遍

#### [Offer 53 - II. 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/)

显然使用二分查找，再重新总结一下套路：首先标定 left & right，然后进入循环：1. 二分；2. 搜索区间的界定；3. 边界情况的判断（left & right 相邻，判断最终返回值的具体位置）

#### [Offer 54. 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

中序遍历，并在 count >= k 时进行剪枝，剪枝的技巧通常在搜索函数的开头，可以把其作为 basic cases

#### [Offer 55 - I. 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)

可以用任一序的遍历解题，我采用了先序，同样为了省去回溯的麻烦，我将 path / depth 作为参数放入了搜索函数当中，这也是递归的思想

#### [Offer 55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)

这一题的迷惑主要是在于剪枝方面。首先我定义了一个递归的解法，在递归的过程中一旦发现不符合就可以不用继续递归了，但是递归的返回值是树的深度，而在计算中会使用这个深度，其中就容易出错了。粗暴的剪枝可以在所有递归结束的地方都进行，而不仅仅是在开头

#### [Offer 56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

这一题是想破头都没相出来，直接看答案吧！答案首先提出使用位运算：异或。首先提出了异或的性质：

1. 交换律：a + b = b + a
2. 可移动性：a + b = c, a + c = b, b + c = a
3. 自反性：a + 0 = a 或表达为 a + b + b = a

答案首先提出了简单例子：只含有一个不一样的数字怎么找出来，就是直接把所有数字取异或操作即可。那么两个不一样的数字，就可以把两个数字分到不同的组，而其他一样的数字分到同一个组即可。符合分组的方法：找到 c (= a + b) 中某一位为 1 的数，让其他所有数字对应位上的数字与其做异或操作，这样就能够达到上述的分组效果

#### [Offer 56 - II. 数组中数字出现的次数 II](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)

这一题没有要求空间复杂度 O(1) 所以先考虑简单做法，使用 Counter 一行骚操作解决。而从位运算的角度来思考，如果全是重复的数字，则每一位0和1出现的次数均位3的倍数，而多了一个单独的数字则会打破3的倍数，我们只需要确定这一位是多少即可，这就是位运算的神奇魔力，不需要确定是哪一个，而是算出来哪一个该是什么值。事实上从题目下方的数字范围有时也能猜测这题是否使用位运算，比如0~2^31

#### [Offer 57. 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)

先用二分查找的方法试了一下，很奇怪，为什么我第一想法不是使用哈希查找呢？但实际上哈希查找的空间复杂度比较高，我没有使用递增这个条件。使用双指针可将空间复杂度降为 O(1)

#### [Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

首先使用了一个栈作为滑窗。另一种方式为，作为连续正数的和，可以使用求和公式简化搜搜

#### [Offer 58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)

使用了 split 方法直接一行带走，当然也要用不使用这个方法实现一次

#### [Offer 59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)

首先想到的是使用堆来维护滑窗的最大值，但是这个堆顶元素可能不再滑动窗口中之中，所以需要进行判定，这样还需要滑动窗口的范围和该堆顶元素的 Index。这里插入堆中的是一个元组 `(number, index)`，注意：插入堆中的元素必须可以比较，元组和队列都行，但字典不可以。但这并不是这一题的最优解，最优应该使用单调（双端）队列来维护滑动窗口的最大值：

1. 获得元素 i
2. 若将此元素入队，判断此时长度是否大于滑动窗口，如果大于则左侧出队
3. 判断是否大于队列尾部元素，如果大于则底部元素出列，因为该元素将不会被作为最大值取到，如此循环，知道碰到大于元素 i 的数
4. 元素入队，并返回队列头部作为最大值

#### [Offer 59 - II. 队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)

这一题就是上面滑动窗口的最大值的翻版，按照之前的算法进行即可，只是少了滑动窗口的长度这一判断条件

#### [Offer 60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

先写了一个简单的搜索，发现时间太长了，赶紧使用动态规划，这里依然要拓展维度，因为添加骰子能够让状态更好把握

#### [Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

关键考虑顺子的充要条件：1. 非零元素不重复；2. 非零元素的最大最小值相差小于5

#### [Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

这一题不应该是个简单题，还是挺难的！一开始使用暴力解法，显然因为删除复杂度太高而超时了。想了动态规划，但是没想明白怎么推导状态方程...然后开始思考递归，最后获得了递归的答案，既然递归能够完成，那么迭代（动态规划）就一定能够完成，最终反推迭代方程解决

开始思考递归和动态规划之间的联系...我感觉二者应该是等价的，不过递归可能发散出去的状态是很多的（例如深度搜索），但是动态规划最终的状态是更清晰的

#### [Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

这一题使用了逻辑运算的短路功能，利用递归来代替循环

#### [Offer 65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

这一题补充一下整数在计算机中的表达的相关知识，参考 [知乎](https://zhuanlan.zhihu.com/p/376848035)：

1. 0b, 0o, 0x 分别表示二进制和十六进制，可能取的是 binary, octal, hexadecimal 的某个字母

2. 关于原码，反码，补码：

   1. 原码：最高位为符号位，0表示正数，1表示负数

      ```python
      print(hex(1)) # = 0x1 补码
      print(hex(-1)) # = -0x1 负号 + 原码 （ Python 特色，Java 会直接输出补码 1111 1101）
      ```

   2. 反码：最高位为符号位，正数的反码等于本身，负数的反码为除符号位外，对应正数各位取反

   3. 补码：最高位为符号位，正数的补码等于本身，负数的补码为反码 + 1

      我们可以把补码当作一个一般的操作（取反 + 1，不需要特殊考虑符号位），对正数我们不做操作，对负数进行补码操作。相当于用补码来表示正数的相反数，在进行计算时，我们用补码代替负数，也即将减法转为为加法。得知负数的补码，在对其取补码，就可得到正数，也即补码的补码就是原码

      ```python
      # 假设 a 为负数，a 的补码为 b + 1，其中 b 为 a 的反码
      # 根据反码的定义有
      a + b = 0xffffffff	# f 代表4个1
      a + b + 1 = 0x00000000
      # 由以上等式得出
      x - a = x + b + 1	# 这样就将减法和加法统一起来了
      
      # 用4个 bit 来做一个示范
      bin(3) = 0b0101		# 3 的反码和补码等于其本身
      bin(-3) = 0b1101	# 将最高位变为 1（这里仅用于示范，与 python 实际的逻辑不符！！！！
      # -3 的反码
      0b1010
      # -3 的补码
      0b1011
      # 从 -3 的补码推测其源码，先确定符号位，然后取反码 + 1
      0b0100 + 1 = 0b0101
      ```

3. 由于 python 的特殊表示，即其没有最高位的概念，输入一个补码的二进制会输出一个正数，所以需要特殊处理

   ```python
   # 同样以 -3 举例
   bin(-3) = 0b1101	# -3 的理论补码表示
   int(0b1101) = 13 > (2**3 - 1)	# -3 在 python 中实际的表示
   # 现在要想把 13 转换为 -3，思路是先转回原码，再使用 ~ 取反得到补码
   # 为了转回原码不能使用 ~，因为 python 没有最高位的概念，~13 = -14
   # 只能使用异或操作进行取反
   0b1101 ^ 0b1111	= 0b0010 = 2
   # ~x 在 python 中等价于 -x - 1
   ~0b0010 = -x - 1 = -2 - 1 = -3
   ```

#### [Offer 66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

没办法使用除法，那就只能高效使用乘法，通过构建上下三角来重复利用已求得的结果

#### [Offer 67. 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)

没什么特别的方法，就是跟着逻辑硬判断，但是其实文字描述并不够清晰...这一题就这样吧，直接抄的答案

#### [Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/) MARK2

我先是没有利用二叉搜索树的性质完成了这一题。就是直接把路径找出来，然后看相同祖先。**当然简单的写法是递归，当左侧没有时，就在右侧；当右侧没有时，就在左侧；当两侧各有一个时，就返回根节点**

利用二叉搜索树的性质能够加速搜索，如果不是二叉搜索树则先将路径搜索出来，然后查询公共节点。使用 append & pop 能够极大加速搜索速度并减少内存，而不使用 + 方法省去剪枝的流程

#### [面试题32 - I. 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

层序遍历

#### [面试题19. 正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)

比较复杂的一道动态规划，调试了很久很久，我其实也不能确定这样的状态转移能够推理出全部的解，我尽可能的写出了为 true 的状态转移方程，显然我写出的方程已经覆盖了所有为 true 的情况，不满足的自然为 false

## 补充：常见输入输出

因为在进行笔试的时候，不像 leetcode 提供了输入输出，而是需要使用标准输入输出 input & print。这里总结一下 python 的标准输入输出模板。要点就是：

1. 所有的输入可以看作为一个文件
2. 每一行的输入都要用 input 接受，通常使用 try & except 处理循环结束 end of file

### 一行输入

每个样例只有一行输入

```python
while True:
    try:
		a = input()
        function(a)
	except:
        break
```

### 多行输入

每个样例有多个输入，这个时候通常会告诉你有多少行，使用循环接收即可

```python
while True:
    try:
        n, m = input()
        for i in range(n):
            a = input()
```

