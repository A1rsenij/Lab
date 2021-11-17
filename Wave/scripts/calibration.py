import numpy as np
import matplotlib.pyplot as plt
import time
import waveFunctions as w

w.initSpiAdc()
height = 0 #insert height
data = []
start = time.time()
finish = start
try:
    while (finish - start) < 10:
        data.append(w.getAdc)
        finish = time.time()
finally:
    w.deinitSpiAdc()
    w.save(data, start, finish, height)
    w.show(data)
