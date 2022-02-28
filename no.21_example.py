"""
问题描述
有n个人，编号分别为1，2，…，n，n为偶数。选择其中的一半人，有C（n，n/2）种组合方式，
每一种组合方式按照编号从小到大排序，再将已排序的组合方式按照字典序排序，求第k种组合方式。
字典序的定义：首先比较两个字符串的长度，长度小的字典序更小，
如果长度相同，则从字符串左边开始逐位比较，找到第一位不同的字符，对应字符小的字符串，字典序更小。


问题示例
给出n=2，k=1，返回[1]，所有组合方式按照字典序排序：[1]，[2]。给出n=4，k=2，返回[1，3]，
所有组合方式按照字典序排序[1，2]，[1，3]，[1，4]，[2，3]，[2，4]，[3，4]。
"""

# my code
class Findtarget:
	def findTarget(self, n, k):
		num_list = []
		if n >2:
			for i in range(1,n+1):
				for j in range(i+1,n+1):
					num_list.append([i,j])
			return num_list[k-1]
		else:
			return [[i] for i in range(1,n+1)][k-1]


# book example
# class Solution:
	
# 	def 


if __name__ == "__main__":
	f = Findtarget()
	n = 8
	k = 11
	print("返回",f.findTarget(n, k)) 


