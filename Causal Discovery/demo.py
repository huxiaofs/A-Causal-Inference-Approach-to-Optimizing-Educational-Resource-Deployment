import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from cdt.causality.graph import PC


def create_and_draw_graph_from_edgelist(file_path):
    G = nx.DiGraph()  # 创建一个有向图
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()  # 分割每一行
            if len(parts) == 3:  # 确保行格式正确
                source = parts[0]
                target = parts[1]
                # 假设每条边的权重都是1，可以根据需要调整
                G.add_edge(source, target, weight=1)

    # 生成布局并绘制图
    pos = nx.spring_layout(G)  # 使用spring布局, 添加seed参数

    plt.figure(figsize=(15, 10))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, width=1)
    plt.title("Complete Causal Graph")
    plt.show()


file_path = "pc_output_edgelist.txt"
create_and_draw_graph_from_edgelist(file_path)
