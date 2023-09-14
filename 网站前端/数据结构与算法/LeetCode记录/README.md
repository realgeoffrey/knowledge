# [LeetCode](https://leetcode-cn.com/)记录

## 目录
1. [简单](#简单)

    1. [用两个栈实现队列](#用两个栈实现队列)
    1. [包含min函数的栈](#包含min函数的栈)
    1. [从尾到头打印链表](#从尾到头打印链表)
    1. [反转链表](#反转链表)
    1. [替换空格](#替换空格)
    1. [左旋转字符串](#左旋转字符串)
    1. [数组中重复的数字](#数组中重复的数字)
    1. [在排序数组中查找数字 I](#在排序数组中查找数字-i)
    1. [0～n-1中缺失的数字](#0n-1中缺失的数字)
    1. [旋转数组的最小数字](#旋转数组的最小数字)
    1. [第一个只出现一次的字符](#第一个只出现一次的字符)
    1. [二叉树的镜像](#二叉树的镜像)
    1. [对称的二叉树](#对称的二叉树)
    1. [斐波那契数列](#斐波那契数列)
    1. [青蛙跳台阶问题](#青蛙跳台阶问题)
    1. [连续子数组的最大和](#连续子数组的最大和)
    1. [移除元素](#移除元素)
    1. [有序数组的平方](#有序数组的平方)
    1. [两数之和](#两数之和)
    1. [移动零](#移动零)
1. [中等](#中等)

    1. [复杂链表的复制](#复杂链表的复制)
    1. [二维数组中的查找](#二维数组中的查找)
    1. [从上到下打印二叉树 I](#从上到下打印二叉树-i)
    1. [从上到下打印二叉树 II](#从上到下打印二叉树-ii)
    1. [从上到下打印二叉树 III](#从上到下打印二叉树-iii)
    1. [树的子结构](#树的子结构)
    1. [股票的最大利润](#股票的最大利润)
    1. [鸡蛋掉落-两枚鸡蛋](#鸡蛋掉落-两枚鸡蛋)
    1. [长度最小的子数组](#长度最小的子数组)
    1. [螺旋矩阵 II](#螺旋矩阵-ii)
    1. [字母异位词分组](#字母异位词分组)
    1. [最长连续序列](#最长连续序列)
    1. [盛最多水的容器](#盛最多水的容器)
    1. [三数之和](#三数之和)
    1. [无重复字符的最长子串](#无重复字符的最长子串)

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

---
## 简单

### 用两个栈实现队列
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

1. 解法

    ```javascript
    var CQueue = function () {
      // 2个栈，意味着只能 shift unshift 的数组
      // 实现队列，因此要实现类似数组的 unshift pop

      // 存放插入的数据
      this.arr1 = [];

      // 处理移出的数据。当为空时，从arr1中获取全部数据
      this.arr2 = [];
    };

    /**
     * @param {number} value
     * @return {void}
     */
    CQueue.prototype.appendTail = function (value) {
      this.arr1.unshift(value);
    };

    /**
     * @return {number}
     */
    CQueue.prototype.deleteHead = function () {
      if (this.arr2.length > 0) {
        return this.arr2.shift();
      } else if (this.arr1.length > 0) {
        while (this.arr1.length > 0) {
          this.arr2.unshift(this.arr1.shift());
        }
        return this.arr2.shift();
      } else {
        return -1;
      }
    };

    /**
     * Your CQueue object will be instantiated and called as such:
     * var obj = new CQueue()
     * obj.appendTail(value)
     * var param_2 = obj.deleteHead()
     */
    ```

### 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 $O(1)$ 。

示例：
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```
1. 解法一

    ```javascript
    /**
     * initialize your data structure here.
     */
    var MinStack = function () {
      // 存放栈数据
      this.list = [];
      // 存放最小数
      this.minList = [];
    };

    /**
     * @param {number} x
     * @return {void}
     */
    MinStack.prototype.push = function (x) {
      this.list.unshift(x);

      if (this.minList.length === 0 || x <= this.minList[0]) {
        this.minList.unshift(x);
      }
    };

    /**
     * @return {void}
     */
    MinStack.prototype.pop = function () {
      if (this.list.length > 0) {
        const value = this.list.shift();

        if (value === this.minList[0]) {
          this.minList.shift();
        }
        return;
      }

      throw Error("栈内为空");
    };

    /**
     * @return {number}
     */
    MinStack.prototype.top = function () {
      if (this.list.length > 0) {
        return this.list[0];
      }

      throw Error("栈内为空");
    };

    /**
     * @return {number}
     */
    MinStack.prototype.min = function () {
      if (this.minList.length > 0) {
        return this.minList[0];
      }

      throw Error("栈内为空");
    };

    /**
     * Your MinStack object will be instantiated and called as such:
     * var obj = new MinStack()
     * obj.push(x)
     * obj.pop()
     * var param_3 = obj.top()
     * var param_4 = obj.min()
     */
    ```
2. 解法二

    ```javascript
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

    MinStack.prototype.min = function () {
      if (this.minList.length > 0) {
        return this.minList[0];
      }

      throw Error("栈内为空");
    };
    ```

### 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例：
```
输入：head = [1,3,2]
输出：[2,3,1]
```

1. 解法一

    ```javascript
    /**
     * Definition for singly-linked list.
     * function ListNode(val) {
     *     this.val = val;
     *     this.next = null;
     * }
     */
    /**
     * @param {ListNode} head
     * @return {number[]}
     */
    var reversePrint = function (head) {
      const arr = [];

      while (head) {
        arr.unshift(head.val);
        head = head.next;
      }

      return arr;
    };
    ```
2. 解法二

    ```javascript
    var reversePrint = function (head) {
      // 递归
      return head ? [...reversePrint(head.next), head.val] : [];
    };
    ```

### 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

1. 解法一

    ```javascript
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
      let beforeHead = null;

      while (head) {
        const nextHead = head.next;
        head.next = beforeHead;
        beforeHead = head;
        head = nextHead;
      }
      return beforeHead;
    };
    ```
2. 解法二

    ```javascript
    var reverseList = function (head) {
      // 递归
      if (head === null || head.next === null) {
        return head;
      }
      const newHead = reverseList(head.next);
      head.next.next = head;
      head.next = null;
      return newHead;
    };
    ```

### 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
```
输入：s = "We are happy."
输出："We%20are%20happy."
```

1. 解法一

    ```javascript
    /**
     * @param {string} s
     * @return {string}
     */
    var replaceSpace = function (s) {
      // 还有 split/join 等解法
      return s.replace(/ /g, "%20");
    };
    ```
2. 解法二

    ```javascript
    var replaceSpace = function (s) {
      // 模拟的 C++ 语言中的可变长度字符串的实现原理，将其 O(n^2) 的空间复杂度降低到 O(1)
      const arr = s.split("");
      let oldLen = arr.length;
      let spaceCount = 0;
      for (let i = 0; i < oldLen; i++) {
        if (arr[i] === " ") spaceCount++;
      }
      arr.length += spaceCount * 2;
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

    ```javascript
    /**
     * @param {string} s
     * @param {number} n
     * @return {string}
     */
    var reverseLeftWords = function (s, n) {
      // 以及其他简单拼接法
      return s.slice(n) + s.slice(0, n);
    };
    ```
2. 解法二

    ```javascript
    var reverseLeftWords = function (s, n) {
      if (n >= s.length) {
        return s;
      }
      // 复制一遍字符串，再截取
      return (s + s).slice(n, n + s.length);
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

    ```javascript
    /**
     * @param {number[]} nums
     * @return {number}
     */
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
2. 解法二

    ```javascript
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
3. 解法三

    ```javascript
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
4. 解法四

    ```javascript
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

    暴力搜索、穷举搜索。

    ```javascript
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    var search = function (nums, target) {
      let count = 0;
      nums.forEach((x) => {
        if (x === target) count++;
      });
      return count;
    };
    ```

    ```javascript
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

    ```javascript
    const search = function (nums, target) {
      return nums.reduce((a, b) => (b === target ? a + 1 : a), 0);
    };
    ```
2. 解法二

    ```javascript
    var search = function (nums, target) {
      const length = nums.length;
      let start = -1;
      let end = -1;

      let left = 0;
      let right = length - 1;
      // 二分搜索：找到左边界，找到第一次出现
      while (left <= right) {
        let mid = Math.floor((left + right) / 2);
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
        let mid = Math.floor((left + right) / 2);
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

    ```javascript
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

    暴力搜索、穷举搜索。

    ```javascript
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var missingNumber = function (nums) {
      for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i) return i;
      }
      return nums.length;
    };
    ```

    ```javascript
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

    ```javascript
    var missingNumber = function (nums) {
      // 任何数字异或自己等于0，0异或任何数字等于这个数字
      let xor = 0;
      for (let i = 0; i < nums.length; i++) {
        xor ^= nums[i] ^ i;
      }
      return xor ^ nums.length;
    };
    ```
2. 解法二

    >开闭区间的选择？

    ```javascript
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

    ```javascript
    /**
     * @param {number[]} numbers
     * @return {number}
     */
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
2. 解法二

    ```javascript
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
        // 若相等，则最右边的项一定不是目标（3种情况判断的结果）
        else {
          right -= 1;
        }
      }
      // 退出时，left === right
      return numbers[left];
    };
    ```

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

    ```javascript
    /**
     * @param {string} s
     * @return {character}
     */
    var firstUniqChar = function (s) {
      const strArr = s.split("");
      return (
        strArr.find((str) => {
          return strArr.indexOf(str) === strArr.lastIndexOf(str);
        }) ?? " "
      );
    };
    ```
2. 解法二

    ```javascript
    var firstUniqChar = function (s) {
      const strArr = s.split("");
      const map = new Map();
      for (let str of strArr) {
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
3. 解法三

    ```javascript
    var firstUniqChar = function (s) {
      for (let char of new Set(s)) {
        if (s.match(new RegExp(char, "g")).length === 1) {
          return char;
        }
      }
      return " ";
    };
    ```
4. 解法四

    ```javascript
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

### 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

```
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
```

镜像输出：

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

示例 1：

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```

1. 解法一

    不修改原二叉树。

    ```typescript
    class TreeNode {
      val: number;
      left: TreeNode | null;
      right: TreeNode | null;
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
      }
    }

    function mirrorTree(root: TreeNode | null): TreeNode | null {
      // 递归
      if (root === null) {
        return root;
      }

      return new TreeNode(root.val, mirrorTree(root.right), mirrorTree(root.left));
    }
    ```
2. 解法二

    修改原二叉树。

    ```javascript
    var mirrorTree = function (root) {
      // 递归
      if (!root) {
        return null;
      }
      const temp = root.left;
      root.left = root.right;
      root.right = temp;

      mirrorTree(root.left);
      mirrorTree(root.right);

      return root;
    };
    ```

    ```typescript
    function mirrorTree(root: TreeNode | null): TreeNode | null {
      if (root === null) {
        return root;
      }
      // 二叉树广度优先，用队列
      const queue = [root];
      while (queue.length) {
        const node = queue.pop();
        const temp = node.left;
        node.left = node.right;
        node.right = temp;
        if (node.left) {
          queue.unshift(node.left);
        }
        if (node.right) {
          queue.unshift(node.right);
        }
      }
      return root;
    }
    ```

    ```typescript
    function mirrorTree(root: TreeNode | null): TreeNode | null {
      if (root === null) {
        return root;
      }
      // 二叉树深度优先（先序），用栈
      const stack = [root];
      while (stack.length) {
        const node = stack.shift();
        const temp = node.left;
        node.left = node.right;
        node.right = temp;
        if (node.left) {
          stack.unshift(node.left);
        }
        if (node.right) {
          stack.unshift(node.right);
        }
      }
      return root;
    }
    ```

### 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```

示例 1：

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

示例 2：

```
输入：root = [1,2,2,null,3,null,3]
输出：false
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

    ```javascript
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
      if (root1 === null && root2 === null) {
        return true;
      }
      if (root1 === null || root2 === null) {
        return false;
      }

      return (
        root1.val === root2.val &&
        helper(root1.left, root2.right) &&
        helper(root1.right, root2.left)
      );
    };
    ```
2. 解法二

    ```javascript
    var isSymmetric = function (root) {
      if (root === null) {
        return true;
      }

      // 栈，需要对比的一双，一起推入和推出
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

### 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

```
输入：n = 2
输出：1
```

示例 2：

```
输入：n = 5
输出：5
```

1. 解法一

    ```javascript
    /**
     * @param {number} n
     * @return {number}
     */
    var fib = function (n) {
      // 动态规划
      if (n < 2) {
        return n;
      }
      const modulo = 1000000007;
      let previous = 0;
      let current = 1;
      // 迭代：记录 前一个值 和 当前值
      for (let i = 2; i <= n; i++) {
        const temp = previous;
        previous = current;
        current =
          temp + current >= modulo
            ? temp + current - modulo
            : temp + current;
      }
      return current;
    };
    ```
2. 解法二

    ```javascript
    var fib = function (n) {
      // 递归

      // 保存计算过的结果，避免递归时超时
      this.map = this.map || new Map();
      if (this.map.has(n)) {
        return map.get(n);
      }

      if (n < 2) {
        map.set(n, n);
        return n;
      }

      const modulo = 1000000007;
      const result = ((fib(n - 1) % modulo) + (fib(n - 2) % modulo)) % modulo; // (a+b)%c === (a%c+b%c)%c
      map.set(n, result);
      return result;
    };
    ```
3. 解法三

    >todo：矩阵快速幂

### 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

```
输入：n = 2
输出：2
```

示例 2：

```
输入：n = 7
输出：21
```

示例 3：

```
输入：n = 0
输出：1
```

- <details>

    <summary>解析：青蛙跳台问题</summary>

    设跳上 n 级台阶有 f(n) 种跳法。在所有跳法中，青蛙的最后一步只有两种情况：跳上 1 级或 2 级台阶，即 f(n)=f(n−1)+f(n−2)。本题可转化为 求斐波那契数列第 n 项的值。
    </details>

1. 解法

    略。与上一题（[斐波那契数列](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#斐波那契数列)）基本一致，改下初始值即可。

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

    ```javascript
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var maxSubArray = function (nums) {
      // 动态规划
      let max = nums[0];
      for (let i = 1, tempResult = nums[0]; i < nums.length; i++) {
        // tempResult：以元素nums[i]为结尾 的连续子数组最大和
        tempResult = nums[i] + Math.max(tempResult, 0);
        max = Math.max(max, tempResult);
      }
      return max;
    };
    ```

### 移除元素
给你一个数组 `nums` 和一个值 `val`，你需要 **原地** 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 $O(1)$ 额外空间并 **原地** 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以 **「引用」** 方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

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
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

1. 解法一

    ```javascript
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
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
2. 解法二

    **双指针法（快慢指针法）：通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。**

    ```javascript
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
3. 解法三

    暴力解法，O(n^2)。

    ```javascript
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

1. 解法一

    暴力解法。

    ```javascript
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    var sortedSquares = function(nums) {
        // 先计算平方，再排序（注意排序算法的时间复杂度）
        return nums.map(i => i * i).sort((a, b) => a - b);
    };
    ```
2. 解法二

    双指针法。

    ```javascript
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

    暴力解法，O(n^2)。

    ```javascript
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
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
2. 解法二

    哈希法（**当我们需要查询一个元素是否出现过，或者一个元素是否在集合里的时候，就要第一时间想到哈希法**），O(n)。

    ```javascript
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

    ```javascript
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
          noZeroIndex += 1;
        }
      }

      nums.fill(0, noZeroIndex);

      return nums;
    };
    ```
2. 解法二

    双指针。

    ```javascript
    var moveZeroes = function (nums) {
      // 双指针。如果i项!==0，替换i、j项的值并j指针自增。
      for (let i = 0, j = 0; i < nums.length; i++) {
        if(nums[i] !== 0){
          const tmp = nums[i]
          nums[i] = nums[j];
          nums[j] = tmp

          j++
        }
      }
    };
    ```

---
## 中等

### 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
![剑指Offer35-1](./images/剑指Offer35-1.png)
```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

示例 2：
![剑指Offer35-2](./images/剑指Offer35-2.png)
```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

示例 3：
![剑指Offer35-3](./images/剑指Offer35-3.png)
```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```

示例 4：
```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```

1. 解法一

    ```javascript
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
    var copyRandomList = function (head, cachedMap = new Map()) {
      // 递归，哈希表
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
2. 解法二

    ```javascript
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

### 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

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

    ```javascript
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
      // O(n+m)，从右上角开始行动（类似二叉树搜索或二分搜索）
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

    ```javascript
    var findNumberIn2DArray = function (matrix, target) {
      const columnLength = matrix.length;
      const rowLength = matrix[0]?.length ?? 0;

      let column = columnLength - 1;
      let row = 0;
      // O(n+m)，从左下角开始行动（类似二叉树搜索或二分搜索）
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
2. 解法二

    ```javascript
    var findNumberIn2DArray = function (matrix, target) {
      // 列长度
      const columnLength = matrix.length;
      // 行长度
      const rowLength = matrix[0]?.length ?? 0;

      let column = columnLength - 1;
      let row = 0;
      // O(log n + log m)，从左下角开始行动（类似二叉树搜索或二分搜索）
      while (column >= 0 && row <= rowLength - 1) {
        const columnArr = matrix[column];

        // 搜索同行的数。若找到target则返回true；否则查找大于target且本行最小；若找不到则返回false
        if (columnArr[row] < target) {
          const result = hasTarget1({ arr: columnArr, target, start: row });
          if (Object.prototype.toString.call(result) === "[object Boolean]") {
            return result;
          } else {
            row = result;
          }
        }
        // 搜索同列的数。若找到target则返回true；否则查找小于target且本行最大；若找不到则返回false
        else if (columnArr[row] > target) {
          const result = hasTarget2({
            arr: matrix.map((rowArr) => {
              return rowArr[row];
            }),
            target,
            start: column,
          });
          if (Object.prototype.toString.call(result) === "[object Boolean]") {
            return result;
          } else {
            column = result;
          }
        }
        // 找到
        else {
          return true;
        }
      }
      return false;
    };

    /**
     * 针对Number型递增数组，从前往后二分搜索，
     *   若数组存在target则返回`true`；若不存在则返回 `第一个大于target的数所在的数组下标`；若不存在大于target的数则返回 `false`
     * @param {number[]} arr  递增数组
     * @param {number} target 目标
     * @param {number} [start = 0] 数组开始下标
     * @param {number} [end = arr.length - 1] 数组结束下标
     * @return {boolean | number}
     */
    var hasTarget1 = function ({
      arr = [],
      target,
      start = 0,
      end = arr.length - 1,
    } = {}) {
      let left = start;
      let right = end;

      let foundBigger = false;

      while (left <= right) {
        const middle = Math.floor((left + right) / 2);
        if (arr[middle] > target) {
          right = middle - 1;
          foundBigger = middle;
        } else if (arr[middle] < target) {
          left = middle + 1;
        } else {
          return true;
        }
      }

      return foundBigger;
    };

    /**
     * 针对Number型递增数组，从后往前二分搜索，
     *   若数组存在target则返回`true`；若不存在则返回 `第一个小于target的数所在的数组下标`；若不存在小于target的数则返回 `false`
     * @param {number[]} arr  递增数组
     * @param {number} target 目标
     * @param {number} [start = arr.length - 1] 数组开始下标
     * @param {number} [end = 0] 数组结束下标
     * @return {boolean | number}
     */
    var hasTarget2 = function ({
      arr = [],
      target,
      start = arr.length - 1,
      end = 0,
    } = {}) {
      let right = start;
      let left = end;

      let foundSmaller = false;

      while (right >= left) {
        const middle = Math.floor((right + left) / 2);
        if (arr[middle] > target) {
          right = middle - 1;
        } else if (arr[middle] < target) {
          left = middle + 1;
          foundSmaller = middle;
        } else {
          return true;
        }
      }

      return foundSmaller;
    };
    ```

### 从上到下打印二叉树 I
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:

给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```

返回：

```
[3,9,20,15,7]
```

1. 解法一

    ```javascript
    /**
     * Definition for a binary tree node.
     * function TreeNode(val) {
     *     this.val = val;
     *     this.left = this.right = null;
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    var levelOrder = function (root) {
      if (root === null) {
        return [];
      }
      const result = [];
      // 二叉树广度优先，用队列
      const queue = [root];
      while (queue.length) {
        const node = queue.pop();
        result.push(node.val);
        if (node.left) {
          queue.unshift(node.left);
        }
        if (node.right) {
          queue.unshift(node.right);
        }
      }
      return result;
    };
    ```
2. 解法二

    ```typescript
    class TreeNode {
      val: number;
      left: TreeNode | null;
      right: TreeNode | null;
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
      }
    }

    function levelOrder(root: TreeNode | null): number[] {
      let list: number[][] = [];
      levelHelper(list, root, 0);
      return list.reduce((prev, curr) => [...prev, ...curr], []);
    }

    // 二叉树深度优先（先序）+递归
    function levelHelper(list: number[][], root: TreeNode | null, level: number): void {
      if (root === null) {
        return;
      }
      // 有新的一层就创建一个新的空数组，每个数组存放当前层的所有数字
      if (level === list.length) {
        list.push([]);
      }
      list[level].push(root.val);
      levelHelper(list, root.left, level + 1);
      levelHelper(list, root.right, level + 1);
    }
    ```

### 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:

给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [9,20],
  [15,7]
]
```

1. 解法一

    ```javascript
    /**
     * Definition for a binary tree node.
     * function TreeNode(val) {
     *     this.val = val;
     *     this.left = this.right = null;
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    var levelOrder = function (root) {
      if (!root) {
        return [];
      }
      const result = [];
      // 二叉树广度优先，用队列
      const queue = [[root]];
      // 队列，每一项是一整层
      while (queue.length) {
        const currentRes = [];
        const currentChildren = [];
        queue.pop().forEach((node) => {
          currentRes.push(node.val);
          if (node.left) {
            currentChildren.push(node.left);
          }
          if (node.right) {
            currentChildren.push(node.right);
          }
        });
        if (currentChildren.length) {
          queue.unshift(currentChildren);
        }
        if (currentRes.length) {
          result.push(currentRes);
        }
      }
      return result;
    };
    ```
2. 解法二

    ```javascript
    var levelOrder = function (root) {
      if (root === null) {
        return [];
      }
      const result = [];
      // 二叉树广度优先，用队列
      const queue = [root];
      while (queue.length) {
        const currentNodes = [];
        // 推出一整层，再加入下一整层
        for (let i = 0, length = queue.length; i < length; i++) {
          const node = queue.pop();
          currentNodes.push(node.val);
          if (node.left) {
            queue.unshift(node.left);
          }
          if (node.right) {
            queue.unshift(node.right);
          }
        }
        result.push(currentNodes);
      }
      return result;
    };
    ```
3. 解法三

    ```javascript
    var levelOrder = function (root) {
      if (root === null) {
        return [];
      }
      const result = [];
      // 二叉树广度优先，用队列
      const queue = [[root, 0]];
      while (queue.length) {
        const [node, level] = queue.pop();
        if (result.length === level) {
          result.push([]);
        }
        result[level].push(node.val);
        if (node.left) {
          queue.unshift([node.left, level + 1]);
        }
        if (node.right) {
          queue.unshift([node.right, level + 1]);
        }
      }
      return result;
    };
    ```
4. 解法四

    ```typescript
    class TreeNode {
      val: number;
      left: TreeNode | null;
      right: TreeNode | null;
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
      }
    }

    function levelOrder(root: TreeNode | null): number[] {
      let list: number[][] = [];
      levelHelper(list, root, 0);
      return list;
    }

    // 二叉树深度优先（先序）+递归
    function levelHelper(list: number[][], root: TreeNode | null, level: number): void {
      if (root === null) {
        return;
      }
      // 有新的一层就创建一个新的空数组，每个数组存放当前层的所有数字
      if (level === list.length) {
        list.push([]);
      }
      list[level].push(root.val);
      levelHelper(list, root.left, level + 1);
      levelHelper(list, root.right, level + 1);
    }
    ```

### 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:

给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [20,9],
  [15,7]
]
```

1. 解法

    略。与上一题（[从上到下打印二叉树 II](https://github.com/realgeoffrey/knowledge/blob/master/网站前端/数据结构与算法/LeetCode记录/README.md#从上到下打印二叉树-ii)）基本一致，根据奇偶改下每行输出即可。

### 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:

给定的树 A:

```
     3
    / \
   4   5
  / \
 1   2
```

给定的树 B：

```
   4
  /
 1
```

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

```
输入：A = [1,2,3], B = [3,1]
输出：false
```

示例 2：

```
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```

示例 3：

```
输入：A = [1,2,3,4,5], B = [1,2]
输出：true
```

1. 解法

    ```typescript
    class TreeNode {
      val: number;
      left: TreeNode | null;
      right: TreeNode | null;
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
      }
    }

    function isSubStructure(A: TreeNode | null, B: TreeNode | null): boolean {
      if (A === null || B === null) {
        return false;
      }

      // 递归A的所有节点（先序遍历）：先找到匹配的根节点，再判断其子树是否匹配
      return dfs(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B);
    }

    // 递归判断A为根节点的子树是否包含B
    function dfs(A: TreeNode | null, B: TreeNode | null): boolean {
      if (B === null) {
        return true;
      }
      if (A === null) {
        return false;
      }

      return A.val === B.val && dfs(A.left, B.left) && dfs(A.right, B.right);
    }
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

1. 解法

    ```javascript
    /**
     * @param {number[]} prices
     * @return {number}
     */
    var maxProfit = function (prices) {
      // 动态规划
      let minPrice = prices[0] || 0;    // 或 = Number.MAX_VALUE;
      let maxProfit = 0;
      for (let price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
      }
      return maxProfit;
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

    ```javascript
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

    ```javascript
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

    ```javascript
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    var minSubArrayLen = function (target, nums) {
      let result = Number.MAX_SAFE_INTEGER;

      for (let i = 0, j = 0, sum = 0; i < nums.length; i++) {
        sum += nums[i];
        while (sum >= target) {
          result = Math.min(i - j + 1, result);
          sum -= nums[j];
          j++;
        }
      }

      return result === Number.MAX_SAFE_INTEGER ? 0 : result;
    };
    ```
2. 解法二

    暴力解法，O(n^2)，已超时。

    ```javascript
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

    ```javascript
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

    ```javascript
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

### 螺旋矩阵 II
todo

给你一个正整数 `n` ，生成一个包含 `1` 到 `n2` 所有元素，且元素按顺时针顺序螺旋排列的 `n x n` 正方形矩阵 `matrix` 。

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

    ```javascript
    /**
     * @param {number} n
     * @return {number[][]}
     */
    var generateMatrix = function(n) {

    };
    ```

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

    ```javascript
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

    ```javascript
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

    哈希表，为了达到 O(n)，仅对最小的数字进行累加计数操作。

    ```javasciprt
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var longestConsecutive = function (nums) {
      // 去除相同的项
      const set = new Set(nums);

      let longestLen = 0;

      for (const i of set) {
        // 为了保证 O(n) 所以只处理连续数字中最小的
        if (!set.has(i - 1)) {
          let currentLen = 1;
          let currentNum = i;
          while (set.has(currentNum + 1)) {
            currentLen += 1;
            currentNum += 1;
          }
          longestLen = Math.max(longestLen, currentLen);
        }
      }

      return longestLen;
    };
    ```
2. 解法二

    哈希表，仅遍历一次，哈希表key代表数字、value代表该key数字连续长度。

    ```javascript
    var longestConsecutive = function (nums) {
      // 把连续次数存放在哈希表（key：数字；value：连续长度）
      let hash = new Map();
      let longestLen = 0;

      for (let i of nums) {
        let num = i;
        // 相同数字仅处理一次
        if (!hash.has(num)) {
          // 前后一个数字是否有值
          let left = hash.get(num - 1) || 0;
          let right = hash.get(num + 1) || 0;

          let currentLen = 1 + left + right;
          longestLen = Math.max(currentLen, longestLen);

          hash.set(num, currentLen);
          // 同步更新2端边界
          hash.set(num - left, currentLen);
          hash.set(num + right, currentLen);
        }
      }

      return longestLen;
    };
    ```

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

    ```javascript
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
2. 解法二

    暴力解法，O(n^2)，已超时。

    ```javascript
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
- `-10 ** 5 <= nums[i] <= 10 ** 5`

1. 解法一

    双指针，O(n^2)。关键在去除重复答案。

    ```javascript
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    function threeSum(nums) {
      // 先排序，因为去重和算法逻辑需要
      nums.sort((a, b) => a - b);

      const resultArr = [];

      for (let left = 0; left < nums.length; left++) {
        if (nums[left] > 0) {
          return resultArr; // nums经过排序后，只要nums[left]>0, 此后的nums[left] + nums[middle] + nums[right]均大于0,可以提前终止循环。
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
            resultArr.push([nums[left], nums[middle], nums[right]]);

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
      return resultArr;
    }
    ```

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

    ```javascript
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
2. 解法二

    暴力解法，O(n^2) + 嵌套的判断无重复的时间复杂度。

    1. 利用`Set`

        ``javascript
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

        ```javascript
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
