# Datele inițiale
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Dictionar pentru preturi
preturi_dict = {produs: pret for produs, pret in preturi}

# Dictionar pentru stoc, pentru a urmări câte produse sunt disponibile
stoc_produse = {"papanasi": meniu.count("papanasi"), "ceafa": meniu.count("ceafa"), "guias": meniu.count("guias")}

# 1. Comenzi - Simulare procesare comenzi
print("Procesare comenzi:")
for student in list(studenti):  # folosim o copie a listei pentru a modifica originalul în timp ce iterăm
    if comenzi and studenti and tavi:
        comanda = comenzi.pop(0)  # eliminam prima comanda (FIFO)
        studenti.pop(0)  # eliminam primul student (FIFO)
        tavi.pop()  # eliminam o tava (LIFO)
        istoric_comenzi.append(comanda)  # actualizam istoricul comenzilor
        stoc_produse[comanda] -= 1  # scadem din stoc produsul comandat

        # Afisam comanda procesata
        print(f"{student} a comandat {comanda}.")
    else:
        break

print("\n")

# 2. Inventar - Calculam numarul de comenzi pentru fiecare produs si verificam inventarul
inventar_comenzi = {produs: istoric_comenzi.count(produs) for produs in set(istoric_comenzi)}

print("Inventar:")
for produs, numar_comenzi in inventar_comenzi.items():
    print(f"S-au comandat {numar_comenzi} {produs}.")

# Afisam tăvile rămase
print(f"Mai sunt {len(tavi)} tavi.")

# Verificari de stoc
for produs in ["ceafa", "papanasi", "guias"]:
    disponibil = stoc_produse[produs] > 0  # verificam stocul ramas
    print(f"Mai este {produs}: {disponibil}.")

print("\n")

# 3. Finanțe - Calculam incasarile și identificam produsele ieftine
incasari = sum(preturi_dict[produs] for produs in istoric_comenzi)
produse_ieftine = [produs for produs, pret in preturi if pret <= 7]

print("Finanțe:")
print(f"Cantina a încasat: {incasari} lei.")
print(f"Produse care costă cel mult 7 lei: {produse_ieftine}")
