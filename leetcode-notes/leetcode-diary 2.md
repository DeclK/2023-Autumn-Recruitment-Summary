---
title: Leetcode-diary 2
tags:
  - Leetcode
categories:
  - 编程
  - Leetcode
abbrlink: 65138f4a
date: 2022-03-01 15:39:28
---

# leetcode-diary 2

diary 1 & diary 2 的目的是了解多种题型，没有深入

## DFS & BFS

在进行刷题之前，有必要小小总结一下深度优先搜索（Depth First Search, DFS）和广度优先搜索（Broad First Search, BFS）

两个搜索除了深度和广度两个重要概念外，还需要更多的关键概念：

1. 候选元素 candidates，存储与节点联系的其他节点。这些节点将作为 candidates 在未来进行遍历
2. 访问状态 visited，存储节点是否被经过的状态
3. 目标 target

**深度优先**我自己总结为：逐层循环中嵌套递归（递归+回溯？

```python
# grpah[v] 存储节点 v 的相邻节点
def DFS(v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbour in graph[v]:
        if visited[neighbour] == False:
            DFS(neighbour, visited)
```

**广度优先**总结为：使用容器，逐层循环，直至容器为空

```python
# graph[v] 存储节点 v 的相邻节点
def BFS(v, graph, visited):
    container = []
    container.append(v)
    visited[v] = True
    while container:
        v = container.pop()
        print(v, end='')
        for v_ in graph[v]:
            if visited[v_] == False:
                container.append(v_)
                visited[v_] == True
```

以上的代码仅体现思想，并没有 return 任何值，而且仅仅是使用了遍历图的特例，具体情况需要具体分析

### 40 Combination Sum ii

