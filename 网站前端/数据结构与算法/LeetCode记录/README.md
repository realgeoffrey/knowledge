# [LeetCode](https://leetcode-cn.com/)记录

## 目录
1. [链表](#链表)（虚拟头结点）

    - [反转链表](#反转链表)
    - [移除链表元素](#移除链表元素)
    - [链表相交](#链表相交)
    - [合并两个有序链表](#合并两个有序链表)
    - [回文链表](#回文链表)

    1. **[设计链表](#设计链表)**（头、尾、任意位置 插入，任意位置删、查）
    1. [随机链表的复制](#随机链表的复制)
    1. [两两交换链表中的节点](#两两交换链表中的节点)
    1. [删除链表的倒数第 N 个结点](#删除链表的倒数第-n-个结点)
    1. [环形链表 II](#环形链表-ii)
1. [二叉树](#二叉树)

    - [二叉树的前序遍历](#二叉树的前序遍历)（中序、后续 只需修改代码位置）
    - [翻转二叉树](#翻转二叉树)
    - [对称二叉树](#对称二叉树)
    - [二叉树的所有路径](#二叉树的所有路径)
    - [左叶子之和](#左叶子之和)
    - [完全二叉树的节点个数](#完全二叉树的节点个数)
    - [平衡二叉树](#平衡二叉树)
    - [路径总和](#路径总和)
    - [合并二叉树](#合并二叉树)
    - [二叉搜索树中的众数](#二叉搜索树中的众数)
    - [将有序数组转换为二叉搜索树](#将有序数组转换为二叉搜索树)

    1. **[二叉树的层序遍历](#二叉树的层序遍历)**（广度优先遍历-队列实现）
    1. [子结构判断](#子结构判断)
    1. 构造二叉树

        1. [从中序与后序遍历序列构造二叉树](#从中序与后序遍历序列构造二叉树)
        1. [从前序与中序遍历序列构造二叉树](#从前序与中序遍历序列构造二叉树)
        1. [最大二叉树](#最大二叉树)
    1. [二叉树的最近公共祖先](#二叉树的最近公共祖先)
    1. [从二叉树一个节点到另一个节点每一步的方向](#从二叉树一个节点到另一个节点每一步的方向)
    1. [二叉搜索树的最近公共祖先](#二叉搜索树的最近公共祖先)
    1. [二叉搜索树中的插入操作](#二叉搜索树中的插入操作)
    1. [删除二叉搜索树中的节点](#删除二叉搜索树中的节点)
    1. [修剪二叉搜索树](#修剪二叉搜索树)
    1. [把二叉搜索树转换为累加树](#把二叉搜索树转换为累加树)
1. [数组](#数组)（二分法、双指针、滑动窗口、模拟行为）

    - [移除元素](#移除元素)
    - [有序数组的平方](#有序数组的平方)
    - [数组中重复的数字](#数组中重复的数字)
    - [在排序数组中查找数字 I](#在排序数组中查找数字-i)
    - [0～n-1中缺失的数字](#0n-1中缺失的数字)
    - [旋转数组的最小数字](#旋转数组的最小数字)
    - [合并两个有序数组](#合并两个有序数组)
    - [删除有序数组中的重复项](#删除有序数组中的重复项)
    - [判断扑克牌顺子](#判断扑克牌顺子)
    - [移动零](#移动零)

    1. [搜索二维矩阵 II](#搜索二维矩阵-ii)
    1. [长度最小的子数组](#长度最小的子数组)
    1. [螺旋矩阵 II](#螺旋矩阵-ii)
    1. [和为 K 的子数组](#和为-k-的子数组)
    1. [除自身以外数组的乘积](#除自身以外数组的乘积)
    1. [扁平化嵌套数组](#扁平化嵌套数组)
    1. [删除有序数组中的重复项 II](#删除有序数组中的重复项-ii)
    1. [合并区间](#合并区间)
    1. [对角线遍历](#对角线遍历)
1. [字符串](#字符串)（双指针、哈希表）

    - [反转字符串](#反转字符串)
    - [反转字符串 II](#反转字符串-ii)
    - [替换空格](#替换空格)
    - [左旋转字符串](#左旋转字符串)
    - [第一个只出现一次的字符](#第一个只出现一次的字符)
    - KMP

    1. [反转字符串中的单词](#反转字符串中的单词)
1. [动态规划](#动态规划)

    - [斐波那契数](#斐波那契数)
    - [爬楼梯](#爬楼梯)
    - [三步问题](#三步问题)
    - [连续子数组的最大和](#连续子数组的最大和)

    1. [股票的最大利润](#股票的最大利润)
    1. [鸡蛋掉落-两枚鸡蛋](#鸡蛋掉落-两枚鸡蛋)
    1. [最大子数组和](#最大子数组和)
    1. [最长回文子串](#最长回文子串)
1. [哈希表](#哈希表)

    - [两个数组的交集](#两个数组的交集)
    - [查找共用字符](#查找共用字符)
    - [快乐数](#快乐数)
    - [两数之和](#两数之和)
    - [有效的字母异位词](#有效的字母异位词)

    1. [找到字符串中所有字母异位词](#找到字符串中所有字母异位词)
    1. [字母异位词分组](#字母异位词分组)
    1. [三数之和](#三数之和)
    1. [四数之和](#四数之和)
    1. [四数相加 II](#四数相加-ii)
    1. [最长连续序列](#最长连续序列)
1. [栈与队列](#栈与队列)

    - [用栈实现队列](#用栈实现队列)
    - [用队列实现栈](#用队列实现栈)
    - [有效的括号](#有效的括号)
    - [删除字符串中的所有相邻重复项](#删除字符串中的所有相邻重复项)
    - [最小栈](#最小栈)

    1. [逆波兰表达式求值](#逆波兰表达式求值)
    1. [前 K 个高频元素](#前-k-个高频元素)
    1. [每日温度](#每日温度)

    - [滑动窗口最大值](#滑动窗口最大值)
1. [回溯](#回溯)（递归的副产品）

    1. [组合](#组合)
    1. [组合总和 III](#组合总和-iii)
    1. [电话号码的字母组合](#电话号码的字母组合)
    1. [组合总和](#组合总和)
    1. [组合总和 II](#组合总和-ii)
1. [岛屿相关](#岛屿相关)

    1. [岛屿数量](#岛屿数量)
    1. [统计封闭岛屿的数目](#统计封闭岛屿的数目)
    1. [飞地的数量](#飞地的数量)
    1. [岛屿的最大面积](#岛屿的最大面积)
    1. [统计子岛屿](#统计子岛屿)
    1. [不同岛屿的数量](#不同岛屿的数量)
1. [中等](#中等)

    1. [盛最多水的容器](#盛最多水的容器)
    1. [无重复字符的最长子串](#无重复字符的最长子串)
    1. [下一个排列](#下一个排列)
    1. [寻找峰值](#寻找峰值)
    1. [森林中的兔子](#森林中的兔子)
    1. [课程表 II](#课程表-ii)
    1. [比较版本号](#比较版本号)
1. [困难](#困难)

    1. [接雨水](#接雨水)

---
<details>
<summary>解题思路</summary>

1. 对称的数据结构（如：二叉树），多用递归解题，从整体的对称性思考，把大问题分解成子问题进行递归，即不是单独考虑一部分(如：树的左子树)，而是同时考虑对称的两部分(如：左右子树)，从而写出对称性的递归代码。

    1. 可能需要辅助函数。
    2. 一般先找到匹配的根节点，再判断其子树是否匹配
2. 动态规划（Dynamic programming，DP）

    1. 通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法

        1. 状态定义。e.g. `dp(n)`定义为题目要求解的含义。
        2. 转移方程（递归）。e.g. `dp(n)`与`dp(n-1)`等的关系。
        3. 初始状态。e.g. 当`n`为最初的若干值时，`dp`的返回结果。
        4. 返回值
    2. 解题流程（包含：递归、记忆化、滚动数组）：

        1. 先想递归
        2. 发现重复计算

            1. 通过记忆化等方法（填表）去掉重复计算（空间换时间）
            2. 若记忆法会导致内存超出等问题，则考虑利用 **计算顺序**、**滚动数组** 来压缩空间

                >滚动数组：是DP中的一种编程思想。让数组滚动起来，每次都使用固定的几个存储空间，来达到压缩、节省存储空间的作用。因为DP题目是一个自底向上的扩展过程，常常需要用到的是连续的解，前面的解往往可以舍去。
</details>

>面试做算法题或编程题时，先讲思路，边说边写。面试官关注：书写速度、逻辑思路、**变量命名**。

---
## 链表

### 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

1. 解法一

    迭代，从前往后。

    ```js
    /**
     * Definition for singly-linked list.
     * function ListNode(val) {
     *     this.val = val;
     *     this.next = null;
     * }
     */
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    var reverseList = function (head) {
      let pre = null;
      let cur = head;
      while (cur) {
        const temp = cur.next;
        cur.next = pre;     // 翻转

        // pre、cur后移，准备下一次迭代
        pre = cur;
        cur = temp;
      }
      return pre;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    递归，从前往后。和上面迭代逻辑一致。

    ```js
    var reverseList = function (head) {
      return reverse(null, head);
    };

    // 从前往后
    var reverse = function (pre, cur) {
      if (cur === null) { return pre; }

      const temp = cur.next;
      cur.next = pre; // 翻转

      pre = cur;
      return reverse(pre, temp);
    };
    ```
3. 解法三

    递归，从后往前。看不懂。

    ```js
    var reverseList = function (head) {
      if (head === null || head.next === null) { return head; }

      // 递归调用，翻转第二个节点开始往后的链表
      const last = reverseList(head.next);

      // 翻转头节点与第二个节点的指向
      head.next.next = head;
      // 此时的 head 节点为尾节点，next 需要指向 NULL
      head.next = null;
      return last;
    };
    ```
</details>

### 移除链表元素
给你一个链表的头节点 `head` 和一个整数 `val` ，请你删除链表中所有满足 `Node.val == val` 的节点，并返回 **新的头节点** 。

示例 1：

![removelinked-list.jpg](./images/removelinked-list.jpg)

```
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
```

示例 2：

```
输入：head = [], val = 1
输出：[]
```

示例 3：

```
输入：head = [7,7,7,7], val = 7
输出：[]
```

1. 解法一

    新增一个节点指向题目给出的头结点，这样可以统一处理删除逻辑。

    ```js
    /**
     * Definition for singly-linked list.
     * function ListNode(val, next) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.next = (next===undefined ? null : next)
     * }
     */
    /**
     * @param {ListNode} head
     * @param {number} val
     * @return {ListNode}
     */
    var removeElements = function (head, val) {
      // 创建一个虚拟头节点
      const vNode = new ListNode(-1, head);

      let cur = vNode;
      let next = vNode.next;
      while (next) {
        if (next.val === val) {
          cur.next = next.next;
        } else {
          cur = next;
        }
        next = next.next;
      }

      return vNode.next;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    不利用新增一个虚拟前置头节点，因此需要分别处理head删除和next删除。不推荐。

    ```js
    var removeElements = function (head, val) {
      // 先把头部自己是val的去掉
      while (head && head.val === val) {
        head = head.next;
      }

      if (head === null) {
        return null;
      }

      // 再处理next
      let cur = head;
      let next = head.next;
      while (next) {
        if (next.val === val) {
          cur.next = next.next;
        } else {
          cur = next;
        }
        next = next.next;
      }

      return head;
    };
    ```
</details>

### 链表相交
给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交：

![160_statement.png](./images/160_statement.png)

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

示例 1：

![160_example_1.png](./images/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

示例 2：

![160_example_2.png](./images/160_example_2.png)

```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

示例 3：

![160_example_3.png](./images/160_example_3.png)

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
```

提示：

- `listA` 中节点数目为 `m`
- `listB` 中节点数目为 `n`
- `0 <= m, n <= 3 * 10 ** 4`
- `1 <= Node.val <= 10 ** 5`
- `0 <= skipA <= m`
- `0 <= skipB <= n`
- 如果 `listA` 和 `listB` 没有交点，`intersectVal` 为 `0`
- 如果 `listA` 和 `listB` 有交点，`intersectVal == listA[skipA + 1] == listB[skipB + 1]`

**进阶**：你能否设计一个时间复杂度 `O(n)` 、仅用 `O(1)` 内存的解决方案？

1. 解法一

    若有相交，则必然是2个链表最后相同长度的部分出现相交点。因此先确定2个链表长度，然后按照短的链表总长度对比找出相交节点。

    ```js
    /**
     * Definition for singly-linked list.
     * function ListNode(val) {
     *     this.val = val;
     *     this.next = null;
     * }
     */
    /**
     * @param {ListNode} headA
     * @param {ListNode} headB
     * @return {ListNode}
     */
    var getIntersectionNode = function (headA, headB) {
      const vNodeA = new ListNode(-1, headA);
      const vNodeB = new ListNode(-1, headB);
      let curA = vNodeA;
      let curB = vNodeB;
      // 获得2个链表的长度
      let aLength = 0;
      let bLength = 0;
      while (curA.next) {
        curA = curA.next;
        aLength++;
      }
      while (curB.next) {
        curB = curB.next;
        bLength++;
      }

      // 移动长的链表节点，不移动短的链表节点，得到2个链表最后一样长度的部分
      curA = vNodeA;
      curB = vNodeB;
      if (aLength > bLength) {
        for (let i = 0; i < aLength - bLength; i++) {
          curA = curA.next;
        }
      } else {
        for (let i = 0; i < bLength - aLength; i++) {
          curB = curB.next;
        }
      }

      // 若有相交，则必然是2个链表最后相同长度的部分出现相交点
      while (curA.next) {
        if (curA.next === curB.next) {
          return curA.next;
        }

        curA = curA.next;
        curB = curB.next;
      }

      return null;
    };
    ```
2. 解法二

    2链表连接在一起一同遍历。当遍历到节点相同时，要不然是交点，要不然是null。

    ```js
    var getIntersectionNode = function (headA, headB) {
      let curA = headA;
      let curB = headB;
      // 2个链表连载一起遍历，当节点相同时退出。若有交点，则退出点是交点；若无交点，则退出点是curA和curB都为null
      while (curA !== curB) {
        curA = curA === null ? headB : curA.next;
        curB = curB === null ? headA : curB.next;
      }
      return curA;
    };
    ```

### 合并两个有序链表
将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

1. 解法一

    迭代。

    ```js
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    var mergeTwoLists = function (list1, list2) {
      const vNode = new ListNode(-1, null);

      let node1 = list1;
      let node2 = list2;
      let cur = vNode;

      while (node1 && node2) {
        if (node1.val > node2.val) {
          cur.next = node2;
          node2 = node2.next;
        } else {
          cur.next = node1;
          node1 = node1.next;
        }
        cur = cur.next;
      }

      if (node1) {
        cur.next = node1;
      } else if (node2) {
        cur.next = node2;
      }

      return vNode.next;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    递归。

    ```js
    var mergeTwoLists = function (list1, list2) {
      if (list1 === null) {
        return list2;
      } else if (list2 === null) {
        return list1;
      } else if (list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
      } else {
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
      }
    };
    ```
</details>

### 回文链表
>回文链表：以链表中间为中心点两边对称。

**进阶**：你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？

1. 解法一

    ①找到中间节点，②反转后半链表，③判断回文，④恢复反转。空间复杂度 O(1)。

    ```js
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    var isPalindrome = function (head) {
      if (head === null) { return true; }

      // 前半部分链表的尾节点
      const preEnd = getHalfNode(head);
      // 最后一个节点，也就是反转之后 后半部分链表的头结点
      const postStart = reverseList(preEnd.next);

      // 判断是否回文
      let p1 = head; // 从前半的头部开始
      let p2 = postStart; // 从后半的尾部开始（反转后的头部）
      let result = true; // 当只有一个节点时，也是回文
      while (result && p2) {  // 若原链表是偶数，则所有节点都对比；若是奇数，则中间一个节点p2会跳过
        if (p1.val !== p2.val) { result = false; }
        p1 = p1.next;
        p2 = p2.next;
      }

      // 优化：还原链表
      reverseList(postStart);

      return result;
    };

    // 反转链表
    const reverseList = function (head) {
      let pre = null;
      let cur = head;
      while (cur) {
        const temp = cur.next;
        cur.next = pre; // 翻转

        // pre、cur后移，准备下一次迭代
        pre = cur;
        cur = temp;
      }
      return pre;
    };

    // 双指针（1个指针走1步，1个指针走2步）找到中点（偶数个找到前一个，奇数个找到正中）
    const getHalfNode = (head) => {
      let fast = head;
      let slow = head;
      while (fast.next !== null && fast.next.next !== null) {
        fast = fast.next.next;
        slow = slow.next;
      }
      return slow;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    转化为数组后判断数组回文。空间复杂度 O(n)。

    ```js
    var isPalindrome = function (head) {
      // 链表转化为数组
      const arr = [];
      while (head !== null) {
        arr.push(head.val);
        head = head.next;
      }

      // 判断数组回文
      for (let i = 0, j = arr.length - 1; i < j; ++i, --j) {
        if (arr[i] !== arr[j]) {
          return false;
        }
      }
      return true;
    };
    ```
</details>

### 设计链表
你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：`val` 和 `next` 。`val` 是当前节点的值，`next` 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 `prev` 以指示链表中的上一个节点。假设链表中的所有节点下标从 **0** 开始。

实现 `MyLinkedList` 类：

- `MyLinkedList()` 初始化 `MyLinkedList` 对象。
- `int get(int index)` 获取链表中下标为 `index` 的节点的值。如果下标无效，则返回 `-1` 。
- `void addAtHead(int val)` 将一个值为 `val` 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
- `void addAtTail(int val)` 将一个值为 `val` 的节点追加到链表中作为链表的最后一个元素。
- `void addAtIndex(int index, int val)` 将一个值为 `val` 的节点插入到链表中下标为 `index` 的节点之前。如果 `index` 等于链表的长度，那么该节点会被追加到链表的末尾。如果 `index` 比长度更大，该节点将 不会插入 到链表中。
- `void deleteAtIndex(int index)` 如果下标有效，则删除链表中下标为 `index` 的节点。

示例：

```
输入
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
输出
[null, null, null, null, 2, null, 3]

解释
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
myLinkedList.get(1);              // 返回 3
```

提示：

- `0 <= index, val <= 1000`

1. 解法一

    工具函数getNode，通过新增一个节点指向头结点来查询；需要维护链表 head、size。

    ```ts
    class LinkNode {
      val: number;
      next: LinkNode;

      constructor(val, next) {
        this.val = val;
        this.next = next;
      }
    }

    class MyLinkedList {
      size = 0;
      head = null;

      // 工具函数：获取第index个节点
      getNode(index: number): LinkNode | null {
        if (index >= this.size) { return null; }

        const vNode = new LinkNode(-1, this.head);
        let cur = vNode;
        for (let i = 0; i <= index; i++) {
          cur = cur.next;
        }
        return cur;
      }

      get(index: number): number {
        if (index >= this.size) { return -1; }
        return this.getNode(index).val;
      }

      addAtHead(val: number): void {
        this.head = new LinkNode(val, this.head);
        this.size++;
      }

      addAtTail(val: number): void {
        if (this.size === 0) {
          this.addAtHead(val);
          return;
        }

        const node = this.getNode(this.size - 1);
        node.next = new LinkNode(val, null);
        this.size++;
      }

      addAtIndex(index: number, val: number): void {
        if (index > this.size) { return; }

        if (index === 0) {
          this.addAtHead(val);
          return;
        }

        if (index === this.size) {
          this.addAtTail(val);
          return;
        }

        // 获取目标节点的上一个的节点
        const node = this.getNode(index - 1);
        node.next = new LinkNode(val, node.next);
        this.size++;
      }

      deleteAtIndex(index: number): void {
        if (index >= this.size) { return; }

        if (index === 0) {
          this.head = this.head.next;
          this.size--;
          return;
        }

        // 获取目标节点的上一个的节点
        const node = this.getNode(index - 1);
        node.next = node.next.next;
        this.size--;
      }
    }
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    工具函数getNode，通过新增一个节点指向头结点来查询；需要维护链表 head、tail、size。

    ```js
    class LinkNode {
      constructor(val, next) {
        this.val = val;
        this.next = next;
      }
    }

    class MyLinkedList {
      size = 0;
      head = null;
      tail = null;
    }

    // 工具函数：获取第index个节点
    MyLinkedList.prototype.getNode = function (index) {
      if (index >= this.size) { return null; }

      const vNode = new LinkNode(-1, this.head);
      let cur = vNode;
      for (let i = 0; i <= index; i++) {
        cur = cur.next;
      }
      return cur;
    };

    /**
     * @return {number}
     */
    MyLinkedList.prototype.get = function (index) {
      if (index >= this.size) { return -1; }

      return this.getNode(index).val;
    };

    /**
     * @return {void}
     */
    MyLinkedList.prototype.addAtHead = function (val) {
      this.head = new LinkNode(val, this.head);
      if (this.size === 0) {
        this.tail = this.head;
      }
      this.size++;
    };

    /**
     * @return {void}
     */
    MyLinkedList.prototype.addAtTail = function (val) {
      const newNode = new LinkNode(val, null);

      if (this.size === 0) {
        this.tail = newNode
        this.head = newNode
      }else{
        this.tail.next = newNode
        this.tail = newNode
      }
      this.size++;
    };

    /**
     * @return {void}
     */
    MyLinkedList.prototype.addAtIndex = function (index, val) {
      if (index > this.size) { return; }

      if (index === 0) {
        this.addAtHead(val);
        return;
      }

      if (index === this.size) {
        this.addAtTail(val);
        return;
      }

      // 获取目标节点的上一个的节点
      const node = this.getNode(index - 1);
      node.next = new LinkNode(val, node.next);
      this.size++;
    };

    /**
     * @return {void}
     */
    MyLinkedList.prototype.deleteAtIndex = function (index) {
      if (index >= this.size) { return; }

      if (index === 0) {
        this.head = this.head.next;
        // 如果删除的这个节点同时是尾节点，要处理尾节点
        if(this.size === 1){
          this.tail = this.head
        }
        this.size--;
        return;
      }

      // 获取目标节点的上一个的节点
      const node = this.getNode(index - 1);
      node.next = node.next.next;
      // 处理尾节点
      if (index === this.size - 1) {
        this.tail = node;
      }
      this.size--;
    };
    ```
</details>

### 随机链表的复制
给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **深拷贝**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点** 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

- `val`：一个表示 `Node.val` 的整数。
- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为  `null` 。
你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

示例 1：

![e1.png](./images/e1.png)

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

示例 2：

![e2.png](./images/e2.png)

```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

示例 3：

![e3.png](./images/e3.png)

```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```

提示：

- `0 <= n <= 1000`
- `-(10 ** 4) <= Node.val <= 10 ** 4`
- `Node.random` 为 `null` 或指向链表中的节点。

1. 解法一

    递归+哈希表。

    ```js
    /**
     * // Definition for a Node.
     * function Node(val, next, random) {
     *    this.val = val;
     *    this.next = next;
     *    this.random = random;
     * };
     */
    /**
     * @param {Node} head
     * @return {Node}
     */
    var copyRandomList = function (head, cachedMap = new WeakMap()) {
      if (head) {
        if (!cachedMap.has(head)) {
          cachedMap.set(head, {
            val: head.val,
            // 直接写在这里会导致栈溢出，因此先创建新的Map项，再递归
            // next: copyRandomList(head.next, cachedMap),
            // random: copyRandomList(head.random,cachedMap),
          });
          Object.assign(cachedMap.get(head), {
            next: copyRandomList(head.next, cachedMap),
            random: copyRandomList(head.random, cachedMap),
          });
        }

        return cachedMap.get(head);
      }

      return head;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    3次循环。

    ```js
    var copyRandomList = function (head) {
      if (head === null) {
        return null;
      }
      // 创建新的Node，并改变旧的Node的next指向
      for (let node = head; node !== null; node = node.next.next) {
        const nodeNew = new Node(node.val, node.next, null);
        node.next = nodeNew;
      }
      // 复制random指向到新的Node
      for (let node = head; node !== null; node = node.next.next) {
        const nodeNew = node.next;
        nodeNew.random = node.random !== null ? node.random.next : null;
      }

      // 先保存新的Node的第一个，因为之后要设置新的Node链和旧的Node链不关联
      const headNew = head.next;

      // 恢复旧的Node的next指向，并设置新的Node的next指向
      for (let node = head; node !== null; node = node.next) {
        const nodeNew = node.next;
        node.next = node.next.next;
        nodeNew.next = nodeNew.next !== null ? nodeNew.next.next : null;
      }
      return headNew;
    };
    ```
</details>

### 两两交换链表中的节点
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：

![swap_ex1.jpg](./images/swap_ex1.jpg)

```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

示例 2：

```
输入：head = []
输出：[]
```

示例 3：

```
输入：head = [1]
输出：[1]
```

1. 解法

    迭代，虚拟头节点，若下2个节点都存在则进行交换。

    ```js
    /**
     * Definition for singly-linked list.
     * function ListNode(val, next) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.next = (next===undefined ? null : next)
     * }
     */
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    var swapPairs = function (head) {
      let vNode = new ListNode(-1, head);
      let pre = vNode; // 2个交换节点的前一个节点
      while (pre.next && pre.next.next) { // 若后2个节点同时存在则交换（// 由pre->1->2->3 交换为 pre->2->1->3）
        const node1 = pre.next; // 1节点
        const node2 = pre.next.next; // 2节点
        const node3 = pre.next.next.next; // 3节点

        pre.next = node2; // 头->2
        node2.next = node1; // 2->1
        node1.next = node3; // 1->3

        pre = pre.next.next; // pre向后移动两位，准备下一轮交换
      }
      return vNode.next;
    };
    ```

### 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

示例 1：

![remove_ex1.jpg](./images/remove_ex1.jpg)

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

示例 2：

```
输入：head = [1], n = 1
输出：[]
```

示例 3：

```
输入：head = [1,2], n = 1
输出：[1]
```

提示：

- 链表中结点的数目为 `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**进阶**：你能尝试使用一趟扫描实现吗？

1. 解法

    双指针（快慢指针）。

    ```js
    /**
     * Definition for singly-linked list.
     * function ListNode(val, next) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.next = (next===undefined ? null : next)
     * }
     */
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    var removeNthFromEnd = function(head, n) {
      const vNode = new ListNode(-1, head)
      let cur = vNode;
      // 向前先走n步（快指针）
      for (let i = 0; i < n; i++) {
        cur = cur.next
      }

      // 一起走直到抵达结尾
      let deletePre = vNode;  // 慢指针
      while (cur.next) {
        cur = cur.next;
        deletePre = deletePre.next;
      }

      deletePre.next = deletePre.next.next;

      return vNode.next;
    };
    ```

### 环形链表 II
给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 *如果链表无环*，则返回 `null`。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意**：`pos` **不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**不允许修改** 链表。

示例 1：

![circularlinkedlist.png](./images/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

示例 2：

![circularlinkedlist_test2.png](./images/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

示例 3：

![circularlinkedlist_test3.png](./images/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
```

提示：

- `pos` 的值为 -`1` 或者链表中的一个有效索引

**进阶**：你是否可以使用 `O(1)` 空间解决此题？

1. 解法一

    双指针（快慢指针），走1和走2步，会在环内相遇 或 null退出循环。然后通过数学证明，从head出发1个指针 和 从相遇节点出发1个指针，每次都只走1个节点，相遇点就是环形入口。

    ```js
    /**
     * Definition for singly-linked list.
     * function ListNode(val) {
     *     this.val = val;
     *     this.next = null;
     * }
     */
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    var detectCycle = function(head) {
      let slowNode = head;
      let fastNode = head;

      while (fastNode && fastNode.next) {
        // ①fast指针走2步，slow指针走1步，会在环内相遇 或 null退出循环
        slowNode = slowNode.next;
        fastNode = fastNode.next.next;

        // ②若相遇，则需要再找到环形入口
        if (slowNode === fastNode) {
          // 从头结点出发一个指针 和 从相遇节点出发一个指针，每次都只走1个节点，相遇点就是环形入口（证明略）
          slowNode = head;
          while (slowNode !== fastNode) {
            slowNode = slowNode.next;
            fastNode = fastNode.next;
          }
          return slowNode;
        }
      }
      return null;
    }
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    哈希表，记录每一个节点。空间复杂度 O(n)。

    ```js
    var detectCycle = function (head) {
      // hash，保存节点地址
      const visited = new Set();

      while (head !== null) {
        if (visited.has(head)) {
          return head;
        }
        visited.add(head);
        head = head.next;
      }
      return null;
    };
    ```
</details>

---
## 二叉树

### 二叉树的前序遍历
>以下递归和迭代都为统一写法：中序、后续 只需修改代码位置。

>中序遍历，类似题目可微调解法解决：验证二叉搜索树、二叉搜索树中的众数。

1. 解法一

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    var preorderTraversal = function (root) {
      const result = [];
      preOrder(root, result);
      return result;
    };

    function preOrder(root, arr) {
      if (root === null) { return; }
      arr.push(root.val);
      preOrder(root.left, arr);
      preOrder(root.right, arr);
    }
    ```
2. 解法二

    迭代。

    ```js
    // 先序。压栈顺序：右左中；出栈顺序：中左右
    // 中序。压栈顺序：右中左；出栈顺序：左中右
    // 后序。压栈顺序：中右左；出栈顺序：左右中
    var preorderTraversal = function (root) {
      const result = []

      // 访问的节点放入栈（对中节点特殊处理）
      const stack = [];
      root && stack.push(root);
      while (stack.length) {
        const node = stack.pop();
        if (node === null) {  // 是标记为中节点（下一个栈是中节点），才写入结果
          result.push(stack.pop().val);
        } else {
          if (node.right) { stack.push(node.right); } // 右节点
          if (node.left) { stack.push(node.left); }   // 左节点

          stack.push(node); // 作为中节点重新插入，只有当前节点被当做中节点才能写入结果
          stack.push(null); // 标记法
        }
      }
      return result;
    };
    ```

### 翻转二叉树
0. 通用解法

    [二叉树的层序遍历](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#二叉树的层序遍历)
1. 解法一

    递归，不修改原二叉树。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    var invertTree = function (root) {
      if (root === null) { return root; }
      return new TreeNode(root.val, invertTree(root.right), invertTree(root.left));
    };
    ```
2. 解法二

    递归，修改原二叉树。

    ```js
    var invertTree = function (root) {
      if (root === null) { return null; }

      const temp = root.left;
      root.left = root.right;
      root.right = temp;

      invertTree(root.left);
      invertTree(root.right);

      return root;
    };
    ```

### 对称二叉树
>类似题目可微调解法解决：相同的树、另一棵树的子树。

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

示例 1：

```
二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
```

示例 2：

```
二叉树 [1,2,2,null,3,null,3] 不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
```

- <details>

    <summary>解析：对称二叉树</summary>

    对于树中任意两个对称节点 L 和 R，一定存在：

    1. L.val = R.val：

        即此两对称节点值相等。
    2. L.left.val = R.right.val：

        即 L 的 左子节点 和 R 的 右子节点 对称。
    3. L.right.val = R.left.val：

        即 L 的 右子节点 和 R 的 左子节点 对称。
    </details>

1. 解法一

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val) {
     *     this.val = val;
     *     this.left = this.right = null;
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    var isSymmetric = function (root) {
      return helper(root, root);
    };

    // 递归
    var helper = function (root1, root2) {
      // 空节点判断
      if (root1 === null && root2 === null) {
        return true;
      }
      if (root1 === null || root2 === null) {
        return false;
      }

      // 非空节点
      return (
        root1.val === root2.val &&
        helper(root1.left, root2.right) &&
        helper(root1.right, root2.left)
      );
    };
    ```
2. 解法二

    迭代，栈。

    ```js
    var isSymmetric = function (root) {
      if (root === null) { return true; }

      // 栈，要对比的一双，需要一起推入和推出
      const stack = [];
      stack.unshift(root.left);
      stack.unshift(root.right);
      while (stack.length) {
        const left = stack.shift();
        const right = stack.shift();
        if (left === null && right === null) {
          continue;
        }
        if (left === null || right === null || left.val !== right.val) {
          return false;
        }
        stack.unshift(left.left);
        stack.unshift(right.right);
        stack.unshift(left.right);
        stack.unshift(right.left);
      }
      return true;
    };
    ```

### 二叉树的所有路径
>类似题目可微调解法解决：路径总和 II。

给你一个二叉树的根节点 `root` ，按 **任意顺序** ，返回所有从根节点到叶子节点的路径。

**叶子节点** 是指没有子节点的节点。

示例 1：

![paths-tree.jpg](./images/paths-tree.jpg)

```
输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
```

示例 2：

```
输入：root = [1]
输出：["1"]
```

1. 解法

    递归+回溯（回溯和递归是一一对应的，有一个递归，就要有一个回溯）。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {string[]}
     */
    var binaryTreePaths = function (root) {
      const result = [];
      traversal(root, [], result);
      return result;
    };

    function traversal(cur, path, result) { // 递归
      // 推入（注意回溯要推出）
      path.push(cur.val);

      if (cur.left) {
        traversal(cur.left, path, result);  // 方法代码有推入
        path.pop(); // 回溯（回溯和递归是一一对应的，有一个递归，就要有一个回溯）
      }

      if (cur.right) {
        traversal(cur.right, path, result);
        path.pop(); // 回溯
      }

      // 是叶子节点
      if (cur.left === null && cur.right === null) {
        // 转化路径为输出
        let strPath = "";
        for (let i = 0; i <= path.length - 1; i++) {
          strPath += String(path[i]) + (i === path.length - 1 ? "" : "->");
        }
        result.push(strPath);
      }
    }
    ```

### 左叶子之和
给定二叉树的根节点 `root` ，返回所有左叶子之和。

示例 1：

![leftsum-tree.jpg](./images/leftsum-tree.jpg)

```
输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
```

示例 2:

```
输入: root = [1]
输出: 0
```

1. 解法一

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    var sumOfLeftLeaves = function (root) {
      // 递归退出条件：自己为空 || (左节点为空 && 右节点为空)
      if (root === null || (root.left === null && root.right === null)) {
        return 0;
      }

      let value = 0;
      // 左节点是左叶子（必须通过父节点判断是不是左叶子）：左节点不为空 && 左节点的左节点为空 && 左节点的右节点为空
      if (root.left !== null && root.left.left === null && root.left.right === null) {
        value = root.left.val;
      }

      return value + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    };
    ```
2. 解法二

    迭代，与二叉树的遍历（前、中、后均可）类似。

    ```js
    var sumOfLeftLeaves = function (root) {
      let result = 0;

      // 访问的节点放入栈
      const stack = [];
      root && stack.push(root);
      while (stack.length) {
        const node = stack.pop();
        // 左节点是左叶子（必须通过父节点判断是不是左叶子）：左节点不为空 && 左节点的左节点为空 && 左节点的右节点为空
        if (node.left !== null && node.left.left === null && node.left.right === null) {
          result += node.left.val;
        }

        if (node.right) { stack.push(node.right); } // 右节点
        if (node.left) { stack.push(node.left); }   // 左节点
      }
      return result;
    };
    ```

### 完全二叉树的节点个数
**进阶**：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？

1. 解法一

    递归，把完全二叉树拆分成 根节点+左右2棵满二叉树。利用满二叉树原理：h层（h从1开始）节点总数等于`2^h - 1`。时间复杂度：O(log n × log n)。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    var countNodes = function (root) {
      if (root === null) { return 0; }

      // 获取左右子树的深度
      let left = root.left;
      let right = root.right;
      let leftDepth = 1;
      let rightDepth = 1;
      while (left) {
        left = left.left;
        leftDepth++;
      }
      while (right) {
        right = right.right;
        rightDepth++;
      }

      // 是满二叉树
      if (leftDepth === rightDepth) {
        // 满二叉树节点总是：2^h - 1（跟节点h为1）
        return Math.pow(2, leftDepth) - 1;
      } else {
        // 1根节点数 + 递归寻找子树是否是满二叉树
        return 1 + countNodes(root.left) + countNodes(root.right);
      }
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    递归，O(n)。

    ```js
    var countNodes = function (root) {
      if (root === null) { return 0; }
      return 1 + countNodes(root.left) + countNodes(root.right);
    };
    ```
3. 解法三

    [二叉树的层序遍历](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#二叉树的层序遍历)，O(n)。

    ```js
    var countNodes = function (root) {
      let result = 0;

      const queue = [];

      root && queue.unshift(root);

      while (queue.length > 0) {
        // 记录当前层级节点数
        const length = queue.length;

        for (let i = 0; i < length; i++) {
          const node = queue.pop();
          result++;
          // 存放当前层下一层的节点
          node.left && queue.unshift(node.left);
          node.right && queue.unshift(node.right);
        }
      }
      return result;
    };
    ```
</details>

### 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

1. 解法

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    var isBalanced = function (root) {
      return getDepth(root) !== -1;
    };

    // 返回以node为根节点的树高度，若当前左子树右子树高度相差大于1则返回-1
    function getDepth(node) {
      if (node === null) { return 0; }

      // 递归获取左右子树高度
      let leftDepth = getDepth(node.left);
      if (leftDepth === -1) { return -1; }
      let rightDepth = getDepth(node.right);
      if (rightDepth === -1) { return -1; }

      if (Math.abs(leftDepth - rightDepth) > 1) { return -1; }

      // 当前树的高度 = 1根节点 + 最大值(左子树的高度, 右子树的高度)
      return 1 + Math.max(leftDepth, rightDepth);
    }
    ```

### 路径总和
给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

1. 解法一

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {number} targetSum
     * @return {boolean}
     */
    var hasPathSum = function (root, targetSum) {
      if (root === null) { return false; }
      if (root.left === null && root.right === null && targetSum === root.val) { return true; }
      return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    迭代。

    ```js
    let hasPathSum = function (root, targetSum) {
      if (root === null) { return false; }
      const nodeArr = [root];
      const valArr = [0];
      while (nodeArr.length) {
        const curNode = nodeArr.shift();
        let curVal = valArr.shift() + curNode.val;

        // 为叶子结点，且和等于目标数，返回true
        if (curNode.left === null && curNode.right === null && curVal === targetSum) {
          return true;
        }

        // 左节点，将当前的数值也对应记录下来
        if (curNode.left) {
          nodeArr.push(curNode.left);
          valArr.push(curVal);
        }
        // 右节点，将当前的数值也对应记录下来
        if (curNode.right) {
          nodeArr.push(curNode.right);
          valArr.push(curVal);
        }
      }
      return false;
    };
    ```
3. 解法三

    递归+回溯，类似[二叉树的所有路径](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#二叉树的所有路径)。

    ```js
    var hasPathSum = function (root, targetSum) {
      const result = [];
      if (root === null) { return false; }
      traversal(root, [], result);
      return result.some((one) => {
        return one === targetSum;
      });
    };

    function traversal(cur, path, result) {
      // 推入（注意回溯要推出）
      path.push(cur.val);

      // 是叶子节点
      if (cur.left === null && cur.right === null) {
        // 转化路径为输出
        let sum = 0;
        for (let i = 0; i <= path.length - 1; i++) {
          sum += path[i];
        }
        result.push(sum);
        return;
      }

      if (cur.left) {
        traversal(cur.left, path, result);
        path.pop(); // 回溯（回溯和递归是一一对应的，有一个递归，就要有一个回溯）
      }

      if (cur.right) {
        traversal(cur.right, path, result);
        path.pop(); // 回溯
      }
    }
    ```
</details>

### 合并二叉树
![merge.jpg](./images/merge.jpg)

1. 解法一

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root1
     * @param {TreeNode} root2
     * @return {TreeNode}
     */
    var mergeTrees = function (root1, root2) {
      // 判断空节点
      if (root1 === null) { return root2; }
      if (root2 === null) { return root1; }

      root1.val += root2.val;
      root1.left = mergeTrees(root1.left, root2.left);
      root1.right = mergeTrees(root1.right, root2.right);
      return root1;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    迭代。

    ```js
    var mergeTrees = function (root1, root2) {
      if (root1 === null) return root2;
      if (root2 === null) return root1;

      let queue = [];
      queue.push(root1);
      queue.push(root2);
      while (queue.length) {
        let node1 = queue.shift();
        let node2 = queue.shift();
        node1.val += node2.val;
        if (node1.left !== null && node2.left !== null) {
          queue.push(node1.left);
          queue.push(node2.left);
        }
        if (node1.right !== null && node2.right !== null) {
          queue.push(node1.right);
          queue.push(node2.right);
        }
        if (node1.left === null && node2.left !== null) {
          node1.left = node2.left;
        }
        if (node1.right === null && node2.right !== null) {
          node1.right = node2.right;
        }
      }
      return root1;
    };
    ```
</details>

### 二叉搜索树中的众数
给你一个含重复值的二叉搜索树（BST）的根节点 `root` ，找出并返回 BST 中的所有 **众数**（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 **任意顺序** 返回。

假定 BST 满足如下定义：

- 结点左子树中所含节点的值 **小于等于** 当前节点的值
- 结点右子树中所含节点的值 **大于等于** 当前节点的值
- 左子树和右子树都是二叉搜索树


示例 1：

```
输入：root = [1,null,2,2]
输出：[2]
```

示例 2：

```
输入：root = [0]
输出：[0]
```

提示：

- 树中节点的数目在范围 `[1, 10 ** 4]` 内

**进阶**：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

1. 解法

    二叉搜索树的中序排序是递增输出。递归，从最左边最小的数开始，然后中然后右，达成按递增顺序执行「中：处理」。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    var findMode = function (root) {
      let count = 0;
      let maxCount = 1;
      let pre = root;
      let result = [];
      // 中序遍历（二叉搜索树会按照递增排序）
      const travelTree = function (cur) {
        if (cur === null) { return; }

        // 左
        travelTree(cur.left);

        // 中：处理（因为递增，所以以下处理逻辑）
        if (pre.val === cur.val) {
          count++;
        } else {
          count = 1;
        }
        pre = cur;
        if (count === maxCount) {
          result.push(cur.val);
        }
        if (count > maxCount) {
          result = [];
          maxCount = count;
          result.push(cur.val);
        }

        // 右
        travelTree(cur.right);
      };

      travelTree(root);
      return result;
    };
    ```

### 将有序数组转换为二叉搜索树
1. 解法

    递归。获取有序数组中间的数，作为每个子树的根节点。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {number[]} nums
     * @return {TreeNode}
     */
    var sortedArrayToBST = function (nums) {
      return buildTree(nums, 0, nums.length - 1);
    };

    const buildTree = (arr, left, right) => {
      if (left > right) { return null; }

      const mid = Math.floor((right + left) / 2); // 向上、向下取整不影响

      const root = new TreeNode(arr[mid]);
      root.left = buildTree(arr, left, mid - 1);
      root.right = buildTree(arr, mid + 1, right);
      return root;
    };
    ```

### 二叉树的层序遍历
>类似题目可微调解法解决：二叉树的层序遍历 II、二叉树的右视图、二叉树的层平均值、N 叉树的层序遍历、在每个树行中找最大值、填充每个节点的下一个右侧节点指针、填充每个节点的下一个右侧节点指针 II、二叉树的最大深度、二叉树的最小深度、翻转二叉树、找树左下角的值、二叉树的锯齿形层序遍历。

1. 解法

    **层序遍历 -> 广度优先遍历（队列实现）。**

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    var levelOrder = function (root) {
      const result = [];

      const queue = [];

      root && queue.unshift(root);

      while (queue.length > 0) {
        // 记录当前层级节点数
        const length = queue.length;

        // 存放每一层的节点
        const curLevel = [];
        for (let i = 0; i < length; i++) {
          const node = queue.pop();
          curLevel.push(node.val);
          // 存放当前层下一层的节点
          node.left && queue.unshift(node.left);
          node.right && queue.unshift(node.right);
        }
        // 把每一层的结果放到结果数组
        result.push(curLevel);
      }
      return result;
    };
    ```

### 子结构判断
给定两棵二叉树 `tree1` 和 `tree2`，判断 `tree2` 是否以 `tree1` 的某个节点为根的子树具有 **相同的结构和节点值** 。
注意，**空树** 不会是以 `tree1` 的某个节点为根的子树具有 **相同的结构和节点值** 。

1. 解法

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val) {
     *     this.val = val;
     *     this.left = this.right = null;
     * }
     */
    /**
     * @param {TreeNode} A
     * @param {TreeNode} B
     * @return {boolean}
     */
    var isSubStructure = function(A, B) {
      if (A === null || B === null) { return false; }

      // 递归A的所有节点（先序遍历）：先找到匹配的根节点，再判断其子树是否匹配
      return dfs(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B);
    }

    // 递归判断A为根节点的子树是否包含B
    function dfs(A, B) {
      if (B === null) { return true; }
      if (A === null) { return false; }

      return A.val === B.val && dfs(A.left, B.left) && dfs(A.right, B.right);
    }
    ```

### 从中序与后序遍历序列构造二叉树
给定两个整数数组 `inorder` 和 `postorder` ，其中 `inorder` 是二叉树的中序遍历， `postorder` 是同一棵树的后序遍历，请你构造并返回这颗 *二叉树* 。

示例 1:

![tree.jpg](./images/tree.jpg)

```
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
```

示例 2:

```
输入：inorder = [-1], postorder = [-1]
输出：[-1]
```

提示:

- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- `inorder` 和 `postorder` 都由 **不同** 的值组成
- `postorder` 中每一个值都在 `inorder` 中
- `inorder` **保证**是树的中序遍历
- `postorder` **保证**是树的后序遍历

1. 解法

    递归，构造二叉树。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {number[]} inorder
     * @param {number[]} postorder
     * @return {TreeNode}
     */
    var buildTree = function (inorder, postorder) {
      if (inorder.length === 0) return null;
      const rootVal = postorder.pop(); // 推出 后序的最后一个元素：根节点值
      const rootIndex = inorder.indexOf(rootVal); // 根节点值 所在 中序的下标（可以分割 左右子树）
      const root = new TreeNode(rootVal); // 创建根节点
      // 有了根节点位置，能分割左右子树：中序[左节点n个, 根, 右节点m个]，后序[左节点n个, 右节点m个, 根]（注意，后序最后一个节点已经推出）
      root.left = buildTree(inorder.slice(0, rootIndex), postorder.slice(0, rootIndex),); // 左子树的根节点
      root.right = buildTree(inorder.slice(rootIndex + 1), postorder.slice(rootIndex),); // 右子树的根节点
      return root;
    };
    ```

### 从前序与中序遍历序列构造二叉树
1. 解法

    递归，构造二叉树。

    ```js
    var buildTree = function (preorder, inorder) {
      if (preorder.length === 0) return null;
      const rootVal = preorder.shift(); // 推出 前序的第一个元素：根节点值
      const rootIndex = inorder.indexOf(rootVal); // 根节点值 所在 中序的下标（可以分割 左右子树）
      const root = new TreeNode(rootVal); // 创建根节点
      // 有了根节点位置，能分割左右子树：前序[根, 左节点n个, 右节点m个]（注意，前序第一个节点已经推出），中序[左节点n个, 根, 右节点m个]
      root.left = buildTree(preorder.slice(0, rootIndex), inorder.slice(0, rootIndex),); // 左子树的根节点
      root.right = buildTree(preorder.slice(rootIndex), inorder.slice(rootIndex + 1),); // 右子树的根节点
      return root;
    };
    ```

### 最大二叉树
给定一个不重复的整数数组 `nums` 。 **最大二叉树** 可以用下面的算法从 `nums` 递归地构建:

1. 创建一个根节点，其值为 `nums` 中的最大值。
2. 递归地在最大值 **左边** 的 **子数组前缀上** 构建左子树。
3. 递归地在最大值 **右边** 的 **子数组后缀上** 构建右子树。

返回 `nums` 构建的 *最大二叉树* 。

示例 1：

![tree1_.jpg](./images/tree1_.jpg)

```
输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。
```

示例 2：

![tree2_.jpg](./images/tree2_.jpg)

```
输入：nums = [3,2,1]
输出：[3,null,2,null,1]
```

提示：

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- `nums` 中的所有整数 **互不相同**

1. 解法

    递归，构造二叉树。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {number[]} nums
     * @return {TreeNode}
     */
    var constructMaximumBinaryTree = function (nums) {
      if (nums.length === 0) { return null; }

      let maxIndex = 0;
      let maxVal = nums[0];
      // 找到 最大值、最大值下标
      for (let i = 1; i < nums.length; i++) {
        if (nums[i] > maxVal) {
          maxIndex = i;
          maxVal = nums[i];
        }
      }

      const rootNode = new TreeNode(maxVal);
      rootNode.left = constructMaximumBinaryTree(nums.slice(0, maxIndex));
      rootNode.right = constructMaximumBinaryTree(nums.slice(maxIndex + 1));
      return rootNode;
    };
    ```

### 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

示例 1：

![binarytree.png](./images/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
```

示例 2：

![binarytree.png](./images/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
```

示例 3：

```
输入：root = [1,2], p = 1, q = 2
输出：1
```

提示：

- 树中节点数目在范围 `[2, 10 ** 5]` 内。
- `-(10 ** 9) <= Node.val <= 10 ** 9`
- 所有 `Node.val` `互不相同` 。
- `p != q`
- `p` 和 `q` 均存在于给定的二叉树中。

1. 解法

    递归，就是数学证明。看不懂……

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val) {
     *     this.val = val;
     *     this.left = this.right = null;
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    var lowestCommonAncestor = function (root, p, q) {    // 最近公共祖先：左右子树分别包含p、q 或 p、q自己就是另一个节点的祖先
      if (root === null) { return null; }
      if (root === p || root === q) {
        return root;
      }

      let left = lowestCommonAncestor(root.left, p, q);
      let right = lowestCommonAncestor(root.right, p, q);
      if (left === null) {
        return right;
      }
      if (right === null) {
        return left;
      }
      if (right && left) {
        return root;
      }
      return null;
    };
    ```

### 从二叉树一个节点到另一个节点每一步的方向
>类似题目可微调解法解决：求其路径节点值、求其路径长度。

请找到从节点 `s` 到节点 `t` 的 **最短路径** ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 `'L'` ，`'R'` 和 `'U'` 分别表示一种方向：

- `'L'` 表示从一个节点前往它的 **左孩子** 节点。
- `'R'` 表示从一个节点前往它的 **右孩子** 节点。
- `'U'` 表示从一个节点前往它的 **父** 节点。

请你返回从 `s` 到 `t` **最短路径** 每一步的方向。

1. 解法

    从root出发，找到抵达 起点 和 终点 的路径，然后去掉前缀相同的部分——找到最近公共祖先，最后解为：起点 -> 最近公共祖先 -> 终点。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {number} startValue
     * @param {number} destValue
     * @return {string}
     */
    var getDirections = function (root, startValue, destValue) {
      let pathToStart = [root];
      helper(root, startValue, pathToStart);

      let pathToDest = [root];
      helper(root, destValue, pathToDest);

      let commonParent = null;  // 最近公共祖先（若要求返回节点值）

      // 找到最近公共祖先
      while (
        pathToStart.length > 0 &&
        pathToDest.length > 0 &&
        pathToStart[0] === pathToDest[0]
      ) {
        commonParent = pathToStart[0];

        pathToStart = pathToStart.slice(1);
        pathToDest = pathToDest.slice(1);
      }

      // 左边向上 + 右边向下
      return "U".repeat(pathToStart.length) + pathToDest.join("");

      // 若要求返回节点值，则：
      // return pathToStart.reverse().concat(commonParent).concat(pathToDest).map((node)=>node.val);

      // 若要求返回长度，则：
      // return pathToStart.length + 1 + pathToDest.length;
    };

    // 递归、深度优先，查找：以node为根节点，目标是target的路径，路径存储在path
    function helper(node, target, path) {
      if (node === null) { return false; }

      if (node.val === target) { return true; }

      // 向左
      path.push("L" /* 若要求返回节点值，则：node.left */);
      if (helper(node.left, target, path)) { return true; }
      path.pop(); // 没找到，回溯

      // 向右
      path.push("R" /* 若要求返回节点值，则：node.right */);
      if (helper(node.right, target, path)) { return true; }
      path.pop(); // 没找到，回溯

      return false;
    }
    ```

### 二叉搜索树的最近公共祖先
1. 解法一

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val) {
     *     this.val = val;
     *     this.left = this.right = null;
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    var lowestCommonAncestor = function (root, p, q) {
      if (root === null) { return root; }

      if (root.val > p.val && root.val > q.val) { // 向左子树查询
        return lowestCommonAncestor(root.left, p, q);
      }
      if (root.val < p.val && root.val < q.val) { // 向右子树查询
        return lowestCommonAncestor(root.right, p, q);
      }
      return root;
    };
    ```
2. 解法二

    迭代。

    ```js
    var lowestCommonAncestor = function (root, p, q) {
      while (root) {
        if (root.val > p.val && root.val > q.val) {
          root = root.left;
        } else if (root.val < p.val && root.val < q.val) {
          root = root.right;
        } else {
          return root;
        }
      }
      return null;
    };
    ```

### 二叉搜索树中的插入操作
1. 解法

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {number} val
     * @return {TreeNode}
     */
    var insertIntoBST = function (root, val) {
      return setInOrder(root, val);
    };

    const setInOrder = (root, val) => {
      if (root === null) { return new TreeNode(val); }

      if (root.val > val) { root.left = setInOrder(root.left, val); }
      if (root.val < val) { root.right = setInOrder(root.right, val); }

      return root;
    };
    ```

### 删除二叉搜索树中的节点
1. 解法

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {number} key
     * @return {TreeNode}
     */
    var deleteNode = function (root, key) {
      if (root === null) { return null; }

      if (key > root.val) {
        root.right = deleteNode(root.right, key);
        return root;
      } else if (key < root.val) {
        root.left = deleteNode(root.left, key);
        return root;
      }
      // 找到删除点
      else {
        // 1. 该节点是叶节点：直接删除
        if (root.left === null && root.right === null) {
          return null;
        }

        // 2. 有一个孩子节点不存在：另一个顶替删除节点位置
        if (root.left && root.right === null) {
          return root.left;
        } else if (root.right && root.left === null) {
          return root.right;
        }

        // 3. 左右节点都存在：右边节点的最左边（最小节点）替换删除节点位置
        // 获取右边节点最小值节点
        const minNode = getMinNode(root.right);
        // 将待删除节点的值替换为最小值节点值
        root.val = minNode.val;
        // 删除最小值节点
        root.right = deleteNode(root.right, minNode.val);
        return root;
      }
    };

    // 获取最左边节点（二叉搜索树最小节点）
    function getMinNode(root) {
      while (root.left) {
        root = root.left;
      }
      return root;
    }
    ```

### 修剪二叉搜索树
给你二叉搜索树的根节点 `root` ，同时给定最小边界`low` 和最大边界 `high`。通过修剪二叉搜索树，使得所有节点的值在`[low, high]`中。修剪树 **不应该** 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 **唯一的答案** 。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

1. 解法

    递归。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @param {number} low
     * @param {number} high
     * @return {TreeNode}
     */
    var trimBST = function (root, low, high) {
      if (root === null) { return null; }

      if (root.val < low) {
        return trimBST(root.right, low, high);
      }
      if (root.val > high) {
        return trimBST(root.left, low, high);
      }

      root.left = trimBST(root.left, low, high);
      root.right = trimBST(root.right, low, high);
      return root;
    };
    ```

### 把二叉搜索树转换为累加树
1. 解法

    递归，反中序遍历（后->中->前）累加。

    ```js
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    var convertBST = function (root) {
      let pre = 0;
      const ReverseInOrder = (cur) => {
        if (cur === null) { return; }

        ReverseInOrder(cur.right);

        cur.val += pre;
        pre = cur.val;

        ReverseInOrder(cur.left);
      };
      ReverseInOrder(root);
      return root;
    };
    ```

---
## 数组

### 移除元素
给你一个数组 `nums` 和一个值 `val`，你需要 **原地** 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1：

```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
```

示例 2：

```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
```

提示：

- `0 <= nums.length <= 100`

1. 解法一

    **双指针法（快慢指针法）：通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。**

    ```js
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    var removeElement = function(nums, val) {
      let j = 0; // 慢指针j：指向更新 新数组下标的位置

      // 快指针i：寻找新数组的元素 ，新数组就是不含有目标元素的数组
      for(let i = 0; i < nums.length; i++){
        if(nums[i] !== val){
          nums[j++] = nums[i]
        }
      }

      return j;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    ```js
    var removeElement = function(nums, val) {
        let delCount = 0;
        const len = nums.length;

        // 类似双指针
        for (let i = 0; i < len; i++) {
            if (nums[i] === val) {
                delCount += 1;
            } else if (delCount !== 0) {
                nums[i - delCount] = nums[i];
            }
        }

        return len - delCount;
    };
    ```
3. 解法三

    暴力解法，O(n^2)。

    ```js
    var removeElement = function(nums, val) {
      let len = nums.length;

      for(let i = 0; i < len; i++) {
        if(nums[i] === val){    // 若发现需要移除的元素，则将数组集体向前移动一位
          for(let j = i + 1; j < len; j++) {
            nums[j - 1] = nums[j];
          }
          i--;      // 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
          len--;    // 此时数组的大小-1
        }
      }

      return len;
    };
    ```
</details>

### 有序数组的平方
给你一个按 **非递减顺序** 排序的整数数组 `nums`，返回 **每个数字的平方** 组成的新数组，要求也按 **非递减顺序** 排序。

示例 1：

```
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
```

示例 2：

```
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
```

提示：

- `1 <= nums.length <= 10 ** 4`
- `-(10 ** 4) <= nums[i] <= 10 ** 4`
- `nums` 已按 **非递减顺序** 排序

进阶：

- 请你设计时间复杂度为 $O(n)$ 的算法解决本问题

1. 解法

    双指针法，最大的平方值一定在两端。

    ```js
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    var sortedSquares = function(nums) {
        const newNums = [];
        let left = 0;
        let right = nums.length - 1;

        while (left <= right) {
            // 最大的平方值一定在两端
            if (Math.abs(nums[left]) > nums[right]) {
                newNums.unshift(nums[left] ** 2);
                left++;
            } else {
                newNums.unshift(nums[right] ** 2);
                right--;
            }
        }

        return newNums;
    };
    ```

### 数组中重复的数字
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
```

1. 解法一

    利用题目的条件：数字在下标范围内

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var findRepeatNumber = function (nums) {
      // 利用题目的条件：数字在下标范围内
      const tempNums = [];
      for (let i = 0, length = nums.length; i < length; i++) {
        if (tempNums[nums[i]] === nums[i]) {
          return nums[i];
        }
        tempNums[nums[i]] = nums[i];
      }
    };
    ```
2. 解法二

    利用题目的条件：数字在下标范围内。并且不用额外的数组。自哈希

    ```js
    var findRepeatNumber = function (nums) {
      // 利用题目的条件：数字在下标范围内。并且不用额外的数组。自哈希
      for (let i = 0, length = nums.length; i < length; i++) {
        // 因为n的长度的数组数字都在0~n-1，所以：要不然所有数字各一个，要不然就必须会有重复
        // 尝试把每个位置放上等于下标的数字
        // 若当前数字跟对应的索引不相同，则交换。
        while (nums[i] !== i) {
          if (nums[i] === nums[nums[i]]) {
            return nums[i];
          }
          const temp = nums[i];
          nums[i] = nums[temp];
          nums[temp] = temp;
        }
      }
    };
    ```

<details>
<summary>其他解法</summary>

3. 解法三

    哈希表。

    ```js
    var findRepeatNumber = function (nums) {
      // 哈希表
      const oneSet = new Set();

      for (let i = 0, length = nums.length; i < length; i++) {
        if (oneSet.has(nums[i])) {
          return nums[i];
        }
        oneSet.set(nums[i]);
      }
    };
    ```
4. 解法四

    排序后比较。

    ```js
    var findRepeatNumber = function (nums) {
      // 排序后比较
      const sortedNums = nums.sort()
      for (let i = 0, length = sortedNums.length; i < length - 1; i++) {
        if (sortedNums[i] === sortedNums[i + 1]) {
          return sortedNums[i]
        }
      }
    };
    ```
</details>

### 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

示例 1:
```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

示例 2:
```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

nums 是一个非递减数组

1. 解法一

    ```js
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    var search = function (nums, target) {
      const leftIdx = binarySearch(nums, target, true);
      const rightIdx = binarySearch(nums, target, false);
      if (leftIdx !== rightIdx) {
        return rightIdx - leftIdx;
      }
      return 0;
    };

    // 二分搜索：nums中，第一个大于等于 或 第一个大于 target 的下标
    const binarySearch = (nums, target, equal) => {
      let left = 0;
      let right = nums.length - 1;
      // 定义超出数组长度（表明nums中不存在要求的下标）
      let resultIndex = nums.length;

      while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] > target || (equal && nums[mid] === target)) {
          right = mid - 1;
          resultIndex = mid;
        } else {
          left = mid + 1;
        }
      }
      return resultIndex;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    ```js
    var search = function (nums, target) {
      const length = nums.length;
      let start = -1;
      let end = -1;

      let left = 0;
      let right = length - 1;
      // 二分搜索：找到左边界，找到第一次出现
      while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) {
          start = mid;
          right = mid - 1;
        } else if (nums[mid] > target) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }

      if (start === -1) {
        return 0;
      }

      left = 0;
      right = length - 1;
      // 二分搜索：找到右边界，找到最后一次出现
      while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) {
          end = mid;
          left = mid + 1;
        } else if (nums[mid] > target) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }

      return end - start + 1;
    };
    ```
3. 解法三

    暴力搜索、穷举搜索。

    ```js
    var search = function (nums, target) {
      let count = 0;
      nums.forEach((x) => {
        if (x === target) count++;
      });
      return count;
    };
    ```

    ```js
    var search = function (nums, target) {
      let left = 0;
      let right = nums.length - 1;

      // 左边搜索
      while (nums[left] !== target && left < nums.length) {
        ++left;
      }

      // 右边搜索
      while (nums[right] !== target && right >= 0) {
        --right;
      }

      return left <= right ? right - left + 1 : 0;
    };
    ```

    ```js
    const search = function (nums, target) {
      return nums.reduce((a, b) => (b === target ? a + 1 : a), 0);
    };
    ```
</details>

### 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
```
输入: [0,1,3]
输出: 2
```

示例 2:
```
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
```

1. 解法一

    >开闭区间的选择？

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var missingNumber = function (nums) {
      let left = 0;
      // 设置超出数组的下标，这样可以多判断一次，因为最大下标比长度小1，而最大数字等于长度
      let right = nums.length;
      // 二分搜索
      while (left < right) {
        const middle = Math.floor((left + right) / 2);
        if (nums[middle] === middle) {
          // middle可以排除
          left = middle + 1;
        } else {
          // middle不能被排除
          right = middle;
        }
      }
      return left;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    暴力搜索、穷举搜索。

    ```js
    var missingNumber = function (nums) {
      for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i) return i;
      }
      return nums.length;
    };
    ```

    ```js
    var missingNumber = function (nums) {
      let length = nums.length;
      // 等差数列求和
      let sum = (length + 1) * length / 2;
      for (let i of nums) {
        sum -= i;
      }
      return sum;
    };
    ```

    ```js
    var missingNumber = function (nums) {
      // 任何数字异或自己等于0，0异或任何数字等于这个数字
      let xor = 0;
      for (let i = 0; i < nums.length; i++) {
        xor ^= nums[i] ^ i;
      }
      return xor ^ nums.length;
    };
    ```
</details>

### 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。

示例 1：

```
输入：[3,4,5,1,2]
输出：1
```

示例 2：

```
输入：[2,2,2,0,1]
输出：0
```

1. 解法一

    二分法查找，对比中点值和最右边值。

    ```js
    /**
     * @param {number[]} numbers
     * @return {number}
     */
    var minArray = function (numbers) {
      let left = 0;
      let right = numbers.length - 1;
      while (left < right) {
        const middle = Math.floor((right + left) / 2);
        if (numbers[middle] < numbers[right]) {
          right = middle;
        } else if (numbers[middle] > numbers[right]) {
          left = middle + 1;
        }

        // 若相等，则无论right是不是最小值，都有替代品，因此right-1，让迭代滚起来
        else {
          right -= 1;
        }
      }
      // 退出时，left === right
      return numbers[left];
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    ```js
    var minArray = function (numbers) {
      const firstOne = numbers[0];
      const lastOne = numbers[numbers.length - 1];

      // 全部旋转（或者没有旋转）
      if (firstOne < lastOne) {
        return firstOne;
      }
      // 第一个和最后一个数字相等，用遍历
      else if (firstOne === lastOne) {
        for (let i = numbers.length - 1; i > 0; i--) {
          if (numbers[i] < numbers[i - 1]) {
            return numbers[i];
          }
        }
        return firstOne;
      }
      // 第一个比最后一个大，用二分搜索：找到 左边第一个小于firstOne的数
      else {
        let left = 0;
        let right = numbers.length - 1;
        let result = lastOne;

        while (left <= right) {
          const middle = Math.floor((left + right) / 2);
          if (numbers[middle] < firstOne) {
            right = middle - 1;
            result = numbers[middle];
          } else if (numbers[middle] >= firstOne) {
            left = middle + 1;
          }
        }
        return result;
      }
    };
    ```
</details>

### 合并两个有序数组
给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意**：最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 0 ，应忽略。`nums2` 的长度为 `n` 。


示例 1：

```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

示例 2：

```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

示例 3：

```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```

提示：

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-(10 ** 9) <= nums1[i], nums2[j] <= 10 ** 9`

**进阶**：你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？

1. 解法一

    从后向前，双指针。

    ```js
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
     var merge = function (nums1, m, nums2, n) {
       let i = m - 1;
       let j = n - 1;
       let k = m + n - 1;
       while (i >= 0 && j >= 0) {
         // 从后往前放
         if (nums1[i] <= nums2[j]) {
           nums1[k] = nums2[j];
           j--;
         } else {
           nums1[k] = nums1[i];
           i--;
         }
         k--;
       }

       // 若nums2还没有到头，则需要直接把nums2顶部剩余项直接替换nums1顶部
       if (j >= 0) {
         nums1.splice(0, j + 1, ...nums2.slice(0, j + 1));
       }
     };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    暴力解法，利用一个新数据（空间复杂度O(m+n)）。不推荐。

    ```js
    var merge = function (nums1, m, nums2, n) {
      let result = [];

      let i = 0;
      let j = 0;
      while (i < m && j < n) {
        if (nums1[i] <= nums2[j]) {
          result.push(nums1[i]);
          i++;
        } else {
          result.push(nums2[j]);
          j++;
        }
      }

      if (i === m) {
        result.push(...nums2.slice(j));
      }

      if (j === n) {
        result.push(...nums1.slice(i, m));
      }

      nums1.splice(0, n + m, ...result);
    };
    ```
</details>

### 删除有序数组中的重复项
给你一个 **非严格递增排列** 的数组 `nums` ，请你 原地 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。

考虑 `nums` 的唯一元素的数量为 `k` ，你需要做以下事情确保你的题解可以被通过：

- 更改数组 `nums` ，使 `nums` 的前 `k` 个元素包含唯一元素，并按照它们最初在 `nums` 中出现的顺序排列。`nums` 的其余元素与 `nums` 的大小不重要。
- 返回 `k` 。

判题标准:

系统会用下面的代码来测试你的题解:

```
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有断言都通过，那么您的题解将被 **通过**。

示例 1：

```
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
```

示例 2：

```
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
```

提示：

- `1 <= nums.length <= 3 * 10 ** 4`
- `-(10 ** 4) <= nums[i] <= 10 ** 4`
- `nums` 已按 **非严格递增** 排列

1. 解法

    双指针。

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var removeDuplicates = function (nums) {
      let left;
      let right;
      for (left = 0, right = 1; right < nums.length; right++) {
        if (nums[left] !== nums[right]) {
          if (right - left > 1) {  // 可选优化：否则 left + 1 === right
            nums[left + 1] = nums[right];
          }

          left++;
        }
      }
      return left + 1;
    };
    ```

### 判断扑克牌顺子
0代表任意数。

1. 解法

    ```js
    /**
     * @param {number[]} places
     * @return {boolean}
     */
    var checkDynasty = function (places) {
      // 排序
      places.sort((a, b) => {
        return a - b;
      });

      // 0数量
      let zeroNum = places.filter((num) => {
        return num === 0;
      }).length;

      for (let i = zeroNum + 1, pre = places[zeroNum]; i < places.length; i++) {
        if (places[i] === pre) {
          return false;
        } else if (places[i] === pre + 1) {

        } else {
          if (places[i] - pre - 1 <= zeroNum) { // 0足够补
            zeroNum -= places[i] - pre - 1;
          } else {
            return false;
          }
        }

        pre = places[i];
      }
      return true;
    };
    ```

### 移动零
给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

```
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
```

示例 2:

```
输入: nums = [0]
输出: [0]
```

提示:

- `1 <= nums.length <= 10 ** 4`
- `-(2 ** 31) <= nums[i] <= 2 ** 31 - 1`


进阶：你能尽量减少完成的操作次数吗？

1. 解法一

    双指针。

    ```js
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    var moveZeroes = function (nums) {
      // 双指针，移动数组，最后补0
      let noZeroIndex = 0;
      for (let i = 0; i < nums.length; i++) {
        if (i !== noZeroIndex) {
          nums[noZeroIndex] = nums[i];
        }

        if (nums[i] !== 0) {
          noZeroIndex++;
        }
      }

      nums.fill(0, noZeroIndex);
    };
    ```
2. 解法二

    双指针。

    ```js
    var moveZeroes = function (nums) {
      // 双指针。若 i项!==0，则替换i、j项的值并j指针自增。
      for (let right = 0, left = 0; right < nums.length; right++) {
        if (nums[right] !== 0) {
          [nums[right], nums[left]] = [nums[left], nums[right]];
          left++;
        }
      }
    };
    ```

### 搜索二维矩阵 II
编写一个高效的算法来搜索 `m x n` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：

- 每行的元素从左到右升序排列。
- 每列的元素从上到下升序排列。

示例:

```
现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。

给定 target = 20，返回 false。
```

1. 解法一

    从右上角开始行动（类似二叉树搜索或二分搜索），只能向下和向左，O(n+m)。

    ```js
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    var findNumberIn2DArray = function (matrix, target) {
      const columnLength = matrix.length;
      const rowLength = matrix[0]?.length ?? 0;

      let column = 0;
      let row = rowLength - 1;
      // 从右上角开始行动（类似二叉树搜索或二分搜索），只能向下和向左
      while (column < columnLength && row >= 0) {
        if (matrix[column][row] < target) {
          column++;
        } else if (matrix[column][row] > target) {
          row--;
        } else {
          return true;
        }
      }
      return false;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    从左下角开始行动（类似二叉树搜索或二分搜索），只能向上或向右，O(n+m)。

    ```js
    var findNumberIn2DArray = function (matrix, target) {
      const columnLength = matrix.length;
      const rowLength = matrix[0]?.length ?? 0;

      let column = columnLength - 1;
      let row = 0;
      // 从左下角开始行动（类似二叉树搜索或二分搜索），只能向上或向右
      while (column >= 0 && row < rowLength) {
        if (matrix[column][row] < target) {
          row++;
        } else if (matrix[column][row] > target) {
          column--;
        } else {
          return true;
        }
      }
      return false;
    };
    ```
</details>

### 长度最小的子数组
给定一个含有 `n` 个正整数的数组和一个正整数 `target` 。

找出该数组中满足其总和大于等于 `target` 的长度最小的 **连续子数组** `[nums[l], nums[l+1], ..., nums[r-1], nums[r]]` ，并返回其长度。如果不存在符合条件的子数组，返回 `0` 。

示例 1：

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```

示例 2：

```
输入：target = 4, nums = [1,4,4]
输出：1
```

示例 3：

```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

提示：

- `1 <= target <= 10 ** 9`
- `1 <= nums.length <= 10 ** 5`
- `1 <= nums[i] <= 10 ** 5`


进阶：

- 如果你已经实现 $O(n)$ 时间复杂度的解法, 请尝试设计一个 $O(n*log(n))$ 时间复杂度的解法。

1. 解法一

    滑动窗口（双指针）。

    ```js
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    var minSubArrayLen = function (target, nums) {
      let result = Number.MAX_SAFE_INTEGER;

      for (let right = 0, left = 0, sum = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
          result = Math.min(right - left + 1, result);
          sum -= nums[left];
          left++;
        }
      }

      return result === Number.MAX_SAFE_INTEGER ? 0 : result;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    暴力解法，O(n^2)，已超时。

    ```js
    var minSubArrayLen = function (target, nums) {
      let minLen = 0;
      for (let i = 0; i < nums.length; i++) {
        let sum = nums[i];
        if (sum >= target) {
          minLen = 1;
          break;
        }
        for (let j = i + 1; j < nums.length; j++) {
          sum = sum + nums[j];
          if (sum >= target) {
            minLen = minLen === 0 ? j - i + 1 : Math.min(j - i + 1, minLen);
            break;
          }
        }
      }
      return minLen;
    };
    ```

    ```js
    var minSubArrayLen = function(target, nums) {
        let minLen = 0;
        for(let i = 0; i < nums.length; i++){
            let sum = nums[i]

            // 已超时
            for(let j = i; j < nums.length;sum+= nums[++j]){
                if(sum >= target){
                    minLen =  minLen === 0 ? j - i + 1 : Math.min(j - i + 1,minLen);
                    break;
                }
            }
        }
        return minLen;
    };
    ```
3. 解法三

    把暴力解法改成二分法，从而达到O(n*logn)。

    ```js
    var minSubArrayLen = function (target, nums) {
      const len = nums.length;

      let result = Number.MAX_SAFE_INTEGER;

      // 前缀和
      // sums[0] = 0 意味着前 0 个元素的前缀和为 0
      // sums[1] = nums[0] 前 1 个元素的前缀和为 nums[0]
      // sums[2] = nums[0] + nums[1]
      // sums比nums长度多1
      const sums = [0];

      for (let i = 1; i <= len; i++) {
        sums[i] = sums[i - 1] + nums[i - 1];
      }

      for (let j = 0; j < len; j++) {
        let endValue = sums[j] + target;

        let bound = binarySearch(sums, endValue, j, len);
        if (bound !== -1) {
          result = Math.min(result, bound - j);
        }
      }

      return result === Number.MAX_SAFE_INTEGER ? 0 : result;
    };

    // 二分搜索查找大于等于searchVal
    function binarySearch(arr, searchVal, leftIndex, rightIndex) {
      while (leftIndex <= rightIndex) {
        const middleIndex = Math.floor((leftIndex + rightIndex) / 2);

        if (searchVal < arr[middleIndex]) {
          rightIndex = middleIndex - 1;
        } else if (searchVal > arr[middleIndex]) {
          leftIndex = middleIndex + 1;
        } else {
          return middleIndex;
        }
      }

      // 找不到等于的，再判断是否有大于的
      return arr[leftIndex] > searchVal ? leftIndex : -1;
    }
    ```
</details>

### 螺旋矩阵 II
给你一个正整数 `n` ，生成一个包含 `1` 到 `n^2` 所有元素，且元素按顺时针顺序螺旋排列的 `n x n` 正方形矩阵 `matrix` 。

示例 1：

![螺旋矩阵 II-1](./images/Spiral-Matrix-II-1.jpg)

```
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
```

示例 2：

```
输入：n = 1
输出：[[1]]
```

提示：

- `1 <= n <= 20`

1. 解法一

    四个边界按顺序填入，然后边界缩小，左闭右闭。

    ```js
    /**
     * @param {number} n
     * @return {number[][]}
     */
    var generateMatrix = function (n) {
      // 二维数组
      const res = new Array(n).fill(0).map(() => new Array(n).fill(0));

      // 四个边界
      let left = 0;
      let right = n - 1;
      let top = 0;
      let bottom = n - 1;

      // 累加值
      let count = 1;
      // 结束值
      const endCount = n * n;

      // 左闭右闭
      while (count <= endCount) {
        for (let i = left; i <= right; i++) res[top][i] = count++; // left to right.
        top++;
        for (let i = top; i <= bottom; i++) res[i][right] = count++; // top to bottom.
        right--;
        for (let i = right; i >= left; i--) res[bottom][i] = count++; // right to left.
        bottom--;
        for (let i = bottom; i >= top; i--) res[i][left] = count++; // bottom to top.
        left++;
      }

      return res;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    注意确定区间的开闭统一，比如此解就是规定所有边都是左闭右开。

    ```js
    var generateMatrix = function (n) {
      // 二维数组
      const res = new Array(n).fill(0).map(() => new Array(n).fill(0));

      // 定义每循环一个圈的起始位置
      let startX = 0;
      let startY = 0;
      // 需要控制每一条边遍历的长度，每次循环各边界收缩一位（左闭右开）
      let offset = 1;
      // 每个圈循环几次，例如n为奇数3，那么loop = 1 只是循环一圈，矩阵中间的一个值最后单独处理
      let loop = Math.floor(n / 2);
      // 用来给矩阵中每一个空格累加赋值
      let count = 1;

      while (loop > 0) {
        let i; // x轴
        let j; // y轴

        // 下面开始的四个for就是模拟转了一圈

        // 模拟填充上行从左到右（左闭右开）
        for (i = startX; i < n - offset; i++) {
          res[startY][i] = count;
          count++;
        }

        // 模拟填充右列从上到下（左闭右开）
        for (j = startY; j < n - offset; j++) {
          res[j][i] = count;
          count++;
        }

        // 模拟填充下行从右到左（左闭右开）
        for (; i > startX; i--) {
          res[j][i] = count;
          count++;
        }

        // 模拟填充左列从下到上（左闭右开）
        for (; j > startY; j--) {
          res[j][i] = count;
          count++;
        }

        // 新的一圈，起始位置要各自加1，例如：第一圈起始位置是(0, 0)，第二圈起始位置是(1, 1)
        startX++;
        startY++;
        // 控制每一条边遍历的长度加1
        offset++;

        loop--
      }

      // 如果n为奇数的话，需要单独给矩阵最中间的位置赋值
      if (n % 2) {
        const mid = Math.floor(n / 2);
        res[mid][mid] = count;
      }

      return res;
    };
    ```
</details>

### 和为 K 的子数组
给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 该数组中和为 `k` 的连续子数组的个数 。

子数组是数组中元素的连续非空序列。

示例 1：

```
输入：nums = [1,1,1], k = 2
输出：2
```

示例 2：

```
输入：nums = [1,2,3], k = 3
输出：2
```

提示：

- `1 <= nums.length <= 2 * 10 ** 4`
- `-1000 <= nums[i] <= 1000`
- `-(10 ** 7) <= k <= 10 ** 7`

1. 解法一

    暴力解法，O(n^2)。

    ```js
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    var subarraySum = function (nums, k) {
      let result = 0;
      for (let i = 0; i < nums.length; i++) {
        for (let sum = 0, j = i; j < nums.length; j++) {
          sum += nums[j];
          if (sum === k) {
            result++;
          }
        }
      }

      return result;
    };
    ```
2. 解法二

    前缀和+哈希表，O(n)。

    ```js
    const subarraySum = (nums, k) => {
      let result = 0;

      // 哈希表 {前缀和的数值: 数量}
      const map = new Map([[0, 1]]); // 需要初始化0个项前缀和为0有1个的情况，用于避免遗漏后面第一个直接等于k的前缀和计数

      // 前缀和
      let prefixSum = 0;

      for (let i = 0; i < nums.length; i++) {
        prefixSum += nums[i];

        // 单向查找：若之前的前缀和存在 prefixSum - k 的值，则累计
        if (map.has(prefixSum - k)) {
          result += map.get(prefixSum - k);
        }

        if (map.has(prefixSum)) {
          map.set(prefixSum, map.get(prefixSum) + 1);
        } else {
          map.set(prefixSum, 1);
        }
      }
      return result;
    };
    ```

### 除自身以外数组的乘积
给你一个整数数组 `nums`，返回 *数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积* 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32** 位 整数范围内。

请 **不要使用除法**，且在 `O(n)` 时间复杂度内完成此题。

**进阶**：你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）

1. 解法

    分别计算左右乘积，2次循环、用result存储计算过程，从而减少空间复杂度。时间复杂度：O(1)。

    ```js
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    var productExceptSelf = function (nums) {
      const len = nums.length;
      const result = Array.from({ length: len });

      // result[i]：先保存索引i左侧所有元素的乘积
      result[0] = 1; // 因为索引0左侧没有元素
      for (let i = 1; i < len; i++) {
        result[i] = nums[i - 1] * result[i - 1];
      }

      // r：循环时右侧所有元素的乘积
      let r = 1; // 因为索引len-1右侧没有元素
      for (let i = len - 1; i >= 0; i--) {
        // 除自身以外数组的乘积 result[i] = 左边的乘积 result[i] * 右边的乘积 r
        result[i] = result[i] * r;

        r *= nums[i]; // 下一个循环时，索引i+1右侧所有元素的乘积
      }

      return result;
    };
    ```

### 扁平化嵌套数组
请你编写一个函数，它接收一个 **多维数组** `arr` 和它的深度 `n` ，并返回该数组的 **扁平化** 后的结果。

**多维数组** 是一种包含整数或其他 **多维数组** 的递归数据结构。

数组 **扁平化** 是对数组的一种操作，定义是将原数组部分或全部子数组删除，并替换为该子数组中的实际元素。只有当嵌套的数组深度大于 `n` 时，才应该执行扁平化操作。第一层数组中元素的深度被认为是 0。

请在没有使用内置方法 `Array.flat` 的前提下解决这个问题。

示例 1：

```
输入
arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 0
输出
[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

解释
传递深度 n=0 的多维数组将始终得到原始数组。这是因为 子数组(0) 的最小可能的深度不小于 n=0 。因此，任何子数组都不应该被平面化。
```

示例 2：

```
输入
arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 1
输出
[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]

解释
以 4 、7 和 13 开头的子数组都被扁平化了，这是因为它们的深度为 0 ， 而 0 小于 1 。然而 [9,10,11] 其深度为 1 ，所以未被扁平化。
```

示例 3：

```
输入
arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 2
输出
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

解释
所有子数组的最大深度都为 1 。因此，它们都被扁平化了。
```

1. 解法一

    递归

    ```js
    /**
     * @param {Array} arr
     * @param {number} depth
     * @return {Array}
     */
    var flat = function (arr, n) {
      if (n > 0) {
        let result = [];

        for (let item of arr) {
          if (Array.isArray(item)) {
            result.push(...flat(item, n - 1))
          } else {
            result.push(item);
          }
        }
        return result;
      } else {
        return arr;
      }
    };
    ```
2. 解法二

    循环（利用了`Array.prototype.concat`对参数尝试去掉一层嵌套的机制）。

    ```js
    var flat = function (arr, n) {
      while (n > 0 && arr.some(Array.isArray)) {
        arr = [].concat(...arr); // concat会尝试对所有参数解一层嵌套（否则还是需要一层for循环实现）
        n--;
      }
      return arr;
    };
    ```

### 删除有序数组中的重复项 II
给你一个有序数组 `nums` ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素**只出现两次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 **修改输入数组** 并在使用 `O(1)` 额外空间的条件下完成。

示例 1：

```
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
```

示例 2：

```
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
```

提示：

- `1 <= nums.length <= 3 * 10 ** 4`
- `-(10 ** 4) <= nums[i] <= 10 ** 4`
- `nums` 已按升序排列

1. 解法

    双指针。

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var removeDuplicates = function (nums, maxRepeatTimes = 1) {
      let left;
      let right;
      let repeatTimes = 0;

      for (left = 0, right = 1; right < nums.length; right++) {
        if (nums[left] === nums[right]) {
          repeatTimes++;

          if (repeatTimes <= maxRepeatTimes) {
            nums[left + 1] = nums[right];
            left++;
          }
        } else {
          repeatTimes = 0;

          nums[left + 1] = nums[right];
          left++;
        }
      }

      return left + 1;
    };
    ```

### 合并区间
以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 *一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间* 。

示例 1：

```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

示例 2：

```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

提示：

- `1 <= intervals.length <= 10 ** 4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10 ** 4`

1. 解法

    必须先排序，然后才能顺序比较。

    ```js
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    var merge = function (intervals) {
      if (intervals.length <= 1) { return intervals; }

      const result = [];

      // 先排序：按第一个数（[0]）升序排序
      intervals.sort((a, b) => {
        return a[0] - b[0];
      });

      let temp = intervals[0];
      // 从前往后比较，需要数组是按[0]升序排序
      for (let i = 1; i < intervals.length; i++) {
        if (isCovered(temp, intervals[i])) {
          temp = [
            Math.min(temp[0], intervals[i][0]),
            Math.max(temp[1], intervals[i][1]),
          ];
        } else {
          result.push(temp);
          temp = intervals[i];
        }
      }
      result.push(temp);
      return result;
    };

    // 判断是否重合
    function isCovered(arr1, arr2) {
      if (arr2[0] > arr1[1] || arr1[0] > arr2[1]) {
        return false;
      }
      return true;
    }
    ```

### 对角线遍历
给你一个大小为 `m x n` 的矩阵 `mat` ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

示例1：

![diag1-grid.jpg](./images/diag1-grid.jpg)

```
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
```

示例 2：

```
输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
```

1. 解法

    参考[对角线打印二维数组](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/JS方法积累/手写代码/README.md#对角线打印二维数组)。

    ```js
    /**
     * @param {number[][]} mat
     * @return {number[]}
     */
    var findDiagonalOrder = function (mat) {
      const result = [];

      const row = mat[0].length; // 行长度
      const column = mat.length; // 列长度

      let flag = false;

      // i、_i：行下标；j：列下标
      for (let i = 0; i <= row - 1; i++) {
        const tempArr = [];
        for (let j = 0, _i = i; j <= column - 1 && _i >= 0; j++, _i--) {
          flag ? tempArr.push(mat[j][_i]) : tempArr.unshift(mat[j][_i]);
        }
        result.push(...tempArr);
        flag = !flag;
      }

      // i：行下标；j、_j：列下标
      for (let j = 1; j <= column - 1; j++) {
        const tempArr = [];
        for (let i = row - 1, _j = j; i >= 0 && _j <= column - 1; i--, _j++) {
          flag ? tempArr.push(mat[_j][i]) : tempArr.unshift(mat[_j][i]);
        }
        result.push(...tempArr);
        flag = !flag;
      }

      return result;
    };
    ```

---
## 字符串

### 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `s` 的形式给出。

不要给另外的数组分配额外的空间，你必须**原地修改输入数组**、使用 `O(1)` 的额外空间解决这一问题。

1. 解法

    前后镜像调换。

    ```js
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    var reverseString = function (s) {
      for (let i = 0, j = s.length - 1; i < j; i++, j--) {
        [s[i], s[j]] = [s[j], s[i]];
      }
      return s;
    };
    ```

### 反转字符串 II
给定一个字符串 `s` 和一个整数 `k`，从字符串开头算起，每计数至 `2k` 个字符，就反转这 `2k` 字符中的前 `k` 个字符。

- 如果剩余字符少于 `k` 个，则将剩余字符全部反转。
- 如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。

1. 解法一

    ```js
    /**
     * @param {string} s
     * @param {number} k
     * @return {string}
     */
    var reverseStr = function (s, k) {
      let result = "";
      while (s.length > 0) {
        let str = s.slice(0, 2 * k);
        s = s.slice(2 * k);

        result += [...str.slice(0, k)].reverse().join("") + str.slice(k);
      }
      return result;
    };
    ```
2. 解法二

    ```js
    var reverseStr = function (s, k) {
      const len = s.length;
      let resultArr = s.split("");
      for (let i = 0; i < len; i += 2 * k) {
        let l = i;
        let r = (i + k > len ? len : i + k) - 1;
        while (l < r) {
          [resultArr[l], resultArr[r]] = [resultArr[r], resultArr[l]];
          ++l;
          --r;
        }
      }
      return resultArr.join("");
    };
    ```

### 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
```
输入：s = "We are happy."
输出："We%20are%20happy."
```

1. 解法

    双指针。模拟的 C++ 语言中的可变长度字符串的实现原理，将其 O(n^2) 的空间复杂度降低到 O(1)。

    ```js
    var replaceSpace = function (s) {
      const arr = s.split("");
      let oldLen = s.length;

      // 空格数量
      let spaceCount = 0;
      for (let i = 0; i < oldLen; i++) {
        if (arr[i] === " ") spaceCount++;
      }

      arr.length += spaceCount * 2; // 1个空格转化为3个字母
      // 数组遍历，一定要从后往前遍历，避免从前往后，造成字符被修改，导致错误！
      for (let i = oldLen - 1, j = arr.length - 1; i >= 0; i--, j--) {
        if (arr[i] !== " ") arr[j] = arr[i];
        else {
          arr[j - 2] = "%";
          arr[j - 1] = "2";
          arr[j] = "0";
          j -= 2;
        }
      }
      return arr.join("");
    };
    ```

### 左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
```
输入: s = "abcdefg", k = 2
输出: "cdefgab"
```

示例 2：
```
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
```

1. 解法一

    三次翻转。

    ```js
    /**
     * @param {string} s
     * @param {number} n
     * @return {string}
     */
    var reverseLeftWords = function (s, n) {
      let strArr = s.split("");
      let length = strArr.length;

      // 全部翻转
      reverseWords(strArr);
      // 翻转回前面部分（0 ~ length-1-n）
      reverseWords(strArr, 0, length - n - 1);
      // 翻转回后面部分（length-n ~ 结尾）
      reverseWords(strArr, length - n);
      return strArr.join("");
    };

    // 翻转数组的 start到end 之间的项
    function reverseWords(strArr, start = 0, end = strArr.length - 1) {
      while (start < end) {
        [strArr[start], strArr[end]] = [strArr[end], strArr[start]];
        start++;
        end--;
      }
    }
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    直接截取。

    ```js
    var reverseLeftWords = function (s, n) {
      // 以及其他简单拼接法
      return s.slice(n) + s.slice(0, n);
    };
    ```
3. 解法三

    复制一遍截取。

    ```js
    var reverseLeftWords = function (s, n) {
      if (n >= s.length) {
        return s;
      }
      // 复制一遍字符串，再截取
      return (s + s).slice(n, n + s.length);
    };
    ```
</details>

### 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

s 只包含小写字母。

示例 1:

```
输入：s = "abaccdeff"
输出：'b'
```

示例 2:

```
输入：s = ""
输出：' '
```

1. 解法一

    哈希表保存所有字符出现次数。

    ```js
    /**
     * @param {string} s
     * @return {character}
     */
    var firstUniqChar = function (s) {
      const map = new Map();
      for (const str of s) {
        map.set(str, (map.get(str) ?? 0) + 1);
      }
      for (let val of map) {
        if (val[1] === 1) {
          return val[0];
        }
      }
      return " ";
    };
    ```
2. 解法二

    26个字母的数组保存所有字符出现次数。

    ```js
    var firstUniqChar = function (s) {
      const arr = new Array(26).fill(0);
      const unicodeA = "a".charCodeAt(0);

      for (let c of s) {
        arr[c.charCodeAt(0) - unicodeA] += 1;
      }

      for (let c of s) {
        if (arr[c.charCodeAt(0) - unicodeA] === 1) {
          return c;
        }
      }
      return " ";
    };
    ```
3. 解法三

    若`indexOf`与`lastIndexOf`相等，则说明是唯一。

    ```js
    var firstUniqChar = function (s) {
      const strArr = s.split("");
      return (
        strArr.find((str) => {
          return strArr.indexOf(str) === strArr.lastIndexOf(str);
        }) ?? " "
      );
    };
    ```

<details>
<summary>其他解法</summary>

4. 解法四

    正则查找。

    ```js
    var firstUniqChar = function (s) {
      for (let char of new Set(s)) {
        if (s.match(new RegExp(char, "g")).length === 1) {
          return char;
        }
      }
      return " ";
    };
    ```
</details>

### 反转字符串中的单词
给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。

**单词** 是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的 **单词** 分隔开。

返回 **单词** 顺序颠倒且 **单词** 之间用单个空格连接的结果字符串。

注意：输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

**进阶**：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 `O(1)` 额外空间复杂度的 **原地** 解法。

1. 解法

    先移除多余空格，再翻转整个字符串，再把单词翻转。

    ```js
    /**
     * @param {string} s
     * @return {string}
     */
    var reverseWords = function (s) {
      // 字符串转数组
      const strArr = Array.from(s);

      // 移除多余空格
      removeExtraSpaces(strArr);
      // 翻转整个字符串数组（此时单词被翻转了，需要之后再转回来）
      reverse(strArr, 0, strArr.length - 1);

      // 翻转每一个单词
      for (let i = 0, start = 0; i <= strArr.length; i++) {
        if (strArr[i] === " " || i === strArr.length) {
          // 翻转单词（i位置是空格 或 数组结尾+1）
          reverse(strArr, start, i - 1);
          start = i + 1;
        }
      }

      return strArr.join("");
    };

    // 删除多余空格
    function removeExtraSpaces(strArr) {
      let slowIndex = 0;
      let fastIndex = 0;

      while (fastIndex < strArr.length) {
        // 第1个单词前不能有空格 && 之后的单词前不能有2个空格
        if (
          strArr[fastIndex] === " " &&
          (fastIndex === 0 || strArr[fastIndex - 1] === " ")
        ) {
          fastIndex++;
        } else {
          strArr[slowIndex] = strArr[fastIndex];
          slowIndex++; // 注意最后需要判断是否最后一个是空格
          fastIndex++;
        }
      }

      // 移除末尾空格
      strArr.length = strArr[slowIndex - 1] === " " ? slowIndex - 1 : slowIndex;
    }

    // 翻转从 start 到 end 的数组
    function reverse(strArr, start, end) {
      while (start < end) {
        // 交换
        [strArr[start], strArr[end]] = [strArr[end], strArr[start]];
        start++;
        end--;
      }
    }
    ```

---
## 动态规划

### 斐波那契数
**斐波那契数** （通常用 `F(n)` 表示）形成的序列称为 **斐波那契数列** 。该数列由 **0** 和 **1** 开始，后面的每一项数字都是前面两项数字的和。也就是：

```
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
```

给定 `n` ，请计算 `F(n)` 。

答案需要取模 1e9+7(1000000007) ，如计算初始结果为：1000000008，请返回 1。

示例 1：

```
输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
```

示例 2：

```
输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
```

示例 3：

```
输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
```

提示：

- `0 <= n <= 100`

1. 解法一

    动态规划，记录。

    ```js
    /**
     * @param {number} n
     * @return {number}
     */
    var fib = function (n) {
      // dp[i]：斐波那契数列 结果
      const dp = Array.from({ length: n + 1 });
      dp[0] = 0;
      dp[1] = 1;

      const modulo = 1000000007;

      for (let i = 2; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % modulo;
      }

      return dp[n];
    };
    ```
2. 解法二

    动态规划，滚动、不记录。

    ```js
    var fib = function (n) {
      if (n < 2) { return n; }

      const modulo = 1000000007;
      let previous = 0;
      let current = 1;
      // 迭代：记录 前一个值 和 当前值
      for (let i = 2; i <= n; i++) {
        const temp = previous;
        previous = current;
        current = temp + current >= modulo ? temp + current - modulo : temp + current;
      }
      return current;
    };
    ```
3. 解法三

    递归。动态规划，记录。

    ```js
    var fib = function (n, cache = new Map()) {
      // 保存计算过的结果，避免递归时超时
      if (cache.has(n)) {
        return cache.get(n);
      }

      // 递归
      if (n < 2) {
        cache.set(n, n);
        return n;
      }

      const modulo = 1000000007;
      const result = (fib(n - 1, cache) + fib(n - 2, cache)) % modulo;
      cache.set(n, result);
      return result;
    };
    ```

### 爬楼梯
需要 `n` 阶你才能到达楼顶。每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

1. 解法

    设跳上 n 级台阶有 f(n) 种跳法。在所有跳法中，最后一步只有两种情况：跳上 1 级或 2 级台阶，即 f(n)=f(n−1)+f(n−2)。本题可转化为 求斐波那契数列第 n 项的值。

    略。与上一题（[斐波那契数](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#斐波那契数)）基本一致，改下初始值即可：初始值`1`、`2`。

### 三步问题
楼梯有n阶台阶，一次可以上1阶、2阶或3阶。计算上n阶有多少种走法。结果可能很大，你需要对结果模1000000007。

1. 解法一

    动态规划。

    ```js
    /**
     * @param {number} n
     * @return {number}
     */
    var waysToStep = function (n) {
      // dp[i]：登上第i阶的方式数量
      const dp = [];
      const modulo = 1000000007;

      dp[1] = 1;
      dp[2] = 2;
      dp[3] = 4;

      for (let i = 4; i <= n; i++) {
        // 转移方程（跳到倒一、跳到倒二、跳到倒三，注意剩下3台阶不能再加数量，否则会重复）
        // 任意2次相加取模都可
        dp[i] = (dp[i - 3] + ((dp[i - 2] + dp[i - 1]) % modulo)) % modulo;
      }
      return dp[n];
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    滚动数组（优化空间）。

    ```js
    var waysToStep = (n) => {
      if (n === 1) {
        return 1;
      }
      if (n === 2) {
        return 2;
      }
      if (n === 3) {
        return 4;
      }

      const modulo = 1000000007;

      let a = 4;
      let b = 2;
      let c = 1;
      for (let i = 3; i <= n; i++) {
        const temp_a = a;
        const temp_b = b;
        a = (a + ((b + c) % modulo)) % modulo;
        b = temp_a;
        c = temp_b;
      }
      return a;
    };
    ```
</details>

### 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为 $O(n)$ 。

示例1:

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

1. 解法

    动态规划。

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var maxSubArray = function (nums) {
      let result = nums[0];

      // 动态规划
      for (let i = 1, tempResult = nums[0]; i < nums.length; i++) {
        // tempResult：以元素nums[i]为结尾 的连续子数组最大和
        tempResult = nums[i] + Math.max(tempResult, 0);
        result = Math.max(result, tempResult);
      }
      return result;
    };
    ```

### 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

示例 2:

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

提示：

- `1 <= prices.length <= 10 ** 5`
- `0 <= prices[i] <= 10 ** 4`

1. 解法

    动态规划，滚动、不记录。

    ```js
    /**
     * @param {number[]} prices
     * @return {number}
     */
    var maxProfit = function (prices) {
      let result = 0;

      // 动态规划（滚动、不记录）
      let minPrice = prices[0] || 0; // 记录历史最低价格。或 = Number.MAX_VALUE;
      for (const price of prices) {
        minPrice = Math.min(minPrice, price); // 滚动更新的 历史最低价格
        result = Math.max(result, price - minPrice);
      }
      return result;
    };
    ```

### 鸡蛋掉落-两枚鸡蛋
给你**2 枚相同**的鸡蛋，和一栋从第`1`层到第`n`层共有`n`层楼的建筑。

已知存在楼层`f`，满足`0 <= f <= n`，任何从**高于**`f`的楼层落下的鸡蛋都**会碎** ，从`f`**楼层或比它低**的楼层落下的鸡蛋都**不会碎**。

每次操作，你可以取一枚**没有碎**的鸡蛋并把它从任一楼层`x`扔下（满足`1 <= x <= n`）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中**重复使用**这枚鸡蛋。

请你计算并返回要确定`f`**确切的值**的**最小操作次数**是多少？

示例 1：

```
输入：n = 2
输出：2
解释：我们可以将第一枚鸡蛋从 1 楼扔下，然后将第二枚从 2 楼扔下。
如果第一枚鸡蛋碎了，可知 f = 0；
如果第二枚鸡蛋碎了，但第一枚没碎，可知 f = 1；
否则，当两个鸡蛋都没碎时，可知 f = 2。
```

示例 2：

```
输入：n = 100
输出：14
解释：
一种最优的策略是：
- 将第一枚鸡蛋从 9 楼扔下。如果碎了，那么 f 在 0 和 8 之间。将第二枚从 1 楼扔下，然后每扔一次上一层楼，在 8 次内找到 f 。总操作次数 = 1 + 8 = 9 。
- 如果第一枚鸡蛋没有碎，那么再把第一枚鸡蛋从 22 层扔下。如果碎了，那么 f 在 9 和 21 之间。将第二枚鸡蛋从 10 楼扔下，然后每扔一次上一层楼，在 12 次内找到 f 。总操作次数 = 2 + 12 = 14 。
- 如果第一枚鸡蛋没有再次碎掉，则按照类似的方法从 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99 和 100 楼分别扔下第一枚鸡蛋。
不管结果如何，最多需要扔 14 次来确定 f 。
```

提示：

`1 <= n <= 1000`

1. 解法一

    数学规律。

    ```js
    // ①第一枚鸡蛋用于从低到高、间隔楼层直到破碎
    // ②第二枚鸡蛋用于在第一枚鸡蛋确认的最高不碎层到最低破碎层之间，由低到高逐层测试
    // ③为了稳定操作数，第一枚鸡蛋确定的间隔层 每测试成功一次都要递减1。
    //   假设第一次间隔层是f，那么第二次间隔层就是f-1，以此类推至最后一个间隔是1：
    //   f + f-1 + f-2 + ... + f-(f-1)=总楼层数n
    //   这样得到的f就是操作数的上限
    function twoEggDrop(n) {
      let f;
      // 找到第一个小于或等于 n 的等差求和的项数（第一项是1，公差是1）
      for (f = 1; sumOfArithmeticSequence(1, 1, f) < n; f++) {}
      return f;
    };

    // 等差数列的求和。a1：第1项；d：公差；n：项数
    function sumOfArithmeticSequence (a1, d, n) {
      const an = a1 + (n - 1) * d;
      return ((a1 + an) * n) / 2;
    }
    ```
2. 解法二

    动态规划。

    ```js
    function twoEggDrop(n, k = 2) {
      // 初始化：题解的数组[最大n层楼][最大k枚鸡蛋]
      let memo = new Array(n + 1).fill(0).map((i, n) => {
        return new Array(k + 1).fill(0).map((j, k) => {
          return k === 1 ? n : 0;
        });
      });
      return dp(n, k);

      // k枚，n层的题目解：表示现在有n层楼需要验证，此时你手里有k个鸡蛋，返回此时的最小操作次数
      function dp(n, k) {
        // base case
        if (n === 0) {
          return 0;
        }
        if (k === 1) {
          return n;
        }

        // 查表
        if (memo[n][k] !== 0) {
          return memo[n][k];
        }

        let res = Number.MAX_SAFE_INTEGER;
        // 选i层楼扔鸡蛋
        for (let i = 1; i <= n; i++) {
          // Math.max：寻找（第i层碎或不碎）最坏的情况
          // Math.min：在最坏的情况里，选出最小的操作次数
          res = Math.min(res, Math.max(dp(i - 1, k - 1), dp(n - i, k)) + 1);
        }

        // dp(n, k)需要的操作次数，是在所有楼层中选择 最坏情况下需要的操作次数最小的楼层 扔鸡蛋。所以需要遍历所有楼层，找到Math.min(res, Math.max(dp(i-1, k-1), dp(n-i, k)) + 1)
        memo[n][k] = res;
        return res;
      }
    }
    ```

### 最大子数组和
给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组** 是数组中的一个连续部分。

示例 1：

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

示例 2：

```
输入：nums = [1]
输出：1
```

示例 3：

```
输入：nums = [5,4,-1,7,8]
输出：23
```

提示：

- `1 <= nums.length <= 10 ** 5`
- `-(10 ** 4) <= nums[i] <= 10 ** 4`

**进阶**：如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。

1. 解法一

    O(n)，贪心。

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var maxSubArray = function (nums) {
      let result = Number.NEGATIVE_INFINITY;

      for (let i = 0, sum = 0; i < nums.length; i++) {
        // 若sum小于等于0，则不要之前的sum
        if (sum <= 0) {
          sum = nums[i];
        } else {
          sum = sum + nums[i];
        }

        result = Math.max(result, sum);
      }
      return result;
    };
    ```
2. 解法二

    O(n)，动态规划。

    ```js
    var maxSubArray = function (nums) {
      let result;

      // dp[i]：以nums[i]为结尾的最大连续子序列和为dp[i]。
      const dp = [];

      dp[0] = nums[0];
      for (let i = 1; i < nums.length; i++) {
        if (dp[i - 1] <= 0) {
          dp[i] = nums[i];
        } else {
          dp[i] = dp[i - 1] + nums[i];
        }

        result = Math.max(dp[i - 1], dp[i]);
      }
      return result;
    };
    ```

### 最长回文子串
给你一个字符串 `s`，找到 `s` 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：

```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

示例 2：

```
输入：s = "cbbd"
输出："bb"
```

提示：

- `1 <= s.length <= 1000`
- `s` 仅由数字和英文字母组成

1. 解法

    动态规划，一个回文去掉两头依然是回文：dp[i][j] = (s[i]===s[j]) && dp[i+1][j-1]（注意边界）。

    ```js
    /**
     * @param {string} s
     * @return {string}
     */
    var longestPalindrome = function (s) {
      const len = s.length;
      if (len < 2) { return s; }

      let maxLen = 1;
      let begin = 0;

      // 动态规划：dp[i][j] 表示 s[i..j] 是否是回文串。一个回文去掉两头依然是回文：dp[i][j] = (s[i]===s[j]) && dp[i+1][j-1]
      const dp = Array.from({ length: len }).map(() =>
        Array.from({ length: len }).fill(false),
      );

      // 初始化：所有长度为 1 的子串都是回文串（可省略）
      for (let i = 0; i < len; i++) {
        dp[i][i] = true;
      }

      // dp每个参考左下方的dp的值，因此从第2列开始 && 先 列 再 行
      for (let j = 1; j < len; j++) { // 行（字符串有边界）
        for (let i = 0; i < j; i++) { // 列（字符串左边界）
          // 头尾字符不等
          if (s[i] !== s[j]) {
            dp[i][j] = false;
          }
          // 头尾字符相等
          else {
            // 头尾去掉后：没有字符(j-i<i+1) || 仅剩1个字符（j-1===i+1）
            if (j - i <= 2) { // j-1-(i+1)<=0
              dp[i][j] = true;
            } else {
              dp[i][j] = dp[i + 1][j - 1];
            }
          }

          // 若是回文，则判断是否最长
          if (dp[i][j] && j - i + 1 > maxLen) {
            maxLen = j - i + 1;
            begin = i;
          }
        }
      }

      return s.slice(begin, begin + maxLen);
    };
    ```

---
## 哈希表

### 两个数组的交集
给定两个数组 `nums1` 和 `nums2` ，返回 *它们的交集* 。输出结果中的每个元素一定是 **唯一** 的。我们可以 **不考虑输出结果的顺序** 。

1. 解法

    哈希表，2次哈希。

    ```js
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number[]}
     */
    var intersection = function(nums1, nums2) {
      const nums1Map = new Map();
      for (const num of nums1) {
        nums1Map.set(num, true);
      }

      const nums2Map = new Map();
      for (const num of nums2) {
        nums2Map.set(num, nums1Map.get(num));
      }

      // 输出
      const result = [];
      for (const [key, value] of nums2Map) {
        if (value) {
          result.push(key);
        }
      }
      return result;
    };
    ```

### 查找共用字符
给你一个字符串数组 `words` ，请你找出所有在 `words` 的每个字符串中都出现的共用字符（ **包括重复字符**），并以数组形式返回。你可以按 **任意顺序** 返回答案。

提示：

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` 由小写英文字母组成

1. 解法

    哈希表，每个单词都进行哈希 并且 对比第一个单词的哈希，取少的数量。

    ```js
    /**
     * @param {string[]} words
     * @return {string[]}
     */
    var commonChars = function (words) {
      // 统计字符串中字符出现的次数，以第一个字符串
      const minCount = new Map();
      for (const str of words[0]) {
        minCount.set(str, (minCount.get(str) || 0) + 1);
      }

      // 从第二个单词开始
      for (let i = 1; i < words.length; i++) {
        // 统计 （从第二个单词开始）字符串中字符出现的次数
        const charCount = new Map();
        for (const str of words[i]) {
          charCount.set(str, (charCount.get(str) || 0) + 1);
        }

        // minCount重新写入 minCount、charCount 中少的数量
        for (const [key] of minCount) {
          minCount.set(
            key,
            Math.min(minCount.get(key) || 0, charCount.get(key) || 0),
          );
        }
      }

      // 输出
      const result = [];
      for (const [key, value] of minCount) {
        if (value > 0) {
          result.push(...key.repeat(value).split("")); // 包含重复字符
        }
      }
      return result;
    };
    ```

### 快乐数
**「快乐数」** 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
- 如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

示例 1：

```
输入：n = 19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

示例 2：

```
输入：n = 2
输出：false
```

提示：

- `1 <= n <= 2 ** 31 - 1`

1. 解法

    哈希表。

    ```js
    var isHappy = function (n) {
      const map = new Map();

      while (true) {
        // n出现过，证明已陷入无限循环
        if (map.has(n)) { return false; }

        if (n === 1) { return true; }

        map.set(n, true);
        n = getSum(n);
      }
    };

    // 取数值各个位上的单数之和
    const getSum = (num) => {
      let sum = 0;
      while (num !== 0) {
        sum += (num % 10) ** 2;
        num = Math.floor(num / 10);
      }
      return sum;
    };
    ```

### 两数之和
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

示例 2：

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

示例 3：

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

提示：

- `2 <= nums.length <= 10 ** 4`
- `-(10 ** 9) <= nums[i] <= 10 ** 9`
- `-(10 ** 9) <= target <= 10 ** 9`
- 只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？

1. 解法一

    哈希法（**当我们需要查询一个元素是否出现过，或者一个元素是否在集合里的时候，就要第一时间想到哈希法**），O(n)。

    ```js
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    var twoSum = function (nums, target) {
      // 利用Map类型：不重复键的键-值集合。键存nums项的value，值存nums项的key
      const hash = new Map();
      for (let i = 0; i < nums.length; i++) {
        const leftValue = target - nums[i];
        if (hash.get(leftValue) !== undefined) {
          return [i, hash.get(leftValue)];
        } else {
          hash.set(nums[i], i);
        }
      }
      return [];
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    暴力解法，O(n^2)。

    ```js
    var twoSum = function (nums, target) {
      for (let i = 0; i < nums.length; i++) {
        const left = target - nums[i];

        for (let j = i + 1; j < nums.length; j++) {
          if (nums[j] === left) {
            return [i, j];
          }
        }
      }
      return [];
    };
    ```
</details>

### 有效的字母异位词
1. 解法

    ```js
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    var isAnagram = function (s, t) {
      const arr1 = new Array(26).fill(0);
      const arr2 = new Array(26).fill(0);

      const unicodeA = "a".charCodeAt(0);

      for (let c of s) {
        arr1[c.charCodeAt(0) - unicodeA] += 1;
      }
      for (let c of t) {
        arr2[c.charCodeAt(0) - unicodeA] += 1;
      }

      return String(arr1) === String(arr2);
    };
    ```

### 找到字符串中所有字母异位词
给定两个字符串 `s` 和 `p`，找到 s 中所有 p 的 **异位词** 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**异位词** 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:

```
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```

 示例 2:

```
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```

提示:

- `1 <= s.length, p.length <= 3 * 10 ** 4`
- `s` 和 `p` 仅包含小写字母

1. 解法一

    滑动窗口。

    ```js
    /**
     * @param {string} s
     * @param {string} p
     * @return {number[]}
     */
    var findAnagrams = function (s, p) {
      const sLen = s.length;
      const pLen = p.length;

      // 特例：s长度小于p长度
      if (sLen < pLen) {
        return [];
      }

      const result = [];

      // 在字符串 s 中构造一个长度为与字符串 p 的长度相同的滑动窗口，并在滑动中维护窗口中每种字母的数量；当窗口中每种字母的数量与字符串 p 中每种字母的数量相同时，则说明当前窗口为字符串 p 的异位词。
      const sCount = new Array(26).fill(0);
      // 对比用
      const pCount = new Array(26).fill(0);
      for (let i = 0; i < pLen; ++i) {
        ++sCount[s[i].charCodeAt() - "a".charCodeAt()];
        ++pCount[p[i].charCodeAt() - "a".charCodeAt()];
      }

      if (sCount.toString() === pCount.toString()) {
        result.push(0);
      }

      // 滑动窗口，滑动 sLen - pLen 次
      for (let i = 0; i < sLen - pLen; ++i) {
        // 滑动：去除前一个字符，就要在pLen后面加一个字符
        --sCount[s[i].charCodeAt() - "a".charCodeAt()];
        ++sCount[s[i + pLen].charCodeAt() - "a".charCodeAt()];

        if (sCount.toString() === pCount.toString()) {
          result.push(i + 1);
        }
      }

      return result;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    滑动窗口（不再维护每种字母的数量，而维护每种字母数量的差），逻辑较复杂。

    ```js
    var findAnagrams = function (s, p) {
      const sLen = s.length;
      const pLen = p.length;

      // 特例：s长度小于p长度
      if (sLen < pLen) {
        return [];
      }

      const result = [];

      // count[i]：i序号字母在s和p的相差数量。0：数量相同；正数：s多出现次数；负数：s少出现次数
      const count = Array(26).fill(0);
      for (let i = 0; i < pLen; ++i) {
        ++count[s[i].charCodeAt() - "a".charCodeAt()];
        --count[p[i].charCodeAt() - "a".charCodeAt()];
      }

      // 字母不同数量（值：0~26），若count[i]为0则i序号字母相同，否则不同
      let differ = 0;
      for (let j = 0; j < 26; ++j) {
        if (count[j] !== 0) {
          ++differ;
        }
      }

      if (differ === 0) {
        result.push(0);
      }

      // 滑动窗口，滑动 sLen - pLen 次
      for (let i = 0; i < sLen - pLen; ++i) {
        // 去除前一个字符
        // 若原来多1个，则去掉就数量相同，differ减少1
        if (count[s[i].charCodeAt() - "a".charCodeAt()] === 1) {
          --differ;
        }
        // 若原来数量相同，则去掉就少1个，differ增加1
        else if (count[s[i].charCodeAt() - "a".charCodeAt()] === 0) {
          ++differ;
        } // 其他差距值不会影响differ
        --count[s[i].charCodeAt() - "a".charCodeAt()];

        // 增加pLen后一个字符
        // 若原来少1个，则增加就数量相同，differ减少1
        if (count[s[i + pLen].charCodeAt() - "a".charCodeAt()] === -1) {
          --differ;
        }
        // 若原来数量相同，则增加就多1个，differ增加1
        else if (count[s[i + pLen].charCodeAt() - "a".charCodeAt()] === 0) {
          ++differ;
        } // 其他差距值不会影响differ
        ++count[s[i + pLen].charCodeAt() - "a".charCodeAt()];

        if (differ === 0) {
          result.push(i + 1);
        }
      }

      return result;
    };
    ```
</details>

### 字母异位词分组
给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

**字母异位词** 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:

```
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

示例 2:

```
输入: strs = [""]
输出: [[""]]
```

示例 3:

```
输入: strs = ["a"]
输出: [["a"]]
```

提示：

- `1 <= strs.length <= 10 ** 4`
- `0 <= strs[i].length <= 100`
- `strs[i] 仅包含小写字母`

1. 解法一

    先排序，再哈希表。

    ```js
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    var groupAnagrams = function (strs) {
      // 以排序过的每个项字符串为key，以原数组每个字符串的值为value
      const hash = new Map();

      const newStrs = strs.map((str) => {
        return str.split("").sort().join("");
      });

      for (let i = 0; i < newStrs.length; i++) {
        if (hash.has(newStrs[i])) {
          hash.get(newStrs[i]).push(strs[i]);
        } else {
          hash.set(newStrs[i], [strs[i]]);
        }
      }

      return [...hash.values()];
    };
    ```
2. 解法二

    先单词的字母计数，再哈希表。

    ```js
    var groupAnagrams = function (strs) {
      // 每个key都是按照单词所占的26个字母数量，如：'abda'的key为'2:1:0:1:...'
      const hash = new Map();

      for (let i = 0; i < strs.length; i++) {
        // 把单词转变成按顺序的26个字母数量的字符串
        const letterArr = Array.from({ length: 26 }).fill(0);
        for (let j of strs[i]) {
          letterArr[j.charCodeAt() - "a".charCodeAt()] += 1;
        }
        const key = letterArr.join(":");

        if (hash.get(key)) {
          hash.get(key).push(strs[i]);
        } else {
          hash.set(key, [strs[i]]);
        }
      }

      return [...hash.values()];
    };
    ```

### 三数之和
给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请

你返回所有和为 `0` 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

示例 2：

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

示例 3：

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```

提示：

- `3 <= nums.length <= 3000`
- `-(10 ** 5) <= nums[i] <= 10 ** 5`

1. 解法

    双指针，O(n^2)。关键在去除重复答案。

    ```js
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    function threeSum(nums) {
      const result = [];

      // 先排序，因为去重和算法逻辑需要
      nums.sort((a, b) => a - b);

      for (let left = 0; left < nums.length; left++) {
        if (nums[left] > 0) {
          return result; // nums经过排序后，只要nums[left]>0, 此后的nums[left] + nums[middle] + nums[right]均大于0,可以提前终止循环。
        }
        // 去重
        if (left > 0 && nums[left] === nums[left - 1]) {
          continue;
        }
        let middle = left + 1;
        let right = nums.length - 1;
        while (middle < right) {
          let total = nums[left] + nums[middle] + nums[right];
          if (total === 0) {
            result.push([nums[left], nums[middle], nums[right]]);

            // 去重需要，所以2个指针同时移动
            middle++;
            right--;

            // 去重需要
            while (nums[right] === nums[right + 1]) {
              right--;
            }
            // 去重需要
            while (nums[middle] === nums[middle - 1]) {
              middle++;
            }
          } else if (total < 0) {
            middle++;
          } else {
            right--;
          }
        }
      }
      return result;
    }
    ```

### 四数之和
给你一个由 `n` 个整数组成的数组 `nums` ，和一个目标值 `target` 。请你找出并返回满足下述全部条件且**不重复**的四元组 `[nums[a], nums[b], nums[c], nums[d]]` （若两个四元组元素一一对应，则认为两个四元组重复）。

1. 解法

    双指针，O(n^3)。关键在去除重复答案。

    ```js
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[][]}
     */
    var fourSum = function (nums, target) {
      const len = nums.length;
      if (len < 4) { return []; }

      const result = [];

      // 先排序，因为去重和算法逻辑需要
      nums.sort((a, b) => a - b);
      for (let i = 0; i < len - 3; i++) {
        // 去重i
        if (i > 0 && nums[i] === nums[i - 1]) { continue; }

        for (let j = i + 1; j < len - 2; j++) {
          // 去重j
          if (j > i + 1 && nums[j] === nums[j - 1]) { continue; }

          let l = j + 1;
          let r = len - 1;
          while (l < r) {
            const sum = nums[i] + nums[j] + nums[l] + nums[r];

            if (sum < target) {
              l++;
              continue;
            }
            if (sum > target) {
              r--;
              continue;
            }

            result.push([nums[i], nums[j], nums[l], nums[r]]);
            // 对nums[l]和nums[r]去重
            while (l < r && nums[l] === nums[l + 1]) { l++; }
            while (l < r && nums[r] === nums[r - 1]) { r--; }
            // 找到答案时，双指针同时收缩
            l++;
            r--;
          }
        }
      }
      return result;
    };
    ```

### 四数相加 II
给你四个整数数组 `nums1`、`nums2`、`nums3` 和 `nums4` ，数组长度都是 `n` ，请你计算有多少个元组 `(i, j, k, l)` 能满足：

- `0 <= i, j, k, l < n`
- `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

提示：

- `-(2 ** 28) <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2 ** 28`

1. 解法

    哈希表，1次针对2个数的写哈希，1次针对另外2个数的找哈希。

    ```js
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @param {number[]} nums3
     * @param {number[]} nums4
     * @return {number}
     */
    var fourSumCount = function (nums1, nums2, nums3, nums4) {
      let result = 0;

      const twoSumMap = new Map();
      // nums1+nums2的值和次数，存在map
      for (const n1 of nums1) {
        for (const n2 of nums2) {
          const sum = n1 + n2;
          twoSumMap.set(sum, (twoSumMap.get(sum) || 0) + 1);
        }
      }

      // 找到出现 0-(nums3+nums4) 在map中出现的次数
      for (const n3 of nums3) {
        for (const n4 of nums4) {
          const sum = n3 + n4;
          result += twoSumMap.get(0 - sum) || 0;
        }
      }

      return result;
    };
    ```

### 最长连续序列
给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

示例 2：

```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

提示：

- `0 <= nums.length <= 10 ** 5`
- `-(10 ** 9) <= nums[i] <= 10 ** 9`

1. 解法一

    哈希表，仅遍历一次，哈希表key代表数字、value代表该key数字连续长度。

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var longestConsecutive = function (nums) {
      let result = 0;

      // 把连续次数存放在哈希表（key：数字；value：连续长度）
      const hash = new Map();

      for (const num of nums) {
        if (!hash.has(num)) {    // 相同数字仅处理一次
          // 前后一个数字是否有值
          const left = hash.get(num - 1) || 0;
          const right = hash.get(num + 1) || 0;

          const currentLen = 1 + left + right;
          result = Math.max(currentLen, result);

          hash.set(num, currentLen);
          // 同步更新2端边界
          hash.set(num - left, currentLen);
          hash.set(num + right, currentLen);
        }
      }

      return result;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    哈希表，为了达到 O(n)，仅对最小的数字进行累加计数操作。

    ```js
    var longestConsecutive = function (nums) {
      // 去除相同的项
      const set = new Set(nums);

      let result = 0;

      for (const i of set) {
        // 为了保证 O(n) 所以只处理连续数字中最小的
        if (!set.has(i - 1)) {
          let currentLen = 1;
          let currentNum = i;
          while (set.has(currentNum + 1)) {
            currentLen += 1;
            currentNum += 1;
          }
          result = Math.max(result, currentLen);
        }
      }

      return result;
    };
    ```
</details>

---
## 栈与队列

### 用栈实现队列
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（`push`、`pop`、`peek`、`empty`）：

实现 `MyQueue` 类：

- `void push(int x)` 将元素 x 推到队列的末尾
- `int pop()` 从队列的开头移除并返回元素
- `int peek()` 返回队列开头的元素
- `boolean empty()` 如果队列为空，返回 `true` ；否则，返回 `false`

说明：

- 你 **只能** 使用标准的栈操作 —— 也就是只有 `push to top`, `peek/pop from top`, `size`, 和 `is empty` 操作是合法的。
- 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

示例 1：

```
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

提示：

- `1 <= x <= 9`
- 最多调用 `100` 次 `push`、`pop`、`peek` 和 `empty`
- 假设所有操作都是有效的 （例如，一个空的队列不会调用 `pop` 或者 `peek` 操作）

**进阶**：

- 你能否实现每个操作均摊时间复杂度为 `O(1)` 的队列？换句话说，执行 `n` 个操作的总时间复杂度为 `O(n)` ，即使其中一个操作可能花费较长时间。

1. 解法

    **所有`用2个栈实现1个队列`的方法：2个栈，一个栈出 -> 一个栈入 所有数据之后，就能够把原顺序颠倒。**

    ```ts
    // 模拟栈，意味着只能 unshift shift 的数组（或只能 push pop）
    // 实现队列，因此要实现类似数组的 unshift pop（或 push shift）
    class MyQueue {
      // 存放插入的数据（栈入）
      inStack = [];
      // 处理移出的数据。
      // 当为空时，inStack栈出->outStack栈入 所有数据（2个栈，一个栈出一个栈入就能够把原顺序颠倒）
      outStack = [];

      push(x: number): void {
        this.inStack.unshift(x);
      }

      pop(): number {
        // 若outStack为空，则把inStack栈出给outStack栈入，这样原顺序颠倒
        if (this.outStack.length === 0) {
          while (this.inStack.length) {
            this.outStack.unshift(this.inStack.shift());
          }
        }
        return this.outStack.shift();
      }

      peek(): number {
        if (this.outStack.length === 0) {
          while (this.inStack.length) {
            this.outStack.unshift(this.inStack.shift());
          }
        }
        return this.outStack[0];
      }

      empty(): boolean {
        return this.inStack.length === 0 && this.outStack.length === 0;
      }

      size(): number {
        return this.inStack.length + this.outStack.length;
      }
    }
    ```

### 用队列实现栈
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（`push`、`top`、`pop` 和 `empty`）。

实现 `MyStack` 类：

- `void push(int x)` 将元素 x 压入栈顶。
- `int pop()` 移除并返回栈顶元素。
- `int top()` 返回栈顶元素。
- `boolean empty()` 如果栈是空的，返回 `true` ；否则，返回 `false` 。

注意：

- 你只能使用队列的基本操作 —— 也就是 `push to back`、`peek/pop from front`、`size` 和 `is empty` 这些操作。
- 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

示例：

```
输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
```

提示：

- `1 <= x <= 9`
- 最多调用`100` 次 `push`、`pop`、`top` 和 `empty`
- 每次调用 `pop` 和 `top` 都保证栈不为空

**进阶**：你能否仅用一个队列来实现栈。

1. 解法一

    **所有`用1个队列实现1个栈`的方法：正常压入，移除时执行 长度-1的 移除-压入，最后一个就是移除结果（或反过来：压入时处理，移除时正常移除）。**

    ```ts
    // 模拟队列，意味着只能 unshift pop 的数组（或只能 push shift）
    // 实现栈，因此要实现类似数组的 unshift shift（或 push pop）
    class MyStack {
      // 存放插入的数据（队列入）
      queue = [];

      push(x: number): void {
        this.queue.unshift(x);
      }

      pop(): number {
        // 队列重新插入，剩下最后一个就是要移除的（或插入的时候处理，移除的时候就不用处理）
        for (let i = 0; i < this.queue.length - 1; i++) {
          this.queue.unshift(this.queue.pop());
        }
        return this.queue.pop();
      }

      top(): number {
        return this.queue[0];
      }

      empty(): boolean {
        return this.queue.length === 0;
      }

      size(): number {
        return this.queue.length;
      }
    }
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    用2个队列的话，只是把原本1个队列自己移除-自己压入，变成有一个辅助队列帮助，逻辑不变。不推荐。

    ```js
    let MyStack = function () {
      this.queue = [];
      // 仅辅助作用，暂时保存queue数据
      this._queue = [];
    };

    MyStack.prototype.push = function (x) {
      this.queue.push(x);
    };

    MyStack.prototype.pop = function () {
      while (this.queue.length > 1) {
        this._queue.push(this.queue.shift());
      }
      let result = this.queue.shift();

      while (this._queue.length) {
        this.queue.push(this._queue.shift());
      }
      return result;
    };

    MyStack.prototype.top = function () {
      return this.queue[this.queue.length - 1];
    };

    MyStack.prototype.empty = function () {
      return this.queue.length === 0;
    };
    ```
</details>

### 有效的括号
给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例 1：

```
输入：s = "()"
输出：true
```

示例 2：

```
输入：s = "()[]{}"
输出：true
```

示例 3：

```
输入：s = "(]"
输出：false
```

提示：

- `1 <= s.length <= 10 ** 4`
- `s` 仅由括号 `'()[]{}'` 组成

1. 解法

    栈（有先进后出就用栈）。

    ```js
    /**
     * @param {string} s
     * @return {boolean}
     */
    var isValid = function (s) {
      // 优化点性能
      if (s.length % 2 === 1) { return false; }

      // 字符串是左括号就入栈，字符串是右括号则出栈对比
      const stack = [];

      for (const str of s) {
        if (str === "(" || str === "[" || str === "{") {
          stack.push(str);
        }
        // 默认只输入6种字符，所以这里不再判断
        else {
          const pop = stack.pop();

          if (
            (str === ")" && pop === "(") ||
            (str === "]" && pop === "[") ||
            (str === "}" && pop === "{")
          ) {
            // ok
          } else {
            return false;
          }
        }
      }

      if (stack.length > 0) {
        return false;
      }
      return true;
    };
    ```

### 删除字符串中的所有相邻重复项
给出由小写字母组成的字符串 `S`，**重复项删除操作**会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

1. 解法

    ```js
    var removeDuplicates = function (s) {
      const result = [];

      for (const i of s) {
        // 将要推入的 === 栈中最后一个相等
        if (i === result[result.length - 1]) {
          result.pop();
        } else {
          result.push(i);
        }
      }
      return result.join("");
    };
    ```

### 最小栈
请你设计一个 **最小栈** 。它提供 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素val推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

示例 1:

```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[2],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,2,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(2);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 2.
minStack.getMin();   --> 返回 -2.
```

提示：

- `-(2 ** 31) <= val <= 2 ** 31 - 1`
- `pop`、`top` 和 `getMin` 操作总是在 非空栈 上调用
- `push`、`pop`、`top` 和 `getMin` 最多被调用 `3 * 10 ** 4` 次

1. 解法一

    ```ts
    class MinStack {
      // 存放栈数据
      list = [];
      // 存放最小数
      minList = [];

      push(val: number): void {
        this.list.unshift(val);

        // 若插入的值没有比之前最小值更小或相等，就不插入minList
        if (this.minList.length === 0 || val <= this.minList[0]) {
          this.minList.unshift(val);
        }
      }

      pop(): void {
        if (this.list.length > 0) {
          const value = this.list.shift();

          if (value === this.minList[0]) {
            this.minList.shift();
          }
          return;
        }

        throw Error("栈内为空");
      }

      top(): number {
        if (this.list.length > 0) {
          return this.list[0];
        }

        throw Error("栈内为空");
      }

      getMin(): number {
        if (this.minList.length > 0) {
          return this.minList[0];
        }

        throw Error("栈内为空");
      }
    }
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    保持2个数组相同长度，但插入minList的不一定最后插入的值 而必须是和之前最小值对比更小的值。

    ```js
    var MinStack = function () {
      // 存放栈数据
      this.list = [];
      // 存放最小数
      this.minList = [];
    };

    MinStack.prototype.push = function (x) {
      this.list.unshift(x);

      if (this.minList.length === 0) {
        this.minList.unshift(x);
      } else {
        // 保持2个数组都相同长度，但是插入minList的永远都是最小值（因此可能插入的不是x而是上一个最小值）
        this.minList.unshift(Math.min(x, this.minList[0]));
      }
    };

    MinStack.prototype.pop = function () {
      if (this.list.length > 0) {
        this.list.shift();
        this.minList.shift();
        return;
      }

      throw Error("栈内为空");
    };

    MinStack.prototype.top = function () {
      if (this.list.length > 0) {
        return this.list[0];
      }

      throw Error("栈内为空");
    };

    MinStack.prototype.getMin = function () {
      if (this.minList.length > 0) {
        return this.minList[0];
      }

      throw Error("栈内为空");
    };
    ```
</details>

### 逆波兰表达式求值
给你一个字符串数组 `tokens` ，表示一个根据 **逆波兰表示法** 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

注意：

- 有效的算符为 `+`、`-`、`*` 和 `/` 。
- 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
- 两个整数之间的除法总是 **向零截断** 。
- 表达式中不含除零运算。
- 输入是一个根据逆波兰表示法表示的算术表达式。
- 答案及所有中间计算结果可以用 **32 位** 整数表示。

1. 解法

    ```js
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    var evalRPN = function (tokens) {
      const stack = [];
      for (const token of tokens) {
        // 非数字
        if (isNaN(Number(token))) {
          // 出栈两个数字
          const n2 = stack.pop();
          const n1 = stack.pop();

          // 判断运算符类型，算出新数入栈
          switch (token) {
            case "+":
              stack.push(n1 + n2);
              break;
            case "-":
              stack.push(n1 - n2);
              break;
            case "*":
              stack.push(n1 * n2);
              break;
            case "/":
              const num = n1 / n2;
              stack.push(num < 0 ? Math.ceil(num) : Math.floor(num)); // 向零截断
              break;
          }
        }
        // 数字
        else {
          stack.push(Number(token));
        }
      }

      return stack[0];
    };
    ```

### 前 K 个高频元素
给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

1. 解法一

    利用sort。

    ```js
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    function topKFrequent(nums, k) {
      const countMap = new Map();
      for (let num of nums) {
        countMap.set(num, (countMap.get(num) || 0) + 1);
      }

      // 利用sort
      return [...countMap.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, k)
        .map((i) => i[0]);
    }
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    堆。没有认真看

    ```js
    // js 没有堆 需要自己构造
    class Heap {
      constructor(compareFn) {
        this.compareFn = compareFn;
        this.queue = [];
      }

      // 添加
      push(item) {
        // 推入元素
        this.queue.push(item);

        // 上浮
        let index = this.size() - 1; // 记录推入元素下标
        let parent = Math.floor((index - 1) / 2); // 记录父节点下标

        while (parent >= 0 && this.compare(parent, index) > 0) {
          // 注意compare参数顺序
          [this.queue[index], this.queue[parent]] = [
            this.queue[parent],
            this.queue[index],
          ];

          // 更新下标
          index = parent;
          parent = Math.floor((index - 1) / 2);
        }
      }

      // 获取堆顶元素并移除
      pop() {
        // 堆顶元素
        const out = this.queue[0];

        // 移除堆顶元素 填入最后一个元素
        this.queue[0] = this.queue.pop();

        // 下沉
        let index = 0; // 记录下沉元素下标
        let left = 1; // left 是左子节点下标 left + 1 则是右子节点下标
        let searchChild = this.compare(left, left + 1) > 0 ? left + 1 : left;

        while (searchChild !== undefined && this.compare(index, searchChild) > 0) {
          // 注意compare参数顺序
          [this.queue[index], this.queue[searchChild]] = [
            this.queue[searchChild],
            this.queue[index],
          ];

          // 更新下标
          index = searchChild;
          left = 2 * index + 1;
          searchChild = this.compare(left, left + 1) > 0 ? left + 1 : left;
        }

        return out;
      }

      size() {
        return this.queue.length;
      }

      // 使用传入的 compareFn 比较两个位置的元素
      compare(index1, index2) {
        // 处理下标越界问题
        if (this.queue[index1] === undefined) return 1;
        if (this.queue[index2] === undefined) return -1;

        return this.compareFn(this.queue[index1], this.queue[index2]);
      }
    }

    const topKFrequent = function (nums, k) {
      const map = new Map();

      for (const num of nums) {
        map.set(num, (map.get(num) || 0) + 1);
      }

      // 创建小顶堆
      const heap = new Heap((a, b) => a[1] - b[1]);

      // entry 是一个长度为2的数组，0位置存储key，1位置存储value
      for (const entry of map.entries()) {
        heap.push(entry);

        if (heap.size() > k) {
          heap.pop();
        }
      }

      // 或 return heap.queue.map(e => e[0]);

      const res = [];

      for (let i = heap.size() - 1; i >= 0; i--) {
        res[i] = heap.pop()[0];
      }

      return res;
    };
    ```
</details>

### 每日温度
给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来替代。

示例 1:

```
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
```

示例 2:

```
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
```

示例 3:

```
输入: temperatures = [30,60,90]
输出: [1,1,0]
```

提示：

- `1 <= temperatures.length <= 10 ** 5`
- `30 <= temperatures[i] <= 100`

1. 解法

    **通常是一维数组，要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置，此时我们就要想到可以用单调栈。** O(n)。

    ```js
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    var dailyTemperatures = function (temperatures) {
      // 单调栈（栈头至栈底 递增，但存储的是下标）
      const stack = [];

      const answer = new Array(temperatures.length).fill(0);

      for (let i = 0; i < temperatures.length; i++) {
        // 第一个元素 || i项 小于等于 栈顶元素
        if (
          stack.length === 0 ||
          temperatures[i] <= temperatures[stack[stack.length - 1]]
        ) {
          // i项如栈
          stack.push(i);
        } else {
          // 栈不空 && i项 大于 栈顶元素
          while (
            stack.length > 0 &&
            temperatures[i] > temperatures[stack[stack.length - 1]]
          ) {
            // 栈顶元素存储的下标 找到了第一个大于自己的值，得到它的解答、出栈
            answer[stack[stack.length - 1]] = i - stack[stack.length - 1];
            stack.pop();
          }

          // 没有比 i项 小的 栈元素，i项入栈
          stack.push(i);
        }
      }
      return answer;
    };
    ```

### 滑动窗口最大值
给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 *滑动窗口中的最大值* 。

示例 1：

```
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

示例 2：

```
输入：nums = [1], k = 1
输出：[1]
```

提示：

- `1 <= nums.length <= 10 ** 5`
- `-(10 ** 4) <= nums[i] <= 10 ** 4`
- `1 <= k <= nums.length`

1. 解法

    借助单调队列。

    ![借助单调递减队列](./images/239.gif)

    ```js
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    var maxSlidingWindow = function (nums, k) {
      const helperQueue = new MonoQueue();
      let i = 0;
      let j = 0;
      let resArr = [];

      // 补齐第一次窗口k数量的单调队列（递减）
      while (j < k) {
        helperQueue.enqueue(nums[j++]);
      }
      resArr.push(helperQueue.top());

      // 滑动窗口
      for (; j < nums.length; i++, j++) {
        helperQueue.enqueue(nums[j]);
        helperQueue.dequeue(nums[i]);
        resArr.push(helperQueue.top());
      }
      return resArr;
    };

    /** 单调队列（递减，从大到小：[大,中,小]） */
    class MonoQueue {
      queue = [];

      // 入队：value如果大于队尾元素，则将队尾元素删除，直至队尾元素大于value，或队列为空
      enqueue(value) {
        let back = this.queue[this.queue.length - 1];
        while (back !== undefined && back < value) {
          this.queue.pop();
          back = this.queue[this.queue.length - 1];
        }
        this.queue.push(value);
      }

      // 出队：只有当队头元素等于value，才出队
      dequeue(value) {
        let top = this.top();
        if (top !== undefined && top === value) {
          this.queue.shift();
        }
      }

      // 队头元素，也就是最大的值
      top() {
        return this.queue[0];
      }
    }
    ```

---
## 回溯

- 回溯算法的模板框架：

    ```js
    function backtracking(参数) {
        if (终止条件) {
            存放结果;
            return;
        }

        for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
            处理节点;
            backtracking(路径，选择列表); // 递归
            回溯，撤销处理结果
        }
    }
    ```

### 组合
给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

你可以按 **任何顺序** 返回答案。

1. 解法

    回溯。时间复杂度: O(n * 2^n)。

    ```js
    /**
     * @param {number} n
     * @param {number} k
     * @return {number[][]}
     */
    var combine = function (n, k) {
      const result = [];
      const path = [];

      const helper = (index) => {
        if (path.length === k) {
          result.push([...path]);
          return;
        }

        for (let i = index; i <= n - (k - path.length) + 1; i++) {
          path.push(i);
          helper(i + 1); // 递归
          path.pop(); // 回溯
        }
      };

      helper(1); // 题目要求[1, n]所以传1。若要求[0, n]则传0

      return result;
    };
    ```

### 组合总和 III
找出所有相加之和为 `n` 的 `k` 个数的组合，且满足下列条件：

- 只使用数字1到9
- 每个数字 **最多使用一次**

返回 *所有可能的有效组合的列表* 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

1. 解法

    回溯。时间复杂度: O(n * 2^n)。

    ```js
    /**
     * @param {number} k
     * @param {number} target
     * @return {number[][]}
     */
    var combinationSum3 = function (k, target) {
      const result = [];
      const path = [];
      let sum = 0;

      const helper = (index) => {
        // 剪枝操作
        if (sum > target) { return; }

        if (path.length === k) {
          if (sum === target) {
            result.push([ ...path ]);
          }
          return;
        }

        for (let i = index; i <= 9 - (k - path.length) + 1; i++) {
          path.push(i);
          sum += i;
          index += 1;
          helper(index);  // 递归
          sum -= i; // 回溯
          path.pop(); // 回溯
        }
      };

      helper(1);

      return result;
    };
    ```

### 电话号码的字母组合
给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![phone.png](./images/phone.png)

提示：

- `digits[i]` 是范围 `['2', '9']` 的一个数字。

1. 解法

    回溯。

    ```js
    /**
     * @param {string} digits
     * @return {string[]}
     */
    var letterCombinations = function (digits) {
      const length = digits.length;
      const map = [
        "", // 0
        "", // 1
        "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
      ];

      if (!length) { return []; }
      if (length === 1) { return map[digits].split(""); }

      const result = [];
      const path = [];

      function helper(index) {
        if (path.length === length) {
          result.push(path.join(""));
          return;
        }

        for (const char of map[digits[index]]) {
          path.push(char);
          helper(index + 1);    // 递归
          path.pop();   // 回溯
        }
      }

      helper(0);

      return result;
    };
    ```

### 组合总和
给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有 **不同组合** ，并以列表形式返回。你可以按 **任意顺序** 返回这些组合。

`candidates` 中的 **同一个** 数字可以 **无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。

提示：

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- `candidates` 的所有元素 **互不相同**
- `1 <= target <= 40`

1. 解法

    回溯。

    ```js
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    var combinationSum = function (candidates, target) {
      const result = [];
      const path = [];
      let sum = 0;

      candidates.sort((a, b) => a - b); // 排序

      function helper(index) {
        if (sum === target) {
          result.push([...path]);
          return;
        }

        for (let i = index; i < candidates.length; i++) {
          const num = candidates[i];
          if (num > target - sum) { break; }

          path.push(num);
          sum += num;
          helper(i); // 递归
          path.pop(); // 回溯
          sum -= num; // 回溯
        }
      }

      helper(0);

      return result;
    };
    ```

### 组合总和 II
给定一个候选人编号的集合 `candidates` 和一个目标数 `target` ，找出 `candidates` 中所有可以使数字和为 `target` 的组合。

`candidates` 中的每个数字在每个组合中只能使用 **一次** 。

注意：解集不能包含重复的组合。

1. 解法

    递归。

    ```js
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    var combinationSum2 = function (candidates, target) {
      const result = [];
      const path = [];
      let sum = 0;

      candidates.sort((a, b) => a - b); // 排序

      function backtracking(index) {
        if (sum === target) {
          result.push([...path]);
          return;
        }

        for (let i = index; i < candidates.length; i++) {
          const num = candidates[i];

          // 若当前元素和前一个元素相等，则本次循环结束，防止出现重复组合（注意，这里不是递归进来的，这里表示同一层树枝，比较绕）
          if (i > index && candidates[i] === candidates[i - 1]) { continue; }

          // 当前元素值 > 目标值-总和
          if (num > target - sum) { break; }

          path.push(num);
          sum += num;
          backtracking(i + 1); // 递归
          path.pop(); // 回溯
          sum -= num; // 回溯
        }
      }

      backtracking(0);

      return result;
    };
    ```

---
## 岛屿相关

### 岛屿数量
给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：

```
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
```

示例 2：

```
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
```

提示：

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` 的值为 `'0'` 或 `'1'`

1. 解法

    深度优先遍历，为了避免重复遍历，需要把相连的陆地（整个岛屿）全淹了。

    ```js
    /**
     * @param {String[][]} grid
     * @return {number}
     */
    var numIslands = function (grid) {
      let result = 0;
      const m = grid.length;
      const n = grid[0].length;
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          // 发现岛屿
          if (grid[i][j] === "1") {
            result++;

            // 使用 DFS 把相连的陆地（整个岛屿）全淹了
            dfs(grid, i, j);
          }
        }
      }
      return result;
    };

    // 从 (i, j) 开始，把自己和相邻的陆地都变成海水
    const dfs = function (grid, i, j) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) {    // 超出索引边界
        return;
      }
      if (grid[i][j] === "0") {    // 已经是海水了（不能再查找陆地）
        return;
      }

      // 将 (i, j) 变成海水（或设置成其他标记，那上面的判断也要加上）
      grid[i][j] = "0";

      // 淹没上下左右的陆地
      dfs(grid, i - 1, j);
      dfs(grid, i + 1, j);
      dfs(grid, i, j - 1);
      dfs(grid, i, j + 1);
    };
    ```

### 统计封闭岛屿的数目
二维矩阵 `grid` 由 `0` （土地）和 `1` （水）组成。岛是由最大的4个方向连通的 `0` 组成的群，封闭岛是一个 `完全` 由1包围（左、上、右、下）的岛。

请返回 *封闭岛屿* 的数目。

示例 1：

![sample_3_1610.png](./images/sample_3_1610.png)

```
输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
```

示例 2：

![sample_4_1610.png](./images/sample_4_1610.png)

```
输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
```

示例 3：

```
输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2
```

提示：

- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <=1`

1. 解法一

    深度优先遍历把 上下左右边 的岛屿先排除掉（先全淹了），剩下的就是封闭岛屿（与[岛屿数量](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#岛屿数量)类似：深度优先遍历，为了避免重复遍历，需要把相连的陆地（整个岛屿）全淹了）。

    ```js
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    var closedIsland = function (grid) {
      let result = 0;
      const m = grid.length;
      const n = grid[0].length;

      // 把 上下 的岛屿淹没
      for (let j = 0; j < n; j++) {
        dfs(grid, 0, j);
        dfs(grid, m - 1, j);
      }
      // 把 左右 的岛屿淹没
      for (let i = 0; i < m; i++) {
        dfs(grid, i, 0);
        dfs(grid, i, n - 1);
      }

      // 剩下的都是封闭岛屿
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          // 发现岛屿
          if (grid[i][j] === 0) {
            result++;

            // 使用 DFS 将相连的陆地（整个岛屿）全淹了
            dfs(grid, i, j);
          }
        }
      }
      return result;
    };

    // 从 (i, j) 开始，将自己和相邻的陆地都变成海水
    const dfs = function (grid, i, j) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) {// 超出索引边界
        return;
      }
      if (grid[i][j] === 1) {// 已经是海水了（不能再查找陆地）
        return;
      }

      // 将 (i, j) 变成海水（或设置成其他标记，那上面的判断也要加上）
      grid[i][j] = 1;

      // 淹没上下左右的陆地
      dfs(grid, i - 1, j);
      dfs(grid, i + 1, j);
      dfs(grid, i, j - 1);
      dfs(grid, i, j + 1);
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    深度优先遍历。不推荐。

    ```js
    var closedIsland = function (grid) {
      let result = 0;
      const m = grid.length;
      const n = grid[0].length;
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          if (grid[i][j] === 0 && dfs(grid, i, j)) {  // 若是陆地，则深度优先搜索上下左右是否接触到海水
            result++;
          }
        }
      }
      return result;
    };

    // 把陆地接触到的变成水，递归上下左右，直到 触碰到水 或 超出索引边界。true：是封闭岛屿；false：不是
    const dfs = function (grid, i, j) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) { // 超出索引边界
        return false;
      }
      if (grid[i][j] === 1) { // 抵达：水
        return true;
      }

      grid[i][j] = 1; // 将 (i, j) 变成水

      const top = dfs(grid, i - 1, j);
      const bottom = dfs(grid, i + 1, j, grid);
      const left = dfs(grid, i, j - 1, grid);
      const right = dfs(grid, i, j + 1, grid);

      // 递归上下左右
      return top && bottom && left && right;
    };
    ```
</details>

### 飞地的数量
给你一个大小为 `m x n` 的二进制矩阵 `grid` ，其中 `0` 表示一个海洋单元格、`1` 表示一个陆地单元格。

一次 **移动** 是指从一个陆地单元格走到另一个相邻（**上、下、左、右**）的陆地单元格或跨过 `grid` 的边界。

返回网格中 **无法** 在任意次数的移动中离开网格边界的陆地单元格的数量。

示例 1：

![enclaves1.jpg](./images/enclaves1.jpg)

```
输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
```

示例 2：

![enclaves2.jpg](./images/enclaves2.jpg)

```
输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
```

提示：

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid[i][j]` 的值为 `0` 或 `1`

1. 解法

    深度优先遍历把 上下左右边 的岛屿先排除掉（先全淹了），剩下的就是飞地。

    ```js
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    var numEnclaves = function (grid) {
      let result = 0;
      const m = grid.length;
      const n = grid[0].length;

      // 把 上下 的岛屿淹没
      for (let j = 0; j < n; j++) {
        dfs(grid, 0, j);
        dfs(grid, m - 1, j);
      }
      // 把 左右 的岛屿淹没
      for (let i = 0; i < m; i++) {
        dfs(grid, i, 0);
        dfs(grid, i, n - 1);
      }

      // 剩下的陆地都是飞地
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          // 发现飞地
          if (grid[i][j] === 1) {
            result++;
          }
        }
      }
      return result;
    };

    // 从 (i, j) 开始，将自己和相邻的陆地都变成海水
    const dfs = function (grid, i, j) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) {// 超出索引边界
        return;
      }
      if (grid[i][j] === 0) {// 已经是海水了（不能再查找陆地）
        return;
      }

      // 将 (i, j) 变成海水（或设置成其他标记，那上面的判断也要加上）
      grid[i][j] = 0;

      // 淹没上下左右的陆地
      dfs(grid, i - 1, j);
      dfs(grid, i + 1, j);
      dfs(grid, i, j - 1);
      dfs(grid, i, j + 1);
    };
    ```

### 岛屿的最大面积
给你一个大小为 `m x n` 的二进制矩阵 `grid` 。

**岛屿** 是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在 **水平或者竖直的四个方向上** 相邻。你可以假设 `grid` 的四个边缘都被 `0`（代表水）包围着。

岛屿的面积是岛上值为 `1` 的单元格的数目。

计算并返回 `grid` 中最大的岛屿面积。如果没有岛屿，则返回面积为 `0` 。

示例 1：

![maxarea1-grid.jpg](./images/maxarea1-grid.jpg)

```
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
```

示例 2：

```
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0
```

提示：

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` 为 `0` 或 `1`

1. 解法

    深度优先遍历，为了避免重复遍历，需要把相连的陆地（整个岛屿）全淹了，淹的时候记录岛屿面积。

    ```js
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    var maxAreaOfIsland = function (grid) {
      let result = 0;
      const m = grid.length;
      const n = grid[0].length;
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          // 发现岛屿
          if (grid[i][j] === 1) {
            // 使用 DFS 把相连的陆地（整个岛屿）全淹了，并返回岛屿面积
            result = Math.max(dfs(grid, i, j), result);
          }
        }
      }
      return result;
    };

    // 1. 从 (i, j) 开始，把自己和相邻的陆地都变成海水
    // 2. 返回陆地数量（岛屿面积）
    const dfs = function (grid, i, j) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) { // 超出索引边界
        return 0;
      }
      if (grid[i][j] === 0) { // 已经是海水了（不能再查找陆地）
        return 0;
      }

      // 将 (i, j) 变成海水（或设置成其他标记，那上面的判断也要加上）
      grid[i][j] = 0;

      // 淹没上下左右的陆地，并获取岛屿面积
      return (
        1 +
        dfs(grid, i - 1, j) +
        dfs(grid, i + 1, j) +
        dfs(grid, i, j - 1) +
        dfs(grid, i, j + 1)
      );
    };
    ```

### 统计子岛屿
给你两个 `m x n` 的二进制矩阵 `grid1` 和 `grid2` ，它们只包含 `0` （表示水域）和 `1` （表示陆地）。一个 **岛屿** 是由 **四个方向** （水平或者竖直）上相邻的 `1` 组成的区域。任何矩阵以外的区域都视为水域。

如果 `grid2` 的一个岛屿，被 `grid1` 的一个岛屿 **完全** 包含，也就是说 `grid2` 中该岛屿的每一个格子都被 `grid1` 中同一个岛屿完全包含，那么我们称 `grid2` 中的这个岛屿为 **子岛屿** 。

请你返回 `grid2` 中 **子岛屿** 的 **数目** 。

示例 1：

![test1.png](images/test1.png)

```
输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
输出：3
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
```

示例 2：

![testcasex2.png](images/testcasex2.png)

```
输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
输出：2
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
```

提示：

- `m == grid1.length == grid2.length`
- `n == grid1[i].length == grid2[i].length`
- `1 <= m, n <= 500`
- `grid1[i][j]` 和 `grid2[i][j]` 都要么是 `0` 要么是 `1` 。

1. 解法

    深度优先遍历把 不是子岛屿 的岛屿先排除掉（先全淹了），剩下的就是子岛屿（与[岛屿数量](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#岛屿数量)类似：深度优先遍历，为了避免重复遍历，需要把相连的陆地（整个岛屿）全淹了）。

    ```js
    /**
     * @param {number[][]} grid1
     * @param {number[][]} grid2
     * @return {number}
     */
    var countSubIslands = function (grid1, grid2) {
      let result = 0;
      const m = grid1.length;
      const n = grid1[0].length;

      // 找到不是子岛屿的先淹没
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          // 若grid1是海水 && grid2是陆地，则说明这个grid2的岛屿一定不是grid1的子岛屿
          if (grid1[i][j] === 0 && grid2[i][j] === 1) {
            // 淹没grid2不是子岛屿的岛屿
            dfs(grid2, i, j);
          }
        }
      }

      // grid2剩下的都是grid1的子岛屿
      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          if (grid2[i][j] === 1) {
            result++;

            dfs(grid2, i, j);
          }
        }
      }
      return result;
    };

    // 从 (i, j) 开始，将自己和相邻的陆地都变成海水
    const dfs = function (grid, i, j) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) { // 超出索引边界
        return;
      }
      if (grid[i][j] === 0) { // 已经是海水了（不能再查找陆地）
        return;
      }

      // 将 (i, j) 变成海水（或设置成其他标记，那上面的判断也要加上）
      grid[i][j] = 0;

      // 淹没上下左右的陆地
      dfs(grid, i - 1, j);
      dfs(grid, i + 1, j);
      dfs(grid, i, j - 1);
      dfs(grid, i, j + 1);
    };
    ```

### 不同岛屿的数量
给定一个非空 01 二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 `1` 组成，你可以认为网格的四周被海水包围。

请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。

示例 1：

![distinctisland1-1-grid.jpg](./images/distinctisland1-1-grid.jpg)

```
输入: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
输出：1
```

示例 2：

```
输入: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
输出: 3
```

![distinctisland1-2-grid.jpg](./images/distinctisland1-2-grid.jpg)

提示：

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` 仅包含 `0` 或 `1`

1. 解法

    深度优先遍历，为了避免重复遍历，需要把相连的陆地（整个岛屿）全淹了，淹的时候记录序列化路径。

    ```js
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    var numDistinctIslands = function (grid) {
      // 记录所有岛屿的序列化结果
      const result = new Set();

      const m = grid.length;
      const n = grid[0].length;

      for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
          // 发现岛屿
          if (grid[i][j] === 1) {
            const path = [];
            // 淹掉这个岛屿，同时存储岛屿的序列化结果
            dfs(grid, i, j, path, "开始");    // "开始"文本可以替换成任意（只要有值并且和下面的上下左右不同即可）
            result.add(path.toString());
          }
        }
      }

      return result.size;
    };

    // 从 (i, j) 开始，把自己和相邻的陆地都变成海水，并记录线路（path、dir）
    const dfs = function (grid, i, j, path, dir) {
      const m = grid.length;
      const n = grid[0].length;

      if (i < 0 || j < 0 || i >= m || j >= n) { // 超出索引边界
        return;
      }
      if (grid[i][j] === 0) { // 已经是海水了（不能再查找陆地）
        return;
      }

      // 将 (i, j) 变成海水（或设置成其他标记，那上面的判断也要加上）
      grid[i][j] = 0;

      // 路线进入
      path.push(dir);

      dfs(grid, i - 1, j, path, "top");     // 上
      dfs(grid, i + 1, j, path, "bottom");  // 下
      dfs(grid, i, j - 1, path, "left");    // 左
      dfs(grid, i, j + 1, path, "right");   // 右

      // 路线退出（若不退出，则会导致不同岛屿却路径可能一样）
      path.push(-dir);
    };
    ```

---
## 中等

### 盛最多水的容器
给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1：

![question_11.jpg](./images/question_11.jpg)

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

示例 2：

```
输入：height = [1,1]
输出：1
```

提示：

- `n == height.length`
- `2 <= n <= 10 ** 5`
- `0 <= height[i] <= 10 ** 4`

1. 解法一

    双指针。缩减搜索空间如何保证不漏情况。

    ```js
    /**
     * @param {number[]} height
     * @return {number}
     */
    var maxArea = function (height) {
      let maxArea = 0;
      // 第一个和最后一个项为双指针初始状态
      for (let left = 0, right = height.length - 1; left < right; ) {
        maxArea = Math.max(
          maxArea,
          (right - left) * Math.min(height[left], height[right]),
        );

        // 需要验证：缩小短的一边能找到最大面积（相等的边缩短哪一边都一样）
        if (height[left] < height[right]) {
          left++;
        } else {
          right--;
        }
      }

      return maxArea;
    };

    // 缩减搜索空间，如何找到最大的面积：
    //   1. 在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 −1 变短，
    //   2.1. 若向内 移动短板 ，水槽的短板可能 变大或不变或变小，因此下个水槽的面积 可能增大；
    //   2.2. 若向内 移动长板 ，水槽的短板可能 不变或变小，因此下个水槽的面积 一定变小。
    //   缩小短的一边能找到最大面积。
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    暴力解法，O(n^2)，已超时。

    ```js
    var maxArea = function (height) {
      let maxvolume = 0;
      for (let i = 0; i < height.length - 1; i++) {
        for (let j = i + 1; j < height.length; j++) {
          maxvolume = Math.max(maxvolume, (j - i) * Math.min(height[i], height[j]));
        }
      }
      return maxvolume;
    };
    ```
</details>

### 无重复字符的最长子串
给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

示例 1:

```
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

示例 2:

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

示例 3:

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

提示：

- `0 <= s.length <= 5 * 10 ** 4`
- `s` 由英文字母、数字、符号和空格组成

1. 解法一

    滑动窗口（双指针）。

    ```js
    /**
     * @param {string} s
     * @return {number}
     */
    var lengthOfLongestSubstring = function (s) {
      // 哈希表
      const hash = new Set();

      let longestLen = 0;

      // 双指针
      for (let left = 0, right = 0; left < s.length; ++left) {
        if (left === 0) {
          // 初始化
          hash.add(s[0]);
          longestLen = 1;
        } else {
          // 左指针向右移动一格，移除一个字符
          hash.delete(s[left - 1]);
        }

        // 不断地移动右指针，直到长度尽头或者重复
        while (right + 1 < s.length && !hash.has(s[right + 1])) {
          hash.add(s[right + 1]);
          ++right;
        }

        longestLen = Math.max(longestLen, right - left + 1);
      }
      return longestLen;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    暴力解法，O(n^2) + 嵌套的判断无重复的时间复杂度。

    1. 利用`Set`

        ```js
        var lengthOfLongestSubstring = function (s) {
          let longestLen = 0;
          for (let i = 0; i < s.length; i++) {
            longestLen = Math.max(longestLen, 1);

            const hash = new Set([s[i]]);

            for (let j = i + 1; j < s.length; j++) {
              if (hash.has(s[j])) {
                break;
              }
              hash.add(s[j]);
              longestLen = Math.max(longestLen, j - i + 1);
            }
          }
          return longestLen;
        };
        ```
    2. 利用`String.prototype.includes`

        ```js
        var lengthOfLongestSubstring = function (s) {
          let longestLen = 0;
          for (let i = 0; i < s.length; i++) {
            longestLen = Math.max(longestLen, 1);

            for (let j = i + 1; j < s.length; j++) {
              if (s.slice(i, j).includes(s[j])) {
                break;
              }
              longestLen = Math.max(longestLen, j - i + 1);
            }
          }
          return longestLen;
        };
        ```
</details>

### 下一个排列
整数数组的一个 **排列**  就是将其所有成员以序列或线性顺序排列。

- 例如，`arr = [1,2,3]` ，以下这些都可以视作 `arr` 的排列：`[1,2,3]`、`[1,3,2]`、`[3,1,2]`、`[2,3,1]` 。

整数数组的 **下一个排列** 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 **下一个排列** 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

- 例如，`arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。
- 类似地，`arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。
- 而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。

给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。

必须 **原地** 修改，只允许使用额外常数空间。

示例 1：

```
输入：nums = [1,2,3]
输出：[1,3,2]
```

示例 2：

```
输入：nums = [3,2,1]
输出：[1,2,3]
```

示例 3：

```
输入：nums = [1,1,5]
输出：[1,5,1]
```

提示：

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

1. 解法一

    由后往前，若找到第一个后面项大于前面项，则调换位置，此时前面项之后的所有项都保持递减排序，需要对之后项用递增排序或reverse；若找不到，则说明原来就是最大排列，需要对所有项用递增排序或reverse。

    ```js
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    var nextPermutation = function (nums) {
      // 第一层：从后往前遍历，到达0结束
      for (let i = nums.length - 1; i >= 0; i--) {
        // 第二层：从后往前遍历，到达i后一个结束
        for (let j = nums.length - 1; j > i; j--) {
          // 若找到第一个后面项大于前面项的，则调换i、j项位置。此时i后面项是递减排序，需要逆序
          if (nums[j] > nums[i]) {
            let temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;

            // i后项也保持递减，需要逆序（实现reverse数组部分项）
            let l = i + 1;
            let r = nums.length - 1;
            while (l < r) {
              [nums[l], nums[r]] = [nums[r], nums[l]];
              l++;
              r--;
            }
            return;
          }
        }
      }

      // 若所有都是递减数字会走到这里，则需要重回到最小排列，需要逆序
      nums.reverse();
    };
    ```
2. 解法二

    把解法一的嵌套for改为2遍扫描。

    ```js
    var nextPermutation = function (nums) {
      let i;
      // 从后往前，找到第一个相邻的项i满足 前面小于后面（若找不到则i===-1）
      for (i = nums.length - 2; i >= 0 && nums[i] >= nums[i + 1]; i--) {}

      if (i >= 0) {
        let j;
        // 从后往前，找到第一个i项小于j项
        for (j = nums.length - 1; j >= 0 && nums[i] >= nums[j]; j--) {}

        // 换i、j项位置。
        [nums[i], nums[j]] = [nums[j], nums[i]];

        // 此时i后面项是递减排序，需要逆序i+1到最后1项
      }

      // 若i===-1，则表示原本是最大排列，需要逆序i+1到最后1项

      // reverse
      let l = i + 1;
      let r = nums.length - 1;
      while (l < r) {
        [nums[l], nums[r]] = [nums[r], nums[l]];
        l++;
        r--;
      }
    };
    ```

### 寻找峰值
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)` 的算法来解决此问题。

示例 1：

```
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
```

示例 2：

```
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
```

提示：

- `1 <= nums.length <= 1000`
- `-(2 ** 31) <= nums[i] <= 2 ** 31 - 1`
- 对于所有有效的 `i` 都有 `nums[i] != nums[i + 1]`

1. 解法

    二分法。重点是验证二分法一定能找到题解：因为题目表示`nums[-1] = nums[n] = -∞`数组边界当做是负无穷 且 `nums[i] != nums[i + 1]`不存在相邻项相等，所以任意相邻的项中，朝更大的项的方向一定能找到峰值。

    ```js
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var findPeakElement = function (nums) {
      let left = 0;
      let right = nums.length - 1;
      let middle;
      while (left < right) {
        middle = Math.floor((left + right) / 2);
        if (nums[middle] < nums[middle + 1]) {
          left = middle + 1;
        } else {
          right = middle;
        }
      }

      return left;
    };
    ```

### 森林中的兔子
森林中有未知数量的兔子。提问其中若干只兔子 **"还有多少只兔子与你（指被提问的兔子）颜色相同?"** ，将答案收集到一个整数数组 `answers` 中，其中 `answers[i]` 是第 `i` 只兔子的回答。

给你数组 `answers` ，返回森林中兔子的最少数量。

示例 1：

```
输入：answers = [1,1,2]
输出：5
解释：
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。
```

示例 2：

```
输入：answers = [10,10,10]
输出：11
```

提示：

- `1 <= answers.length <= 1000`
- `0 <= answers[i] < 1000`

1. 解法

    ```js
    /**
     * @param {number[]} answers
     * @return {number}
     */
    var numRabbits = function (answers) {
      // {回答x只: 回答x只的兔子数}
      const map = new Map();
      answers.filter((answer) => {
        map.set(answer, map.get(answer) ? map.get(answer) + 1 : 1);
      });

      return [...map].reduce((acc, [answer, times]) => {
        // 一组内最多相同的兔子：answer + 1；兔子：times；组数：向上取整(兔子/一组内最多相同的兔子)
        return acc + (answer + 1) * Math.ceil(times / (answer + 1));
      }, 0);
    };
    ```

### 课程表 II
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 **任意一种** 就可以了。如果不可能完成所有课程，返回 **一个空数组** 。

1. 解法一

    有向图的拓扑排序，利用入度（依赖几个就入度几），广度优先搜索。

    ```js
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    var findOrder = function (numCourses, prerequisites) {
      const result = [];
      // 有向图（二维数组。一维是被依赖项，二维是主依赖者数组）
      const edges = new Array(numCourses).fill().map(() => []);
      // 节点的入度（入度n：依赖n个其他节点）
      const indegree = new Array(numCourses).fill(0);

      // 初始化：有向图、入度数组
      for (const [course, prerequisite] of prerequisites) {
        edges[prerequisite].push(course);
        indegree[course]++;
      }

      // 入度为0的节点加入queque
      const queue = [];
      // 将所有入度为 0 的节点（依赖0个其他节点）放入队列（后面统一处理）
      for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) {
          queue.unshift(i);
        }
      }

      // 广度优先搜索
      while (queue.length > 0) {
        const indegree0 = queue.pop();
        result.push(indegree0);

        // 去掉一个入度为0的节点，使 依赖这个节点的所有节点入度-1
        if (edges[indegree0]) {
          for (const v of edges[indegree0]) {
            indegree[v]--;

            // 若新生成入度为0的节点，则加入queque
            if (indegree[v] === 0) {
              queue.unshift(v);
            }
          }
        }
      }

      // 若有环，则总会有入度不为0的节点
      if (result.length !== numCourses) { return []; }

      // 拓扑排序
      return result;
    };
    ```

<details>
<summary>其他解法</summary>

2. 解法二

    有向图的拓扑排序，深度优先搜索。

    ```js
    var findOrder = function (numCourses, prerequisites) {
      const result = [];
      // 有向图（二维数组。一维是被依赖项，二维是主依赖者数组）
      const edges = new Array(numCourses).fill().map(() => []);
      // 标记每个节点访问状态：0=未搜索，1=搜索中，2=已完成（为了判定是否有环：若2次被范围则说明有环）
      const visited = new Array(numCourses).fill(0);
      // 判断有向图中是否有环
      let valid = true;

      // 初始化：有向图
      for (const [course, prerequisite] of prerequisites) {
        edges[prerequisite].push(course);
      }

      // 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
      for (let i = 0; i < numCourses && valid; i++) {
        if (visited[i] === 0) {
          dfs(i);
        }
      }

      // 环
      if (!valid) { return []; }

      // 拓扑排序
      return result;

      // 深度优先搜索
      function dfs(pre) {
        // 标记为「搜索中」
        visited[pre] = 1;

        // 搜索其相邻节点
        for (const main of edges[pre]) {
          // 如果「未搜索」那么搜索相邻节点
          if (visited[main] === 0) {
            dfs(main);

            // 只要发现有环，立刻停止搜索
            if (!valid) { return; }
          }
          // 如果「搜索中」说明找到了环
          else if (visited[main] === 1) {
            valid = false;
            return;
          }
        }
        // 将节点标记为「已完成」
        visited[pre] = 2;

        result.unshift(pre);
      }
    };
    ```
</details>

### 比较版本号
比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 **忽略任何前导零后的整数值** 。也就是说，修订号 `1` 和修订号 `001` **相等** 。如果版本号没有指定某个下标处的修订号，则该修订号视为 `0`

1. 解法

    字符串分割。

    ```js
    /**
     * @param {string} version1
     * @param {string} version2
     * @return {number}
     */
    var compareVersion = function (version1, version2) {
      let v1 = version1.split(".").map((v) => {
        return Number(v); // 去除前导零
      });
      let v2 = version2.split(".").map((v) => {
        return Number(v);
      });

      const v1Len = v1.length;
      const v2Len = v2.length;
      // 补齐一样长度的数组
      if (v1Len > v2Len) {
        v2 = v2.concat(Array.from({ length: v1Len - v2Len }).map(() => 0));
      } else {
        v1 = v1.concat(Array.from({ length: v2Len - v1Len }).map(() => 0));
      }
      for (let i = 0; i < v1.length; i++) {
        if (v1[i] !== v2[i]) {
          return v1[i] > v2[i] ? 1 : -1;
        }
      }

      return 0;
    };
    ```

---
## 困难

### 接雨水
给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

![rainwatertrap.png](./images/rainwatertrap.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
```

示例 2：

```
输入：height = [4,2,0,3,2,5]
输出：9
```

提示：

- `n == height.length`
- `1 <= n <= 2 * 10 ** 4`
- `0 <= height[i] <= 10 ** 5`


1. 解法一

    单调栈（类似[每日温度](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#每日温度)），O(n)。

    ```js
    var trap = function (height) {
      // if (height.length <= 2) return 0; // 可选

      // 单调栈（栈头至栈底 递增，但存储的是下标）
      const stack = [];

      let sum = 0;
      for (let i = 0; i <= height.length; i++) {
        // 第一个元素 || i项 小于等于 栈顶元素
        if (stack.length === 0 || height[i] <= height[stack[stack.length - 1]]) {
          // i项如栈
          stack.push(i);
        } else {
          // 栈不空 && i项 大于 栈顶元素
          while (stack.length > 0 && height[i] > height[stack[stack.length - 1]]) {
            const middle = stack.pop();

            // （推出middle之前）栈内需要有2个及以上元素才能够形成凹槽积水
            if (stack.length > 0) {
              const h = Math.min(height[stack[stack.length - 1]], height[i]) - height[middle];
              const w = i - stack[stack.length - 1] - 1;
              // 每次累加一个凹槽面积
              sum += h * w;
            }
          }
          stack.push(i);
        }
      }
      return sum;
    };
    ```
2. 解法二

    双指针（优化动态规划需要的空间复杂度），O(n)。

    ```js
    var trap = function (height) {
      // 按列累加
      let sum = 0;

      // 记录从左往右判断，左边最高的柱子高度
      let leftMax = 0;
      // 记录从右往左判断，右边最高的柱子高度
      let rightMax = 0;

      // 双指针
      let left = 0;
      let right = height.length - 1;
      while (left < right) {
        // 若左边小，则左边可能出现低洼
        if (height[left] < height[right]) {
          // 若当前比左边最大的还大，说明无法形成低洼，则更新左边最高高度
          if (height[left] > leftMax) {
            leftMax = height[left];
          } else {
            sum += leftMax - height[left];
          }

          ++left;
        }
        // 右边同理左边
        else {
          if (height[right] > rightMax) {
            rightMax = height[right];
          } else {
            sum += rightMax - height[right];
          }

          --right;
        }
      }
      return sum;
    };
    ```

<details>
<summary>其他解法</summary>

3. 解法三

    暴力解法，计算每一列，O(n^2)

    ```js
    /**
     * @param {number[]} height
     * @return {number}
     */
    var trap = function (height) {
      // 计算每一列雨水高度，暴力相加
      let sum = 0;
      // 第一个柱子和最后一个柱子不接雨水
      for (let i = 1; i < height.length - 1; i++) {
        let rHeight = height[i]; // 记录右边柱子的最高高度（若没有大于项i的，则保存项i的值）
        let lHeight = height[i]; // 记录左边柱子的最高高度（若没有大于项i的，则保存项i的值）
        for (let r = i + 1; r < height.length; r++) {
          rHeight = Math.max(height[r], rHeight);
        }
        for (let l = i - 1; l >= 0; l--) {
          lHeight = Math.max(height[l], lHeight);
        }
        // 当前列能接的雨水 等于 左右最高柱子中矮的 - 当前列高度。正数才能接雨水
        const h = Math.min(lHeight, rHeight) - height[i];
        if (h > 0) sum += h;
      }
      return sum;
    };
    ```
4. 解法四

    动态规划，先计算并保存左右柱子最大高度，把暴力解法的嵌套计算逻辑放在外面，较少遍历层级，计算每一列，O(n)。

    ```js
    var trap = function (height) {
      // if (height.length <= 2) return 0;  // 可选

      const size = height.length;

      // 项i的值：项i左边柱子最大高度（若没有大于项i的，则保存项i的值）
      const maxLeft = new Array(height.length).fill(0);
      maxLeft[0] = height[0];
      for (let i = 1; i < size; i++) {
        maxLeft[i] = Math.max(height[i], maxLeft[i - 1]);
      }

      // 项i的值：项i右边柱子最大高度（若没有大于项i的，则保存项i的值）
      const maxRight = new Array(height.length).fill(0);
      maxRight[size - 1] = height[size - 1];
      for (let i = size - 2; i >= 0; i--) {
        maxRight[i] = Math.max(height[i], maxRight[i + 1]);
      }

      // 求和
      let sum = 0;
      for (let i = 0; i < size; i++) {
        // 当前列能接的雨水 等于 左右最高柱子中矮的 - 当前列高度。正数才能接雨水
        const h = Math.min(maxLeft[i], maxRight[i]) - height[i];
        if (h > 0) sum += h;
      }
      return sum;
    };
    ```
</details>
