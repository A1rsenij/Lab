import numpy as np
import matplotlib.pyplot as plt
import bloodFunctions as b

def prox(data, pr):
    i = 0
    while data[i] > pr:
        i += 1
    return i

### calibration ###

#assembling data
pressure = np.array([40.0, 80.0, 120.0, 160.0])
adc_data = []
#40 mm
file = 'blood-data 2021-12-02 15:57:02 40 mm.txt' #insert filename
data, dur, l = b.read(file)
adc_data.append(data.mean())
#80mm
file = 'blood-data 2021-12-02 15:58:22 80 mm.txt' #insert filename
data, dur, l = b.read(file)
adc_data.append(data.mean())
#120mm
file = 'blood-data 2021-12-02 15:59:26 120 mm.txt' #insert filename
data, dur, l = b.read(file)
adc_data.append(data.mean())
#160mm
file = 'blood-data 2021-12-02 16:00:14 160 mm.txt' #insert filename
data, dur, l = b.read(file)
adc_data.append(data.mean())
#fit
k = np.polyfit(adc_data, pressure, 1)
apr = np.polyval(k, np.linspace(400, 1800, 100))

#plot
fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.scatter(pressure, adc_data, label='Измерения', marker='*')
ax.plot(apr, np.linspace(400, 1800, 100), label='P = {:.3f} * N {:.3f} [мм рт. ст.]'.format(k[0], k[1]), c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper left')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.1)

ax.axis([apr[0] - 10, apr.max() + 10, 400 - 50, 1800 + 50])

ax.set_title('Калибровочный график зависимости показаний АЦП от давления', loc='center', fontsize=15)
ax.set_ylabel('Отсчёты АЦП', loc='center', fontsize=10)
ax.set_xlabel('Давление [мм рт. ст.]', loc='center', fontsize=10)

plt.show()

fig.savefig("pressure-calibration.png", dpi = 500)

### processing ###

#rest

file = 'blood-data 2021-12-02 16:06:33 rest.txt' #insert filename
data, dur, l = b.read(file)
pulse = []
duration = np.linspace(0, dur, len(data))
for i in range(0, len(data) - 500, 500):
    pulse.append((data[i + 500] - data[i]) / (duration[i + 500] - duration[i]))
data = data[:l // 2:]
data = np.polyval(k, data)
duration = np.linspace(0, 30, len(data))

s_pr, d_pr = 115, 78 #insert pressure
i_s, i_d = prox(data, s_pr), prox(data, d_pr)

fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, data, label='Давление - {}/{} [мм рт. ст.]'.format(int(s_pr), int(d_pr)), c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper right')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.1)

ax.axis([0, 30, data.min() - 10, data.max() + 10])

ax.set_title('Артериальное давление\n до физической нагрузки', loc='center', fontsize=15)
ax.set_ylabel('Давление [мм рт. ст.]', loc='center', fontsize=10)
ax.set_xlabel('Время [c]', loc='center', fontsize=10)

plt.text(duration[i_s], data[i_s] + 5, 'Systole')
plt.text(duration[i_d], data[i_d] + 5, 'Diastole')
plt.scatter(duration[i_s], data[i_s], label='Systole', marker='*', color='red')
plt.scatter(duration[i_d], data[i_d], label='Diastole', marker='*', color='red')

plt.show()

fig.savefig("rest-pressure.png", dpi = 500)

l = len(pulse)
pulse = np.array(pulse[l//6 : l//2 :]) / 125
duration = np.linspace(10, 30, len(pulse))

p = 75 #insert pulse

fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, pulse, label='Пульс - {} [уд/мин]'.format(p), c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper left')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.1)

ax.axis([10, 30, pulse.min() - 1, pulse.max()  + 1])

ax.set_title('Пульс\n до физической нагрузки', loc='center', fontsize=15)
ax.set_ylabel('Изменеие давления в артерии [мм рт. ст.]', loc='center', fontsize=10)
ax.set_xlabel('Время [c]', loc='center', fontsize=10)

plt.show()

fig.savefig("rest-pulse.png", dpi = 500)

#fitness

file = 'blood-data 2021-12-02 16:09:02 fit.txt' #insert filename
data, dur, l = b.read(file)
pulse = []
duration = np.linspace(0, dur, len(data))
for i in range(0, len(data) - 500, 500):
    pulse.append((data[i + 500] - data[i]) / (duration[i + 500] - duration[i]))
data = data[:l // 2:]
data = np.polyval(k, data)
duration = np.linspace(0, 30, len(data))

s_pr, d_pr = 152, 77 #insert pressure
i_s, i_d = prox(data, s_pr), prox(data, d_pr)

fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, data, label='Давление - {}/{} [мм рт. ст.]'.format(int(s_pr), int(d_pr)), c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper right')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.1)

ax.axis([0, 30, data.min() - 10, data.max() + 10])

ax.set_title('Артериальное давление\n после физической нагрузки', loc='center', fontsize=15)
ax.set_ylabel('Давление [мм рт. ст.]', loc='center', fontsize=10)
ax.set_xlabel('Время [c]', loc='center', fontsize=10)
plt.text(duration[i_s], data[i_s] + 5, 'Systole')
plt.text(duration[i_d], data[i_d] + 5, 'Diastole')
plt.scatter(duration[i_s], data[i_s], label='Systole', marker='*', color='red')
plt.scatter(duration[i_d], data[i_d], label='Diastole', marker='*', color='red')

plt.show()

fig.savefig("fitness-pressure.png", dpi = 500)

l = len(pulse)
pulse = np.array(pulse[l//6 : l//2 :]) / 125
duration = np.linspace(10, 30, len(pulse))

p =  123 #insert pulse

fig, ax = plt.subplots(figsize=(9, 6), dpi=100)
ax.plot(duration, pulse, label='Пульс - {} [уд/мин]'.format(p), c='orange', linewidth=1.2)

ax.legend(fontsize=10, loc='upper left')

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

fig.subplots_adjust(bottom=0.15, left=0.1)

ax.axis([10, 30, pulse.min() - 1, pulse.max()  + 1])

ax.set_title('Пульс\n после физической нагрузки', loc='center', fontsize=15)
ax.set_ylabel('Изменеие давления в артерии [мм рт. ст.]', loc='center', fontsize=10)
ax.set_xlabel('Время [c]', loc='center', fontsize=10)

plt.show()

fig.savefig("fitness-pulse.png", dpi = 500)
