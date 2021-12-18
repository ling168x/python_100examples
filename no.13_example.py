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

s = ["F1Enter10", "F1Exit18", "F1Enter19", "F1Exit20"]
for i in s:
    if "Enter" in i:
        print(i.split("Enter"))
    if "Exit" in i:
        print(i.split("Exit"))