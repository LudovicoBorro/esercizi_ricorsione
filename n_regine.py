from time import time

class NRegine:

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0

    #==============================================APPROCCIO 2=====================================================
    # Rappresentiamo soluzione come un vettore di N regine,
    # ognuno rappresentante una regina come riga e colonna
    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione2([], N)

    # Parziale è un vettore di coppie (riga, colonna)
    # come riga e colonna
    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1

        # Caso terminale: ho messo N regine
        if len(parziale) == N:
            # if self._is_soluzione(parziale):
                # self.n_soluzioni += 1
                # print(parziale)
            self.n_soluzioni += 1
            print(parziale)
        # Caso ricorsivo: ho messo < N regine
        else:
            for riga in range(N):
                for col in range(N):
                    # Verifico se la nuova regina sia ammissibile
                    nuova_regina = [riga, col]
                    if self._step_is_valid(nuova_regina, parziale):
                        # Aggiungi pezzetto di soluzione in parziale
                        parziale.append(nuova_regina)
                        # Andare avanti con la ricorsione
                        self._ricorsione2(parziale, N)
                        # Backtracking
                        parziale.pop()

    # Funzione che prende due regine e restituisce True se non si possono attaccare
    # altrimenti, restituisce False
    def _is_pair_admissible(self, regina1, regina2) -> bool:
        # 1) Verifico la riga. Se non va bene, return False
        if regina1[0] == regina2[0]:
            return False
        # 2) Verifico la colonna. Se non va bene, return False
        if regina1[1] == regina2[1]:
            return False
        # 3) Verifico diagonale 1. Se non va bene, return False
        # per fare questa verifica devo controllare che
        # colonna di regina1 - riga di regina1 ==
        # colonna di regina2 - riga di regina2
        if (regina1[1] - regina1[0]) == (regina2[1] - regina2[0]):
            return False
        # 4) Verifico diagonale 2. Se non va bene, return False
        # per fare questa verifica devo controllare che
        # colonna di regina1 + riga di regina1 ==
        # colonna di regina2 + riga di regina2
        if (regina1[1] + regina1[0]) == (regina2[1] + regina2[0]):
            return False
        # 5) Ho passato tutti i controlli, return True
        return True

    # Metodo che data una possibile soluzione (lista con N regine) verifica se sia ammissibile
    # e restituisce True se ammissibile, False se non ammissibile
    def _is_soluzione(self, soluzione_possibile) -> bool:
        for i in range(len(soluzione_possibile)-1):
            for j in range(i+1, len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    return False
        return True

    # Funzione che controlla se la nuova regina da inserire sia ammissibile rispetto
    # alla soluzione parziale costruita finora.
    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True

if __name__ == "__main__":
    nreg = NRegine()
    start_time = time()
    nreg.solve2(4)
    end_time = time()

    print(f"Elapsed time: {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")