from actions.Ranker import Ranker
from Gigle import Gigle
from actions.Controler import Controler

if __name__ == '__main__':
    c = Controler()
    c.upustvo()
    program = Gigle()
    while True:
        print
        rec = raw_input("Pretraga: ")
        stasam = c.handler(rec)
        if isinstance(stasam, basestring) and stasam == 'rec':  # Pretraga reci
            rec = rec.lower()
            rezultat = program.stablo.find(program.stablo.root, rec)
            # print "Rec je pronadjena u %d fajlova." % len(rezultat.values())
            Ranker.lista_heuristika(rezultat, program.graf)
        elif isinstance(stasam, basestring) and stasam == 'prazno':  # Prazan string
            pass
        elif isinstance(stasam, basestring) and stasam == 'fraza':  # Fraza
            rezultat = program.stablo.nadji_frazu(program.stablo.root, rec)
        else:  # Logika
            rezultat = program.stablo.logicfind(program.stablo.root, stasam, program.graf.vertices())
            Ranker.lista_heuristika(rezultat, program.graf, True)
        pitanje = raw_input("Da li zelite da nastavite? ")
        print
        if pitanje.lower() == 'ne':
            break
        else:
            continue
