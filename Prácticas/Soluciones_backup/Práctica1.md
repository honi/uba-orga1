# Práctica 1

## Ejercicio 1

a)

```
33 = 16 × 2 + 1
16 =  8 × 2 + 0
 8 =  4 × 2 + 0
 4 =  2 × 2 + 0
 2 =  0 × 2 + 1
⟹ (33)₁₀ = (10001)₂
```

```
33 = 11 × 3 + 0
11 =  3 × 3 + 2
 3 =  1 × 3 + 0
 1 =  0 × 3 + 1
⟹ (33)₁₀ = (1020)₃
```

```
33 = 6 × 5 + 3
 6 = 1 × 5 + 1
 1 = 0 × 5 + 1
⟹ (33)₁₀ = (113)₅
```

```
100 = 50 × 2 + 0
 50 = 25 × 2 + 0
 25 = 12 × 2 + 1
 12 =  6 × 2 + 0
  6 =  3 × 2 + 0
  3 =  1 × 2 + 1
  1 =  0 × 2 + 1
⟹ (100)₁₀ = (1100100)₂
```

```
100 = 33 × 3 + 1
 33 = 11 × 3 + 0
 11 =  3 × 3 + 2
  3 =  1 × 3 + 0
  1 =  0 × 3 + 1
⟹ (100)₁₀ = (10201)₃
```

```
100 = 20 × 5 + 0
 20 =  4 × 5 + 0
  4 =  0 × 5 + 4
⟹ (100)₁₀ = (400)₅
```

```
1023 = 511 × 2 + 1
 511 = 255 × 2 + 1
 255 = 127 × 2 + 1
 127 =  63 × 2 + 1
  63 =  31 × 2 + 1
  31 =  15 × 2 + 1
  15 =   7 × 2 + 1
   7 =   3 × 2 + 1
   3 =   1 × 2 + 1
   1 =   0 × 2 + 1
⟹ (1023)₁₀ = (1111111111)₂
```

```
1023 = 341 × 3 + 0
 341 = 113 × 3 + 2
 113 =  37 × 3 + 2
  37 =  12 × 3 + 1
  12 =   4 × 3 + 0
   4 =   1 × 3 + 1
   1 =   0 × 3 + 1
⟹ (1023)₁₀ = (1101220)₃
```

```
1023 = 204 × 5 + 3
 204 =  40 × 5 + 4
  40 =   8 × 5 + 0
   8 =   1 × 5 + 3
   1 =   0 × 5 + 1
⟹ (1023)₁₀ = (13043)₅
```

b)

*Nota: a la derecha del igual se interpretan todos los números en base 10.*

```
(1111)₂ = (1 × 2³) + (1 × 2²) + (1 × 2¹) + (1 × 2⁰)
        = 8 + 4 + 2 + 1
        = 15
```

```
(1111)₃ = (1 × 3³) + (1 × 3²) + (1 × 3¹) + (1 × 3⁰)
        = 27 + 9 + 3 + 1
        = 40
```

```
(1111)₅ = (1 × 5³) + (1 × 5²) + (1 × 5¹) + (1 × 5⁰)
        = 125 + 25 + 5 + 1
        = 156
```

```
(CAFE)₁₆ = (12 × 16³) + (10 × 16²) + (15 × 16¹) + (14 × 16⁰)
         = 49152 + 2560 + 240 + 14
         = 51966
```

c)

```
(17)₈ = (1 × 8¹) + (7 × 8⁰) = (15)₁₀

15 = 3 × 5 + 0
 3 = 0 × 5 + 3

⟹ (17)₈ = (15)₁₀ = (30)₅
```

```
(BABA)₁₃ = (11 × 13³) + (10 × 13²) + (11 × 13¹) + (10 × 13⁰) = (26010)₁₀

26010 = 4335 × 6 + 0
 4335 =  722 × 6 + 3
  722 =  120 × 6 + 2
  120 =   20 × 6 + 0
   20 =    3 × 6 + 2
    3 =    0 × 6 + 3

⟹ (BABA)₁₃ = (26010)₁₀ = (320230)₆
```

d)

```
(10 01 01 10 10 10 01 01)₂ = (21122211)₄
(001 001 011 010 100 101)₂ = (113245)₈
(1001 0110 1010 0101)₂ = (96A5)₁₆
```

## Ejercicio 2

```
  100001₂
+ 011110₂
---------
  111111₂ (no hubo acarreo)
```

```
  111111   <-- acarreo
   100001₂
+  011111₂
----------
  1000000₂ (hubo acarreo)
```

```
  1111   <-- acarreo
  01111₂
+ 01111₂
--------
  11110₂ (hubo acarreo)
```

