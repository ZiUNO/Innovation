# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 15:16
"""


class Edge(object):
    def __init__(self, vertexes):
        self.__half_edges = []
        assert len(vertexes) == 2, 'Edge: [init] the length of the vertexes of a edge must be 2'
        self.__vertexes = set(vertexes)
        # print('[created]' + self.__str__())

    @property
    def half_edges(self):
        return self.__half_edges

    @half_edges.setter
    def half_edges(self, half_edges):
        self.__half_edges = half_edges

    @property
    def vertexes(self):
        return self.__vertexes

    def __str__(self):
        half_edges_str = 'null' if len(self.__half_edges) == 0 else str(self.__half_edges)
        return 'Edge:{half_edges: ' + half_edges_str + '}'

    def __eq__(self, other):
        return self.__vertexes == other.vertexes
