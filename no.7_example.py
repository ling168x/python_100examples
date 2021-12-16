"""
问题描述
计算字符串中的单词数，其中一个单词定义为不含空格的连续字符串。

问题示例
输入"Hello，my name is John"，输出5。
"""
# my code
import re

class reStr:
	def returnStr(self, string):
		return len(re.findall(r'\w*[^\s]',string))

if __name__ == '__main__':
	restr = reStr()
	string = "Hello, my name is John"
	print('输入：',string)
	print('输出：',restr.returnStr(string))

# book example
class Solution:
	# @parm s:字符串
	# @return 整数
	def countSegments(self, s):
		res = 0
		for i in range(len(s)):
			if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
				res += 1
		return res

if __name__ == '__main__':
	s = Solution()
	string = "Hello, my name is John"
	print('输入：',string)
	print('输出：',s.countSegments(string))