from heapq import *
from actions.parser import Parser


class Ranker(object):

    @staticmethod
    def lista_heuristika(recnik, graf, logika=False):
        heap = []
        sva = 0
        for path in recnik.keys():
            ponavljanja = len(recnik[path])
            heur = Ranker.heuristika(graf, path, recnik) + ponavljanja
            sva += ponavljanja
            heappush(heap, (-heur, path))
        # print "Sva ponavljanja: %d" % sva
        sledeci = 'da'
        while sledeci != 'ne':
            Ranker.stampaj(heap, recnik, logika)
            sledeci = raw_input("\nDa li zelite sledecih 10 rezultata? ")
            sledeci = sledeci.lower()

    @staticmethod
    def heuristika(graf, path, recnik):
        linkovi = []
        cvorovi = graf.vertices()
        for cvor in cvorovi:
            if cvor == path:
                klinkove = graf.incident_edges(cvor, False)
                for link in klinkove:
                    linkovi.append(link)
                break
        pronadjeni = recnik.keys()
        ponavljanja = 0
        for link in linkovi:
            if link.endpoints()[0].element() in pronadjeni:
                ponavljanja += len(recnik[link.endpoints()[0].element()])
        if len(linkovi) < 50:
            return 1 + ponavljanja // 2
        elif len(linkovi) < 100:
            return 2 + ponavljanja // 2
        elif len(linkovi) < 150:
            return 3 + ponavljanja // 2
        else:
            return 4 + ponavljanja // 2

    @staticmethod
    def stampaj(heap, recnik, logika):
        if logika:
            if len(heap) > 10:
                for i in xrange(10):
                    tapl = heappop(heap)
                    print "%d) %s" % (i + 1, tapl[1])
                    # print "%d) %s: %d heuristika" % (i + 1, tapl[1], -tapl[0])
                return
            elif 0 < len(heap) < 10:
                i = 1
                while len(heap) != 0:
                    tapl = heappop(heap)
                    print "%d) %s" % (i, tapl[1])
                    # print "%d) %s: %d heuristika" % (i, tapl[1], -tapl[0])
                return
            else:
                print "Nema rezultata"
                return

        p = Parser()
        if len(heap) > 10:
            for i in xrange(10):
                tapl = heappop(heap)
                links, words = p.parse(tapl[1])
                print "%d) %s" % (i+1, tapl[1])
                # print "%d) %s: %d heuristika" % (i + 1, tapl[1], -tapl[0])
                if 0 < recnik[tapl[1]][0] < len(words) - 1:
                    print "... %s %s %s %s ...\n" % (
                    words[recnik[tapl[1]][0] - 1], words[recnik[tapl[1]][0]], words[recnik[tapl[1]][0] + 1],
                    words[recnik[tapl[1]][0] + 2])
                elif recnik[tapl[1]][0] == 0:
                    print "... %s %s %s %s ...\n" % (
                    words[recnik[tapl[1]][0]], words[recnik[tapl[1]][0] + 1], words[recnik[tapl[1]][0] + 2],
                    words[recnik[tapl[1]][0] + 3])
                elif len(words) - 1 == recnik[tapl[1]][0]:
                    print "... %s %s %s %s ...\n" % (
                    words[recnik[tapl[1]][0]], words[recnik[tapl[1]][0] - 1], words[recnik[tapl[1]][0] - 2],
                    words[recnik[tapl[1]][0] - 3])
                else:
                    print 'Los ti uslov u if-u ccc...'
        elif 0 < len(heap) < 10:
            i = 1
            while len(heap) != 0:
                tapl = heappop(heap)
                links, words = p.parse(tapl[1])
                print "%d) %s" % (i, tapl[1])
                # print "%d) %s: %d heuristika" % (i, tapl[1], -tapl[0])
                i += 1
                if 0 < recnik[tapl[1]][0] < len(words) - 1:
                    print "... %s %s %s %s ...\n" % (
                    words[recnik[tapl[1]][0] - 1], words[recnik[tapl[1]][0]], words[recnik[tapl[1]][0] + 1],
                    words[recnik[tapl[1]][0] + 2])
                elif recnik[tapl[1]][0] == 0:
                    print "... %s %s %s %s ...\n" % (
                    words[recnik[tapl[1]][0]], words[recnik[tapl[1]][0] + 1], words[recnik[tapl[1]][0] + 2],
                    words[recnik[tapl[1]][0] + 3])
                elif len(words) - 1 == recnik[tapl[1]][0]:
                    print "... %s %s %s %s ...\n" % (
                    words[recnik[tapl[1]][0]], words[recnik[tapl[1]][0] - 1], words[recnik[tapl[1]][0] - 2],
                    words[recnik[tapl[1]][0] - 3])
                else:
                    print 'Los ti uslov u if-u ccc...'
        else:
            print 'Nije pronadjena rec nigde'