[leetcode link](https://leetcode-cn.com/problems/combination-sum-ii/)

这一题出了深度搜索是解题关键外，另一个关键在于剪枝。对于重复数字 x 重复了 m 次，应当使用 m 个循环建立状态的转移，而不是采用比较原始的深度搜索思想，即 2^m 次搜索，这会浪费很多时间

这一题其实有很多的东西需要学习。我这里简要总结一下：

1. python 的 nonlocal & global 关键字作用。二者的作用是相似，都可以将变量的命名空间延长到“局部”，[知乎](https://zhuanlan.zhihu.com/p/341378844)

2. copy 是 shallow copy，对于列表来讲只拷贝顶层，考虑使用副本的时候可以使用，[菜鸟教程](https://www.runoob.com/python3/python3-att-list-copy.html)

3. 列表的 + 运算符一般会创造一个新的列表对象，如果想要原地修改列表有几个选择：

   1. append
   2. += 运算也能够原地修改
   3. List[:] 切片修改

   ```python
   a = [1, 2, 3]
   print(id(a))	
   # 2588593621952
   a += [1]
   print(id(a))
   # 2588593621952
   a = a + [1]
   print(id(a))
   # 2588593875520
   ```

更需要学习的其实是深度搜索的思想：

1. 给一个清晰的定义：从某个节点开始遍历所有的
2. 剪枝是一个节省计算资源的重要操作，不仅是 visited 记录状态，还排除不可能的搜索空间

深度搜索的思想，还需要进一步的理解，尤其是对于**回溯**时候的操作**（回溯仅在空间复杂度很大的使用，不然直接创建多条路径就可以了）**

1. 之前关于 copy 的矛盾来自于一个赋值操作（实际上是让指针指向了 copy 对象，从而之后都修改了 copy 对象）

   如果需要修改原对象，需要使用方法 `sub_ans[:] = sub_ans[:-r_]` 否则会返回新的对象/新的 id，`a = sub_ans[:]` 和 `a = sub_ans.copy()` 是等效的
   
2. 加号 + 和 append 对于 list 的区别：+ 一般会创建一个新的对象，而 append 不会，并且 append 速度更快，但是 += 方法不会创建新的对象

3. nonlocal 和 global 是相似的，只是使用场合不同

## Stack

### 225 & 232 Implement Stack using Queues & vice versa

[leetcode link](https://leetcode-cn.com/problems/implement-stack-using-queues/solution/yong-dui-lie-shi-xian-zhan-by-leetcode-solution/)

### 150 Evaluate Reverse Polish Notation

[leetcode link](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

之前接触过类似的题，所以做起来很快，使用栈来计算。注意使用 int 来进行整数转换

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol = ['+', '-', '*', '/']
        stack = []
        for input in tokens:
            if input in symbol:
                b = stack.pop()
                a = stack.pop()
                if input == '+':
                    c = a + b
                elif input == '-':
                    c = a - b
                elif input == '*':
                    c = a * b
                else:
                    c = int(a / b)
                stack.append(c)
            else:
                stack.append(int(input))
        return stack[-1]
```

## PriorityQueue

### 347 Top K Frequent Elements 

[leetcode link](https://leetcode-cn.com/problems/top-k-frequent-elements/submissions/)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        top_k = counter.most_common(k)
        return [obj[0] for obj in top_k]
```

### 973 K Closest Points to Origin

[leetcode link](https://leetcode-cn.com/problems/k-closest-points-to-origin/)

了解 sorted 的 key 怎么用

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sort = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        top_k = [sort[i] for i in range(k)]

        return top_k
```

使用**堆**数据结构可以降低复杂度，到 O(nlogk)，下面简单介绍一下堆：

- 堆总是一棵完全二叉树
- 堆中某个结点的值总是不大于或不小于其父结点的值

堆有3个常用操作：1. 插入数据 insert 2. 删除堆顶 pop 3. 获得堆顶 peak

## DP

### 120 Triangle

[leetcode link](https://leetcode-cn.com/problems/triangle/)

函数的自调用可以有两个不同的作用：

1. 形成递归，以数学归纳法的方式。需要解决最简单的情况
2. 形成深度搜索，进行状态转移

数学归纳法的形式比较直观，深度搜索的代码就没有那么直觉了。这里总结一些深度搜索中的重要元素：

1. 当前状态 status。通常包括当前节点，当前搜索路径 path 等建模当前环境的条件
2. 目标 target，搜索的目标，也是停止搜索的条件
3. 剪枝条件 conditions (optional)，通常用于减少计算量
4. 状态转移，从当前状态转移到其他状态

但是动态规划一般不需要自调用，只需要循环。因为自调用形成递归被 memoization 替代，具体来说是被一个数组替代，这个数组存储了最优子问题的答案。这样看来动态规划更像是一种迭代

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            if i == 0:
                continue
            for j in range(len(triangle[i])):
                if j == 0:
                    right = triangle[i][j] + triangle[i - 1][j]
                    triangle[i][j] = right
                elif j == i - 1 + 1:
                    left = triangle[i][j] + triangle[i - 1][j -1]
                    triangle[i][j] = left
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])
```

###  518 Coin Change 2

[leetcode link](https://leetcode-cn.com/problems/coin-change-2/)

看到这一题，我首先想到的就是 40 题，先用搜索的方法实现了一遍，顺便复习了一下深度搜索

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        num = 0
        n = len(coins)
        def search(pos, target):
            nonlocal num
            if target == 0:
                # 判定 target
                num += 1
                return
            if pos == n or coins[pos] > target:
                # 剪枝
                return
            for i in range(pos, n):
                # 子搜索空间
                times = target // coins[i]
                for r_ in range(1, times + 1):
                    # 子搜索空间中的状态转移
                    search(i + 1, target - r_ * coins[i])
        search(0, amount)
        return num
```

最终时间超时，想了很久都没有结果，于是乎只能看解答，这样才能感受动态规划的魔力啊

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]
    	# small case looks like this
        #       amount 1 2 3 4 5
        # coin1        1 1 1 1 1
        # coin2        1 2 2 3 3
        # coin5        1 2 2 3 4
```

简短的几行代码直接秒杀通关...当然思想咱还是要学一学，首先看看自己的思路差在哪里：当放弃使用深度搜索采用动态规划时，我需要先定义状态，很自然地就想到以 coins 为状态，但是这个思路很快就被否定了...因为假设已知子问题 coins' 的答案，基于此再添加一个新的面额，也很难得到问题的答案。事实上问题就出在对于状态的定义，似乎不够详细，巧妇难为无米之炊！如果知道 coins’ 在 1~amount 所有数值的组合数，是否可以得到问题的答案呢？这是可以的

假设有 `amount = 500, coins = [3,5,7,8,9,10]`，已知 `coins' = [3,5,7,8,9]` 从 1~500 的所有 amount 的组合数，记为 `dp, len(dp) = 500`。先从简单的情况开始，然后逐步递进：

1. 硬币面值只使用一次：结果为 `result = dp[490] + dp[500]`，也就是说是和为500的组合数，加上和为490的组合数（因为新加入了面值为10的硬币）
2. 接下来就有灵感了，如果硬币面值能使用两次：结果为 `result = dp[480] + dp[490] + dp[500]`
3. 如果硬币面值能不限次数的使用：结果为 `result = dp[10] + ... + dp[500]`
4. 为了让所有的状态都进行更新，除了计算 `amount = 500` 的结果，还需要计算 `amount = 1~499` 的结果

这里的状态和之前的不太一样，感觉多了一个**维度**，拓展了可使用的子结构

### 64 Minimum Path Sum

[leetcode link](https://leetcode-cn.com/problems/minimum-path-sum/)

没啥好说的，跟120题一样的

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up, left = i - 1, j - 1
                if up < 0:
                    grid[i][j] += grid[i][left]
                elif left < 0:
                    grid[i][j] += grid[up][j]
                else:
                    grid[i][j] += min(grid[up][j],grid[i][left])
        return grid[m-1][n-1]
```

## Bit Manipulation

### 421 Maximum XOR of Two Numbers in an Array

[leetcode link](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/)

这块知识真心不会，虽然实现了暴力解法，但时间超太多了，直接上参考链接：[leetcode](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/li-yong-yi-huo-yun-suan-de-xing-zhi-tan-xin-suan-f/), [bilibili](https://www.bilibili.com/video/BV15q4y1L7n9?from=search&seid=1379165254846016152)

关于 python 位运算：[bilibili](https://www.bilibili.com/video/BV16K41137ZM?from=search&seid=1575516065609888964)，`<<, >>, ~, &, |, ^`

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0
        for i in range(30, -1, -1):
            mask |= (1 << i)

            # 当前得到的所有前缀都放在这个哈希表中
            s = set()
            for num in nums:
                s.add(mask & num)

            # 先“贪心地”假设这个数位上是 “1” ，如果全部前缀都看完，都不符合条件，这个数位上就是 “0” 
            temp = res | (1 << i)

            for prefix in s:
                if temp ^ prefix in s:
                    res = temp
                    break
        return res
```

### 89 Gray Code

[leetcode link](https://leetcode-cn.com/problems/gray-code/)


这一题有两种思路，一个是自己想的逐步插入推导，另一个就是参考答案中的镜像法


```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        def expand(idx, num):
            if idx % 2 == 0:
                return [num << 1, (num << 1) + 1]
            else:
                return [(num << 1) + 1, num << 1]
        sub = self.grayCode(n - 1)
        ret = []
        for i in range(len(sub)):
            ret += expand(i, sub[i])
        return ret

```

另一个思路，速度一样，但是代码更简单

```python

        

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        sub = self.grayCode(n - 1)
        rev = [num + (1<<(n-1)) for num in sub[::-1]]
        return sub + rev
```

注意其中的位运算只是计算了 $2^{n-1}$，但速度更快

### 190 Reverse Bits 

[leetcode link](https://leetcode-cn.com/problems/reverse-bits/)

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            # 获得第 i 位置的数
            if n & (1 << i):
                ret = ret | (1 << (31 - i))
        return ret

n = 0b00000010100101000001111010011100	# python 表示二进制
```

### 191 Number of 1 Bits 

[leetcode link](https://leetcode-cn.com/problems/number-of-1-bits/)

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(32):
            if n & (1 << i):
               ret += 1
        return ret 
```

### 201 Bitwise AND of Numbers Range

[leetcode link](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/)

两个思路：

1. 找 left 和 right 的公共前缀
2. 查看每一位是否有可能为0

```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 逐个某个位是否会经过零，那么我们就假定这个位为0，来看看什么会发生
        # 如果这个位高于 right 则必定为0，如果低于 right，则需要看 left 决定是否能经过 0
        # 实际上将 right 这一位数字变为0，后面的数字全为 1，如果这个数字小于 left 则这一位不能经过0，反之一定能经过0
        ret = 0
        mask = 1 << 32 - 1
        for i in range(32, 0, -1):
            mask = mask >> 1
            if right < (1 << (i - 1)) or left < (1 << (i - 1)):
                continue
            if right & (1 << (i - 1)):
                tempt = right ^ (1 << (i - 1))
                tempt = tempt | mask
                if tempt < left:
                    ret += (1 << (i - 1))
        return ret
```

## Graph

### 785 Is Graph Bipartite?

[leetcode link](https://leetcode-cn.com/problems/is-graph-bipartite/)

这题一看就是需要使用并查集的思想，再加上深度搜索就解决了

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        status = [-1 for i in range(n)]
        ret = True
        def dfs(node, status):
            nonlocal ret
            for neighbor in graph[node]:
                if status[node]:
                    if status[neighbor] == 1:
                        return False
                    elif status[neighbor] == -1:
                        status[neighbor] = 0
                        ret = dfs(neighbor, status)
                else:
                    if status[neighbor] == 0:
                        return False
                    elif status[neighbor] == -1:
                        status[neighbor] = 1
                        ret = dfs(neighbor, status)
            return ret
        while -1 in status:
            node = status.index(-1)
            status[node] = 0
            ret = dfs(node, status) and ret
        return ret
```

虽然代码比较丑，但是管用...

至此完成了几乎所有类型的题目，下面的任务就是增加题量了！

