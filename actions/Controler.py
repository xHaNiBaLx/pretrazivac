class Controler(object):

    def handler(self, string):
        if string:
            if string[0] == "'":
                return 'fraza'
            elif len(string.split()) > 1:
                mapa = self.provera(string)
                return mapa
            else:
                return 'rec'
        else:
            print "Uneli ste prazan string"
            return 'prazno'

    def provera(self, string):
        reci = string.split()
        nott = False
        mapa = []
        privremena = "OR"
        for i, rec in enumerate(reci):
            if rec == "AND":
                if i == 0:
                    continue
                else:
                    privremena = "AND"
            elif rec == "OR":
                if i == 0:
                    continue
                else:
                    privremena = "OR"
            elif rec == "NOT":
                if i == 0:
                    continue
                else:
                    nott = True
            else:
                mapa.append([rec, nott, privremena])
                privremena = "OR"
                nott = False
        return mapa

    def upustvo(self):
        print "Dobrodosli u Giggle\n"
        print "Upustvo za upotrebu:"
        print "=========================================================================="
        print "1) Uneti rec za pretragu reci"
        print "2) Uneti vise reci i izmenju njih AND, OR, i NOT za napredniju pretragu"
        print "3) Uneti frazu pod navodnicima npr. 'ovo je fraza' za pretragu po frazama"
