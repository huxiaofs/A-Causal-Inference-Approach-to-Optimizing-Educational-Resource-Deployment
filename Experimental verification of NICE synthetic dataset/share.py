import numpy as np
import pandas as pd
import networkx as nx
from random import choice, randint, uniform
from itertools import chain

# 参数定义
num_dags = 1  # DAG数量
# num_nodes_range = (4)  # 每个DAG节点数量范围
sample_sizes = [100, 200, 500]  # 数据集规模
noise_levels = [0.1, 0.5, 1.0]  # 噪声强度

# 存储结果
dag_data = []

# 生成随机DAG，满足马尔可夫条件和忠实性
for i in range(num_dags):
    # 生成随机节点数量的DAG
    num_nodes = 4
    G = nx.DiGraph()
    G.add_nodes_from(range(num_nodes))
    # 0, 0, a, b
    # 0, 0, 0, 0
    # 0, d, 0, c
    # 0, e, 0, 0
    # 创建邻接矩阵，并随机生成有向边
    adj_matrix = np.zeros((num_nodes, num_nodes))
    adj_matrix[0, 2] = uniform(0.1, 1.0)
    adj_matrix[0, 3] = uniform(0.1, 1.0)
    adj_matrix[2, 1] = uniform(0.1, 1.0)
    adj_matrix[2, 3] = uniform(0.1, 1.0)
    adj_matrix[3, 1] = uniform(0.1, 1.0)
    for u in range(num_nodes):
        for v in range(num_nodes):
            if adj_matrix[u, v] > 0:
                G.add_edge(u, v, weight=adj_matrix[u, v])

    # 打印邻接矩阵
    print(f"\nDAG {i} Adjacency Matrix with Weights:\n", adj_matrix)

    # 选择干预和结果变量
    intervention_var = 2
    outcome_var = 1


    # 识别后门调整集
    def find_backdoor_adjustment_set(G, X, Y):
        # 找到所有共同祖先节点
        ancestors_of_X = nx.ancestors(G, X)
        ancestors_of_Y = nx.ancestors(G, Y)
        common_ancestors = ancestors_of_X.intersection(ancestors_of_Y)
        
        # 存储所有后门路径的节点集合
        backdoor_paths_nodes = []

        # 遍历每个共同祖先节点
        for ancestor in common_ancestors:
            # 找到从公共祖先到X的路径
            paths_to_X = list(nx.all_simple_paths(G, source=ancestor, target=X))
            # 找到从公共祖先到Y的路径
            paths_to_Y = list(nx.all_simple_paths(G, source=ancestor, target=Y))

            # 将从公共祖先到X的路径和从公共祖先到Y的路径组合成完整的后门路径
            for path_X in paths_to_X:
                for path_Y in paths_to_Y:
                    # 从路径中去掉公共祖先和终点X、Y，防止重复
                    full_path = set(path_X[:-1] + path_Y[1:-1])
                    # 添加路径到后门路径集合
                    if full_path:
                        backdoor_paths_nodes.append(full_path)
        
        # 找到覆盖所有路径的最小集合
        return minimum_cover(backdoor_paths_nodes)

    # 求最小覆盖集
    def minimum_cover(sets):
        # 展开集合中的所有元素
        elements = set(chain(*sets))
        cover = set()
        
        while sets:
            # 找到最常出现的元素
            most_common = max(elements, key=lambda e: sum(1 for s in sets if e in s))
            cover.add(most_common)
            
            # 移除包含该元素的所有集合
            sets = [s for s in sets if most_common not in s]
            elements.discard(most_common)
        
        return list(cover)

    backdoor_set = find_backdoor_adjustment_set(G, intervention_var, outcome_var)