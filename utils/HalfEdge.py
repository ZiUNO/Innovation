# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 15:44
"""


class HalfEdge(object):

    def __init__(self, source_vertex, target_vertex, edge, face):
        self.__vertex = target_vertex
        self.__source_vertex = source_vertex
        self.__target_vertex = target_vertex
        self.__edge = edge
        self.__next_half_edge = '[undefined]'
        self.__prev_half_edge = '[undefined]'
        self.__symm_half_edge = '[undefined]'
        self.__face = face
        # print('[created]' + self.__str__())

    @property
    def vertex(self):
        return self.__vertex

    @property
    def source_vertex(self):
        return self.__source_vertex

    @property
    def target_vertex(self):
        return self.__target_vertex

    @property
    def edge(self):
        return self.__edge

    @property
    def next_half_edge(self):
        return self.__next_half_edge

    @next_half_edge.setter
    def next_half_edge(self, next_half_edge):
        self.__next_half_edge = next_half_edge

    @property
    def prev_half_edge(self):
        return self.__prev_half_edge

    @prev_half_edge.setter
    def prev_half_edge(self, prev_half_edge):
        self.__prev_half_edge = prev_half_edge

    @property
    def symm_half_edge(self):
        return self.__symm_half_edge

    @symm_half_edge.setter
    def symm_half_edge(self, symm_half_edge):
        self.__symm_half_edge = symm_half_edge

    @property
    def face(self):
        return self.__face

    # def __str__(self):
    #     return 'HalfEdge:{vertex: ' + self.__vertex + ', source_vertex: ' \
    #            + self.__source_vertex + ', target_vertex: ' \
    #            + self.__target_vertex + ', edge: ' + self.__edge + ', next_half_edge: ' + self.__next_half_edge \
    #            + ', prev_half_edge: ' + self.__prev_half_edge + ', symm_half_edge: ' + self.__symm_half_edge \
    #            + ', face: ' + self.__face + '}'
