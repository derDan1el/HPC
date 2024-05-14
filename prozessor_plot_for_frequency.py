import numpy as np

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 7))
# Daten aus der Datei lesen
data = np.genfromtxt('output_file.txt', delimiter=',\t', dtype=None, names=True, encoding='utf-8')

# Spalten extrahieren
prozessor = data['processor_name']# alle Zeilen, nur 1. Spalte
ghz = data['frequency']# alle Zeilen, nur 3. Spalte
generation = data['generation']# alle Zeilen,nur 4. Spalte


# Plot erstellen
plt.scatter(generation, ghz, 5)

# Liste der bereits verwendeten Positionen
used_positions = []

# Prozessornamen an den Punkten anzeigen
for i, txt in enumerate(prozessor):
    position = (generation[i], ghz[i])
    
    # Überprüfen, ob die Position bereits verwendet wurde
    if position not in used_positions:
        plt.annotate(txt, position, fontsize=8)
        used_positions.append(position)

# Achsenbeschriftungen setzen
plt.xlabel('Generation')
plt.ylabel('GHz')

# Achsenlimits setzen
plt.xlim(-1,11)

# X-Achse umkehren
plt.gca().invert_xaxis()

# Setzen Sie die Positionen der Ticks auf der x-Achse
#plt.xticks(np.arange(-1, 11, 3.0))

plt.title("CPU Speeds Across Generations")
plt.figtext(0.5, 0.01, " Other processors of the same generation and with the same cpu speed have been omitted for reasons of text overlap.\n CPUs of the X series are listed in the next plot and have been omitted here.", ha="center", fontsize=8, wrap=True)

# Plot anzeigen
plt.savefig('prozessor_plot_for_frequency.png', dpi=300)