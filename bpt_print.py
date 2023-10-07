import idaapi
# import idadbg
import idc


print("hello world")
class MyDbgHook(idaapi.DBG_Hooks): 
    #ye class saare bkpoints ko handle krega or unki working ko dekhega
    def __init__(self):
        idaapi.DBG_Hooks.__init__(self)
    #ye fn use initialize krega
    
    def dbg_bpt(self,tid,ea): #tid is the thread id
    #ye fn breakpoint hit hote hi call hoga
         print(f"Breakpoint hit at : {hex(ea)}")
         registers_display=["RAX","RDX"]
         for register in registers_display:
             value=idc.get_reg_value(register)
             #get_reg_value gets the value of all registers mentioned
             print(register,"=",value)
    
debug_hook = MyDbgHook()
#an object of the desired class

debug_hook.hook()
#this will call the methods of the class
idaapi.run_requests()
#helps in interface of debugger and the interpreter