main:	MOV R2, 0x0004
	MOV R1, [R2] 
	CMP R1, [[0x0004]] 
	JE main
	JNE seguir
	DW 0x0034
seguir:	ADD [R2 + 0x0008], 0xA64B 
	SUB R1, R2
