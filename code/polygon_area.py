'''
P是多边形端点坐标的列表。
给定端点坐标，该函数可以计算任意简单多边形的面积。
不仅凸多边形，还有各种奇形怪状的凹多边形，都可以用该方法(本质上是格林公式)求出面积
https://www.zhihu.com/question/53259589/answer/134574326
'''

def polygon_area(P):
    n = len(P)
    P.append(P[0])
    S = 0
    for i in range(0, n):
        x1, y1 = P[i]
        x2, y2 = P[i + 1]
        S = S + (x1 + x2) * (y2 - y1)
    return 0.5 * abs(S)


triangle = [(0, 0), (2, 0), (1, 1)]
polygon_area(triangle)
