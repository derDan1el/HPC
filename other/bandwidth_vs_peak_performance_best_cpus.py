import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
data = [
    [2011, 'i7-3960X', 51.2, 158.4],
    [2012, 'i7-3970X', 51.2, 168.0],
    [2013, 'i7-4960X', 59.7, 172.8],
    [2014, 'i7-5960X', 68, 192.0],
    [2017, 'i9-7980XE', 85, 1497.6],
    [2018, 'i9-9980XE', 85, 1738.1],
    [2019, 'i9-10980XE', 94, 1728.0],
    [2021, 'i9-11900K', 50, 448.0],
    [2022, 'i9-13900K', 89.6, 473.6],
    [2023, 'i9-14900K', 89.6, 512.0],
    [2024, 'i9-14900KS', 89.6, 512.0]
]

years = [row[0] for row in data]
bandwidth = [row[2] for row in data]
peak_performance = [row[3] for row in data]
cpu_names = [row[1] for row in data]

plt.plot(years, bandwidth, label='Bandbreite')
plt.plot(years, peak_performance, label='maximal mögliche Rechenleistung')

for i, name in enumerate(cpu_names):
    if((i+1)%2 ==0):
        plt.text(years[i], peak_performance[i], name, ha='left', va='bottom', fontsize='small')
    else:
        plt.text(years[i], peak_performance[i], name, ha='left', va='top', fontsize='small')

for i in range(len(years)):
    plt.vlines(years[i], peak_performance[i], bandwidth[i], linestyles='dashed')

plt.text(2014, -450, 'Abgebildet ist der Vergleich der Entwicklung von der der Speicherbandbreite und der theoretischen maximalen Rechenleistung \n Dattenquelle : https://www.intel.de', fontsize='x-small')

plt.xlabel('Year')
plt.ylabel('GB/s / GFLOP/s')
plt.legend()

# Zusätzliche Beschriftung für die maximale Bandbreite
plt.text(2009.8, 89.6, '89.6-', ha='left', va='center', fontsize='smaller')

plt.savefig("bandwidth_vs_peak_performance_best_cpus.png")
