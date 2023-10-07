import idautils

# Iterate through all segments in the IDB
for seg_ea in idautils.Segments():
    # Iterate through instructions in the segment
    for ea in idautils.FuncItems(seg_ea):
        # Check if the current address contains code
        if idaapi.is_code(idaapi.get_full_flags(ea)):
            # Get the disassembly text for the current instruction
            disassembly = idc.generate_disasm_line(ea,GENDSM_FORCE_CODE)
            print(f"Address: 0x{ea:08X}, Disassembly: {disassembly}")


            '''
            GENDSM_FORCE_CODE: Forces generation as code (ignores potential data).
GENDSM_NO_ONELINE: Suppresses one-line comments.
GENDSM_COMMENT: Includes regular comments.
GENDSM_RPTCMT: Includes repeatable comments.
GENDSM_NOSPACE: Suppresses space at the beginning of the line.
GENDSM_SHOW_XREFS: Includes cross-references.
GENDSM_SHOW_LABELS: Includes labels (e.g., function names).'''

#These flags can  be used to generate a desired format of the disassembly of the code of the file given

