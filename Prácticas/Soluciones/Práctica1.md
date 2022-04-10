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
(1 001 011 010 100 101)₂ = (113245)₈
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
  111111   <-- acarreos
   100001₂
+  011111₂
----------
  1000000₂ (hubo acarreo)
```

```
  1111   <-- acarreos
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
  1 1     <-- acarreos
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

```
+-------------------+
|        -4         |
+-------------------+
| 2 | 0 | 0 | 0 | 0 |
+---+---+---+---+---+
| 3 | 0 | 0 | 0 | 0 |
+---+---+---+---+---+
| 4 | 0 | 0 | 0 | 0 |
+---+---+---+---+---+
```

<table style="font: monospace">
    <tr>
        <th colspan="5" style="text-align: center;">-4</th>
    </tr>
    <tr>
        <th>2</th>
        <td>.</td>
        <td>.</td>
        <td>.</td>
        <td>.</td>
    </tr>
    <tr>
        <th>3</th>
        <td>.</td>
        <td>.</td>
        <td>.</td>
        <td>.</td>
    </tr>
    <tr>
        <th>4</th>
        <td>.</td>
        <td>.</td>
        <td>.</td>
        <td>.</td>
    </tr>
</table>
