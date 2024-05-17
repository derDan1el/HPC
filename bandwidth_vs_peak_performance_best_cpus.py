import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
data = [
    [2011, 'i7-3960X', 51.2, 187.2],
    [2012, 'i7-3970X', 51.2, 192.0],
    [2013, 'i7-4960X', 59.7, 192.0],
    [2014, 'i7-5960X', 68.3, 448.0],
    [2015, 'i7-6950X', 76.8, 560.0],
    [2017, 'i9-7980XE', 85.3, 2419.2],
    [2018, 'i9-9980XE', 85.3, 2534.4],
    [2019, 'i9-10980XE', 85.3, 2649.6],
    [2021, 'i9-11900K', 50, 1356.8],
    [2022, 'i9-13900K', 89.6, 1843.2],
    [2023, 'i9-14900K', 89.6, 1894.4],
    [2024, 'i9-14900KS', 89.6, 1945.6]
]

years = [row[0] for row in data]
bandwidth = [row[2] for row in data]
peak_performance = [row[3] for row in data]
cpu_names = [row[1] for row in data]

plt.plot(years, bandwidth, label='Bandwidth')
plt.plot(years, peak_performance, label='Peak Performance')

for i, name in enumerate(cpu_names):
    if i == 0:
        plt.text(years[i], peak_performance[i], name, ha='left', va='top', fontsize='smaller')
    elif i == 1:
        plt.text(years[i], peak_performance[i], name, ha='right', va='bottom', fontsize='smaller')
    elif i == 2:
        plt.text(years[i], peak_performance[i], name, ha='left', va='bottom', fontsize='smaller')
    elif i == 11:
        plt.text(years[i], peak_performance[i], name, ha='center', va='bottom', fontsize='smaller')
    elif i == 9:
        plt.text(years[i], peak_performance[i], name, ha='center', va='top', fontsize='smaller')
    elif i == 10:
        plt.text(years[i], peak_performance[i], name, ha='center', va='bottom', fontsize='smaller')
    else:
        plt.text(years[i], peak_performance[i], name, ha='center', va='top', fontsize='smaller')

for i in range(len(years)):
    plt.vlines(years[i], peak_performance[i], bandwidth[i], linestyles='dashed')

plt.text(2014, -450, 'arithmetic performance = amount of cores * frequency * FLOPS per cycle \nSource of CPU vlaues  : https://www.intel.de', fontsize='x-small')

plt.xlabel('Year')
plt.ylabel('GB/s / GFLOP/s')
plt.title('Bandwidth vs Peak Performance')
plt.legend()

# Zusätzliche Beschriftung für die maximale Bandbreite
plt.text(2009.8, 89.6, '89.6-', ha='left', va='center', fontsize='smaller')

plt.savefig("bandwidth_vs_peak_performance_best_cpus.png")
