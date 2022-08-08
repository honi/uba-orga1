init:
SET R0, 0x00
SET R1, 0x01
SET R2, 0x02

main:
MSTR [R0], 0x01
MMOV [R1], [R0]
MADD [R2], [R0]
MADD [R2], [R1]
MLOAD R3, [R2]

; Al finalizar la ejecución, deberíamos observar:
; R3 = 0x02
; Las primeras 3 posiciones de MemoryPlus son: 0x01, 0x01, 0x02

halt:
JMP halt
