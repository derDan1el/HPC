import matplotlib.pyplot as plt

# Daten aus der Textdatei lesen
data = []
with open('output_file_without_X.txt', 'r') as file:
    next(file)  # Überspringe die erste Zeile
    for line in file:
        line = line.strip().split(',')
        generation = line[3].strip()
        cores = int(line[1].strip())
        data.append((generation, cores))

# Generationsnamen anpassen
generation_names = {
    '4th': '4',
    '5th': '5',
    '6th': '6',
    '7th': '7',
    '8th': '8',
    '9th': '9',
    '10th': '10',
    '11th': '11',
    '12th': '12',
    '13th': '13',
    '14th': '14'
}

# Daten für den Plot vorbereiten
x = []
y = []
for generation, cores in data:
    x.append(generation_names.get(generation, generation))
    y.append(cores)

# Höchste Punkte pro Generation finden
max_points = {}
for generation, cores in data:
    if generation not in max_points or cores > max_points[generation]:
        max_points[generation] = cores

# Daten für die Kurve vorbereiten
curve_x = []
curve_y = []
for generation, cores in max_points.items():
    curve_x.append(generation_names.get(generation, generation))
    curve_y.append(cores)

# Plot erstellen
plt.plot(x, y, marker='o', linestyle='None')  # Keine Verbindungen zwischen den Punkten
plt.plot(curve_x, curve_y, marker='o')  # Kurve durch die höchsten Punkte
plt.xlabel('Generation')
plt.ylabel('Anzahl der Kerne')
plt.xticks(rotation=45)
plt.grid(True)

# Plot umkehren
plt.gca().invert_xaxis()

# Y-Achse anpassen
plt.yticks(range(min(y), max(y)+1, 2))

# Plot als PNG speichern
plt.savefig('prozessor_plot_cores.png')