import matplotlib
import csv
import os

import matplotlib.pyplot as plt

matplotlib.use("agg")

arraySize = []
stridedStore = []
stridedLoad = []
script_dir = os.path.dirname(__file__)
rel_path = "data_memory_bandwidth_matrix_transpose_all.csv"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    header = next(plots)
    for row in plots:
        arraySize.append(int(row[0]))
        stridedStore.append(float(row[1]))
        stridedLoad.append(float(row[2]))

plt.plot(arraySize, stridedStore, label="Strided Store")
plt.plot(arraySize, stridedLoad, label="Strided Load")
plt.xlabel("Array Size [bytes]")
plt.xscale("log", base=2)
plt.ylabel("Data Access Speed [GB/s]")
plt.axvline(
    45, color="r", linestyle="--", label="L1d Cache Size"
)  # todo: adjust to real cachesizes
plt.axvline(
    128, color="r", linestyle="--", label="L2 Cache Size"
)  # todo: adjust to real cachesizes
plt.axvline(
    886, color="r", linestyle="--", label="L3 Cache Size"
)  # todo: adjust to real cachesizes
plt.title("Abbildung 15: Bandbreitenmessung für Strided Load und Strided Store")
plt.legend()
plt.savefig(os.path.join(script_dir, "memory_bandwidth_plot_matrix_transpose.png"))