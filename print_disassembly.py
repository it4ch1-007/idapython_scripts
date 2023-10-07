import idaapi
import idautils
for function in idautils.Functions():
	for function_ea in idautils.Functions():
	    for ins in idautils.FuncItems(function_ea):
	        if idaapi.isCode(idaapi.getFlags(ins)):
	            print idc.GetMnem(ins)