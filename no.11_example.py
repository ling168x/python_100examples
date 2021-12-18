"""
问题描述
给出一个数组，在数组中找到2个数，使得它们的和最接近但不超过目标值，返回它们的和。

问题示例
输入target=15，array=[1, 3, 5, 11, 7]，输出14，11+3=14。
输入target=16，array=[1, 3, 5, 11, 7]，输出16，11+5=16。
"""


# my code
class Target:
    def findTarget(self, array, target):
        array.sort()
        for i in range(len(array)):
            if array[-(i + 1)] > target:
                continue
            else:
                for j in range(len(array) - i - 1):
                    if array[:len(array) - i - 1][-(j + 1)] + array[-(i + 1)] > target:
                        continue
                    else:
                        return array[-(i + 1)], array[:len(array) - i - 1][-(j + 1)]


# book example
class Solution:
    # @parm array:输入列表
    # @parm target:目标值
    # @return 整数
    def closestTargetValue(self, target, array):
        n = len(array)
        if n < 2:
            return -1
        array.sort()
        diff = 0x7fffffff
        left = 0
        right = n - 1
        while left < right:
            if array[left] + array[right] > target:
                right -= 1
            else:
                diff = min(diff, target - array[left] - array[right])
                left += 1
        if diff == 0x7fffffff:
            return -1
        else:
            return target - diff


if __name__ == '__main__':
    t = Target()
    # array = [3, 5, 11, 7, 14]
    array = [1, 3, 5, 11, 7]
    target = 15
    a, b = t.findTarget(array, target)
    print('输入：', array)
    print(a)
    print(b)
    print('最近可得到的值：', a + b)

    s = Solution()
    print('输入：', array)
    print('最近可得到的值：', s.closestTargetValue(target, array))
