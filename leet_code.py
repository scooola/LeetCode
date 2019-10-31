#-*- coding:utf-8 -*-


# 1.两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 执行用时 :64 ms, 在所有 python3 提交中击败了93.62%的用户
# 内存消耗 :15.5 MB, 在所有 python3 提交中击败了5.05%的用户

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         num_dict = {}
#         for index, value in enumerate(nums):
#             num_dict[value] = index
#
#         for index, value in enumerate(nums):
#             v = num_dict.get(target-value)
#             if v is not None and v != index:
#                 return[index, v]
#
#
# s = Solution()
# nums = [3, 2, 4]
# target = 6
# print(s.twoSum(nums, target))


# 2.两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 执行用时 :72 ms, 在所有 python3 提交中击败了98.47%的用户
# 内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.06%的用户

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         base = ListNode(0)
#         tmp = base
#         curry = 0  # 两数相加，大于10时的十位，即进位，需在下一位加上该值
#         while l1 and l2:
#             sum = l1.val + l2.val + curry
#             index = sum % 10
#             tmp.next = ListNode(index)
#             curry = sum // 10
#             l1 = l1.next
#             l2 = l2.next
#             tmp = tmp.next
#
#         while l1:
#             sum = l1.val + curry
#             index = sum % 10
#             tmp.next = ListNode(index)
#             curry = sum // 10
#             l1 = l1.next
#             tmp = tmp.next
#
#         while l2:
#             sum = l2.val + curry
#             index = sum % 10
#             tmp.next = ListNode(index)
#             curry = sum // 10
#             l2 = l2.next
#             tmp = tmp.next
#         if(sum >= 10):
#             tmp.next = ListNode(sum//10)
#         base = base.next
#         return base
#
#
# s = Solution()
# # l1 = 342
# l1 = ListNode(2)
# l1_next = l1.next = ListNode(4)
# l1_next.next = ListNode(3)
#
# # l2 = 465
# l2 = ListNode(5)
# l2_next = l2.next = ListNode(6)
# l2_next.next = ListNode(4)
# # l1 + l2 = 807
# ret = s.addTwoNumbers(l1, l2)
# while ret:
#     print("ret:", ret.val)
#     ret = ret.next


# 20.有效的括号-栈
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true

# 执行用时 :40 ms, 在所有 python3 提交中击败了91.98%的用户
# 内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.51%的用户

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         for i in s:
#             if(len(stack) <= 0):
#                 stack.append(i)
#                 continue
#             last = stack.pop()
#             # 配对成功
#             if (last == '(' and i == ')' or
#                 last == '[' and i == ']' or
#                 last == '{' and i == '}'):
#                     print(last, " and ", i, "success!")
#             # 配对上一个符号和当前符号一次入栈
#             else:
#                 stack.append(last)
#                 stack.append(i)
#
#         if(len(stack) > 0):
#             return False
#         return True
#
# str_test = "([)]"
# s = Solution()
# print(s.isValid(str_test))

# 1021.删除最外层的括号-栈
# 有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
#
# 如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
#
# 给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
#
# 对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。
#
#
#
# 示例 1：
#
# 输入："(()())(())"
# 输出："()()()"
# 解释：
# 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
# 示例 2：
#
# 输入："(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：
# 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
# 删除每隔部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
# 示例 3：
#
# 输入："()()"
# 输出：""
# 解释：
# 输入字符串为 "()()"，原语化分解得到 "()" + "()"，
# 删除每个部分中的最外层括号后得到 "" + "" = ""。
#  
#
# 提示：
#
# S.length <= 10000
# S[i] 为 "(" 或 ")"
# S 是一个有效括号字符串

# 解析： https://blog.csdn.net/qq_17550379/article/details/89103739  

# 执行用时 :44 ms, 在所有 python3 提交中击败了95.36%的用户
# 内存消耗 :13.6 MB, 在所有 python3 提交中击败了5.61%的用户

# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         stack = []
#         ret_str = ''
#         for i in S:
#             if i == '(':
#                 if(len(stack) >= 1):
#                     ret_str += i
#                 stack.append(i)
#             else:  # i == ')'
#                 if(len(stack) > 1):
#                     ret_str += i
#                 stack.pop()
#         return ret_str
#
#
# s = Solution()
# s_test = "(()())(())(()(()))"
# print(s.removeOuterParentheses(s_test))


# 1047.删除字符串中的所有相邻重复项-栈
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
#
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
#
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
# 示例：
#
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#  
# 提示：
#
# 1 <= S.length <= 20000
# S 仅由小写英文字母组成。

# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         stack = []
#         for i in S:
#             if stack and stack[-1] == i:
#                 stack.pop()
#             else:
#                 stack.append(i)
#
#         ret_str = ''.join(stack)
#         return ret_str
#
# s = Solution()
# print(s.removeDuplicates("abbaca"))


# 71. 简化路径-栈
# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
#
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
#
# 请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
# 示例 1：
#
# 输入："/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。
# 示例 2：
#
# 输入："/../"
# 输出："/"
# 解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
# 示例 3：
#
# 输入："/home//foo/"
# 输出："/home/foo"
# 解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
# 示例 4：
#
# 输入："/a/./b/../../c/"
# 输出："/c"
# 示例 5：
#
# 输入："/a/../../b/../c//.//"
# 输出："/c"
# 示例 6：
#
# 输入："/a//b////c/d//././/.."
# 输出："/a/b/c"

# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack = []
#         path_list = path.split('/')
#         for i in path_list:
#             if len(stack) > 0 and i == "..":
#                 stack.pop()
#             elif i != '.' and i != '' and i != '..':
#                 stack.append(i)
#         return '/' + '/'.join(stack)
#
#
# s = Solution()
# print(s.simplifyPath("/../"))


# 94.二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]

# 执行用时 :44 ms, 在所有 python3 提交中击败了75.75%的用户
# 内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.32%的用户

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def inorderTraversal(self, root: TreeNode):
#         if not root:
#             return []
#         ret, stack = [], []
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             if not stack:
#                 return ret
#             node = stack.pop()
#             if node.val is not None:
#                 ret.append(node.val)
#             root = node.right
#         return ret
#
#
# t = TreeNode(1)
# t.left = None
# t.right = TreeNode(2)
# t2 = t.right
# t2.left = TreeNode(3)
# t2.right = TreeNode(None)
# t3 = t2.left
# t3.left = None
# t3.right = None
# s = Solution()
# ret = s.inorderTraversal(t)
# print(ret)


# 215.数组中的第K个最大元素-堆
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# import heapq
#
#
# class Solution:
#     def findKthLargest(self, nums: [int], k: int) -> int:
#         heap = []
#         for num in nums[:k]:
#             heapq.heappush(heap, num)
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, num)
#         return heap[0]
#
#
# nums = [3, 2, 1, 5, 6, 4]
# s = Solution()
# ret = s.findKthLargest(nums, 2)
# print(ret)


# 264.丑数II-堆
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  
#
# 1 是丑数。
# n 不超过1690。

# 因为丑数是2, 3, 5的倍数，我们不断把它们的倍数压入栈中，再按顺序弹出！
# 时间复杂度：nlogn
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         import heapq
#         heap = []
#         heapq.heappush(heap, 1)
#         for _ in range(n):
#             ret = heapq.heappop(heap)
#             while heap and ret == heap[0]:
#                 ret = heapq.heappop(heap)
#             a, b, c = ret*2, ret*3, ret*5
#             for i in [a, b, c]:
#                 heapq.heappush(heap, i)
#         return ret
#
#
# s = Solution()
# ret = s.nthUglyNumber(9)
# print(ret)


# 313.超级丑数-堆
# 编写一段程序来查找第 n 个超级丑数。
#
# 超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
#
# 示例:
#
# 输入: n = 12, primes = [2,7,13,19]
# 输出: 32
# 解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
# 说明:
#
# 1 是任何给定 primes 的超级丑数。
#  给定 primes 中的数字以升序排列。
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
# 第 n 个超级丑数确保在 32 位有符整数范围内。

# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: [int]) -> int:
#         import heapq
#         heap = []
#         heapq.heappush(heap, 1)
#         for _ in range(n):
#             ret = heapq.heappop(heap)
#             while heap and ret == heap[0]:
#                 ret = heapq.heappop(heap)
#             for i in primes:
#                 heapq.heappush(heap, ret*i)
#         return ret
#
#
# s = Solution()
# primes = [2, 7, 13, 19]
# ret = s.nthSuperUglyNumber(12, primes)
# print(ret)


# 347.前 K 个高频元素-堆
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

# 自己的方法
# class Solution:
#     def topKFrequent(self, nums, k):
#         num_dict = {}
#         for i in nums:
#             if i not in num_dict:
#                 num_dict[i] = 1
#                 continue
#             num_dict[i] += 1
#         ret = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
#         ret = ret[:k]
#         ret = [x[0] for x in ret]
#         return ret


# 用堆
# class Solution:
#     def topKFrequent(self, nums, k):
#         import collections
#         import heapq
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         count = collections.Counter(nums)
#         return heapq.nlargest(k, count.keys(), key=count.get)
#
#
# s = Solution()
# nums = [1, 1, 1, 1, 2, 2, 3]
# ret = s.topKFrequent(nums, 2)
# print(ret)
