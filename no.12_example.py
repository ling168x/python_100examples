"""
问题描述
给出2个数组，求它们的点积。

问题示例
输入为A=[1，1，1]和B=[2，2，2]，输出为6，1*2+1*2+1*2=6。
输入为A=[3，2]和B=[2，3，3]，输出为-1，没有点积。
"""

#  my code
class dotProduct:
    def returnProduct(self, a, b):
        product = 0
        if len(a) == 0 or len(b) == 0 or len(a) != len(b):
            return -1
        else:
            for i in range(len(a)):
                product += a[i] * b[i]
        return product

# book example   一样


if __name__ == '__main__':
    A = [1, 1, 1]
    B = [2, 2, 2]
    C = [3, 2]
    D = [2, 3, 3]

    r = dotProduct()
    print('输入：', A, B)
    print('输出：', r.returnProduct(A, B))
    print('输入：', C, D)
    print('输出：', r.returnProduct(C, D))