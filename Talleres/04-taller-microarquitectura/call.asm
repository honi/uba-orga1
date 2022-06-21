; Resultado final: R0=0x04

init:
SET R7, 0xFF

main:
SET R0, 0x02
SET R1, 0x03
CALL R7, add

halt:
JMP halt

add:
ADD R0, R1
CALL R7, sub
ADD R0, R1
RET R7

sub:
SET R2, 0x04
SUB R0, R2
RET R7
