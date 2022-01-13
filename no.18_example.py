"""
问题描述
给定一个单词列表，返回可以在键盘的一行上使用字母键输入的单词。
可以多次使用键盘中的一个字符，输入字符串仅包含字母表的字母。

问题示例
输入["Hello"，"Alaska"，"Dad"，"Peace"]，输出["Alaska"，"Dad"]，
即这两个单词可以在键盘的第3行输出。
"""

# my code
class Keyborad:
	def serachKey(self, serach, data):
		result = []
		for i in data:
			for m in serach:
				count = 0
				for j in i:
					if j.lower() not in m:
						count += 1
						break
				if count == 0:
					result.append(i)
					break
		return result


# book example 与 my code 一致

if __name__ == '__main__':
	serach = ['qwertyuiop', 'asdfghjkl','zxcvbnm']
	data = ["Hello", "Alaska", "Dad", "Peace"]
	k = Keyborad()
	print(k.serachKey(serach, data))
