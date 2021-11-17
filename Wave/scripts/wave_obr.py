import numpy as np
import matplotlib.pyplot as plt
import waveFunctions as w

### calibration ###

#assembling data
height = np.array([20.0, 40.0, 60.0, 80.0, 100.0, 120.0])
adc_data = []
#20 mm
file = '20 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.sum()/l)
#40mm
file = '40 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.sum()/l)
#60mm
file = '60 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.sum()/l)
#80mm
file = '80 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.sum()/l)
#100mm
file = '100 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.sum()/l)
#120mm
file = '120 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.sum()/l)
adc_data = np.array(adc_data)
#fit
k = np.polyfit(adc_data, height, 5)
apr = np.polyval(k, np.linspace(2000, 3000, 100))
#plot
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.scatter(height, adc_data, label='Измерения', marker='*')
ax.plot(apr, np.linspace(2000, 3000, 100), label='Калибровочная функция в диапазоне [2000:3000] отсчётов АЦП', c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper left')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.1)

ax.axis([apr[0] - 10, apr.max() + 10, 2000 - 50, 3000 + 50])

ax.set_title('Калибровочный график зависимости показаний АЦП от уровня воды', loc='center', fontsize=15)
ax.set_ylabel('Отсчёты АЦП', loc='center', fontsize=10)
ax.set_xlabel('Уровень воды [мм]', loc='center', fontsize=10)

plt.show()

#fig.savefig("height-calibration.png")

### handling ###

length = 0.71 #insert length
#120mm
ltime = 0.56 #insert time
file = 'wave.txt' #insert filename
#plot
data, dur, l = w.read(file)
data = data[:int(l/5)]
data = np.polyval(k, data)
duration = np.linspace(0, 3, int(l/10))
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, data, label='Уровень воды в кювете', linewidth=1)
ax.legend(fontsize=10, loc='upper right')
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()
fig.subplots_adjust(bottom=0.15, left=0.1)
ax.axis([0, 3, data.min() - 10, data.max() + 10])
ax.set_title('Уровень воды в кювете после открытия торцевой двери', loc='center', fontsize=15)
ax.set_ylabel('Уровень воды [мм]', loc='center', fontsize=10)
ax.set_xlabel('Время [с]', loc='center', fontsize=10)
plt.text(0.05, 81.5, 'L = {} [м]\nt = {} [c]\nV= {:.2f} [м/c]'.format(length, ltime, length/ltime), fontsize=10, backgroundcolor='white')
ax.vlines(ltime, data.min() - 10, data.max() + 10, color='r', linestyle='--')
plt.show()
#fig.savefig("velocity-120mm.png")
#80mm
ltime = 0.56 #insert time
file = 'wave.txt' #insert filename
#plot
data, dur, l = w.read(file)
data = data[:int(l/5)]
data = np.polyval(k, data)
duration = np.linspace(0, 3, int(l/10))
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, data, label='Уровень воды в кювете', linewidth=1)
ax.legend(fontsize=10, loc='upper right')
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()
fig.subplots_adjust(bottom=0.15, left=0.1)
ax.axis([0, 3, data.min() - 10, data.max() + 10])
ax.set_title('Уровень воды в кювете после открытия торцевой двери', loc='center', fontsize=15)
ax.set_ylabel('Уровень воды [мм]', loc='center', fontsize=10)
ax.set_xlabel('Время [с]', loc='center', fontsize=10)
plt.text(0.05, 81.5, 'L = {} [м]\nt = {} [c]\nV= {:.2f} [м/c]'.format(length, ltime, length/ltime), fontsize=10, backgroundcolor='white')
ax.vlines(ltime, data.min() - 10, data.max() + 10, color='r', linestyle='--')
plt.show()
#fig.savefig("velocity-80mm.png")
#40mm
ltime = 0.56 #insert time
file = 'wave.txt' #insert filename
#plot
data, dur, l = w.read(file)
data = data[:int(l/5)]
data = np.polyval(k, data)
duration = np.linspace(0, 3, int(l/10))
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, data, label='Уровень воды в кювете', linewidth=1)
ax.legend(fontsize=10, loc='upper right')
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()
fig.subplots_adjust(bottom=0.15, left=0.1)
ax.axis([0, 3, data.min() - 10, data.max() + 10])
ax.set_title('Уровень воды в кювете после открытия торцевой двери', loc='center', fontsize=15)
ax.set_ylabel('Уровень воды [мм]', loc='center', fontsize=10)
ax.set_xlabel('Время [с]', loc='center', fontsize=10)
plt.text(0.05, 81.5, 'L = {} [м]\nt = {} [c]\nV= {:.2f} [м/c]'.format(length, ltime, length/ltime), fontsize=10, backgroundcolor='white')
ax.vlines(ltime, data.min() - 10, data.max() + 10, color='r', linestyle='--')
plt.show()
#fig.savefig("velocity-40mm.png")
