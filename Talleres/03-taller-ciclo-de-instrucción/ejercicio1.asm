main:			MOV R1, 0x7000
				ADD R1, 0x6000
				JE  cero
				JL  dioNegativo
				JVS huboOverFlow
cero:			DW  0x0FE0
huboOverFlow:	MOV R2, 0x0030
				SUB R2, 0x00F0
				JVS huboOverFlow
				JE  cero
				JL  dioNegativo
				DW  0x0FE0
dioNegativo:	CMP R2, 0xFF40
				JE  finOk
				DW  0x0FE0
finOk:			DW  0x0000
