import os
from genericpath import isdir
from actions.parser import Parser
from model.Graph import Graph
from model.TrieStablo import TrieStablo
from model.Node import Node


class Gigle(object):

    def __init__(self):
        self.graf = Graph(True)
        root = Node(True)
        self.stablo = TrieStablo(root)
        self.veze = {}
        self.start()
        self.povezi()

    def start(self):
        p = Parser()
        for fajl in os.listdir("./python-2.7.7-docs-html"):
            if fajl[-4:] == "html":
                # parsiraj ga odje
                name = os.path.abspath(os.path.join("./python-2.7.7-docs-html", fajl))
                links, words = p.parse(name)
                self.stablo.insert_list(words, name)  # add to trie name words
                cvor = self.graf.insert_vertex(name)  # add to graph name links
                self.veze[cvor] = links

            elif isdir(os.path.join("./python-2.7.7-docs-html", fajl)):
                for fajl2 in os.listdir(os.path.join("./python-2.7.7-docs-html", fajl)):
                    if fajl2[-4:] == 'html':
                        name2 = os.path.abspath(os.path.join("./python-2.7.7-docs-html", fajl, fajl2))
                        links2, words2 = p.parse(name2)
                        self.stablo.insert_list(words2, name2)  # add to trie name words
                        cvor = self.graf.insert_vertex(name2)  # add to graph name links
                        self.veze[cvor] = links2

    def povezi(self):
        destinacija = None
        for i, links in enumerate(self.veze.values()):
            for link in links:
                for cvor in self.veze.keys():
                    if cvor.element() == link:
                        destinacija = cvor
                        break
                self.graf.insert_edge(self.veze.keys()[i], destinacija)
