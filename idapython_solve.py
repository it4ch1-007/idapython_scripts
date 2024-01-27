import idaapi
import idautils
import idc


class MyDbgHook(idaapi.DBG_Hooks):
    def __init__(self):
        idaapi.DBG_Hooks.__init__(self)
    def dbg_bpt(self,tid,ea):
        if not hasattr(MyDbgHook.dbg_bpt, "_static_var"):
            MyDbgHook.dbg_bpt._static_var = ""
        
        print(f"Breakpoint hit at {hex(ea)}")
        ecx = idc.get_reg_value("ecx")
        esi = idc.get_reg_value("esi")
        # print(type(ecx))
        # print(type(esi))
        xor_value = ecx^esi
        MyDbgHook.dbg_bpt._static_var += chr(xor_value)
        print(MyDbgHook.dbg_bpt._static_var)
dbg_hook = MyDbgHook()
dbg_hook.hook()
idaapi.run_requests()
