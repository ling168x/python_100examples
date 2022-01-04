"""
问题描述
一维棋盘，起点在棋盘的最左侧，终点在棋盘的最右侧，棋盘上有几个位置和其他位置相连，
如果A与B相连，但连接是单向的，即当棋子落在位置A时，
可以选择不投骰子，直接移动棋子从A到B，但不能从B移动到A。
给定这个棋盘的长度（length）和位置的相连情况（connections），
用六面的骰子（点数1~6），问最少需要投几次才能到达终点。

问题示例
输入length=10和connections=[[2，10]]，
输出为1，可以0->2（投骰子），2->10（直接相连）。
输入length=15和connections=[[2，8]，[6，9]]，
输出为2，因为可以0->6（投骰子），6->9（直接相连），9->15（投骰子）。
"""

# my code
class serachCount:
	def onCount(self, lenght, connect):
		count = 0
		net = 0
		while lenght > net:
			net_list = []
			net += 6
			for i in connect:
				if net in range(i[0], i[1]+1):
					net_list.append(i[1])
			if net_list:
				net = max(net_list)
			count += 1
		return count


# book example
class Solution:
	# @parm lenght  棋盘长度
	# @parm connections  跳点集合
	# @return 整数 最小步数

	def modernLudo(self, lenght, connections):
		ans = [i for i in range(lenght+1)]
		for i in range(lenght+1):
			for j in range(1, 7):
				if i - j >= 0:
					ans[i] = min(ans[i], ans[i-j]+1)
			for j in connections:
				if i == j[1]:
					ans[i] = min(ans[i], ans[j[0]])
		return ans[lenght]




if __name__ == '__main__':
	c = serachCount()
	lenght = 10
	connections = [[2, 10]]
	print(c.onCount(lenght,connections))
	
	lenght = 15
	connections = [[2, 8], [6, 9]]
	print(c.onCount(lenght,connections))

	s = Solution()
	print(s.modernLudo(lenght, connections))



