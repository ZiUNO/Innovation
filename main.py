# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/4/12 15:13
"""
from utils.UAVMesh import UAVMesh
from utils.Mesh import Mesh
from utils.Vertex import Vertex

if __name__ == '__main__':
    mesh_input_data = Mesh.read_mesh_file(r'G:\tmp\loveme.m')
    vertexes, faces = mesh_input_data
    mesh = Mesh(vertexes, faces)
    vertex = Vertex([610, 634, 87])
    uav_mesh = UAVMesh(mesh)
    path = uav_mesh.get_uav_path_from_vertex(vertex)
    print(path)
