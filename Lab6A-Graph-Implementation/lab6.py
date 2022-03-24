from GraphAL import GraphAL
from math import inf
from queue import *


def sort_edges_by_weight(nodes):
    for i in range(len(nodes)):
        for j in range(0, len(nodes)-i-1):
            if nodes[j] == None or nodes[j+1] == None:
                continue
            if nodes[j].weight > nodes[j+1].weight:
                temp = nodes[j]
                nodes[j] = nodes[j+1]
                nodes[j+1] = temp


def kruskals_sort(graph):
    # set up array
    edges = graph.get_edges_as_list()
    
    # sort nodes by weight
    # since the graph is not that large, bubble sort is used in order to keep things simple
    sort_edges_by_weight(edges)

    # set up new graph
    min_graph = GraphAL(int(graph.get_num_vertices()), graph.is_directed)

    # insert nodes
    for edge in edges:
        #print("Adding edge " + str(edge.src) + " >>> " + str(edge.dest) + " weight " + str(edge.weight))
        min_graph.add_edge(edge.src, edge.dest, edge.weight)
        if min_graph.contains_cycle():
            #print("Found cycle " + str(edge.src) + " >>> " + str(edge.dest))
            min_graph.remove_edge(edge.src, edge.dest)
       
    
    return min_graph

def compute_indegree_every_vertex(graph):
    in_degrees = []
    for vertex in graph.adj_list:
        in_degrees.append(graph.get_vertex_in_degree(vertex))
    return in_degrees

def topological_sort(graph):
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []

    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)
    while not q.empty():
        u = q.get()

        sort_result.append(u)

        for adj_vertex in graph.get_adj_vertices(u):
            all_in_degrees[adj_vertex] -= 1
            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)
    if len(sort_result) != graph.get_num_vertices():
        return None
    return sort_result

            

def main():
    print("STARTING MAIN")
    # The following graph will be created
    #     1        (8)
    # (2)/ \      3------5
    #   /(1)\ (3)/      /
    #  2     \ /      /(4)
    #   \-----0------4
    #     (10)   (23)


    # Set up graph size
    user_graph = GraphAL(6, False)
    

    # Add edges
    user_graph.add_edge(0,1,1)
    user_graph.add_edge(1,2,2)
    user_graph.add_edge(2,0,10)
    user_graph.add_edge(0,3,3)
    user_graph.add_edge(0,4,23)
    user_graph.add_edge(4,5,4)
    user_graph.add_edge(3,5,8)

    print("USING KRUSKAL'S ALGORITHM...")
    # Show user graph
    print("The graph adjacency list looks like this....")
    user_graph.print_graph()

    print("The min spanning tree looks like this...")
    min_graph = kruskals_sort(user_graph)
    min_graph.print_graph()

    print("")

    print("USING TOPOLOGICAL SORT...")

    print("The min spanning tree looks like this...")
    min_graph = topological_sort(user_graph)
    print(min_graph)


main()