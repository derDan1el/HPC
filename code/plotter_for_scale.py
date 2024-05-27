import matplotlib.pyplot as plt

data = """Array Size used (KBytes),time in ns, time in ns
1,0.769701,1.32084
2,0.732882,1.32437
4,0.706544,1.25371
8,0.692448,1.23072
16,0.709538,1.22268
32,0.698367,1.24536
64,0.684416,1.23561
128,0.686592,1.24284
256,0.689867,1.25325
512,0.72442,1.24848
1024,0.742279,1.23906
2048,0.729262,1.25167
4096,0.723611,1.24493
8192,0.787169,1.25021
16384,0.784605,1.28355
32768,0.777856,1.28917
65536,0.776866,1.28538
131072,0.776725,1.28992
262144,0.781225,1.28783
524288,0.78292,1.29626
"""

# Split the data into x and y values
lines = data.strip().split('\n')
x = [int(line.split(',')[0]) for line in lines[1:]]
y_optimized = [float(line.split(',')[1]) for line in lines[1:]]
y_unoptimized = [float(line.split(',')[2]) for line in lines[1:]]

# Plot the data
plt.plot(x, y_optimized, label='optimized')
plt.plot(x, y_unoptimized, label='unoptimized')

plt.xlabel("Array Size (KBytes)")
plt.ylabel("Time (ns)")
plt.title("Zeiteinsparung durch Loop Fusion")

plt.xscale("log", base=2)
# Set the x-axis tick positions
plt.xticks(x)

# Add vertical lines at x=32 and x=256
plt.axvline(x=32, color='r', linestyle='--')
plt.axvline(x=256, color='r', linestyle='--')
plt.axvline(x=12288, color='r', linestyle='--')

# Show the legend
plt.legend()

plt.savefig("time_consumed2")