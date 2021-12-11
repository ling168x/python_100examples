"""
问题描述
合并两个升序的整数数组A和B，形成一个新的数组，新数组也要有序。

问题示例
输入A=[1]，B=[1]，输出[1，1]，返回合并后的数组。输入A=[1，2，3，4]，B=[2，4，5，6]
输出[1，2，2，3，4，4，5，6]，返回合并所有元素后的数组。
"""

# my code
class ListSort():
    def list_sort(self,a,b):
        c = a+b
        c.sort()
        return c

if __name__ == '__main__':
    # A = [1, 2, 3, 4]
    # B = [2, 4, 5, 6]
    A = [1, 4]
    B = [1, 2, 3, 4]
    L = ListSort()
    print(L.list_sort(A,B))


# book example
class Solution:
    def mergeSortedArray(self, A, B):
        i,j = 0,0
        C = []
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        return C 

if __name__ == '__main__':
    A = [1,4]
    B = [1,2,3]
    D = [1,2,3,4]
    E = [2,4,5,6]
    solution = Solution()
    print('输入：',A ,B)
    print('输出：',solution.mergeSortedArray(A, B))
    print('输入：',D ,E)
    print('输出：',solution.mergeSortedArray(D ,E))