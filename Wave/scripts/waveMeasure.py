import numpy as np
import matplotlib.pyplot as plt
import time
import waveFunctions as w

w.initSpiAdc()
height = 0 #insert height
w.waitForOpen()
data = []
start = time.time()
finish = start
try:
    while (finish - start) < 15:
        data.append(w.getAdc)
        finish = time.time()
finally:
    w.deinitSpiAdc()
    w.save(data, start, finish, height)
    w.show(data)
