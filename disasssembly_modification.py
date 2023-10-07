''' Short and simple transformations in disassembler view
'''

start_ea = 0x00448722
end_ea = 0x00448725


def make_offsets32(start_ea, end_ea):
    ''' Transform data to offsets (using 32-bit length) '''
    for addr in range(start_ea, end_ea, 4): 
        OpOff(addr, 0, 0)


def make_dwords(start_ea, end_ea):
    ''' Transform data to dwords in hex (using 32-bit length) '''
    for addr in range(start_ea, end_ea, 4): 
        OpHex(addr, 0)

make_offsets32(start_ea,end_ea)
print("hello world")