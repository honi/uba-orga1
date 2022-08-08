init:
SET R0, 0x00

main:
INC R0
JP halt ; No salta porque R0 = 0x01
INC R0
JP halt ; Ahora sí salta porque R0 = 0x02
INC R0

halt:
JMP halt
