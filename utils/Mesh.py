# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 15:14
"""
from utils.Edge import Edge
from utils.Face import Face
from utils.HalfEdge import HalfEdge
from utils.Vertex import Vertex


class Mesh(object):

    def __init__(self, vertexes_info, faces_info):
        self.__edges = []
        self.__vertexes = [Vertex(position) for position in vertexes_info]
        self.__faces = []
        for vertexes_info in faces_info:
            face = Face()
            edge_1 = Edge(vertexes_info[: 2])
            if self.__edges.count(edge_1) != 0:
                edge_1 = self.__edges[self.__edges.index(edge_1)]
            else:
                self.__edges.append(edge_1)
            edge_2 = Edge(vertexes_info[1:])
            if self.__edges.count(edge_2) != 0:
                edge_2 = self.__edges[self.__edges.index(edge_2)]
            else:
                self.__edges.append(edge_2)
            edge_3 = Edge([vertexes_info[2], vertexes_info[0]])
            if self.__edges.count(edge_3) != 0:
                edge_3 = self.__edges[self.__edges.index(edge_3)]
            else:
                self.__edges.append(edge_3)
            edges = [edge_1, edge_2, edge_3]
            vertexes = [self.__vertexes[int(vertex_index) - 1] for vertex_index in vertexes_info]
            half_edge_1 = HalfEdge(vertexes[0], vertexes[1], edges[0], face)
            half_edge_2 = HalfEdge(vertexes[1], vertexes[2], edges[1], face)
            half_edge_3 = HalfEdge(vertexes[2], vertexes[0], edges[2], face)
            edge_1.half_edges.append(half_edge_1)
            edge_2.half_edges.append(half_edge_2)
            edge_3.half_edges.append(half_edge_3)
            self.__faces.append(face)
            half_edge_1.next_half_edge = half_edge_2
            half_edge_2.next_half_edge = half_edge_3
            half_edge_3.next_half_edge = half_edge_1
            half_edge_1.prev_half_edge = half_edge_3
            half_edge_2.prev_half_edge = half_edge_1
            half_edge_3.prev_half_edge = half_edge_2
            vertexes[0].half_edges.append(half_edge_1)
            vertexes[1].half_edges.append(half_edge_2)
            vertexes[2].half_edges.append(half_edge_3)
            face.half_edges += [half_edge_1, half_edge_2, half_edge_3]


    @property
    def vertexes(self):
        return self.__vertexes

    @property
    def faces(self):
        return self.__faces

    @property
    def edges(self):
        return self.__edges

    @staticmethod
    def read_mesh_file(mesh_file_path):
        with open(mesh_file_path, 'r') as f:
            lines = f.readlines()
        vertexes_info = []
        faces_info = []
        for line in lines:
            line = line.split()
            element = line[0]
            line_info = line[2:]
            if element == 'Vertex':
                vertexes_info.append(line_info[:-2])
            else:
                faces_info.append(line_info)
        return [vertexes_info, faces_info]
