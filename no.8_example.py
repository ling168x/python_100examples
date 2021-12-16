"""
问题描述
给定一个表示勒索信内容的字符串和另一个表示杂志内容字符串，
写一个方法判断能否通过剪下杂志中的内容构造出这封勒索信，
若可以，返回True，否则返回False。
注：杂志字符串中的每一个字符仅能在勒索信中使用一次。

问题示例
输入ransom Note="aa"，magazine="aab"，
输出True，勒索信的内容可以从杂志内容剪辑而来。
"""

# my code
class findRansom:
	def searchRansom(self, ransomNote, magazine):
		return ransomNote in magazine

if __name__ == '__main__':
	s = findRansom()
	ransomNote="aa"
	magazine="aab"
	print(s.searchRansom(ransomNote, magazine))


# book example
class Solution:
	# @parm ransomNote
	# @parm magazine
	# @return 布尔值
	def canConstruct(self, ransomNote, magazine):
		arr = [0] * 26
		for c in magazine:
			arr[ord(c)-ord('a')] += 1
		for c in ransomNote:
			arr[ord(c)-ord('a')] -= 1
			if arr[ord(c)-ord('a')] < 0:
				return False
		return True

if __name__ == '__main__':
	s = Solution()
	ransomNote="aa"
	magazine="faab"
	print(s.canConstruct(ransomNote, magazine))