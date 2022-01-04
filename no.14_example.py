"""
问题描述
给定一个包含若干个区间的List数组，长度是1000，如[500，1500]、[2100，3100]。
给定一个number，判断number是否在这些区间内，返回True或False。

问题示例
输入是List=[[100，1100]，[1000，2000]，[5500，6500]]和number=6000，输出是True，
因为6000在区间[5500，6500]。
输入是List=[[100，1100]，[2000，3000]]和number=3500，输出是False，
因为3500不在List的任何一个区间中。
"""

# my code
class numberINlist:
	def inlist(self, number, num_list):
		for i in num_list:
			if number in range(i[0],i[1]+1):
				return True
		return False

# book example
class Solution:
	# @parm List 区间列表
	# @Parm number  待查数字
	# @return  字符串 True 或 False

	def isInterval(self, intervalList, number):
		high = len(intervalList) - 1
		low = 0
		while high >= low:
			if 0 < (number - intervalList[(high + low) // 2][0]) <= 1000:
				return "True"
			elif 1000 < number - intervalList[(high + low) // 2][0]:
				low = (high + low) // 2 + 1
			elif 0 >  number - intervalList[(high + low) // 2][0]:
				high = (high + low) // 2 - 1
		return "False"


if __name__ == '__main__':
	n = numberINlist()
	number = 1100
	num_list = [[100, 1100], [1000, 2000], [5500, 6500]]
	print('输入：', num_list,' 数字：',number)
	print('输出：',n.inlist(number, num_list))
	number = 3500
	num_list = [[100, 1100], [1000, 2000]]
	print('输入：', num_list,' 数字：',number)
	print('输出：',n.inlist(number, num_list))

	s = Solution()
	number = 3500
	num_list = [[100, 1100], [1000, 2000]]
	print('输入：', num_list,' 数字：',number)
	print('输出：',s.isInterval(num_list, number))
