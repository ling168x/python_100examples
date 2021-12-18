"""
问题描述
给定两个字符串s和t，每次可以任意交换s的奇数位或偶数位上的字符，
即奇数位上的字符能与其他奇数位的字符互换，偶数位上的字符也能与其他偶数位的字符互换，
问能否经过若干次交换，使s变成t。

问题示例
输入为s="abcd"，t="cdab"，输出是"Yes"，
第1次a与c交换，第2次b与d交换。
输入s="abcd"，t="bcda"，输出是"No"，
无论如何交换，都无法得到bcda。
"""

# my code
class strEquel:
	def str_equel(self, s, t):
		s_even = [i for i in s[::2]]
		s_odd = [i for i in s[1::2]]
		t_even = [i for i in t[::2]]
		t_odd = [i for i in t[1::2]]
		s_even.sort()
		s_odd.sort()
		t_even.sort()
		t_odd.sort()
		if s_even == t_even and s_odd == t_odd:
			return "yes"
		else:
			return "no"

if __name__ == "__main__":
	seq = strEquel()
	s="abcd"
	t="bcda"
	print('输入：',s,' ',t)
	print('输出：',seq.str_equel(s,t))


# book example
class Solution:
	# @parm s 字符串
	# @parm t 字符串
	# @return 字符串,表示能否根据规则转换
	def isTwin(self, s, t):
		if len(s) != len(t):
			return "no"
		oddS = []
		evenS = []
		oddT = []
		evenT = []
		for i in range(len(s)):
			if i&1:
				oddS.append(s[i])
				oddT.append(t[i])
			else:
				evenS.append(s[i])
				evenT.append(t[i])
		oddS.sort()
		evenS.sort()
		oddT.sort()
		evenT.sort()
		for i in range(len(oddS)):
			if oddS[i] != oddT[i]:
				return "no"
		for i in range(len(evenS)):
			if evenS[i] != evenT[i]:
				return "no"
		return "yes"


if __name__ == "__main__":
	s = "abcd"
	t = "cdab"
	solution = Solution()
	print('s与t分别是：',s ,t)
	print('是否为双胞胎：',solution.isTwin(s, t))