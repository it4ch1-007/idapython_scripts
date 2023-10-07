import idaapi
import idautils
import idc


#set_python_bpt(0x08000688, 'view_regs()') 

def set_python_bpt(ea, cond):
    idaapi.add_bpt(ea, 4, 0x0044871D) #to add breakpoint at an address 
    bpt = idaapi.bpt_t()  #this is the breakpoint
    print(bpt)
    # bpt.elang = 'Python'
    # bpt.condition = cond
    idaapi.update_bpt(bpt)
