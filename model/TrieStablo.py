from model.Node import Node


class TrieStablo(object):
    """
    Trie stablo koje cuva sve
    stringove jednog fajla
    """
    def __init__(self, root):
        self.root = root

    def is_empty(self):
        """
        Metoda koja proverava da li stablo
        ima elemenata
        """
        return self.root is None

    def postorder(self, x):
        """
        Postorder obilazak po dubini

        Najpre se vrsi obilazak potomaka a zatim i roditelja

        Argument:
        - `x`: cvor od koga pocinje obilazak
        """
        if not self.is_empty():
            for c in x.children:
                self.postorder(c)
            print x.data

    def insert(self, string, value, path):
        node = self.root
        index_last_char = None
        for index_char, char in enumerate(string):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break

        # append new nodes for the remaining characters, if any
        if index_last_char is not None:
            for char in string[index_last_char:]:
                node.children[char] = Node()
                node = node.children[char]

        # store value in the terminal node
        if path in node.value.keys():
            node.value[path].append(value)
        else:
            node.value[path] = [value]

    def insert_list(self, lista, path):
        indeks = 0
        for rec in lista:
            self.insert(rec, indeks, path)
            indeks += 1

    def find(self, node, key):
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def logicfind(self, node, mapa, vert):  # u mapi rec pod indeksom nula, not je 1 a and ili or su na 2
        konacno = {}
        for rec in mapa:
            rezultat = self.find(node, rec[0].lower())
            konacno = self.obradi((rec[1], rec[2]), rezultat, konacno, vert)
        return konacno

    def obradi(self, tapl, rezultat, konacno, vert):
        if tapl[0]:  # Ako je NOT ispred AND ili OR
            if tapl[1] == "AND":  # Apsolutna zabrana ovih putanja za narednu rec
                zabrisanje = rezultat.keys()
                for bajbaj in zabrisanje:
                    if bajbaj in konacno:
                        del konacno[bajbaj]
                return konacno

            else:  # Sve putanje osim ovih su resenje ali je moguce da se pojave i te putanje (ako bar nema)
                zadodati = []
                for cvor in vert:
                    zadodati.append(cvor.element())
                for novi in zadodati:
                    if novi not in rezultat:
                        if novi in konacno:
                            continue
                        else:
                            konacno[novi] = [0]
                return konacno

        else:  # Ako nema NOT ispred
            if tapl[1] == "AND":  # Mora biti ukljucena bar jedna putanja u konacno resenje
                nebrisi = []
                for kljuc in rezultat:
                    if kljuc in konacno:
                        # konacno[kljuc].append(rezultat[kljuc])
                        konacno[kljuc] = konacno[kljuc] + rezultat[kljuc]
                        nebrisi.append(kljuc)
                    else:
                        continue
                for kljuc in konacno.keys():
                    if kljuc not in nebrisi:
                        del konacno[kljuc]
                return konacno

            else:
                for kljuc in rezultat:  # Sve ove putanje su resenje
                    if kljuc in konacno:
                        # konacno[kljuc].append(rezultat[kljuc])
                        konacno[kljuc] = konacno[kljuc] + rezultat[kljuc]
                    else:
                        konacno[kljuc] = rezultat[kljuc]
                return konacno

    def nadji_frazu(self, node, phrase):
        lista = phrase.strip("'").lower().split()
        rezporeci = []
        for rec in lista:
            rezultat = self.find(node, rec)
            rezporeci.append(rezultat)
        return rezporeci
