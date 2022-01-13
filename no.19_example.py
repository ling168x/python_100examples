"""
问题描述
找出无限正整数数列1，2，…中的第n个数位。

问题示例
输入11，输出0，表示数字序列1，2，…中的第11位是0
"""
s = ''
for i in range(1,12):
    s += '%s'%i
print(s)




# class Solution:
#     """
#     参数n为整数
#     返回整数
#     """
#     def findNthDigit(self, n):
#         # 初始化一位数的个数为9，从1开始
#         length = 1
#         count = 9
#         start = 1
#         while n > length * count:
#             # 以此类推二位数的个数为90，从10开始
#             n -= length * count
#             length += 1
#             count *= 10
#             start *= 10
#         # 找到第n位数所在的整数start 
#         start += (n - 1) // length
#         return int(str(start)[(n - 1) % length])
#主函数
# if __name__ == '__main__':
    # s = Solution()
    # n = 105
    # print("输入为：",n)
    # print("输出为：",s.findNthDigit(n))