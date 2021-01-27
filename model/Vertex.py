class Vertex(object):
    """
    Vertex struktura za graf
    """
    __slots__ = '_element'

    def __init__(self, x):
        """
        Ne pozivati konstruktor direktno.
        Koristiti grafov insert_vertex
        """
        self._element = x

    def element(self):
        """Vraca element"""
        return self._element

    def __hash__(self):  # ovo omogucava vertexu da bude mapiran
        return hash(id(self))

    def __str__(self):
        return str(self._element)

    def __eq__(self, other):
        if self._element == other:
            return True
        else:
            return False
