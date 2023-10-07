##Calling the VirtualAlloc function using the Appcall class

# virtualAlloc = Appcall.proto("kernel32_VirtualAlloc","int __stdcall VirtualAlloc(int addr, SIZE_T sz, DWORD alloctype, DWORD protect);")
# memory = virtualAlloc(0x0, 0x00001000, 0x1000, 0x40)