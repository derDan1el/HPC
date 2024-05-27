import numpy as np

import matplotlib.pyplot as plt

def process_frequency(freq):
    if '(' in freq and ':' in freq:
        # Extract the first value from the tuple
        return float(freq.split(':')[0].strip('()'))
    else:
        # Convert to float directly
        return float(freq)


# Daten aus der Datei lesen
data = np.genfromtxt('output_file.txt', delimiter=',\t', dtype=None, names=True, encoding='utf-8')

# Extract columns
prozessor = data['processor_name']  # all rows, only 1st column
ghz_raw = data['frequency']  # all rows, only 3rd column
generation = data['generation']  # all rows, only 4th column

# Process the frequency column to handle tuples
ghz = np.array([process_frequency(freq) for freq in ghz_raw])

# Create the plot
plt.figure(figsize=(15, 7))
plt.scatter(generation, ghz, 8)

# List of used positions
used_positions = []

# Prozessornamen an den Punkten anzeigen
for i, txt in enumerate(prozessor):
    position = (generation[i], ghz[i])

    # Überprüfen, ob die Position bereits verwendet wurde
    if position not in used_positions:
        plt.annotate(txt, position, fontsize=8)
        used_positions.append(position)

# Set axis labels
plt.xlabel('Generation')
plt.ylabel('GHz')

# Set axis limits
plt.xlim(-1, 12)

# Reverse the x-axis
plt.gca().invert_xaxis()




plt.figtext(0.5, 0.01, "Andere Prozessoren die der gleiche Generation angehören und die gleiche Basistaktfrequenz teilen wurden nicht mitgelistet", ha="center", fontsize=8, wrap=True)

# Save the plot
plt.savefig('prozessor_plot_for_frequency.png', dpi=300)
