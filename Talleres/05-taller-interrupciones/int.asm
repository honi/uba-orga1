JMP init

; Truquito para no romper la memoria, acá guardamos la dirección de la RAI
JMP init

init:
SET R1, 0x03
SET R2, 0x00
SET R3, rai
STR [0x02], R3
STI

loop:
CMP R1, R2
JZ fin
JMP loop

fin: CLI

halt:
JMP halt

rai:
DEC R1
IRET
