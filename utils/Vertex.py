# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 15:15
"""


class Vertex(object):
    def __init__(self, position):
        assert len(position) == 3, '[error]:Vertex: [init] the length of vertex position must be 3'
        self.__position = [int(i) for i in position]
        self.__half_edges = []
        # print('[created]' + self.__str__())

    @property
    def position(self):
        return self.__position

    @property
    def half_edges(self):
        return self.__half_edges

    @half_edges.setter
    def half_edges(self, half_edges):
        self.__half_edges = half_edges

    @property
    def x(self):
        return self.__position[0]

    @property
    def y(self):
        return self.__position[1]

    @property
    def z(self):
        return self.__position[2]

    def __str__(self):
        half_edges_str = 'null' if len(self.__half_edges) == 0 else str(self.__half_edges)
        return 'Vertex:{position: ' + str(self.__position) \
               + ', half_edges: ' + half_edges_str + '}'

    def __eq__(self, other):
        return self.__position == other.position
