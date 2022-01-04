"""
问题描述
在x轴上分布着n个石子，用arr数组表示它们的位置。把这些石子移动
到1，3，5，7，2n-1或者2，4，6，8，2n。
也就是说，这些石子移动到从1开始连续的奇数位，或从2开始连续的偶数位上。
返回最少的移动次数。每次只可以移动1个石子，
只能把石子往左移动1个单位或往右移动1个单位。同一个位置不能同时有2个石子。

问题示例
[5，4，1]，只需要把4移动1步到3，所以输出是1。
arr=[1，6，7，8，9]，
最优的移动方案为把1移动到2，把6移动到4，把7移动到6，把9移动到10，
所以输出是5。
"""

# my code
class Case:
	"""
	1、排序
	2、根据原列表每个值创建对应的相邻的偶数或者奇数 diff 列表
	3、对比原列表需要移动步数，结果存入 result 列表中
	4、返回 result 列表中最小值

	"""
	def minCase(self, arr):
		arr.sort()
		result = []
		for i in arr:
			count = 0
			diff = [i+(arr.index(j)-arr.index(i))*2 for j in arr]
			for m in range(len(diff)):
				count += abs(diff[m] - arr[m])
			result.append(count)

		return min(result)


# book example
class Solution:
	# @parm arr 列表
	# @return 整数 最小移动次数

	def movingStones(self, arr):
		arr =  sorted(arr)
		even = 0
		odd = 0
		for i in range(len(arr)):
			odd += abs(arr[i] - (2*i+1))
			even += abs(arr[i] - (2*i+2))
		if odd < even:
			return odd
		return even


if __name__ == '__main__':
	c = Case()
	arr = [1, 6, 7, 8, 9]
	a = [5, 4, 1]
	print(c.minCase(arr))
	print(c.minCase(a))
	s = Solution()
	print(s.movingStones(arr))




