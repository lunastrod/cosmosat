import pyrocutter
import time


activador=False
autonomous=False
order=False

for idx in range(8000,12000,100):
    print(idx, end=" ")
    pyrocutter.deploy_executor(activador, autonomous, order, idx)
    time.sleep(0.2)