import numpy as np
import math
import matplotlib.pyplot as plt

data_array = np.loadtxt("data.txt", dtype=float)

settings_array = np.loadtxt("settings.txt", dtype = float)
voltstep = settings_array[1]
lentime = settings_array[0]

data_array *= voltstep
timeline = np.linspace(0, lentime, len(data_array))

fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
ax.plot(timeline, data_array, label='V(t)', linewidth=0.8, marker='o', markevery=400, markersize=8)

ax.legend(fontsize=10)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.2)

ax.axis([0, lentime + 10, 0, round(data_array.max())+0.5])

ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке', loc='center', fontsize=15)
ax.set_ylabel('Напряжения, В', loc='center', fontsize=10)
ax.set_xlabel('Время, с', loc='center', fontsize=10)
plt.text(80, 2.5, 'Время зарядки: {:.2f} c'.format(lentime*data_array.argmax()/len(data_array)), fontsize=10)
plt.text(80, 2, 'Время разрядки: {:.2f} c'.format(lentime - lentime*data_array.argmax()/len(data_array)), fontsize=10)
plt.show()

fig.savefig("test.svg")