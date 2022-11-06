from idc_bc695 import *
s = 0x600b00
for i in range(182):
    PatchByte(s + i, Byte(s+i)^0xc)
