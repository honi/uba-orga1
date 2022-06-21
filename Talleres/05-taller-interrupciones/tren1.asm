; Memoria
; Motor = [0xF0]
; Intesidad bocina = [0xF1]

; Constantes
; 0x0F = Velocidad máxima
; 0x0C = Velocidad para curva

JMP init

; Truquito para no romper la memoria, acá guardamos la dirección de la RAI
JMP init

init:
SET R0, 0x0F ; Velocidad actual del motor (iniciamos en la velocidad máxima)
SET R1, 0x0F ; Velocidad máxima para comparar
SET R2, 0x00 ; Cantidad de curvas atravesadas (por 8)
SET R3, 0x08 ; Constante 8 para sumarle a R2
SET R4, 0x02 ; Intensidad actual de la bocina
STR [0xF1], R4 ; Escribimos la intensidad inicial de la bocina

; Configuramos la dirección de la RAI
SET R7, cambiarVelocidad
STR [0x02], R7
STI

loop:
STR [0xF0], R0 ; Escribimos la velocidad del motor
JMP loop

cambiarVelocidad:
CMP R0, R1 ; Decidimos a qué velocidad cambiar
JZ entrarEnCurva

salirDeCurva:
SET R0, 0x0F ; Subimos la velocidad
ADD R2, R3 ; Contabilizamos la curva
JZ subirBocina ; Subimos la intensidad de la bocina si ya contamos 32 veces (8 * 32 = 0 mod(256))
IRET

subirBocina:
INC R4 ; Subimos la intensidad de la bocina
STR [0xF1], R4 ; Escribimos la nueva intensidad de la bocina
IRET

entrarEnCurva:
SET R0, 0x0C ; Bajamos la velocidad
IRET
