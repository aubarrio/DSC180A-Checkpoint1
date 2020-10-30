import pandas as pd
import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def get_summary(file):
    if source == 'snap':
        G = nx.read_edgelist(file, create_using=nx.DiGraph(), nodetype = int)
        lst = list(nx.info(G).split("\n"))

        indices = [x.split(":")[0] for x in lst]
        indices.inser(len(indices) "Network Diameter")
        indices.insert(len(indices), "Average Path Length")
        indices.inser(len(indices), "Average Cluster Coeff")

        values = [x.split(":")[1] for x in lst]
        values.insert(len(vals), "Infinite")
        values.insert(len(vals)), str(nx.average_shortest_path_length(G)))
        values.insert(len(vals), str(nx.average_clustering(G)))

        d = {"Category": idx, "Values": vals}
        df = pd.DataFrame(vals, index = idx, columsn = ['value'])
    return df

def read_edges(source, path):
    """
    Reads in edge data
    """
    if source == 'cora':
        d = pd.read_csv(path, sep='\t', header=None)
    elif source == 'snap':
        d = pd.read_csv(path)
    return d

def read_features(source, path):
    """
    Returns a dataframe of the data inputed
    """
    if source == 'cora':
        d = pd.read_csv(path, sep='\t', header=None)
        d = d.rename(columns={0: 'index'})
    elif source == 'snap':
        with open(path) as json_data:
            data = json.load(json_data)
        d = pd.DataFrame.from_dict(data, orient='index')
        d['index'] = d.index
        d = d.reset_index(drop=True)
    else:
        d = np.NaN
    return d

def index_nodes(d):
    index = d['index']
    in_d = {}
    for i in np.arange(len(index)):
        in_d[int(index[i])] = i
        i += 1
    return in_d

def create_adj(in_d, d_edge):
    adj = np.zeros((len(in_d), len(in_d)), dtype='float32')
    rows = d_edge.iloc[:, 0]
    cols = d_edge.iloc[:, 1]
    for i in np.arange(len(d_edge)):
        adj[in_d[rows[i]], in_d[cols[i]]] = 1.0
    return adj

def complete(source, fp_features, fp_edges, outpath):
    # print("Source is: " + source)
    # print("fp_features is: " + fp_features)
    # print("fp_edges is: " + fp_edges)
    # print("outpath is: " + outpath)
    edge_df = read_edges(source, fp_edges)
    feat_df = read_features(source, fp_features)

    in_d = index_nodes(feat_df)
    adj = create_adj(in_d, edge_df)

    G = nx.from_numpy_matrix(adj, nx.DiGraph())
    plt.figure(figsize=(10,10))
    nx.draw(G, node_size=10, edge_size=1)
    plt.show()
    fig = plt.figure()
    fig.savefig('test.png')
    return -1
