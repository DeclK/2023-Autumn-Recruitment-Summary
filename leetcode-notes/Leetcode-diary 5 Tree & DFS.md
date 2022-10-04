# Leetcode-diary 5 Tree & DFS

#### [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

一道非常简单的递归题目，只需要知道左右子树的最高值，再加1即可

#### [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

同样的递归，但是思路和上一题是有差别的！当左侧不存在子树时，左侧的深度也是不存在的，此时最小深度应当以右侧的最小深度为准

#### [543. 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/)

需要维护两个值，一个是树的深度，一个是树的最大直径。当前树的最大直径，为三者最大和：左子树最大直径，右子树最大直径，两侧深度

#### [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

用递归做很简单，但是用迭代做就比较复杂了。需要手动实现一下

#### [572. 另一棵树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree/)

遍历 + 递归/深度搜索

#### [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

判断一个树是否是平衡二叉树：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1

使用递归的方法，既返回左右侧的高度，又返回是否为子树。如果已经不满足平衡二叉树，就不必要再计算高度了

#### [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

依然是递归方法，不过递归过程有一些区别，返回的是左侧/右侧单支线的最大值，但是更新答案的时候要计算两侧都有的情况

#### [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)

我先使用了递归的方法，比较麻烦。题解使用了中序遍历判断有序，这样的思路更加的简洁！

#### [112. 路径总和](https://leetcode-cn.com/problems/path-sum/)

深度搜索，需要注意一下判定条件：如果该节点是根节点则计算，如果是空节点则返回。113 路径综合2 也是一样的思路，不过要使用回溯

#### [437. 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii/)

我首先使用 N 方的复杂度快速完成了这一题，但实际上有 O(N) 复杂度的解法，需要利用前缀和。这一题不是我想象中的**“路径”**，而是经过简化版本的路径，这就给前缀和查找提出了可能。前缀和使用一个字典存储，方便查询

这里有好几个坑：1. 使用前缀和时需要初始化 `presum_set[0] = 1`；2. 需要回溯时维护前缀和的数值；3. 这是最坑的一点，也就是在计算 ans 的时候要加 `presum_set[target]` 的数值，而不是简单加1

#### [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/)
