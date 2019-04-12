# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 15:16
"""


class Face(object):
    def __init__(self):
        self.__half_edges = []
        # print('[created]' + self.__str__())

    @property
    def half_edges(self):
        return self.__half_edges

    @half_edges.setter
    def half_edges(self, half_edges):
        self.__half_edges = half_edges

    def __str__(self):
        half_edges_str = 'null' if len(self.__half_edges) == 0 else str(self.__half_edges)
        return 'Face:{half_edges: ' + half_edges_str + '}'
