# kd-tree（k-dimensional树的简称），是一种分割k维数据空间的数据结构。
# 主要应用于多维空间关键数据的搜索（如：范围搜索和最近邻搜索）。K-D树是二进制空间分割树的特殊的情况。

from collections import namedtuple
from math import sqrt
import numpy as np


class KDNode(object):
    def __init__(self, value, split, left, right):
        # value=[x,y]
        self.value = value
        self.split = split
        self.right = right
        self.left = left


class KDTree(object):
    def __init__(self, data):
        # data=[[x1,y1],[x2,y2]...,]
        # 维度
        k = len(data[0])

        def CreateNode(split, data_set):
            if not data_set:
                return None
            data_set.sort(key=lambda x: x[split])
            # 整除2
            split_pos = len(data_set) // 2
            median = data_set[split_pos]
            split_next = (split + 1) % k

            return KDNode(median, split, CreateNode(split_next, data_set[: split_pos]),
                          CreateNode(split_next, data_set[split_pos + 1:]))
        self.root = CreateNode(0, data)

    def search(self, root, x, count=1):
        nearest = []
        for i in range(count):
            nearest.append([-1, None])
        self.nearest = np.array(nearest)

        def recurve(node):
            if node is not None:
                axis = node.split
                daxis = x[axis] - node.value[axis]
                if daxis < 0:
                    recurve(node.left)
                else:
                    recurve(node.right)
                dist = sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(x, node.value)))
                for i, d in enumerate(self.nearest):
                    if d[0] < 0 or dist < d[0]:  # 如果当前nearest内i处未标记（-1），或者新点与x距离更近
                        self.nearest = np.insert(self.nearest, i, [dist, node.value], axis=0)  # 插入比i处距离更小的
                        self.nearest = self.nearest[:-1]
                        break
                # 找到nearest集合里距离最大值的位置，为-1值的个数
                n = list(self.nearest[:, 0]).count(-1)
                # 切分轴的距离比nearest中最大的小（存在相交）
                if self.nearest[-n - 1, 0] > abs(daxis):
                    if daxis < 0:  # 相交，x[axis]< node.data[axis]时，去右边（左边已经遍历了）
                        recurve(node.right)
                    else:  # x[axis]> node.data[axis]时，去左边，（右边已经遍历了）
                        recurve(node.left)
        recurve(root)
        return self.nearest


if __name__ == '__main__':
    # 最近坐标点、最近距离和访问过的节点数
    result = namedtuple("Result_tuple", "nearest_point nearest_dist nodes_visited")
    data = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
    kd = KDTree(data)
    # [3, 4.5]最近的3个点
    n = kd.search(kd.root, [3, 4.5], 3)
    print(n)
