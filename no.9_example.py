"""
问题描述
给定一个数组a[]，其中除了2个数，其他均出现2次，请找到不重复的2个数并返回。

问题示例
给出a=[1，2，5，5，6，6]，返回[1，2]，除1和2外其他数都出现了2次，因此返回[1，2]。
给出a=[3，2，7，5，5，7]，返回[2，3]，除了2和3其他数都出现了2次，因此返回[2，3]。
"""

# my code
class Example:
	def countOne(self, a):
		result = []
		for i in a:
			if a.count(i) < 2:
				result.append(i)
		retsult = result.sort()
		return result

if __name__ == '__main__':
	example = Example()
	a = [1, 2, 5, 5, 6, 6]
	b = [3, 2, 7, 5, 5, 7]
	print('输入：', a)
	print('输出：', example.countOne(a))
	print('输入：', b)
	print('输出：', example.countOne(b))


# book example
class Solution:
	# @parm arr  输入待检查列表
	# @return 返回没有重复的两个值的列表
	# 位运算
	def theTwoNumbers(self, a):
		ans = [0, 0]
		for i in a:
			ans[0] = ans[0]^i 
		c = 1
		while c & ans[0] != c:
			c = c<<1
		for i in a:
			if i & c == c:
				ans[1] = ans[1]^i
		ans[0] = ans[0] ^ ans[1]
		return ans 

if __name__ == '__main__':
	s = Solution()
	arr = [1, 2, 5, 1]
	print('输入：', arr)
	print('输出：', s.theTwoNumbers(arr))