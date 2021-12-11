"""
问题描述
根据N名运动员得分，找到相对等级和获得最高分前3名的人，
分别获得金牌、银牌和铜牌。N是正整数，并且不超过10 000。
所有运动员的成绩都保证是独一无二的。

问题示例
输入[5，4，3，2，1]，
输出["Gold Medal"，"Silver Medal"，"Bronze Medal"，"4"，"5"]，
前3名运动员得分较高，根据得分依次获得金牌、银牌和铜牌。
对于后两名运动员，根据分数输出相对等级。
"""

# my code
import copy

class Meadl:
	def gradeMeadl(self, A):
		grade = ['Gold Medal','Silver Medal','Bronze Medal']
		if len(A)>3:
			grade = grade + ["%d"%i for i in range(4,len(A)+1)]
		B = A.copy()
		C = A.copy()
		B.sort()
		for i in range(len(B)):
			C[C.index(B[i])] = grade[i]
		return C

if __name__ == '__main__':
	meadl = Meadl()
	A = [5,9,7,85,1,4,22]
	print('输入：',A)
	print('输出：',meadl.gradeMeadl(A))
	

# book example
class Solution:
	def findRelativeRanks(self, nums):
		score = {}
		for i in range(len(nums)):
			score[nums[i]] = i
		sortedScore = sorted(nums, reverse=True)
		answer = [0] * len(nums)
		for i in range(len(sortedScore)):
			res = str(i + 1)
			if i == 0:
				res = 'Gold Medal'
			if i == 1:
				res = 'Silver Medal'
			if i == 2:
				res = 'Bronze Medal'
			answer[score[sortedScore[i]]] = res 
		return answer

if __name__ == '__main__':
	num = [5,44,13,21,10,192,54]
	s = Solution()
	print('输入：',num)
	print('输出：',s.findRelativeRanks(num))