import bloodFunctions as b
import time

mm = 160 #insert pressure
print("Калибровка " + str(mm))
b.initSpiAdc()
data = []
start = time.time()
finish = start
try:
    while (finish - start) < 10:
        data.append(b.getAdc())
        finish = time.time()
finally:
    b.deinitSpiAdc()
    b.save(data, start, finish, str(mm)+' mm')
    b.show(data)
    print("Калибровка завершена\n")
