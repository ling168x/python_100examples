"""
问题描述
给定一个字符串（以字符数组的形式）和一个偏移量，根据偏移量原地从左向右旋转字符串。

问题示例
输入str="abcdefg"，offset=3，输出"efgabcd"。
输入str="abcdefg"，offset=0，输出"abcdefg"。
输入str="abcdefg"，offset=1，输出"gabcdef"。
输入str="abcdefg"，offset=2，输出"fgabcde"。
"""

# my code
class strOffset:
	def offset(self, A, off):
		B = list(A)
		a = B[-off:]
		b = B[:-off]
		c = a+b
		print('输入str="%s"，offset=%d，输出"%s"'%(A, off, "".join(c)))

if __name__ == '__main__':
    s = strOffset()
    A = "abcdefg"
    s.offset(A,0) 
    s.offset(A,1) 
    s.offset(A,2) 
    s.offset(A,3)


# book example
class Solution:
	def rotateString(self, s, offset):
		if len(s) > 0:
			offset = offset % len(s)
		temp = (s + s)[len(s) - offset : 2 * len(s) - offset]
		for i in range(len(temp)):
			s[i] = temp[i]

if __name__ == '__main__':
	s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	offset = 3
	solution = Solution()
	solution.rotateString(s,offset)
	print('输入：s = ',['a', 'b', 'c', 'd', 'e', 'f', 'g'],'','offset = ',offset)
	print('输出：s =',s)