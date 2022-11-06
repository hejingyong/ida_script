from idc_bc695 import *
start_addr = 0x0000000000202020
l=[]
for i in range(0x1000):
    t = Byte(start_addr)
    l.append(t)
    start_addr+=1
print(l)

    
    
