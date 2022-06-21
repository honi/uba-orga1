; R0 = n >= 0
; R1 = resultado

; Inicializamos la suma en 0
SET R1, 0

; Nuestro ciclo repite mientras R0 != 0. Necesitamos actualizar los flags
; antes de iniciar el ciclo, ya que pueden haber flags viejos de operaciones
; anteriores. Queremos ver si R0 es 0. Como ya cargamos R1=0, hacemos el CMP
; contra R1 porque el set de instrucciones no soporta CMP contra constante.
CMP R0, R1

ciclo:
JZ halt     ; Si llegamos a 0 paramos
ADD R1, R0  ; Sumamos en R1 el próximo número
DEC R0      ; Restamos 1 al n inicial
JMP ciclo   ; Loopeamos

;halt:
;JMP halt