```
  9999₁₆
+ 1111₁₆
--------
  AAAA₁₆ (no hubo acarreo)
```

```
  1 1     <-- acarreo
   F0F0₁₆
+  F0CA₁₆
---------
  1E1BA₁₆ (hubo acarreo)
```

## Ejercicio 3

No puede haber acarreo mayor a 1.

## Ejercicio 4

En base `b` con `k` dígitos, el valor máximo que se puede representar es `b^k - 1`. Consideremos 2 números tales que `n = m = b^k - 1`. Luego, `n × m = (b^k - 1)^2 = b^2k - 2b^k + 1`.

Queremos saber si este número se puede representar con `2k` dígitos. Es decir, si es menor o igual que `b^2k - 1`.

Luego, `b^2k - 2b^k + 1 ≤ b^2k - 1 ⟺ b^k ≥ 1` lo cual es verdadero ya que `k ≥ 0`.

## Ejercicio 5

```
(0)₁₀ = (0000 0000)₂              signo+magnitud
(0)₁₀ = (0000 0000)₂              complemento a 2
```

```
(-1)₁₀ = (1000 0001)₂             signo+magnitud con 8 bits
(-1)₁₀ = (1000 0000 0000 0001)₂   signo+magnitud con 16 bits
(-1)₁₀ = (1111 1111)₂             complemento a 2 con 8 bits
(-1)₁₀ = (1111 1111 1111 1111)₂   complemento a 2 con 16 bits
```

```
(255)₁₀ = (1111 1111)₂            sin signo con 8 bits
(255)₁₀ = (0000 0000 1111 1111)₂  complemento a 2 con 16 bits
```

```
(-128)₁₀ = (1000 0000)₂           complemento a 2 con 8 bits
(-128)₁₀ = (1111 1111 1000 0000)₂ complemento a 2 con 16 bits
```

```
(128)₁₀ = (1000 0000)₂            sin signo con 8 bits
(128)₁₀ = (0000 0000 1000 0000)₂  complemento a 2 con 16 bits
```

## Ejercicio 6

```
r = (1011 1111)₂
s = (1000 0000)₂
t = (1111 1111)₂
```

**Complemento a 2**

```
r = (-65)₁₀
s = (-128)₁₀
t = (-1)₁₀
```

**Signo+magnitud**

```
r = (-63)₁₀
s = (0)₁₀
t = (-127)₁₀
```

## Ejercicio 7

Representación en complemento a 2 con 4 bits:

```
(2)₁₀  = (0010)₂
(-5)₁₀ = (1011)₂
(0)₁₀  = (0000)₂
```

a)

Bits invertidos en el mismo sistema:

```
(1101)₂ = (-3)₁₀
(0100)₂ = (4)₁₀
(1111)₂ = (-1)₁₀
```

b)

Dada la representación de un número en complemento a 2, para obtener la representación de su inverso aditivo (también en complemento a 2) podemos seguir estos pasos:

1. Invertir todos los bits.
2. Sumamos 1 e ignoramos el overflow (si es que hay).

## Ejercicio 8

<table>
    <tr>
        <th></th>
        <th colspan="4" style="text-align: center;">-4</th>
        <th colspan="4" style="text-align: center;">-3</th>
        <th colspan="4" style="text-align: center;">-2</th>
        <th colspan="4" style="text-align: center;">-1</th>
        <th colspan="4" style="text-align: center;">0</th>
        <th colspan="4" style="text-align: center;">1</th>
        <th colspan="4" style="text-align: center;">2</th>
        <th colspan="4" style="text-align: center;">3</th>
    </tr>
    <tr>
        <th>2</th>
        <td colspan="4">overflow</td>
        <td colspan="4">overflow</td>
        <td>-</td><td>-</td><td>1</td><td>0</td>
        <td>-</td><td>-</td><td>1</td><td>1</td>
        <td>-</td><td>-</td><td>0</td><td>0</td>
        <td>-</td><td>-</td><td>0</td><td>1</td>
        <td colspan="4">overflow</td>
        <td colspan="4">overflow</td>
    </tr>
    <tr>
        <th>3</th>
        <td>-</td><td>1</td><td>0</td><td>0</td>
        <td>-</td><td>1</td><td>0</td><td>1</td>
        <td>-</td><td>1</td><td>1</td><td>0</td>
        <td>-</td><td>1</td><td>1</td><td>1</td>
        <td>-</td><td>0</td><td>0</td><td>0</td>
        <td>-</td><td>0</td><td>0</td><td>1</td>
        <td>-</td><td>0</td><td>1</td><td>0</td>
        <td>-</td><td>0</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <th>4</th>
        <td>1</td><td>1</td><td>0</td><td>0</td>
        <td>1</td><td>1</td><td>0</td><td>1</td>
        <td>1</td><td>1</td><td>1</td><td>0</td>
        <td>1</td><td>1</td><td>1</td><td>1</td>
        <td>0</td><td>0</td><td>0</td><td>0</td>
        <td>0</td><td>0</td><td>0</td><td>1</td>
        <td>0</td><td>0</td><td>1</td><td>0</td>
        <td>0</td><td>0</td><td>1</td><td>1</td>
    </tr>
