# Leetcode-diary 6 LinkedList

#### [剑指 Offer II 021. 删除链表的倒数第 n 个结点](https://leetcode-cn.com/problems/SLwz0R/)

需要使用一个空的头节点来处理 head 的特殊情况。然后使用快慢指针，获得需要删除的点的位置，还需要一个 previous 指针获得慢指针的前一个节点

#### [328. 奇偶链表](https://leetcode.cn/problems/odd-even-linked-list/)

使用两个 head 将奇数偶数串起来，并且两步两步地往前推进

#### [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

先使用了递归完成了翻转链表功能，然后就是常规思路：找到开头与结束，以及他们的前后节点，然后将这部分链表进行翻转，之后再接回去。值得一提的是，如果在头部加一个空节点会更方便

#### [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/)

先想了一个暴力解法，直接循环最高次数，如果出不去就算了。这一题可以使用追逐思路/快慢指针，如果有环则必定追上

#### [61. 旋转链表](https://leetcode.cn/problems/rotate-list/)

#### [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

#### [138. 复制带随机指针的链表](https://leetcode.cn/problems/copy-list-with-random-pointer/)

这一题是步骤比较复杂，本身题意非常清楚。如果使用空间复杂度 O(n) 很显然需要使用哈希表建立一个节点和顺序的映射。难点在于使用 O(1) 空间复杂度的情况。**这一题使用了交叉排列新旧节点，这样就能够方便找到随机节点**，因为新节点就跟在旧节点后面。具体一点说：某一个旧节点1的 random 映射到旧节点2，那么新节点1的 random 映射到新节点2，而新节点2就在旧节点2的后面

#### [430. 扁平化多级双向链表](https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/)

很快就想到了递归的思想解决，过程需要注意双向链表的维护

#### [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

使用的暴力解法，先将节点存储起来，然后排序最后合并