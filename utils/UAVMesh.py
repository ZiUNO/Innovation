# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 18:14
"""
from itertools import chain


class UAVMesh(object):
    def __init__(self, mesh):
        self.__mesh = mesh
        self.__vertexes = mesh.vertexes
        self.__edges = mesh.edges
        self.__faces = mesh.faces

    def __oxen_led(self):
        path = []
        half_edges = self.__vertex.half_edges.copy()
        while len(half_edges) != 0:
            half_edge = half_edges[0]
            face = half_edge.face
            if self.__faces.count(face) == 0:
                del half_edges[0]
                continue
            source_vertex = half_edge.source_vertex
            target_vertex = half_edge.target_vertex
            path.append(['oxen-led', self.__vertexes.index(source_vertex), self.__vertexes.index(target_vertex),
                         self.__faces.index(face)])
            self.__faces.remove(face)
            self.__vertex = target_vertex
            half_edges = self.__vertex.half_edges.copy()
        return path

    def __jump_out(self):
        path = []
        source_vertex_index = self.__vertexes.index(self.__vertex)
        half_edges = [face.half_edges for face in self.__faces]
        half_edges = list(chain(*half_edges))
        target_vertex_indexes = [self.__vertexes.index(half_edge.target_vertex) for half_edge in half_edges]
        target_vertex_indexes = list(set(target_vertex_indexes))

        def get_map_dist(mesh):
            map = {}
            for vertex in mesh.vertexes:
                source_index = self.__vertexes.index(vertex)
                map[source_index] = {}
                half_edges = vertex.half_edges
                target_vertexes = [half_edge.target_vertex for half_edge in half_edges]
                target_indexes = [self.__vertexes.index(target_vertex) for target_vertex in target_vertexes]
                for targer_index in target_indexes:
                    map[source_index][targer_index] = 1
            return map

        graph = get_map_dist(self.__mesh)

        def get_cost_dist(map, source):
            cost = {}
            can_go_s = map[source]
            for can_go in can_go_s:
                cost[can_go] = map[source][can_go]
            can_not_go_s = map.keys() - can_go_s
            for can_not_go in can_not_go_s:
                cost[can_not_go] = 999
            cost[source] = 0
            return cost

        cost = get_cost_dist(graph, source_vertex_index)
        visited = [source_vertex_index]
        parents = {}

        def findShorestNode(cost):
            minDist = 999
            node = None
            for i in graph.keys():
                if (cost[i] < minDist) & (i not in visited):
                    minDist = cost[i]
                    node = i
            return node

        node = findShorestNode(cost)
        while node:
            for i in graph[node]:
                newcost = cost[node] + graph[node][i]
                if newcost < cost[i]:
                    parents[i] = node
                    cost[i] = newcost
            visited.append(node)
            node = findShorestNode(cost)
        can_go_costs = []
        can_go_keys = graph[source_vertex_index].keys()
        for target_vertex_index in target_vertex_indexes:
            can_go_costs.append([cost[target_vertex_index], target_vertex_index])
        can_go_costs.sort()
        _, target_vertex_index = can_go_costs[0]
        tmp_path = [target_vertex_index]
        tmp_index = tmp_path[-1]
        while tmp_index not in can_go_keys:
            tmp_path.append(parents[tmp_index])
            tmp_index = tmp_path[-1]
        while len(tmp_path) != 0:
            target_vertex_index = tmp_path[-1]
            half_edges = self.__vertex.half_edges
            for half_edge in half_edges:
                index = self.__vertexes.index(half_edge.target_vertex)
                if index != target_vertex_index:
                    continue
                path.append(['move', source_vertex_index, index])
                del tmp_path[-1]
                self.__vertex = half_edge.target_vertex
                source_vertex_index = index
                break
        return path

    def get_uav_path_from_vertex(self, vertex):
        path = []
        if self.__vertexes.count(vertex) == 0:
            raise ValueError('[error] the start vertex is not in the vertexes')
        vertex = self.__vertexes[self.__vertexes.index(vertex)]
        self.__vertex = vertex
        while len(self.__faces) != 0:
            path.append(self.__oxen_led())
            if len(self.__faces) == 0:
                break
            path.append(self.__jump_out())
        self.__faces = self.__mesh.faces.copy()
        return path