</table>

## Ejercicio 9

```
   0001₂ = (1)₁₀
+  0010₂ = (2)₁₀
--------
   0011₂ = (3)₁₀
```

```
  111
   0111₂ = (7)₁₀
+  1110₂ = (-2)₁₀
--------
   0101₂ = (5)₁₀
```

```
     1   <- acarreo
   0001₂ = (1)₁₀
+  0001₂ = (1)₁₀
--------
   0010₂ = (2)₁₀
```

```
  1 11   <- acarreo y overflow
   1011₂ = (-5)₁₀
+  1011₂ = (-5)₁₀
--------
   0110₂ = (6)₁₀ ≠ (-10)₁₀ fuera del rango de representación
```

```
   1 1   <- acarreo
   0101₂ = (5)₁₀
+  0101₂ = (5)₁₀
--------
   1010₂ = (0)₁₀ ≠ (-16)₁₀ fuera del rango de representación
```

```
  1111   <- acarreo
   1111₂ = (-1)₁₀
+  0001₂ = (1)₁₀
--------
   0000₂ = (0)₁₀
```

```
   0000₂ = (0)₁₀
+  0000₂ = (0)₁₀
--------
   0000₂ = (0)₁₀
```

```
   1     <- overflow
   0100₂ = (4)₁₀
+  0100₂ = (4)₁₀
--------
   1000₂ = (-8)₁₀ ≠ (8)₁₀
```

```
   0001₂ = (1)₁₀
+  1110₂ = (-2)₁₀
--------
   1111₂ = (-1)₁₀
```

## Ejercicio 10

Rangos de representación con `k` dígitos:

- Complemento a 2: `[-2^{k-1}, 2^{k-1} - 1]`
- Signo+magnitud: `[-2^{k-1} + 1, 2^{k-1} - 1]`

Podemos observar que en complemento a 2 tenemos 1 número más que podemos representar: `-2^{k-1}`.

## Ejercicio 11

Utilizando el sistema de representación complemento a 2, podemos reasignar la representación del `0`, es decir, el numeral compuesto de todos 0s, al número `2^{k-1}`.

De esta forma el rango de representación resulta `[-2^{k-1}, 2^{k-1}] - {0}`. Si bien no tenemos forma de representar el `0`, podemos representar exactamente `2^{k-1}` números positivos y `2^{k-1}` números negativos.

El total de números representables resulta `2^{k-1} + 2^{k-1} = 2^k` y esta es exactamente la cantidad de numerales que se pueden formar con `k` dígitos, por lo tanto la representación es biyectiva.

## Ejercicio 12

La afirmación es verdadera. Al tratarse de cadenas binarias, con `k` dígitos podemos obtener `2^k` numerales distintos. Observemos que este número es par. Luego, si asignamos uno de estos numerales al `0`, nos quedan `2^k - 1` numerales para distribuir entre los números positivos y negativos. Como `2^k - 1` es impar, no podemos dividir estar cantidad en exactamente 2 partes iguales, y por lo tanto siempre va a resultar que vamos a tener 1 numeral extra, ya sea para los positivos o los negativos.

## Ejercicio 13

Te lo debo.

## Ejercicio 14

Rango de representación: `[-2^16, 2^16 - 1] = [-65536, 65535]`. Reordenamos los términos para que las sumas parciales cada 2 términos no se vayan fueran del rango de representación.

```
  (7744)₁₆ = (0111 0111 0100 0100)₂ =  (30532)₁₀
+ (88BD)₁₆ = (1000 1000 1011 1101)₂ = (-30531)₁₀
+ (6788)₁₆ = (0110 0111 1000 1000)₂ =  (26504)₁₀
+ (9879)₁₆ = (1001 1000 0111 1001)₂ = (-26503)₁₀
+ (5499)₁₆ = (0101 0100 1001 1001)₂ =  (21657)₁₀
+ (AB68)₁₆ = (1010 1011 0110 1000)₂ = (-21656)₁₀
------------------------------------------------
  (0003)₁₆ = (0000 0000 0000 0011)₂ =      (3)₁₀
```

Resuelto con la ayuda de un [script](p1-14.py).
