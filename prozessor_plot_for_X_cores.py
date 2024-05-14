import matplotlib.pyplot as plt

# Daten aus der Textdatei lesen
data = []
with open('X_series.txt', 'r') as file:
    next(file)  # Überspringe die erste Zeile
    for line in file:
        line = line.strip().split(',')
        generation = line[3].strip()
        cores = int(line[1].strip())
        data.append((generation, cores))

# Generationsnamen anpassen
generation_names = {
    '10X-series': '10X',
    '9X-series': '9X',
    '7X-series': '7X',
    '6X-series': '6X',
    '5X-series': '5X',
    '4X-series': '4X'
}

# Daten für den Plot vorbereiten
x = []
y = []
for generation, cores in data:
    x.append(generation_names.get(generation, generation))
    y.append(cores)

# Plot erstellen
plt.plot(x, y, marker='o', linestyle='None')  # Keine Verbindungen zwischen den Punkten
plt.xlabel('Generation')
plt.ylabel('Anzahl der Kerne')
plt.title('Prozessor-Kerne pro Generation')
plt.xticks(rotation=45)
plt.grid(True)

# Plot umkehren
plt.gca().invert_xaxis()

# Y-Achse anpassen
plt.yticks(range(min(y), max(y)+1, 2))

# Plot als PNG speichern
plt.savefig('prozessor_plot_for_X.png')