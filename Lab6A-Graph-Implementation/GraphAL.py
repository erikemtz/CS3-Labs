class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        self.dsf[a] = self.find(self.dsf[a])

        return self.dsf[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.dsf[rb] = ra

    def get_num_of_sets(self):
        count = 0

        for num in self.dsf:
            if num < 0:
                count += 1

        return count


class GraphALNode:
    def __init__(self, item, weight, next):
        self.item = item
        self.weight = weight
        self.next = next

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed
        
    def get_edges_as_list(self):
        edges = []
        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp != None:
                graphEdge = Edge(i, temp.item, temp.weight)
                edges.append(graphEdge)
                temp = temp.next
        return edges

    def print_graph(self):
        for i in range(len(self.adj_list)):
            print(i , end=" >>> ")
            temp = self.adj_list[i]
            while temp != None:
                print(temp.item , end = " ")
                temp = temp.next
            print("")
                

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        #  TODO: What if src already points to dest?
        # the following checks if the src already points to dest

        temp = self.adj_list[src]
        while temp != None:
            if temp.item == dest:
                print("Test")
                return
            temp = temp.next
        
        self.adj_list[src] = GraphALNode(dest, weight, self.adj_list[src])

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, weight, self.adj_list[dest])

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.adj_list)

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    def __str__(self):
        s = ""

        for i in range(len(self.adj_list)):

            s += str(i) + ": "

            temp = self.adj_list[i]

            while temp is not None:

                s += "(dest = " + str(temp.item) + " , weight = " + str(temp.weight) + ") -> "
                temp = temp.next

            s += " None\n"

        return s
    def get_adj_vertices(self, v):
        if not self.is_valid_vertex(v):
            return
        vertices = []
        temp = self.adj_list[v]

        while temp != None:
            vertices.append(temp.item)
            temp = temp.next

        return vertices
    
    def get_vertex_in_degree(self, v):
        if not self.is_valid_vertex(v.item):
            return

        in_degree_count = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == v:
                    in_degree_count += 1
                    break

                temp = temp.next

        return in_degree_count


    # ---------------------------------------------------------------------------------------
    # --------------------------- Problem 8 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_num_connected_components(self):

        dsf = DisjointSetForest(len(self.adj_list))

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                dsf.union(i, temp.item)

                temp = temp.next

        return dsf.get_num_of_sets()

    # ---------------------------------------------------------------------------------------
    # --------------------------- Problem 9 ---------------------------
    # ---------------------------------------------------------------------------------------
    def create_circle_graph(self, n):

        if n < 2:  # Assumption -> n should be at least 2
            return

        self.adj_list = [None] * n
        self.is_directed = True

        # Add edges
        for i in range(n - 1):
            self.adj_list[i] = GraphALNode(item=(i + 1), weight=1.0, next=None)

        self.adj_list[n - 1] = GraphALNode(item=0, weight=1.0, next=None)

        # Another way of doing the same thing:

        # for i in range(n):
        #     self.adj_list[i] = GraphALNode(item=((i + 1) % n), weight=1.0, next=None)

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P3 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_highest_cost_edge(self):

        highest_cost_edge = -float('inf')

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                highest_cost_edge = max(temp.weight, highest_cost_edge)

                temp = temp.next

        return highest_cost_edge


    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P4 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_num_edges(self):

        num_edges = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                num_edges += 1

                temp = temp.next

        return num_edges

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P5 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_edge_weight(self, src, dest):

        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        temp = self.adj_list[src]

        while temp is not None:
            if temp.item == dest:
                return temp.weight

            temp = temp.next

        return 0

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P6 ---------------------------
    # ---------------------------------------------------------------------------------------
    def reverse_edges(self):

        new_adj_list = [None] * len(self.adj_list)

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                new_adj_list[temp.item] = GraphALNode(i, temp.weight, new_adj_list[temp.item])
                temp = temp.next

        self.adj_list = new_adj_list

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P8 ---------------------------
    # ---------------------------------------------------------------------------------------
    def is_self_edge(self, v):
        if not self.is_valid_vertex(v):
            return False

        temp = self.adj_list[v]

        while temp is not None:

            if temp.item == v:
                return True

            temp = temp.next

        return False

    def get_num_of_self_edges(self):

        num_self_edges = 0

        for u in range(len(self.adj_matrix)):
            if self.is_self_edge(u):
                num_self_edges += 1

        return num_self_edges

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P11 ---------------------------
    # ---------------------------------------------------------------------------------------
    def contains_cycle(self):  # Assumption: Undirected

        dsf = DisjointSetForest(len(self.adj_list))

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if dsf.find(i) == dsf.find(temp.item):
                    return True

                dsf.union(i, temp.item)
                
                temp = temp.next

        return False

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P12 ---------------------------
    # ---------------------------------------------------------------------------------------
    def is_isolated(self, v):
        if not self.is_valid_vertex(v):
            return False

        if self.adj_list[v] is not None:
            return False

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == v:
                    return False

        return True
