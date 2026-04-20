import copy

class XExpansion:

    def __init__(self):
        self.soluzioni = []
        self.soluzioni_list = []

    def calcola_list(self, input):
        self.soluzioni_list.clear()
        self._ricorsione_list([], input)

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione_list(self, parziale, rimanenti):
        # caso terminale
        if len(rimanenti) == 0:
            self.soluzioni_list.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':

                # Ciclare sugli step possibili
                for c in ["0", "1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()
            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])

    def calcola(self, input):
        self.soluzioni.clear()
        self._ricorsione("", input)

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione(self, parziale, rimanenti):
        # caso terminale
        if len(rimanenti) == 0:
            self.soluzioni.append(parziale)
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                self._ricorsione(parziale+'0', rimanenti[1:])
                self._ricorsione(parziale+'1', rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])

#================================================================================
#================================================================================
#================================================================================

def x_expansion2(input):
    soluzioni = []

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def ricorsione(parziale, rimanenti):
        # caso terminale
        if len(rimanenti) == 0:
            soluzioni.append(parziale)
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                ricorsione(parziale+'0', rimanenti[1:])
                ricorsione(parziale+'1', rimanenti[1:])
            else:
                ricorsione(parziale+rimanenti[0], rimanenti[1:])

    ricorsione("", input)
    return soluzioni

if __name__ == "__main__":
    sequenza = "01X0X"
    xexp = XExpansion()

    # Metodo con soluzioni parziali rappresentate come stringhe
    xexp.calcola(sequenza)
    print(xexp.soluzioni)

    # Metodo con soluzioni parziali rappresentate come liste
    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)