"""
问题描述
反转一个只有3位数的整数

问题示例
输入number=123，输出321；输入number=900，输出9
"""

# my code
num = input('Enter three digits\n').strip()
new = list(num)
new.reverse()
for _ in range(3):
	if new[0] == "0":
		new.remove(new[0])
new = "".join(new)
print('输入number=%s，输出%s' % (num, new))

# book example
class Solution:
	def reverseInteger(self,number):
		h = int(number/100)
		t = int(number%100/10)
		z = int(number%10)
		return (100*z+10*t+h)

if __name__ == '__main__':
	solution = Solution()
	num = 123
	ans = solution.reverseInteger(num)
	print('输入：', num)
	print('输出：', ans)