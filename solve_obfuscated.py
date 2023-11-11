from idc import *
from idaapi import *
from idautils import *

set_addr = 0x000000000804810E
xor_addr = 0x0000000008048090
xor_values=[]
set_values=[]
cntr=0
s=""
class MyDbgHook(DBG_Hooks):
    def dbg_bpt(self,tid,ea):
        global s
        global cntr
        print(f"Breapoint hit at {hex(ea)}")
        if (ea ==xor_addr and cntr>=4):
            xor_values.append(idc.get_reg_value("R8"))
        else:
            cntr+=1
        if(ea==set_addr):
            set_values.append(idc.get_reg_value("R9"))
            idc.set_reg_value(idc.get_reg_value("R9"),"R8")
        print(xor_values)
        print(set_values)
        if(len(set_values)==len(xor_values)):
            for i in range(len(xor_values)):
                s+=chr(xor_values[i]^set_values[i])
        print(s)
        return 0
idc.add_bpt(xor_addr)
idc.add_bpt(set_addr)

debug_hook = MyDbgHook()
debug_hook.hook()
# debug_hook.dbg_bpt(xor_addr)
# debug_hook.dbg_bpt(set_addr)

ep = idc.get_inf_attr(INF_START_IP)
request_run_to(ep)
request_step_over()
run_requests()