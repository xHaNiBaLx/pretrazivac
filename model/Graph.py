from model.Vertex import Vertex
from model.Edge import Edge


class Graph(object):

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def _validate_vertex(self, v):
        if not isinstance(v, Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph')

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:  # Ovde ulazi ako je duplikat
            return
            #  raise ValueError('u and v are already adjacent')
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinvt map for incoming edges
        return v


# if __name__ == '__main__':
#     graf = Graph(True)
#     cvor1 = graf.insert_vertex("putanja1")
#     cvor2 = graf.insert_vertex("putanja2")
#     cvor3 = graf.insert_vertex("putanja3")
#     graf.insert_edge(cvor1, cvor2)
#     graf.insert_edge(cvor1, cvor3)
#     graf.insert_edge(cvor2, cvor1)
#     dolazeci = graf.incident_edges(cvor1, False)
#     odlazeci = graf.incident_edges(cvor1)
#     for i in dolazeci:
#         print i
#     print 'sada odlazeci'
#     for i in odlazeci:
#         print i

