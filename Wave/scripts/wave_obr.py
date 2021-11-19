import numpy as np
import matplotlib.pyplot as plt
import waveFunctions as w

def prox(length, ltime):
    step = 3/length
    t, i = 0, 0
    while (t <= ltime):
        t += step
        i += 1
    return i

def time_srch(data, duration, x, start):
    ltime = start
    step = 3/len(data)
    i = prox(len(data), start) 
    i1 = prox(len(data), start - 1)
    k1 = [0, 0]
    while ((-1)*x <= k1[0] <= x and step * i < 3):
        k1 = np.polyfit(list(duration)[i1:i], data[i1:i], 1)
        i += 1
    return step * i

def dv(l, t, dl, dt):
    dv = ((dt/t)**2 + (dl/l)**2)**0.5 * l/t
    return dv

### calibration ###

#assembling data
height = np.array([20.0, 40.0, 60.0, 80.0, 100.0, 120.0])
adc_data = []
#20 mm
file = 'wave-data 2021-11-18 15_52_45 20 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.mean())
#40mm
file = 'wave-data 2021-11-18 15_56_22 40 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.mean())
#60mm
file = 'wave-data 2021-11-18 15_58_20 60 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.mean())
#80mm
file = 'wave-data 2021-11-18 16_01_31 80 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.mean())
#100mm
file = 'wave-data 2021-11-18 16_04_52 100 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.mean())
#120mm
file = 'wave-data 2021-11-18 16_11_00 120 mm.txt' #insert filename
data, dur, l = w.read(file)
adc_data.append(data.mean())
adc_data = np.array(adc_data)
#fit
k = np.polyfit(adc_data, height, 4)
apr = np.polyval(k, np.linspace(1500, 3000, 100))
#plot
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.scatter(height, adc_data, label='Измерения', marker='*')
ax.plot(apr, np.linspace(1500, 3000, 100), label='Калибровочная функция в диапазоне [1500:3000] отсчётов АЦП', c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper left')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([apr[0] - 10, apr.max() + 10, 1500 - 50, 3000 + 50])

ax.set_title('Калибровочный график зависимости показаний АЦП от уровня воды', loc='center', fontsize=15)
ax.set_ylabel('Отсчёты АЦП', loc='center', fontsize=10)
ax.set_xlabel('Уровень воды [мм]', loc='center', fontsize=10)

plt.show()

fig.savefig("height-calibration.png", dpi=500)

### handling ###

fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

length = 1.4100 #insert length
dl = 0.0005
#120mm
file = 'wave-data 2021-11-18 16_13_11 120 mm.txt' #insert filename
#plot
data, dur, l = w.read(file)
data = data[:int(l/5):20]
dt = 15/len(data)
data = np.polyval(k, data)
duration = np.linspace(0, 3, len(data), 0.5)

ltime = time_srch(data, duration, 2.5, 0.5)

ax.plot(duration, data, label='Уровень воды в кювете (120 мм)', linewidth=1, color='black')
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()
ax.axis([0, 3, 0, 150])
ax.set_title('Уровень воды в кювете после открытия торцевой двери', loc='center', fontsize=15)
ax.set_ylabel('Уровень воды [мм]', loc='center', fontsize=10)
ax.set_xlabel('Время [с]', loc='center', fontsize=10)
plt.text(0.05, 125,'L = {:.4f}$\pm${:.4f} [м]\nt = {:.3f}$\pm${:.3f} [c]\nV = {:.3f}$\pm${:.3f} [м/c]'.format(
            length, dl, ltime, dt, length/ltime, dv(length, ltime, dl, dt)),
            fontsize=10, backgroundcolor='white', color='black')
ax.vlines(ltime, 0, 150, color='black', linestyle='--')
#80mm
file = 'wave-data 2021-11-18 16_17_24 80 mm.txt' #insert filename
#plot
data, dur, l = w.read(file)
data = data[:int(l/5):20]
data = np.polyval(k, data)
duration = np.linspace(0, 3, len(data))

ltime = time_srch(data, duration, 0.5, 1.5)

ax.plot(duration, data, label='Уровень воды в кювете (80 мм)', linewidth=1, color='orange')
plt.text(0.05, 85, 'L = {:.4f}$\pm${:.4f} [м]\nt = {:.3f}$\pm${:.3f} [c]\nV = {:.3f}$\pm${:.3f} [м/c]'.format(
            length, dl, ltime, dt, length/ltime, dv(length, ltime, dl, dt)),
            fontsize=10, backgroundcolor='white', color='orange')
ax.vlines(ltime, 0, 150, color='orange', linestyle='--')

#40mm
file = 'wave-data 2021-11-18 16_20_32 40 mm.txt' #insert filename
#plot
data, dur, l = w.read(file)
data = data[:int(l/5):20]
data = np.polyval(k, data)
duration = np.linspace(0, 3, len(data))

ltime = time_srch(data, duration, 0.5, 2.3)

ax.plot(duration, data, label='Уровень воды в кювете (40 мм)', linewidth=1, color='green')
plt.text(0.05, 45, 'L = {:.4f}$\pm${:.4f} [м]\nt = {:.3f}$\pm${:.3f} [c]\nV = {:.3f}$\pm${:.3f} [м/c]'.format(
            length, dl, ltime, dt, length/ltime, dv(length, ltime, dl, dt)),
            fontsize=10, backgroundcolor='white', color='green')
ax.vlines(ltime, 0, 150, color='green', linestyle='--')
ax.legend(fontsize=10, loc='upper right')

plt.show()
fig.savefig("velocity.png", dpi=500)
