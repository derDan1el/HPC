import pandas as pd

import matplotlib.pyplot as plt

# Pfad zu den CSV-Dateien


# Daten aus den CSV-Dateien lesen
data1 = pd.read_csv("5_2_row1.csv")
data2 = pd.read_csv("5_2_col1.csv")

# Datenpunkte extrahieren
x1 = data1['n']
y1 = data1['time']
x2 = data2['n']
y2 = data2['time']

# Plot erstellen
plt.plot(x1, y1, label='mkn')
plt.plot(x2, y2, label='nkm')

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('n')
plt.ylabel('time in s')
plt.title('Vergleich von mkn und nkm')

# Legende anzeigen
plt.legend()

# Plot anzeigen
plt.savefig("plot_for_MMM1.png")