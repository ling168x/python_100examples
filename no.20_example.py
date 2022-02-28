"""
问题描述
给定两个只包含小写字母的字符串s和t。
字符串t由随机打乱字符顺序的字符串s在随机位置添加一个字符生成。
找出在t中添加的字符。


问题示例
例如，输入s ="abcd"，t="abcde"，输出e，e是加入的字符。
"""

# my code
class Findstr:
	def serachStr(self, s, t):
		t = [i for i in t]
		for i in s:
			if i in t:
				t.remove(i)
		return 	"".join(t)


# book example
class Sultion:
	# @parm s 字符串
	# @parm t 字符串
	# @return 字符串
	def findThedifference(self, s, t):
		flag = 0
		for i in range(len(s)):
			flag += (ord(t[i]) - ord(s[i]))
		flag += ord(t[-1])
		return chr(flag)


if __name__ == '__main__':
	f = Findstr()
	s = "abcd"
	t="abdacddce"
	print("加入字符:",f.serachStr(s, t))

	S = Sultion()
	s = "abcd"
	t="abcddd"
	print("加入字符:",S.findThedifference(s, t))