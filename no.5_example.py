"""
问题描述
给定一个排序的整数数组（升序）和一个要查找的目标整数target，
查找到target第1次出现的下标（从0开始），
如果target不存在于数组中，返回-1。

问题示例
输入数组[1，4，4，5，7，7，8，9，9，10]和目标整数1，
输出其所在的位置为0，即第1次出现在第0个位置。

输入数组[1，2，3，3，4，5，10]和目标整数3，
输出2，即第1次出现在第2个位置。

输入数组[1，2，3，3，4，5，10]和目标整数6，
输出-1，即没有出现过6，返回-1。
"""

# my code
class Target:
	def findTarget(self, A, target):
		if target not in A:
			return -1
		else:
			return A.index(target)

if __name__ == '__main__':
	t = Target()
	A = [1,4,4,5,7,7,8,9,9,10]
	target = 1
	print('输入数组：',A,'目标整数: ',target)
	print('输出：',t.findTarget(A, target))
	B = [1,2,3,3,4,5,10]
	target = 3
	print('输入数组：',B,' 目标整数',target)
	print('输出：',t.findTarget(B, target))
	C = [1,2,3,3,4,5,10]
	target = 6
	print('输入数组：', C, ' 目标整数', target)
	print('输出：',t.findTarget(C, target))
	
# book example 二分法
class Solution:
	# @parm  nums:整数数组
	# @parm  target:目标数字
	# @return  目标数字的第1个位置，从0开始
	def binarySearch(self, nums, target):
		return self.search(nums, 0, len(nums)-1, target)

	def search(self, nums, start, end, target):
		if start > end:
			return -1
		mid = (start + end)//2
		if nums[mid] > target:
			return search(nums, start, mid, target)
		if nums[mid] == target:
			return mid
		if nums[mid] < target:
			return search(nums, mid, end, target)

if __name__ == '__main__':
	my_solution = Solution()
	nums = [1,2,3,4,5,6]
	target = 3
	targetIndex = my_solution.binarySearch(nums, target)
	print('输入：nums = ',nums,' ','target = ',target)
	print('输出：',targetIndex)