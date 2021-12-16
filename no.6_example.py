"""
问题描述
两个不重复的数组nums1和nums2，其中nums1是nums2的子集。
在nums2的相应位置找到nums1所有元素的下一个更大数字。
nums1中的数字x的下一个更大数字是nums2中x右边第1个更大的数字。
如果它不存在，则为此数字输出-1。
nums1和nums2中的所有数字都是唯一的，nums1和nums2的长度不超过1000。

问题示例
输入nums1=[4，1，2]，nums2=[1，3，4，2]，
输出[-1，3，-1]。
对于第1个数组中的数字4，在第2个数组中找不到下一个更大的数字，因此输出-1；
对于第1个数组中的数字1，第2个数组中的下一个更大数字是3；
对于第1个数组中的数字2，第2个数组中没有下一个更大的数字，因此输出-1。
"""

# my code

class searchNext:
	def searchNextNum(self, nums1, nums2,):
		result = []
		for i in range(len(nums1)):
			index = nums2.index(nums1[i])
			if index+1 in range(len(nums2)):
				if nums2[index+1] > nums2[index]:
					result.append(nums2[index+1])
				else:
					result.append(-1)
			else:
				result.append(-1)
		return result

if __name__ == '__main__':
	search = searchNext()
	nums1 = [4, 1, 2]
	nums2 = [1, 3, 4, 2]
	result = search.searchNextNum(nums1, nums2)
	print('输入：',nums1,' ',nums2)
	print('输出：',result)


# book example
class Solution:
	# @parm nums1: 整数数组
	# @parm nums2: 整数数组
	# 返回整数数组
	def nextGreateElement(self, nums1, nums2):
		answer = {}
		stack = []
		for x in nums2:
			while stack and stack[-1] < x:
				answer[stack[-1]] = x 
				del stack[-1]
			stack.append(x)
		for x in stack:
			answer[x] = -1
		return [answer[x] for x in nums1]

if __name__ == '__main__':
	s = Solution()
	nums1 = [4, 1, 2]
	nums2 = [1, 3, 4, 2]
	print('输入：',nums1,' ',nums2)
	print('输出：',s.nextGreateElement(nums1, nums2))