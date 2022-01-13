"""
问题描述
给定一个整数数组A。定义B[i]=A[0]*…*A[i-1]*A[i+1]*…*A[n-1]，
即B[i]为剔除A[i]元素之后所有数组元素之积，
计算数组B的时候请不要使用除法，输出数组B。

问题示例
输入A=[1，2，3]，输出[6，3，2]，
即B[0]=A[1]*A[2]=6；B[1]=A[0]*A[2]=3；B[2]=A[0]*A[1]=2。
输入A=[2，4，6]，
输出[24，12，8]。
"""

# my code
import copy
class Listmultiply:
	def multiply(self, A):
		result = []
		for i in A:
			a = A.copy()
			a.remove(i)
			a_multiply = 1
			for j in a:
				a_multiply *= j
			result.append(a_multiply)
		return result


# book example
class Solution:
	# @parm A 整数数组
	# @return B 整数数组
	def productExcldeItself(self, A):
		length, B = len(A), []
		f = [0 for _ in range(length+1)]
		f[length] = 1
		for i in range(length-1, 0, -1):
			f[i] = f[i+1] * A[i]
		tmp = 1
		for i in range(length):
			B.append(tmp * f[i+1])
			tmp *= A[i]
		return B


if __name__ == '__main__':
	m = Listmultiply()
	A = [1, 2, 3]
	print(m.multiply(A))
	B = [2, 4, 5]
	print(m.multiply(B))
	s = Solution()
	print(s.productExcldeItself(A))

