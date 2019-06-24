import matplotlib.pyplot as plt

def showChart(titleList = [], numList = []):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.bar(range(len(numList)), numList)
    plt.xticks(range(len(titleList)), range(len(titleList)))
    plt.show()
