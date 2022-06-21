; Resultado final: R0=0x04

main:
SET R0, 0x02
SET R1, 0x03
CALL add

halt:
JMP halt

add:
ADD R0, R1
CALL sub
ADD R0, R1
RET

sub:
SET R2, 0x04
SUB R0, R2
RET
