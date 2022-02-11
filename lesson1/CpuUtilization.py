import psutil
import os

for x in range(4):
    print(psutil.cpu_percent(interval=1))
print("Number of cores in system", psutil.cpu_count(False))
print(os.cpu_count())
