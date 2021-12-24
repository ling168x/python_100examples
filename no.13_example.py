"""
问题描述
给定一系列描述函数进入和退出的时间，问每个函数的运行时间是多少。

问题示例
输入s=["F1Enter10"，"F2Enter18"，"F2Exit19"，"F1Exit20"]，
则输出["F1|10"，"F2|1"]，
即F1从10时刻进入，20时刻退出，运行时长为10，
F2从18时刻进入，19时刻退出，运行时长为1。

输入s=["F1Enter10"，"F1Exit18"，"F1Enter19"，"F1Exit20"]，
则输出["F1|9"]，
即F1从10时刻进入，18时刻退出；又从19时刻进入，20时刻退出，总运行时长为9。
"""

# my code
class RunTime:
    def runTime(self, s):

        enter_list = []
        exit_list = []

        for i in s:
            if "Enter" in i:
                enter_list.append(i.split("Enter"))
            if "Exit" in i:
                exit_list.append(i.split("Exit"))
        
        time = {}

        for i in enter_list:
            time["%s"%i[0]] = 0

        for i in enter_list:
            for j in exit_list:
                if i[0] == j[0]:
                    time["%s"%i[0]] += abs(int(i[1])-int(j[1]))
                    exit_list.remove(j)
                    break
        return time


# book example
class Solution:
    # @parm s 输入列表
    # @return  列表 对应函数运行时间列表
    def getRuntime(self, a):
        map={}
        for i in a:
            count = 0
            while not i[count] == ' ':
                count = count + 1
            fun = i[0 : count]
            if i[count+2] == 'n':
                count = count + 7
                v = int(i[count:len(i)])
                if fun in map.keys():
                    map[fun] = v - map[fun]
                else:
                    map[fun] = v
            else:
                count = count + 6
                v = int(i[count:len(i)])
                map[fun] = v - map[fun]
        res=[]
        for i in map:
            res.append(i)
        res.sort()
        for i in range(0,len(res)):
            res[i] = res[i] + '|' + str(map[res[i]])
        return res



if __name__ == '__main__':
    s = ["F1Enter10", "F1Exit18", "F1Enter19", "F1Exit20"]
    # s = ["F1Enter10", "F2Enter18", "F2Exit19", "F1Exit20"]
    r = RunTime()
    time = r.runTime(s)
    print('输入：', s)
    print('输出：',["%s|%d"%(i,time[i]) for i in time])

    s1 = ["F1 Enter 10","F2 Enter 18","F2 Exit 19","F1 Exit 20"]
    solution = Solution()
    print('输入：', s1)
    print('输出：',solution.getRuntime(s1))




