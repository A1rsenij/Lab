import bloodFunctions as b
import time

print("Эксперимент")
b.initSpiAdc()
data = []
start = time.time()
finish = start
try:
    while (finish - start) < 60:
        data.append(b.getAdc())
        finish = time.time()
finally:
    b.deinitSpiAdc()
    b.save(data, start, finish)
    b.show(data)
    print("Эксперимент завершен\n")
