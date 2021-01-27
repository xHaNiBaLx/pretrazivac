from model.Vertex import Vertex


class Edge(object):
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return self._origin, self._destination

    def opposite(self, v):
        if not isinstance(v, Vertex):
            raise TypeError('v must be Vertex')
        return self._destination if v is self._origin else self._origin
        raise ValueError('v not incident to edge')

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))

    def __str__(self):
        return '({0},{1},{2})'.format(self._origin, self._destination, self._element)
