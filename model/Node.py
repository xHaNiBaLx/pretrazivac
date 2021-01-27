class Node(object):
    """
    Klasa modeluje cvor trie stabla
    """
    __slots__ = "root","children", "value"

    def __init__(self, root=False):
        self.children = {}  # kljuc: character, vrednost: Node
        self.value = {}
        self.root = root


    def is_root(self):
        """
        Metoda proverava da li je cvor koren stabla.
        """
        return self.root is True

    def is_leaf(self):
        """
        Metoda proverava da li je cvor list stabla.
        """
        return len(self.children) == 0
