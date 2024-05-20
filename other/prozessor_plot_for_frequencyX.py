import numpy as np

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
# Daten aus der Datei lesen
data = np.genfromtxt('X_series.txt', delimiter=',\t', dtype=None, names=True, encoding='utf-8')

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
plt.xlim(-1,6)

# X-Achse umkehren
plt.gca().invert_xaxis()

# Setzen Sie die Positionen der Ticks auf der x-Achse
#plt.xticks(np.arange(-1, 11, 3.0))

plt.title("X-series CPU Speeds Across Generations")

# Plot anzeigen
plt.savefig('prozessor_plot_for_frequencyX.png', dpi=300)